import threading
import queue
import socket
import json
import argparse
import requests

from select import select
from collections import Counter
from bs4 import BeautifulSoup


threads_q = queue.Queue()

tasks = []
to_read = {}
to_write = {}
url_count = 0


def get_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('-w', type=int, default=1, help='Количество воркеров')
    parser.add_argument('-k', type=int, default=5, help='кол-во самых частых слов')
    return parser.parse_args()


def fetch_url(url):
    response = requests.get(url)
    return response.text


def work(n_common, lock):
    while True:
        connection, url = threads_q.get()
        try:
            soup = BeautifulSoup(fetch_url(url), 'lxml')
            most_common = Counter(soup.get_text().split()).most_common(n_common)
            response = json.dumps({url: dict(most_common)}).encode()
            connection.send(response)
        except requests.ConnectionError as e:
            response = json.dumps({'url': url, 'error': str(e)}).encode()
            connection.send(response)
        finally:
            with lock:
                global url_count
                url_count += 1
                print(f'Обработано {url_count} url')
            threads_q.task_done()


def server(threads_num, n_common):
    server_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    server_sock.bind(('localhost', 15000))
    server_sock.listen()

    lock = threading.Lock()

    threads = [
        threading.Thread(target=work, args=(n_common, lock), daemon=True)
        for _ in range(threads_num)
    ]

    for thread in threads:
        thread.start()

    while True:
        yield 'read', server_sock
        client_sock, addr = server_sock.accept()  # read

        client_sock.settimeout(2)
        tasks.append(client(client_sock))


def client(client_sock):
    while True:
        yield 'read', client_sock
        data = client_sock.recv(4096)  # read

        if not data:
            break
        else:
            url = data.decode().strip()
            # yield 'write', client_sock
            threads_q.put((client_sock, url))
    client_sock.close()


def event_loop():
    while any([tasks, to_read, to_write]):
        while not tasks:
            ready_to_read, ready_to_write, _ = select(to_read, to_write, [])

            for sock in ready_to_read:
                tasks.append(to_read.pop(sock))

            for sock in ready_to_write:
                tasks.append(to_write.pop(sock))

        try:
            task = tasks.pop(0)
            op_type, sock = next(task)

            if op_type == 'read':
                to_read[sock] = task
            elif op_type == 'write':
                to_write[sock] = task
        except StopIteration:
            pass


def main():
    args = get_args()
    tasks.append(server(args.w, args.k))
    event_loop()
    threads_q.join()


if __name__ == '__main__':
    main()



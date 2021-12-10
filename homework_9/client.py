import threading
import queue
import socket
import argparse


def get_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('m', type=int, default=1, help='Количество потоков')
    parser.add_argument('u', type=str, default=5, help='файл с url`ами')
    return parser.parse_args()


def get_urls(path_urls):
    with open(path_urls) as file:
        urls = file.read().splitlines()
    return urls


def chunks(lst, ssize):
    for i in range(0, len(lst), ssize):
        yield lst[i:i + ssize]


def work(urls, addr):
    sock = socket.create_connection(addr)

    for url in urls:
        sock.send(url.strip().encode())
        data = sock.recv(1024)

        if not data:
            continue
        print(data.decode())


def main(threads_num, path_urls):
    urls = get_urls(path_urls)
    size_chunk = len(urls) // threads_num + 1

    host = '127.0.0.1'
    port = 15000

    threads = list()
    for i in range(threads_num):
        th = threading.Thread(target=work,
                              args=(urls[i*size_chunk:(i+1)*size_chunk], (host, port)))
        threads.append(th)

    while True:
        for thread in threads:
            thread.start()

        for thread in threads:
            thread.join()

        break
    # close the connection


if __name__ == '__main__':
    args = get_args()
    main(args.m, args.u)

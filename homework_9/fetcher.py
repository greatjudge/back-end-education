import asyncio
import aiohttp
import argparse

from time import time


def get_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('n', type=int, default=1, help='Количество работников')
    parser.add_argument('u', type=str, default=5, help='файл с url`ами')
    return parser.parse_args()


def get_urls(path_urls):
    with open(path_urls) as file:
        urls = file.read().splitlines()
    return urls


def write_html(data):
    filename = f'files/filie-{(int(time()))}.html'
    with open(filename, 'w') as file:
        file.write(data)


async def fetch_content(queue, session):
    while True:
        url = await queue.get()
        async with session.get(url) as response:
            data = await response.read()
            # write_html(data)
        print(f'done {url}')
        queue.task_done()


async def main(workers_num, path):
    queue = asyncio.Queue()
    urls = get_urls(path)

    for url in urls:
        queue.put_nowait(url)

    async with aiohttp.ClientSession() as session:
        tasks = [asyncio.create_task(fetch_content(queue, session))
                 for _ in range(workers_num)]

        await queue.join()
        for task in tasks:
            task.cancel()
        await asyncio.gather(*tasks, return_exceptions=True)


if __name__ == '__main__':
    args = get_args()
    asyncio.run(main(args.n, args.u))

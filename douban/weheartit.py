#!/usr/bin/env python
# -*- coding: utf-8 -*-

import requests
from bs4 import BeautifulSoup

headers = {
    'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.62 Safari/537.36'}


class WeHeartIt:
    BASE_URL = "https://weheartit.com/{}/collections/{}"

    def __init__(self, user_id, collection_id) -> None:
        self.url = WeHeartIt.BASE_URL.format(user_id, collection_id)

    def photos(self):
        """:return photo urls"""
        pass

    def __photos(self, page):
        r = requests.get(self.url, params={
            'scrolling': 'true',
            'page': page,
            'before': ''
        })
        soup = BeautifulSoup(r.content, 'html.parser')
        imgs = soup.find_all('img', class_='entry-thumbnail')
        for img in imgs:
            url = img['src']
            url.replace('superthumb', 'original')
            url = url.split('?', 1)[0]
            yield url


def get_page():
    """
    https://weheartit.com/ma_yu_scandal/collections/106301429-?scrolling=true&page=2&before=298859538
    """
    url = 'https://weheartit.com/ma_yu_scandal/collections/106301429-'
    r = requests.get(url, headers={
        'Host': 'weheartit.com',
        'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36',
    })


if __name__ == '__main__':
    we_heart_it = WeHeartIt('ma_yu_scandal', '106301429-')

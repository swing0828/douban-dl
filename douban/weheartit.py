#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os

import requests
from bs4 import BeautifulSoup

from douban import threadPoolExecutor
from utils import number1, file_utils

headers = {
    'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.62 Safari/537.36'}


class WeHeartIt:
    BASE_URL = "https://weheartit.com/{}/collections/{}"

    def __init__(self, user_id, collection_id) -> None:
        self.url = WeHeartIt.BASE_URL.format(user_id, collection_id)

    def photos(self):
        """:return photo urls"""
        page = 1
        before = ''
        while True:
            photos = self.__photos(page, before)
            before = number1(photos[-1])
            length = len(photos)
            if length == 0:
                break
            for photo in photos:
                yield photo
            page += 1

    def __photos(self, page, before):
        r = requests.get(self.url, params={
            'scrolling': 'true',
            'page': page,
            'before': before
        }, headers={
            'Host': 'weheartit.com',
            'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36'
        })
        soup = BeautifulSoup(r.content, 'html.parser')
        imgs = soup.find_all('img', class_='entry-thumbnail')
        photos = []
        for img in imgs:
            url = img['src']
            url = url.replace('superthumb', 'original')
            url = url.split('?', 1)[0]
            photos.append(url)
        return photos


def get_collection_photos(username, collection_id, path):
    heart = WeHeartIt(username, collection_id)
    idx = 0
    if not os.path.exists(path):
        os.mkdir(path)
    for photo_url in heart.photos():
        photo_name = number1(photo_url) + '.' + photo_url.split('.')[-1]
        full_path = os.path.join(path, photo_name)
        threadPoolExecutor.submit(file_utils.save_from_url, url=photo_url,
                                  headers={
                                      'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36'
                                  },
                                  name=full_path,
                                  index=idx)
        idx += 1


if __name__ == '__main__':
    we_heart_it = get_collection_photos('ma_yu_scandal', '106301429-', '/home/einverne/Pictures/weheartid')

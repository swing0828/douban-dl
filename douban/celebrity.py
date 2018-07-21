#!/usr/bin/env python3
# -*- coding:utf-8 -*-
import requests
from bs4 import BeautifulSoup


class Celebrity:
    BASE_URL = "https://movie.douban.com/celebrity/{}/photos/"

    def __init__(self, celebrity_id):
        self.url = Celebrity.BASE_URL.format(celebrity_id)

    def photos(self):
        start = 0
        while True:
            next_photos = self.__photos(start)
            step = len(next_photos)
            if 0 == step:
                break
            for photo in next_photos:
                # https://img3.doubanio.com/view/photo/thumb/public/p2156276775.jpg
                # https://img3.doubanio.com/view/photo/raw/public/p2156276775.jpg
                # https://img3.doubanio.com/view/photo/photo/public/p2156276775.webp
                # src https://img3.doubanio.com/view/photo/m/public/p2179264053.webp
                src = photo.img['src']
                if 'm/public' in src:
                    src = src.replace("photo/m", "photo/raw")
                if 'photo/thumb' in src:
                    src = src.replace("photo/thumb", "photo/raw")
                if 'webp' in src:
                    src = src.replace("webp", "jpg")
                yield photo.a['href'], src
            start += step

    def __photos(self, start):
        params = {
            "type": "C",
            "start": start,
            "sortby": "like",
            "size": "a",
            "subtype": "a"
        }
        header = {
            'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.115 Safari/537.36'
        }
        r = requests.get(self.url, params=params, headers=header)
        soup = BeautifulSoup(r.text, "html.parser")
        return soup.find_all("div", class_="cover")

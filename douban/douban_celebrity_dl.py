#!/usr/bin/env python3
# -*- coding:utf-8 -*-
import os

from douban.celebrity import Celebrity
from utils import file_utils


def get_celebrity(celebrity, path):
    idx = 0
    if not os.path.exists(path):
        os.mkdir(path)
    os.chdir(path)
    for refer, photo_url in celebrity.photos():
        name = os.path.basename(photo_url)
        if os.path.exists(name):
            print("pic {} exist skip".format(name))
            continue
        print("{}: saving {}".format(idx, name))
        headers = {
            "Referer": refer,
            "user-agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.104 Safari/537.36"
        }
        file_utils.save_from_url(photo_url, headers, name)
        idx += 1
    print("saving celebrity photo to {}".format(path))


if __name__ == "__main__":
    celebrity_id = "1335340"
    celebrity = Celebrity(celebrity_id)
    path = os.path.expanduser("~") + "/Pictures/celebrity/" + celebrity_id
    get_celebrity(celebrity, path)

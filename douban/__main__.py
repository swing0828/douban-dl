#!/usr/bin/env python
# -*- coding: utf-8 -*-
import argparse
import re

from douban.album import Album
from douban.celebrity import Celebrity
from douban.douban_album_dl import get_album
from douban.douban_celebrity_dl import get_celebrity


def get_args():
    """
    argparse 选项的默认语法是基于 Unix 约定， `-` 来表示命令行开关
    :return:
    """
    parser = argparse.ArgumentParser(prog='Douban downloader',
                                     description="""
                                         A tiny tool to download douban resources
                                        """)
    parser.add_argument("url", help="start url of album or celebrity page")
    parser.add_argument('path', default='./douban', nargs='?', help='the path to store all resources defaul is ./douban')  # 可选
    # parser.add_argument('-a', '--album', help='album id', action='store')
    # parser.add_argument('-c', '--celebrity', help='celebrity id', action='store')
    return parser.parse_args()


def parse_url(url, path):
    """
    https://www.douban.com/photos/album/<album_id>
    https://movie.douban.com/celebrity/<celebrity_id>
    :param url:
    :return:
    """
    match = re.match(r'(http|https)://www.douban.com/photos/album/(\d+)', url)
    if match:
        album_id = match.group(2)
        album = Album(album_id)
        get_album(album, path)
        return
    match = re.match(r'(http|https)://movie.douban.com/celebrity/(\d+)', url)
    if match:
        celebrity_id = match.group(2)
        celebrity = Celebrity(celebrity_id)
        get_celebrity(celebrity, path)
        return
    print("Not support this url yet")


def main():
    """Main entry point"""
    args = get_args()
    if args.url is not None:
        parse_url(args.url, args.path)


if __name__ == '__main__':
    main()

douban downloader
=======================

一个简单的下载豆瓣相册、图集、影人图片的小脚本

A simple python script to download douban albums and celebrity


Introduction
-----

目前支持的下载类型

1. 豆瓣相册，比如

        douban-dl https://www.douban.com/photos/album/1641641224/

2. 影人相册图片

        douban-dl https://movie.douban.com/celebrity/1335340/
        douban-dl https://movie.douban.com/celebrity/1335340/photos
    
3. 用户所有相册

        douban-dl https://www.douban.com/people/einverne/
    

4. 电影剧照

        douban-dl https://movie.douban.com/subject/26804147
        
5. We Heart It 

        douban-dl https://weheartit.com/ma_yu_scandal/collections/106301429-

Installation
------------

    $ pip install douban-dl


Usage
-----

    $ douban-dl url [path]

`url` should be like this:

    https://www.douban.com/photos/album/<album_id>
    https://movie.douban.com/celebrity/<celebrity_id>
    https://www.douban.com/people/<douban_id>/photos

`path` is the folder where images saved, defaults to `./douban`.

如果没有指定 `path` ，默认会保存到当前目录下 douban 文件夹中。

更新日志
-------

2019-01-08 增加 We Heart It 支持


License
-------

MIT


Contribute
----------

Feel free to file an issue, or make a pr.

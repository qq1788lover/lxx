#coding : utf-8
#__author__:'sareeliu'
#__date__ : '2018/11/24 15:47'

import requests,sqlite3,re
from contextlib import closing


def download_file(url, path):
    with closing(requests.get(url, stream=True)) as r:
        chunk_size = 1024
        content_size = int(r.headers['content-length'])
        print(content_size)
        with open(path, "wb") as f:
            for chunk in r.iter_content(chunk_size=chunk_size):
                f.write(chunk)
            print("下载完成")


if __name__ == '__main__':

    # 从数据库获取 没被下载过的资源 的结果集，存入list列表
    conn = sqlite3.connect("lxx.db")
    c = conn.cursor()
    db_result = c.execute("select * from yazhou WHERE token = 0 ")
    result_list = []
    for u in db_result:
        result_list.append(u)
    conn.commit()
    conn.close()

    for i in result_list:
        video_name = re.sub("[“”（）？，、。！【】\s]", "", str(i[0]))  # 片名
        prefix = "F:\\videotutorial\\ceshi\\"
        oldpath = prefix + "oldvideo\\" + video_name + ".mp4"
        download_file(i[1], oldpath)
        break
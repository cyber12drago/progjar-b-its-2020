import logging
import requests
import os
import threading
import logging

def download_gambar(angka,url=None):
    if (url is None):
        return False
    ff = requests.get(url)
    tipe = dict()
    tipe['image/png']='png'
    tipe['image/jpg']='jpg'
    tipe['image/jpeg']='jpg'
    content_type = ff.headers['Content-Type']
    logging.warning(content_type)
    if (content_type in list(tipe.keys())):
        namafile = os.path.basename(url)
        namafile= os.path.splitext(namafile)
        ekstensi = tipe[content_type]
        logging.warning(f"writing {namafile[0]}.{ekstensi}")
        fp = open(f"{namafile[0]}({angka+1}).{ekstensi}","wb")
        fp.write(ff.content)
        fp.close()

    else:
        return False




threads = []

if __name__=='__main__':
    for i in range(5):
        t = threading.Thread(target=download_gambar, args=(i,'https://asset.kompas.com/crops/qz_jJxyaZgGgboomdCEXsfbSpec=/0x0:998x665/740x500/data/photo/2020/03/01/5e5b52f4db896.jpg',))
        t.start()


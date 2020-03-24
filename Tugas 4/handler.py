import os

class Person:

    def __init__(self):
        if os.path.exists('file') == False:
            os.makedirs('file')

    def add_file(self,namafile=None,isifile=None):
        f = open('file/' + namafile, 'wb')
        f.write(isifile)
        return True

    def download_file(self,namafile=None):
        f = open('file/' + namafile, 'rb')
        hasil = f.read()
        f.close()
        hasil = str(hasil, "utf-8")
        return hasil

    def list_file(self):
        hasil = os.listdir('file')
        return hasil

if __name__=='__main__':
    p = Person()
<h1>Tugas 4</h1>

<h2>Protokol</h2>
![Protokol](img src="https://github.com/cyber12drago/progjar-b-its-2020/blob/master/Tugas%204/Dokumentasi/Protokol.jpg" )

<h2>Cara Menjalankan</h2>
1. Pertama jalankan server.py
2. Lalu server.py akan melakukan request ke file person_machine.py. 
3. Di person_machine.py, akan dibagi beberapa command yg akan di request ke salah satu fungsi file handler.py.
4. Setelah itu, bisa menjalankan beberapa client seperti berikut

a. FileAdd
Respon yang didapat:
![Add](https://github.com/cyber12drago/progjar-b-its-2020/blob/master/Tugas%204/Dokumentasi/AddFile.jpg" )

hasil setelah dijalankan bisa dicek di folder "file
![HasilAdd]("https://github.com/cyber12drago/progjar-b-its-2020/blob/master/Tugas%204/Dokumentasi/AddSetelahDijalankan.jpg")

b. FileDownload
Respon yang didapat:
![Download]("https://github.com/cyber12drago/progjar-b-its-2020/blob/master/Tugas%204/Dokumentasi/DownloadFile.jpg" )

hasil setelah dijalankan bisa dicek di root
![HasilDownload]("https://github.com/cyber12drago/progjar-b-its-2020/blob/master/Tugas%204/Dokumentasi/DownloadSetelahDijalankan.jpg")

c. ListFile
Respon yang didapat:
![ListFile]("https://github.com/cyber12drago/progjar-b-its-2020/blob/master/Tugas%204/Dokumentasi/ListFile.jpg")

5. Setelah itu hasil request akan kembali ke person_machine.py dan kembali ke server

<h2>Server</h2>
![Server]("https://github.com/cyber12drago/progjar-b-its-2020/blob/master/Tugas%204/Dokumentasi/Server.jpg" )

<h2>Cara Melakukan Request</h2>
Untuk melakukan sebuah request, edit namafile terlebih dahulu di file client_add.py atau client_get.py sesuai dengan nama yang diinginkan.
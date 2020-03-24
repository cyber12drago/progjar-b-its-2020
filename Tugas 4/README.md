<h1>Tugas 4</h1>

<h2>Protokol</h2>
<img src="Dokumentasi/protokol.JPG" >

<h2>Cara Menjalankan</h2>
1. Pertama jalankan server.py
2. Lalu server.py akan melakukan request ke file person_machine.py. 
3. Di person_machine.py, akan dibagi beberapa command yg akan di request ke salah satu fungsi file handler.py.
4. Setelah itu, bisa menjalankan beberapa client seperti berikut

a. FileAdd
Respon yang didapat:
<img src="Dokumentasi/AddFile.JPG" >

hasil setelah dijalankan bisa dicek di folder "file
<img src="Dokumentasi/AddSetelahDijalankan.JPG" >

b. FileDownload
Respon yang didapat:
<img src="Dokumentasi/DownloadFile.JPG" >

hasil setelah dijalankan bisa dicek di root
<img src="Dokumentasi/DownloadSetelahDijalankan.JPG" >

c. ListFile
Respon yang didapat:
<img src="Dokumentasi/ListFile.JPG" >

5. Setelah itu hasil request akan kembali ke person_machine.py dan kembali ke server

<h2>Server</h2>
<img src="Dokumentasi/server.JPG" >

<h2>Cara Melakukan Request</h2>
Untuk melakukan sebuah request, edit namafile terlebih dahulu di file client_add.py atau client_get.py sesuai dengan nama yang diinginkan.
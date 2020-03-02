# Tugas 2
Nama: Muhammad Naufal Refadi
 NRP: 05111740000097
 Kelas: Progjar-B

##### 1. Capture hasil keluaran dari program udpfileclient.py ke alamat 127.0.0.1 ke port 5006
* Pada file udpclient.py , modifikasilah TARGET_IP = "127.0.0.1" dan TARGET_PORT = 5006
* Buka Wireshark dengan interface "Adaptor Loopback traffic capture" dan gunakan filter "ip.src == 127.0.0.1 && ip.dst == 127.0.0.1 && udp.port==5006"
* Capture hasil
Hasil:
![Image description](https://github.com/cyber12drago/progjar-b-its-2020/blob/master/Tugas%202/wireshark_udpclientcapture.jpg)


##### 2. Capture hasil keluaran dari program udp_simple.py ke alamat 127.0.0.1 ke port 5006
* Pada file udp_simple.py , modifikasilah TARGET_IP = "127.0.0.1" dan TARGET_PORT = 5006
* Buka Wireshark dengan interface "Adaptor Loopback traffic capture" dan gunakan filter "ip.src == 127.0.0.1 && ip.dst == 127.0.0.1 && udp.port==5006"
* Capture hasil
Hasil:
![Image description](https://github.com/cyber12drago/progjar-b-its-2020/blob/master/Tugas%202/wireshark_udp_simplecapture.jpg)
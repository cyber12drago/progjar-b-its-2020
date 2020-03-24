from handler import Person
import json
import logging

'''
FORMAT PROTOKOL

string terbagi menjadi 2 bagian yang dipisahkan oleh spasi
Format : command *spasi* parameter *spasi* parameter

Fitur:

a. Meletakkan File  
   Untuk meletakkan file ke dalam folder "file"
   Request : add
   Parameter : namafile *spasi* isi dari file
   Response : berhasil -> "Success"
              gagal -> "ERROR"
              
b. Mengambil File
   Untuk mengambil file berdasarkan nama file yang ada pada folder "file"
   Request : download
   Parameter : namafile yang ingin diambil
   Response: hasil download file sa

c. Melihat List File
   Berguna untuk melihat list file yang ada di dalam folder "file"
   Request : list
   Parameter: -
   Response: list file yang ada di dalam folder "file"

d. Jika command tidak dikenali akan merespon dengan ERRCMD

'''
p = Person()

class PersonMachine:
    def proses(self, string_to_process):
        s = string_to_process
        commands = s.split(" ")
        try:
            command = commands[0].strip()
            #print(command)
            if (command == 'add'):
                logging.warning("add")

                file_name = commands[1].strip()
                file_data = commands[2].strip()
                p.add_file(file_name, file_data.encode())
                return "Success"
            elif (command == 'download'):
                logging.warning("download")
                file_name = commands[1].strip()
                hasil = p.download_file(file_name)
                return hasil
            elif (command == 'list'):
                logging.warning("list")
                list_data = {}
                list_data['files'] = []
                hasil = p.list_file()
                for file in hasil:
                    list_data['files'].append({"namafile": file})
                return json.dumps(list_data, indent=4)
            else:
                return "ERRCMD"
        except:
            return "ERROR"


if __name__ == '__main__':
    pm = PersonMachine()
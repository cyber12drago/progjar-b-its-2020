import sys
import os.path
import uuid
from glob import glob
from datetime import datetime

class HttpServer:
	def __init__(self):
		self.sessions={}
		self.types={}
		self.types['.pdf']='application/pdf'
		self.types['.jpg']='image/jpeg'
		self.types['.txt']='text/plain'
		self.types['.html']='text/html'
	def response(self,kode=404,message='Not Found',messagebody='',headers={}):
		tanggal = datetime.now().strftime('%c')
		resp=[]
		resp.append("HTTP/1.0 {} {}\r\n" . format(kode,message))
		resp.append("Date: {}\r\n" . format(tanggal))
		resp.append("Connection: close\r\n")
		resp.append("Server: myserver/1.0\r\n")
		resp.append("Content-Length: {}\r\n" . format(len(messagebody)))
		for kk in headers:
			resp.append("{}:{}\r\n" . format(kk,headers[kk]))
		resp.append("\r\n")
		resp.append("{}" . format(messagebody))
		response_str=''
		for i in resp:	
			response_str="{}{}" . format(response_str,i)
		return response_str

	def proses(self,data):
		requests = data.split("\r\n")
		#print(requests)

		baris = requests[0]
		#print(baris)

		all_headers = [n for n in requests[1:] if n!='']

		j = baris.split(" ")
		try:
			method=j[0].upper().strip()
			if (method=='GET'):
				object_address = j[1].strip().replace('/', '')
				print(object_address)
				return self.http_get(object_address, all_headers)
			if (method=='POST'):
				object_address = j[1].strip()
				temp1 = requests[-1].split("=")
				temp2 = temp1[1]
				print(temp1, temp2)
				return self.http_post(object_address,  all_headers,temp2)
			else:
				return self.response(400,'Bad Request','',{})
		except IndexError:
			return self.response(400,'Bad Request','',{})
	def http_get(self,object_address,headers):
		headers = {}
		if object_address == 'sending.html':
			fp = open(object_address, 'r')
			isi = fp.read()
			headers['Content-type'] = "text/html"
		else:
			isi = '<h1>SERVER HTTP</h1>'
		return self.response(200, 'OK', isi, headers)
	def http_post(self,object_address,headers,form):
		temp_head=headers
		headers={}
		temp=""
		for i in temp_head:
			temp = temp+i+"\n"
		isi= "Hasil:"+form+"\n"+temp
		return self.response(200,'OK',isi,headers)

















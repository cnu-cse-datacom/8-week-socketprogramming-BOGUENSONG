import socket
import os



ip_addr = 'localhost'
port = 9000
socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
socket.connect((ip_addr,port))

filename =input("Input your file name : ")
size = os.path.getsize(filename)

print("File Transmit Start....")
socket.sendto(filename.encode(),(ip_addr, port))
socket.sendto(str(size).encode(),(ip_addr, port))

data_transferred = 0 #데이터 전송받기
with open(filename, 'rb') as f:
    try:
        data = f.read(1024) # 파일을 1024바이트 읽음
        while data: # 파일이 빈 문자열일때까지 반복
            data_transferred += socket.send(data)
            data = f.read(1024)
            print('current_size / total_size = %d/%d, %f%%' %(data_transferred , size , (data_transferred/size * 100)))
    except Exception as e:
        print(e)

print("ok")
print("file_send_end")
f.close()

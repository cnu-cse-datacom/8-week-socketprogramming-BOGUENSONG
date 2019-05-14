import socket

server_sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server_sock.bind(('', 9000))

data, addr = server_sock.recvfrom(1024)
print("file recv start from ", addr[0])
print(data)

filename = data.decode()
print("File Name:", filename)

data, addr = server_sock.recvfrom(1024)
size = int(data.decode())
print("File Size:", size)

data_transferred = 0 #데이터 전송받기
percent = 0 #퍼센트
data = server_sock.recv(1024)
with open('download/' + filename, 'wb') as f:
    try:
        
        
        while (data):
            f.write(data)
            data_transferred += len(data)
            percent = (data_transferred / size) * 100 
            print('current_size / total_size = %d/%d, %f%%' %(data_transferred , size , percent))
            if (percent >= 100) :
                break
            data = server_sock.recv(1024)

    except Exception as e:
        print(e)



f.close()
server_sock.close()

# coding=utf-8
import socket
from threading import Thread

client = {}
addresses = {}

accept_num = 10

host = '127.0.0.1'
port = 8848

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((host, port))


def handle_client_in(conn, addr):
    nikename = conn.recv(1024).decode('utf8')
    welcome = f'\n\n欢迎 {nikename}\n'
    client[conn] = nikename
    brodcast(bytes(welcome, 'utf8'))

    while True:

        try:
            msg = conn.recv(1024)
            brodcast(msg, '\n'+nikename+':\n')
        except:
            del client[conn]
            brodcast(bytes(f'\n\n{nikename} 离开聊天室\n', 'utf8'))


def brodcast(msg, nikename=''):
    for conn in client:
        print(msg)
        conn.send(bytes(nikename, 'utf8') + msg)


if __name__ == '__main__':
    s.listen(accept_num)
    print('OK.....')

    while True:
        conn, address = s.accept()
        print(address, 'OK')
        conn.send('欢迎来到聊天室\n请输入昵称进行聊天'.encode('utf8'))
        addresses[conn] = address
        Thread(target=handle_client_in, args=(conn, address)).start()
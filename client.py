import socket
import threading

nickname = input("Choose a nickname: ")

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(('18.175.45.228', 55555)) 

def receive():
    while True:
        try:
            message = client.recv(1024).decode('ascii')
            if message == 'NICK':
                pass
            else:
                print(message)

        except:
            print("An error occurred")
            client.close()
            break

def write():
    while True:
        message = f'{nickname}: {input("")}'
        client.send(message.encode('ascii'))

receive_thread = threading.Thread(target = receive)
receive_thread.start()

write_thread = threading.Thread(target = write)
write_thread.start()

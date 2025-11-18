import socket,time
s=socket.socket()
s.bind(("127.0.0.1",9001))
s.listen()
s.settimeout(1)
print("server listening")
time.sleep(2)
print("Connection from ()")

while True:
    try:
        c,_=s.accept()
        print(f"recieved: {c.recv(4096).decode(errors='replace')}")
        print("sent ACK")
        c.sendall(b"ACK")
        c.close()
    except TimeoutError:pass
import socket
import os

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
    sock.bind(('127.0.0.1', 8888))
    sock.listen(socket.SOMAXCONN)

    while True:
        conn, adr = sock.accept()
        with conn:
            data = conn.recv(1024)
            if not data or data.decode() == "exit":
                break
            data = data.decode()[:-1]
#            print(data)
            items = data.split(" ")
#            print(items)
            if items[0] == "put":
                try:
                    value = int(items[2])
                    timestamp = int(items[3])
                except ValueError:
                    conn.sendall(b"error\nwrong command\n\n")
                    continue

                if value < 0 or timestamp < 0:
                    conn.sendall(b"error\nwrong command\n\n")
                    continue

                to_write = "|".join(items[1:]) + "\n"
    #        print(to_write)
                with open("data.txt", "a+") as f:
                    f.write(to_write)
                    conn.sendall(b"ok\n\n")
            elif items[0] == "get":
                key = items[1]
#                print(key)
                with open("data.txt", "r") as f:
                    message = "ok\n"
                    if key == "*":
                        content = f.read()
                        if content == "":
                            message = message + "\n"
                        else:
                            message = message + content.replace("|", " ") + "\n"
                    else:
                        lines = f.readlines()
                        content = ""
                        for line in lines:
                            if key == line[:-1].split("|")[0]:
                                content = content + line
                        if content == "":
                            message = "error\nwrong command\n\n"
                        else:
                            message = message + content.replace("|", " ") + "\n"


                    conn.sendall(message.encode())

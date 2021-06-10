import socket
import time


def sorter(x):
    return x[0]


class ClientError(Exception):
    pass


class Client:

    def __init__(self, host, port, timeout=None):
        self.host = host
        self.port = port
        self.timeout = timeout

        self.sock = socket.create_connection((self.host, self.port), self.timeout)

    def put(self, key, value, timestamp=None):
        if timestamp is None:
            timestamp = str(int(time.time()))
        else:
            timestamp = str(timestamp)
        message = " ".join(["put", str(key), str(value), timestamp]) + "\n"
        self.sock.sendall(message.encode())
        data = self.sock.recv(1024).decode()

        if data == "error\nwrong command\n\n":
            raise ClientError

    def get(self, key):
        result = {}
        keys = []
        message = " ".join(["get", str(key)]) + "\n"
        self.sock.sendall(message.encode())
        data = self.sock.recv(1024).decode()

        if data.split("\n")[0] != "ok":
            raise ClientError

        units = data.split("\n")[1:-2]

        for unit in units:

            items = unit.split(" ")

            if len(items) != 3:
                raise ClientError

            if not result.get(items[0]):
                result[items[0]] = []

            result[items[0]].append((int(items[2]), float(items[1])))
            result[items[0]].sort(key=sorter)

        return result


"""
    def exit(self):
        with socket.create_connection((self.host, self.port), self.timeout) as sock:
            sock.sendall(b"exit")
"""
import asyncio

#storage = {'key': [(5678, 0.6), (1234, 4.0)]}
storage = {}


def run_server(host, port):
    loop = asyncio.get_event_loop()
    coro = loop.create_server(ClientServerProtocol, host, port)
    server = loop.run_until_complete(coro)

    try:
        loop.run_forever()
    except KeyboardInterrupt:
        pass

    server.close()
    loop.run_until_complete(server.wait_closed)
    loop.close()


class ClientServerProtocol(asyncio.Protocol):

    def __init__(self):
        super().__init__()

    def connection_made(self, transport):
        self.transport = transport

    def data_received(self, data):
        resp = self.process_data(data.decode())
        self.transport.write(resp.encode())

    def process_data(self, data):
        if data == "\n":
            return "error\nwrong command\n\n"
        parsed_data = data[:-1].split()
        action = parsed_data[0]

        if action == "put":

            if len(parsed_data) != 4:
                return "error\nwrong command\n\n"

            key, value, timestamp = parsed_data[1:]
            if key == "" or value == "":
                return "error\nwrong command\n\n"

            result = self.put(key, value, timestamp)
            return result
        elif action == "get":

            if len(parsed_data) != 2:
                return "error\nwrong command\n\n"

            key = parsed_data[1]
            if key == "":
                return "error\nwrong command\n\n"

            result = self.get(key)
            return result
        else:
            return "error\nwrong command\n\n"

    def put(self, key, value, timestamp):

        try:
            value = float(value)
            timestamp = int(timestamp)

            if storage.get(key) is None:
                storage[key] = []

            for item in storage[key]:
                if item[0] == timestamp and value >= 0:
                    storage[key].remove(item)
                    storage[key].append((timestamp, value))
                    return "ok\n\n"

            if value >= 0:
                storage[key].append((timestamp, value))
                return "ok\n\n"
            else:
                return "error\nwrong command\n\n"
        except ValueError:
            return "error\nwrong command\n\n"

    def get(self, key):
        if key == "*":
            result = "ok\n"

            for k in storage.keys():
                for item in storage[k]:
                    result = result + " ".join([k, str(item[1]), str(item[0])]) + "\n"

            result = result + "\n"
            return result
        elif key in storage.keys():
            result = "ok\n"
            for item in storage[key]:
                result = result + " ".join([key, str(item[1]), str(item[0])]) + "\n"

            result = result + "\n"
            return result
        else:
            return "ok\n\n"


#run_server("127.0.0.1", 8888)

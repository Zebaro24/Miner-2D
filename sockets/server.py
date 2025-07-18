# server.py
from socket import socket, AF_INET, SOCK_STREAM
from pickle import dumps, loads
from threading import Thread

from map_miner import MapMiner


class Server(socket):
    def __init__(self, host, port, width=100, height=100):
        super().__init__(AF_INET, SOCK_STREAM)
        self.host = host
        self.port = port
        self.players_list = []
        self.client_handlers = []
        self.map = MapMiner(width, height)
        self.map.generate_map()

    def run(self):
        self.bind((self.host, self.port))
        self.listen(5)
        print(f"Server is listening on {self.host}:{self.port}")

        while True:
            try:
                client_socket, client_address = self.accept()
                print(f"Accepted connection from {client_address}")

                client_handler = ClientHandler(client_socket, self)
                self.client_handlers.append(client_handler)
                client_handler.send_initial_world_state()
                client_handler.start()
            except OSError as e:
                print(f"Error accepting connection: {e}")

    def send_changes(self, changes, changes_handler):
        self.map.receive_changes(changes)
        for handler in self.client_handlers:
            if handler != changes_handler:
                handler.send_to_client("changes", changes)


class ClientHandler(Thread):
    def __init__(self, client_socket, server):
        super().__init__()
        self.client_socket = client_socket
        self.server = server

    def send_to_client(self, type_data, data):
        dict_data = {
            "type": type_data,
            "data": data
        }
        data_pickle = dumps(dict_data)
        self.client_socket.send(data_pickle)

    def receive_from_client(self, dict_data):
        print(f"receive {dict_data}")
        if dict_data["type"] == "changes":
            self.server.send_changes(dict_data["data"], self)
        elif dict_data["type"] == "end":
            self.server.client_handlers.remove(self)
            print(f"Client {self.client_socket.getpeername()} has disconnected.")
            self.client_socket.close()

    def send_initial_world_state(self):
        # Отправка начального состояния мира новому клиенту
        self.send_to_client("world_map", self.server.map)

    def run(self):
        try:
            while True:
                data = self.client_socket.recv(40960)
                if not data:
                    break
                dict_data = loads(data)
                self.receive_from_client(dict_data)
        except OSError as e:
            print(f"OSError occurred: {e}")
        finally:
            self.client_socket.close()
            self.server.client_handlers.remove(self)
            print(f"Closed connection. Remaining clients: {len(self.server.client_handlers)}")



if __name__ == "__main__":
    my_server = Server("127.0.0.1", 12345)  # Пример адреса и порта
    my_server.run()

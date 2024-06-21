# server.py
import socket
import pickle  # Для сериализации данных
import threading


class Server:
    def __init__(self, host, port):
        self.host = host
        self.port = port
        self.server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.client_handlers = {}  # Словарь для хранения клиентских обработчиков
        self.world_map = self.generate_world_map()  # Генерация мира игры
        self.player_count = 0  # Счетчик игроков

    def start(self):
        self.server_socket.bind((self.host, self.port))
        self.server_socket.listen(5)
        print(f"Server is listening on {self.host}:{self.port}")

        while True:
            client_socket, client_address = self.server_socket.accept()
            print(f"Accepted connection from {client_address}")

            # Создание нового обработчика клиента
            client_handler = ClientHandler(client_socket, self, self.player_count)
            self.client_handlers[self.player_count] = client_handler
            self.player_count += 1

            # Отправляем новому клиенту текущее состояние мира
            client_handler.send_initial_world_state()

            # Запуск потока для обработки клиента
            client_handler.start()

    def generate_world_map(self):
        # Генерация и возвращение начального состояния мира
        return [[0 for _ in range(100)] for _ in range(100)]  # Пример: мир 100x100 с пустыми блоками

    def broadcast_world_state(self):
        # Отправка текущего состояния мира всем клиентам
        data = pickle.dumps(self.world_map)
        for client_id, client_handler in self.client_handlers.items():
            client_handler.send_data(data)

    def update_world_state(self, new_world_map):
        # Обновление состояния мира на сервере
        self.world_map = new_world_map
        self.broadcast_world_state()


class ClientHandler(threading.Thread):
    def __init__(self, client_socket, server, client_id):
        super().__init__()
        self.client_socket = client_socket
        self.server = server
        self.client_id = client_id

    def send_data(self, data):
        self.client_socket.send(data)

    def send_initial_world_state(self):
        # Отправка начального состояния мира новому клиенту
        data = pickle.dumps(self.server.world_map)
        self.client_socket.send(data)

    def run(self):
        while True:
            try:
                data = self.client_socket.recv(4096)
                if not data:
                    break
                # Обработка данных от клиента, например, изменение состояния мира
                received_map = pickle.loads(data)
                self.server.update_world_state(received_map)
            except Exception as e:
                print(f"Error handling client {self.client_id}: {e}")
                break


if __name__ == "__main__":
    my_server = Server("localhost", 12345)  # Пример адреса и порта
    my_server.start()

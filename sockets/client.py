import socket
import pickle  # Для десериализации данных


class Client:
    def __init__(self, ip):
        self.host, self.port = ip.split(":")
        self.client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.client_socket.connect((self.host, int(self.port)))
        print(f"Connected to server {self.host}:{self.port}")

        self.world_map = None

    def send_data(self, data):
        try:
            serialized_data = pickle.dumps(data)
            self.client_socket.sendall(serialized_data)
        except Exception as e:
            print(f"Error sending data: {e}")

    def receive_data(self):
        try:
            data_chunks = []
            while True:
                chunk = self.client_socket.recv(4096)
                if not chunk:
                    break
                data_chunks.append(chunk)
            serialized_data = b"".join(data_chunks)
            self.world_map = pickle.loads(serialized_data)
        except Exception as e:
            print(f"Error receiving data: {e}")

    def close(self):
        self.client_socket.close()

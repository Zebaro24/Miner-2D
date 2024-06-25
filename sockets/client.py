from socket import socket, AF_INET, SOCK_STREAM
from threading import Thread
from pickle import dumps, loads

from map_miner import MapMiner
from scenes.miner_2d import Miner2D


class Client(socket, Thread):
    def __init__(self, ip_address, miner_2d: Miner2D):
        socket.__init__(self, AF_INET, SOCK_STREAM)
        Thread.__init__(self)
        self.miner_2d = miner_2d
        self.host, self.port = ip_address.split(":")
        self.connect((self.host, int(self.port)))
        print(f"Connected to server {self.host}:{self.port}")

    def set_world_map(self, world_map: MapMiner):
        world_map.send_changes_func = self.send_changes
        self.miner_2d.map = world_map
        self.miner_2d.set_player()

    def send_changes(self, changes):
        self.send_to_server("changes", changes)

    def set_changes(self, changes):
        self.miner_2d.map.receive_changes(changes)

    def send_to_server(self, type_data, data):
        dict_data = {
            "type": type_data,
            "data": data
        }
        print(dict_data)
        data_pickle = dumps(dict_data)
        self.sendall(data_pickle)

    def receive_from_server(self, dict_data):
        if dict_data["type"] == "changes":
            self.set_changes(dict_data["data"])
        elif dict_data["type"] == "world_map":
            print("gg")
            self.set_world_map(dict_data["data"])

    def run(self):
        while True:
            data = self.recv(40960)
            if not data:
                break
            dict_data = loads(data)
            self.receive_from_server(dict_data)

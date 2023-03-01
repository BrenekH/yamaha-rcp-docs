#!/bin/env python
import socket
from pathlib import Path

addr, port = "192.168.0.128", 49280

out_file = Path.cwd() / "saved_notifies.txt"
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# s.settimeout(5)
s.connect((addr, port))

with out_file.open("a") as f:
    while True:
        f.write(s.recv(1024).decode())

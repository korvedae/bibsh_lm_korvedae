#!/usr/bin/python3
import socket
import os, os.path
import sys


# Resolve socket path
xdg_runtime_dir = os.environ.get("XDG_RUNTIME_DIR")

if not xdg_runtime_dir:
	raise EnvironmentError("Missing XDG_RUNTIME_DIR or HYPRLAND_INSTANCE_SIGNATURE environment variable.")

base_path = os.path.join(xdg_runtime_dir, "bibsh")
socket_path = f'{base_path}/bibsh_wm.client.sock'

print(socket_path)

def _send_wm_command(command):
	with socket.socket(socket.AF_UNIX, socket.SOCK_STREAM) as sock:
		sock.connect(socket_path)
		sock.sendall(command.encode())
		response = sock.recv(4096)
		return response.decode().strip()

_send_wm_command(' '.join(sys.argv[1:]))

#!/usr/bin/python3
import socket
import os, os.path


# Resolve socket path
xdg_runtime_dir = os.environ.get("XDG_RUNTIME_DIR")
hypr_sig = os.environ.get("HYPRLAND_INSTANCE_SIGNATURE")

if not xdg_runtime_dir or not hypr_sig:
	raise EnvironmentError("Missing XDG_RUNTIME_DIR or HYPRLAND_INSTANCE_SIGNATURE environment variable.")

base_path = os.path.join(xdg_runtime_dir, "hypr", hypr_sig)
command_socket_path = os.path.join(base_path, ".socket.sock")

# Send a command to Hyprland
def _send_hypr_command(command: str):
	with socket.socket(socket.AF_UNIX, socket.SOCK_STREAM) as sock:
		sock.connect(command_socket_path)
		sock.sendall(command.encode())
		response = sock.recv(4096)
		return response.decode().strip()

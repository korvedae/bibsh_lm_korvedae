#!/usr/bin/python3
import socket
import sys
import struct
import threading
import time
import os, os.path


# Resolve socket paths
xdg_runtime_dir = os.environ.get("XDG_RUNTIME_DIR")
hypr_sig = os.environ.get("HYPRLAND_INSTANCE_SIGNATURE")

if not xdg_runtime_dir or not hypr_sig:
	raise EnvironmentError("Missing XDG_RUNTIME_DIR or HYPRLAND_INSTANCE_SIGNATURE environment variable.")


base_path = os.path.join(xdg_runtime_dir, "hypr", hypr_sig)
event_socket_path = os.path.join(base_path, ".socket2.sock")
command_socket_path = os.path.join(base_path, ".socket.sock")

client_socket_path = f'{os.environ.get("XDG_RUNTIME_DIR")}/hypr_span.client.sock'


# Listener for Hyprland events
def listen_to_events():
	with socket.socket(socket.AF_UNIX, socket.SOCK_STREAM) as sock:
		sock.connect(event_socket_path)
		while True:
			data = sock.recv(4096)
			if not data:
				break
			event_handler(data.decode().strip())
			print("Event:", data.decode().strip())

def _client_socket():
	try:
		os.unlink(client_socket_path)
	except OSError:
		if os.path.exists(client_socket_path):
			raise
	with socket.socket(socket.AF_UNIX, socket.SOCK_STREAM) as sock:
		sock.bind(client_socket_path)
		sock.listen()

		print(f'Client Socket Opened at {client_socket_path}')

		while True:
			conn, _ = sock.accept()
			with conn:
				print("Client connnected")
				data = conn.recv(1024)
				if data:
					command = data.decode()
					client_handler(command)
				else:
					print("No command specified.")
def client_handler(command: str):
	command = command.rstrip()
	print(f'Command recived "{command}"')
	match command:
		case "workspace":
			print("HELLO")
			send_command("dispatch workspace 1001")
			send_command("dispatch workspace 1002")
			send_command("dispatch workspace 1003")
	print(command)
	pass



# Send a command to Hyprland
def send_command(command: str):
    with socket.socket(socket.AF_UNIX, socket.SOCK_STREAM) as sock:
        sock.connect(command_socket_path)
        sock.sendall(command.encode())
        response = sock.recv(4096)
        print("Command Response:", response.decode().strip())

def event_handler(event: str):
	event_keyword = event.rstrip('>>')
	print(f'keyword parsed: {event_keyword}')

# Run event listener in a thread
event_thread = threading.Thread(target=listen_to_events, daemon=True)
event_thread.start()

# Create the client socket
client_socket = threading.Thread(target=_client_socket, daemon=True)
client_socket.start()


# Example: Send a test command
send_command("dispatch workspace 1")

# Keep the main thread alive to receive events
try:
    while True:
    	inp = input("Command")
except KeyboardInterrupt:
    print("Exiting.")

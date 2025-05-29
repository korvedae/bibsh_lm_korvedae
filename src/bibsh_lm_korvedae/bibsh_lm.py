#!/usr/bin/python3

import socket
import threading
import os, os.path
import shlex

def _init():
	from bibsh_lm_korvedae.components import hyprland
	from bibsh_lm_korvedae.components import config

	old_position = ''.join(hyprland._send_hypr_command("cursorpos")).replace(" ", '').split(',')

	if len(config.LayoutConfig['monitors']) > 9:
		print("Config Error: Only 9 monitors max.")
		return

	mon_range = len(config.LayoutConfig['monitors'])
	print(mon_range)

	for x in range(mon_range):
		y = (x + 1) * 5
		i = (y - 5) + 1

		while i <= (y):
			print(f'Workspace {i}')
			hyprland._send_hypr_command(f'dispatch moveworkspacetomonitor {i} {config.LayoutConfig['monitors'][x]}')
			i += 1

	hyprland._send_hypr_command(f'dispatch movecursor {old_position[0]} {old_position[1]}')

def main():
	from bibsh_lm_korvedae.components import config
	from bibsh_lm_korvedae.components import state
	config.init()
	state.init()

	# Commands
	from bibsh_lm_korvedae.commands import layout
	from bibsh_lm_korvedae.commands import movetolayoutsilent

	# Resolve socket paths
	xdg_runtime_dir = os.environ.get("XDG_RUNTIME_DIR")
	hypr_sig = os.environ.get("HYPRLAND_INSTANCE_SIGNATURE")

	if not xdg_runtime_dir or not hypr_sig:
		raise EnvironmentError("Missing XDG_RUNTIME_DIR or HYPRLAND_INSTANCE_SIGNATURE environment variable.")

	cache_dir = f'{os.environ.get("XDG_RUNTIME_DIR")}/bibsh'
	client_socket_path = f'{cache_dir}/bibsh_lm.client.sock'

	if os.path.exists(cache_dir) == False:
		os.mkdir(cache_dir)

	def _client_socket():
		try:
			os.unlink(client_socket_path)
		except OSError:
			if os.path.exists(client_socket_path):
				raise
		with socket.socket(socket.AF_UNIX, socket.SOCK_STREAM) as sock:
			sock.bind(client_socket_path)
			sock.listen()

			while True:
				conn, _ = sock.accept()
				with conn:
					print("Client connnected")
					data = conn.recv(1024)
					if data:
						command = data.decode()
						client_handler(command.rstrip())
					else:
						print("No command specified.")
	def client_handler(command_string: str):
		command = shlex.split(command_string)
		print(f'Command recived "{command}"')
		match command[0]:
			case "workspace":
				layout._run(command)
			case 'movetoworkspacesilent':
				movetolayoutsilent._run(command)
		pass

	_init()

	# Create the client socket
	client_socket = threading.Thread(target=_client_socket, daemon=True)
	client_socket.start()

	# Keep the main thread alive to receive events
	try:
		while True:
			pass
	except KeyboardInterrupt:
		print("\nExiting.")

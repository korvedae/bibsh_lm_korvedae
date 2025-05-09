import commands.SPCommand as spcommand

def _run(command):
	try:
		gotdata = command[1]
	except IndexError:
		return

	match command[1]:
		case "1":
			spcommand._send_hypr_command("dispatch workspace 1001")
			spcommand._send_hypr_command("dispatch workspace 1002")
			spcommand._send_hypr_command("dispatch workspace 1003")
		case "2":
			spcommand._send_hypr_command("dispatch workspace 1011")
			spcommand._send_hypr_command("dispatch workspace 1012")
			spcommand._send_hypr_command("dispatch workspace 1013")
		case "3":
			spcommand._send_hypr_command("dispatch workspace 1011")
			spcommand._send_hypr_command("dispatch workspace 1012")
			spcommand._send_hypr_command("dispatch workspace 1013")
		case _:
			print("This only supports 3 workspaces for now")

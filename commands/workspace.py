import commands.SPCommand as spcommand

def _run(command):
	try:
		gotdata = command[1]
	except IndexError:
		return

	match command[1]:
		case "1":
			test = spcommand._send_hypr_command('cursorpos')
			print(test)
			print(test)
			print(test)
			print(test)
			print(test)
			print(test)
			print(test)
			spcommand._send_hypr_command("dispatch workspace 1001")
			spcommand._send_hypr_command("dispatch workspace 1002")
			spcommand._send_hypr_command("dispatch workspace 1003")
		case "2":
			spcommand._send_hypr_command("dispatch workspace 1011")
			spcommand._send_hypr_command("dispatch workspace 1012")
			spcommand._send_hypr_command("dispatch workspace 1013")
		case "3":
			spcommand._send_hypr_command("dispatch workspace 1021")
			spcommand._send_hypr_command("dispatch workspace 1022")
			spcommand._send_hypr_command("dispatch workspace 1023")
		case "4":
			spcommand._send_hypr_command("dispatch workspace 1031")
			spcommand._send_hypr_command("dispatch workspace 1032")
			spcommand._send_hypr_command("dispatch workspace 1033")
		case "5":
			spcommand._send_hypr_command("dispatch workspace 1041")
			spcommand._send_hypr_command("dispatch workspace 1042")
			spcommand._send_hypr_command("dispatch workspace 1043")
		case _:
			print("This only supports 5 workspaces for now")

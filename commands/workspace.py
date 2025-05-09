import commands.SPCommand as spcommand

def _run(command):
	try:
		gotdata = command[1]
	except IndexError:
		return

	match command[1]:
		case "1":
			spcommand._send_hypr_command("dispatch moveworkspacetomonitor 1001 HDMI-A-2")
			spcommand._send_hypr_command("dispatch moveworkspacetomonitor 1002 DP-1")
			spcommand._send_hypr_command("dispatch moveworkspacetomonitor 1003 HDMI-A-1")
		case "2":
			spcommand._send_hypr_command("dispatch moveworkspacetomonitor 1011 HDMI-A-2")
			spcommand._send_hypr_command("dispatch moveworkspacetomonitor 1012 DP-1")
			spcommand._send_hypr_command("dispatch moveworkspacetomonitor 1013 HDMI-A-1")
		case "3":
			spcommand._send_hypr_command("dispatch moveworkspacetomonitor 1011 HDMI-A-2")
			spcommand._send_hypr_command("dispatch moveworkspacetomonitor 1012 DP-1")
			spcommand._send_hypr_command("dispatch moveworkspacetomonitor 1013 HDMI-A-1")
		case _:
			print("This only supports 3 moveworkspacetomonitors for now")

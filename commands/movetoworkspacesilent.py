import commands.SPCommand as spcommand
import subprocess
import json as json


def _run(command):
	try:
		gotdata = command[1]
	except IndexError:
		return

	old_position = ''.join(spcommand._send_hypr_command("cursorpos")).replace(" ", '').split(',')

	active_workspace_raw = subprocess.run(
		args=["hyprctl activeworkspace -j"],
		shell=True,
		encoding="UTF-8",
		capture_output=True
	).stdout

	active_workspace_info = json.loads(active_workspace_raw)


	print(f'active workspace info: {active_workspace_info}')


	match command[1]:
		case "1":
			# If the cursor is on the primary monitor
			match str(active_workspace_info['id'])[3]:
				case "1": spcommand._send_hypr_command("dispatch movetoworkspacesilent 1001")
				case "2": spcommand._send_hypr_command("dispatch movetoworkspacesilent 1002")
				case "3": spcommand._send_hypr_command("dispatch movetoworkspacesilent 1003")
		case "2":
			match str(active_workspace_info['id'])[3]:
				case "1": spcommand._send_hypr_command("dispatch movetoworkspacesilent 1011")
				case "2": spcommand._send_hypr_command("dispatch movetoworkspacesilent 1012")
				case "3": spcommand._send_hypr_command("dispatch movetoworkspacesilent 1013")
		case "3":
			match str(active_workspace_info['id'])[3]:
				case "1": spcommand._send_hypr_command("dispatch movetoworkspacesilent 1021")
				case "2": spcommand._send_hypr_command("dispatch movetoworkspacesilent 1022")
				case "3": spcommand._send_hypr_command("dispatch movetoworkspacesilent 1023")
		case "4":
			match str(active_workspace_info['id'])[3]:
				case "1": spcommand._send_hypr_command("dispatch movetoworkspacesilent 1031")
				case "2": spcommand._send_hypr_command("dispatch movetoworkspacesilent 1032")
				case "3": spcommand._send_hypr_command("dispatch movetoworkspacesilent 1033")
		case "5":
			match str(active_workspace_info['id'])[3]:
				case "1": spcommand._send_hypr_command("dispatch movetoworkspacesilent 1041")
				case "2": spcommand._send_hypr_command("dispatch movetoworkspacesilent 1042")
				case "3": spcommand._send_hypr_command("dispatch movetoworkspacesilent 1043")
		case _:
			print("This only supports 5 workspaces for now")

	spcommand._send_hypr_command(f'dispatch movecursor {old_position[0]} {old_position[1]}')

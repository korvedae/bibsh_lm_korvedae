import commands.SPCommand as spcommand
import settings
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

	# Only allow 10 spanned workspaces
	if int(command[1]) > 9:
		print("Parameter Error: Only 10 workspaces are allowed")
		return
	if len(settings.spconfig['monitors']) > 9:
		print("Config Error: Only 9 monitors max.")
		return


	spcommand._send_hypr_command(f'dispatch movetoworkspacesilent 10{str(active_workspace_info['id'])[2]}{command[1]}')

	spcommand._send_hypr_command(f'dispatch movecursor {old_position[0]} {old_position[1]}')

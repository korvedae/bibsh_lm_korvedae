from bibsh_lm_korvedae.components import hyprland
from bibsh_lm_korvedae.components import config
import subprocess
import json as json


def _run(command):
	try:
		print(command[1])
	except IndexError:
		return

	old_position = ''.join(hyprland._send_hypr_command("cursorpos")).replace(" ", '').split(',')

	active_workspace_raw = subprocess.run(
		args=["hyprctl activeworkspace -j"],
		shell=True,
		encoding="UTF-8",
		capture_output=True
	).stdout

	active_workspace_info = json.loads(active_workspace_raw)



	# Only allow 10 spanned workspaces
	if int(command[1]) > 9:
		print("Parameter Error: Only 10 workspaces are allowed")
		return
	if len(config.LayoutConfig['monitors']) > 9:
		print("Config Error: Only 9 monitors max.")
		return

	w = (config.LayoutConfig['monitors'].index(active_workspace_info['monitor']) * config.LayoutConfig['layouts']) + int(command[1])

	hyprland._send_hypr_command(f'dispatch movetoworkspacesilent {w}')

	hyprland._send_hypr_command(f'dispatch movecursor {old_position[0]} {old_position[1]}')

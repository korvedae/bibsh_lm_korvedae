from bibsh_lm_korvedae.components import hyprland
from bibsh_lm_korvedae.components import config
from bibsh_lm_korvedae.components import state

def _run(command):
	try:
		print(command[1])
	except IndexError:
		return

	old_position = ''.join(hyprland._send_hypr_command("cursorpos")).replace(" ", '').split(',')

	# Only allow 10 spanned workspaces
	if int(command[1]) > config.LayoutConfig['layouts']:
		print(f"Parameter Error: Config file defines only {config.LayoutConfig['layouts']} per monitor.")
		return
	if len(config.LayoutConfig['monitors']) > 9:
		print("Config Error: Only 9 monitors max.")
		return

	print(f'For workspace {command[1]}')
	for x in range(len(config.LayoutConfig['monitors'])):
		y = (x + 1) * config.LayoutConfig['layouts']
		workspace_num = (y - config.LayoutConfig['layouts']) + int(command[1])
		hyprland._send_hypr_command(f'dispatch workspace {workspace_num}')
		state.write_state({
			"current_layout" : command[1]
		})


	hyprland._send_hypr_command(f'dispatch movecursor {old_position[0]} {old_position[1]}')

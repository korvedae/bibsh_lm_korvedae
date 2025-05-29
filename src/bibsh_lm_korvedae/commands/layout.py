from bibsh_lm_korvedae.commands import SPCommand as spcommand
from bibsh_lm_korvedae.config import LayoutConfig
from bibsh_lm_korvedae import state

def _run(command):
	try:
		print(command[1])
	except IndexError:
		return

	old_position = ''.join(spcommand._send_hypr_command("cursorpos")).replace(" ", '').split(',')

	# Only allow 10 spanned workspaces
	if int(command[1]) > LayoutConfig['workspacesPerMonitor']:
		print(f"Parameter Error: Config file defines only {LayoutConfig['layouts']} per monitor.")
		return
	if len(LayoutConfig['monitors']) > 9:
		print("Config Error: Only 9 monitors max.")
		return

	print(f'For workspace {command[1]}')
	for x in range(len(LayoutConfig['monitors'])):
		y = (x + 1) * LayoutConfig['layouts']
		workspace_num = (y - LayoutConfig['layouts']) + int(command[1])
		spcommand._send_hypr_command(f'dispatch workspace {workspace_num}')
		state.write_state({
			"current_layout" : command[1]
		})


	spcommand._send_hypr_command(f'dispatch movecursor {old_position[0]} {old_position[1]}')

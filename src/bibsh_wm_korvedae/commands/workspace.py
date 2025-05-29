from bibsh_wm_korvedae.commands import SPCommand as spcommand
from bibsh_wm_korvedae import settings
from bibsh_wm_korvedae import state

def _run(command):
	try:
		print(command[1])
	except IndexError:
		return

	old_position = ''.join(spcommand._send_hypr_command("cursorpos")).replace(" ", '').split(',')

	# Only allow 10 spanned workspaces
	if int(command[1]) > settings.spconfig['workspacesPerMonitor']:
		print(f"Parameter Error: Config file defines only {settings.spconfig['workspacesPerMonitor']} workspaces per monitor.")
		return
	if len(settings.spconfig['monitors']) > 9:
		print("Config Error: Only 9 monitors max.")
		return

	print(f'For workspace {command[1]}')
	for x in range(len(settings.spconfig['monitors'])):
		y = (x + 1) * settings.spconfig['workspacesPerMonitor']
		workspace_num = (y - settings.spconfig['workspacesPerMonitor']) + int(command[1])
		spcommand._send_hypr_command(f'dispatch workspace {workspace_num}')
		state.write_state({
			"current_workspace" : command[1]
		})


	spcommand._send_hypr_command(f'dispatch movecursor {old_position[0]} {old_position[1]}')

from bibsh_lm_korvedae.commands import SPCommand as spcommand
from bibsh_lm_korvedae import settings

def _run(command):
	old_position = ''.join(spcommand._send_hypr_command("cursorpos")).replace(" ", '').split(',')

	# Only allow 10 spanned workspaces
	if len(settings.spconfig['monitors']) > 9:
		print("Config Error: Only 9 monitors max.")
		return

	mon_range = len(settings.spconfig['monitors'])
	print(mon_range)

	for x in range(mon_range):
		y = (x + 1) * 5
		i = (y - 5) + 1

		while i <= (y):
			print(f'Workspace {i}')
			spcommand._send_hypr_command(f'dispatch moveworkspacetomonitor {i} {settings.spconfig['monitors'][x]}')
			i += 1





	spcommand._send_hypr_command(f'dispatch movecursor {old_position[0]} {old_position[1]}')

import commands.SPCommand as spcommand
import settings

def _run(command):
	try:
		gotdata = command[1]
	except IndexError:
		return

	old_position = ''.join(spcommand._send_hypr_command("cursorpos")).replace(" ", '').split(',')

	# For determining iterator
	monitor_iterator = 1
	workspace_iterator  = 1

	mask_length = len(settings.spconfig['workspace']['mask'])
	for char_pos in range(mask_length):
		if settings.spconfig['workspace']['mask'][char_pos] == "w":
			# I wanted to do this cleanly using math and powers and stuff
			# But i'm not smart enough for that so this will have to do.
			workspace_iterator = (mask_length - 1) - char_pos

			for thingy in range(workspace_iterator):
				workspace_iterator = str(workspace_iterator)
				workspace_iterator = workspace_iterator + '0'

			print(workspace_iterator)



			# Note: Trying to convert 3 - 2 to 10... somehow

		elif settings.spconfig['workspace']['mask'][char_pos] == "m":
			pass



	match command[1]:
		case "1":
			spcommand._send_hypr_command("dispatch workspace 1001")
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

	spcommand._send_hypr_command(f'dispatch movecursor {old_position[0]} {old_position[1]}')

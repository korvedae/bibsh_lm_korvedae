import json
import os

xdg_runtime_dir = os.environ.get("XDG_RUNTIME_DIR")
runtime_folder = f'{os.environ.get("XDG_RUNTIME_DIR")}/bibsh'
state_file = f'{os.environ.get("XDG_RUNTIME_DIR")}/bibsh/bibsh_lm.state.json'
base_state = {
	"current_layout" : 1
}

def init():
	# If bibsh run folder doesn't exist, make it
	if os.path.exists(runtime_folder):
		os.mkdir(runtime_folder)

	# Delete state file if it exists, then re-create it
	if os.path.exists(state_file):
		os.remove(state_file)

	with open(f'{state_file}', 'w') as file:
		json.dump(base_state, file)


def fetch_state():
	with open(f'{state_file}', 'r', encoding="utf-8") as file:
		read_data = file.read()
		state = json.loads(read_data)
		return state

def write_state(state):
	with open(f'{state_file}', 'w', encoding="utf-8") as file:
		json.dump(state, file)

import json
import os

xdg_runtime_dir = os.environ.get("XDG_RUNTIME_DIR")
state_file = f'{os.environ.get("XDG_RUNTIME_DIR")}/bibsh/state.json'
base_state = {
	"current_workspace" : 1
}

def init():
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

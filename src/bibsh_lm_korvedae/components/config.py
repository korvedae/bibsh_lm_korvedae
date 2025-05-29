import json
import os

def init():
	global LayoutConfig
	with open(f'/home/{os.environ.get("USER")}/.config/hypr/bibsh_lm.json', 'r', encoding="utf-8") as config_file:
		read_data = config_file.read()
		LayoutConfig = json.loads(read_data)

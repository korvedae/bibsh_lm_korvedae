import json
import os

def init():
	global spconfig
	with open(f'/home/{os.environ.get("USER")}/.config/hypr/spconfig.json', 'r', encoding="utf-8") as config_file:
		read_data = config_file.read()
		spconfig = json.loads(read_data)

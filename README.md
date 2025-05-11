Bibsh Workspace
This is a component of my other project, birbshell, but it can be used independently.

Features:
	- Manage workspaces in a KDE-like way ()


Configuration
There are two main configuaration files and they both should be placed in the .config/hypr directory.

The first one should be an normal '.conf' file, which just adheres to hyprland syntax. Use this for setting the usual hyprland keybinds, executables, env files.

The second one should be exactly named spconfig.json. This file is necessary for the script to function properly.
Here are a list of it's configuration options:
 - Monitors: Array - List your monitors, making sure the first index is your primary monitor.
 - Workspace
 	- Offset: int - This is the workspace offset that indicates where bsh_wm should start creating workspaces. You should set this so it doesn't interfere with any other workspaces you might have.
  - mask: str - This determines which number place is used for iterating workspaces and iterating each monitor on those workspaces. THIS SHOULD BE THE SAME LENGTH OF CHARACTERS AS YOUR OFFSET. For example, a mask of "00wm" will have workspaces iterate based on the tenths place, and the monitors iterate on the ones place (workspace 1: 1010, monitor 1: 1011, monitor 2: 1012... and so on).

Bibsh Workspace
This is a component of my other project, birbshell, but it can be used independently.

Just lets you manage hyprland workspaces in a KDE-like way cause I needed that functionality for some reason.

Configuration
There are two main configuaration files and they both should be placed in the .config/hypr directory.

The first one should be an normal '.conf' file, which just adheres to hyprland syntax. Use this for setting the usual hyprland keybinds, executables, env files.

Todo: This probably isn't needed seeing as everything is generated at runtime. I could probably just have this script read the monitor parameters directly from hyprland, sift out the monitor names, then sort based on their id.
The second one should be exactly named spconfig.json. This file is necessary for the script to function properly.
Here are a list of it's configuration options:
 - Monitors: Array - List your monitors, making sure the first index is your primary monitor.

Caveats:
- Monitor switching happens synchronously: the more monitors you have, the slower it is
- Due to how workspaces are "generated", a monitor needs to be focused, then the workspace for that monitor is created (switched to). This means the mouse will flicker (as I make it go back to its original position) every time you change your workspace. If I find an alternative method that doesn't move the mouse(other than directly declaring workspaces in the hyprland config), I'll use that method.

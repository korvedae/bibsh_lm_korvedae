# Bibsh Workspace
This is a component of my other project, birbshell, but it can be used independently.
Just lets you manage hyprland workspaces in a KDE-like way cause I needed that functionality for some reason.

## Configuration
There are two (technically one) main configuaration file(s) and they should be placed in the .config/hypr directory:
 - spconfig.json - Used for determining managed monitors as well as their order
 - spconfig.conf - Doesn't need to be created, but I do it so I can plug-n-play. This is just a json file with an array called "monitors", that has each monitor name as a string.

## Caveats
- Monitor switching happens synchronously: the more monitors you have, the slower it is
- Due to how workspaces are "generated", a monitor needs to be focused, then the workspace for that monitor is created (switched to). This means the mouse will flicker (as I make it go back to its original position) every time you change your workspace. If I find an alternative method that doesn't move the mouse(other than directly declaring workspaces in the hyprland config), I'll use that method.

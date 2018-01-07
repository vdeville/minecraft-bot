## Minecraft chat bot

Minecraft chat bot written in python that parse latest logs from server and execute action called by user in game.

![](img/example-1.png)
![](img/example-2.png)

### Requirements
- UNIX system
- Programm: `python3`, `tail`, `screen`

### How to run

Launch `start.py` : `python start.py`
You can launch this script in a screen to detach and re-attach when youl'd like

By default the script launch minecraft server when it's start

### Base commands
| Command | Argument | Action |
| --- |---| --- |
| info || Retrieve list of map and their descriptions |
| setinfo | (description) | Set description of current map |
| swap | (map_id) | Permet de changer de map |
| stop || Stop mc server |
| restart || Restart mc server |
| stopall || Stop mc and python script |


### Crontibutors
@Warths for the idea and code help

### License
License GPLV3
#!/usr/bin/env python
# -*- coding: utf-8 -*-

import time
import mcutils
import config as conf


def command_info(command_dict):
    if len(command_dict['args']) > 1:
        for element in command_dict['args'][1:]:
            if mcutils.get_map_info(element):
                mcutils.tellraw_minecraft('Map %s : %s' % (element, mcutils.get_map_info(element)),
                                          ('green' if element == mcutils.get_srv_param('level-name') else 'yellow')
                                          )
            else:
                mcutils.tellraw_minecraft("la Map %s n'existe pas" % element, 'red')
    else:
        mcutils.tellraw_minecraft('""')
        mcutils.tellraw_minecraft('Voici la liste des maps:', 'dark_aqua')
        current_map = mcutils.get_srv_param('level-name')
        for name, desc in mcutils.get_map_info().items():
            if name == current_map:
                prefix = "➜"
                current = True
            else:
                prefix = "●"
                current = False
            mcutils.tellraw_minecraft('%s %s: %s' % (prefix, name, desc), ('green' if current else 'yellow'))
        mcutils.tellraw_minecraft('""')
        mcutils.tellraw_minecraft(
            '{"text":"Utilisez !setinfo pour modifier les informations de la map actuellement chargée.",'
            '"italic":true,"color":"gray",'
            '"clickEvent":{"action":"suggest_command","value":"!setinfo "},'
            '"hoverEvent":{"action":"show_text","value":"!setinfo"}}'
        )
    return


def stopall(command_dict):
    mcutils.stop_server()
    exit(0)


def command_update(command_dict):
    mcutils.say_minecraft("test")
    if len(command_dict['args']) == 2:
        if command_dict['args'][1] == mcutils.get_srv_param('level-name'):
            mcutils.say_minecraft('Mise à jour de la map ' + command_dict['args'][1] + '.')
            mcutils.stop_server()
            time.sleep(10)
            mcutils.update_map(command_dict['args'][1])
            mcutils.start_server()
        else:
            if command_dict['args'][1] in mcutils.get_map_info().items():
                mcutils.update_map(command_dict['args'][1])
                mcutils.say_minecraft('Mise à jour de la map %s lancée en tâche de fond.' % command_dict['args'][1])
            else:
                mcutils.say_minecraft("La map n'existe pas.")
        return
    else:
        mcutils.say_minecraft('Usage: ' + conf.SYMBOL_COMMAND + 'update <Map_ID>')


def command_swap(command_dict):
    if len(command_dict['args']) > 1:
        if command_dict['args'][1] == mcutils.get_srv_param('level-name'):
            mcutils.tellraw_minecraft('La map %s est déja chargée.' % command_dict['args'][1], 'green')
        else:
            if not mcutils.get_map_info(command_dict['args'][1]):
                mcutils.tellraw_minecraft("La map demandée n'existe pas ou n'est pas autorisée dans le fichier", 'red')
            else:
                mcutils.tellraw_minecraft('Changement de map programmé:', 'gold')
                mcutils.tellraw_minecraft('Passage de %s ➜ %s' % (
                            mcutils.get_srv_param('level-name'), command_dict['args'][1]
                ), 'green')
                mcutils.stop_server()
                mcutils.set_srv_param('level-name', command_dict['args'][1])
                mcutils.start_server()
    else:
        mcutils.tellraw_minecraft('Usage: %s%s <Map_ID>' % (conf.SYMBOL_COMMAND, command_dict['command']), 'gray')
    return


def command_set_info(command_dict):
    if len(command_dict['args']) > 1:
        str = ' '.join(command_dict['args'][1:])
        mcutils.set_map_info(str)
        mcutils.tellraw_minecraft('✔ La description de la map %s à bien été mise à jour'
                                  % mcutils.get_srv_param('level-name'), 'green'
                                  )
    else:
        mcutils.tellraw_minecraft('Usage: %s%s <Description>' % (conf.SYMBOL_COMMAND, command_dict['command']), 'gray')
    return

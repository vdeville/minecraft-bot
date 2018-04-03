#!/usr/bin/env python
# -*- coding: utf-8 -*-

import mcutils
import config as conf
from minecraftTellrawGenerator import MinecraftTellRawGenerator as mctellraw


def command_info(command_dict):
    if len(command_dict['args']) > 1:
        for element in command_dict['args'][1:]:
            if mcutils.get_map_info(element):
                mcutils.tellraw_minecraft(
                    mctellraw(text='Map %s : %s' % (element, mcutils.get_map_info(element)),
                              color=('green' if element == mcutils.get_srv_param('level-name') else 'yellow')
                              )
                )
            else:
                mcutils.tellraw_minecraft(mctellraw(text="la Map %s n'existe pas" % element, color='red'))
    else:
        mcutils.tellraw_minecraft(mctellraw())
        mcutils.tellraw_minecraft(mctellraw(text='Voici la liste des maps:', color='dark_aqua'))
        current_map = mcutils.get_srv_param('level-name')
        for name, desc in mcutils.get_map_info().items():
            if name == current_map:
                prefix = "➜"
                current = True
            else:
                prefix = "●"
                current = False
            mcutils.tellraw_minecraft(
                mctellraw(text='%s %s: %s' % (prefix, name, desc), color=('green' if current else 'yellow'))
            )
        mcutils.tellraw_minecraft(mctellraw())
        mcutils.tellraw_minecraft(
            mctellraw(text='Utilisez !setinfo pour modifier les informations de la map actuellement chargée.',
                      italic=True, color='gray',
                      hover=mctellraw(text='!setinfo'),
                      click='!setinfo')
        )
    return


def stopall(command_dict):
    mcutils.stop_server()
    exit(0)


def command_swap(command_dict):
    if len(command_dict['args']) > 1:
        if command_dict['args'][1] == mcutils.get_srv_param('level-name'):
            mcutils.tellraw_minecraft(
                mctellraw(text='La map %s est déja chargée.' % command_dict['args'][1], color='green'))
        else:
            if not mcutils.get_map_info(command_dict['args'][1]):
                mcutils.tellraw_minecraft(
                    mctellraw(text="La map demandée n'existe pas ou n'est pas autorisée dans le fichier", color='red')
                )
            else:
                mcutils.tellraw_minecraft(mctellraw(text='Changement de map programmé:', color='gold'))
                mcutils.tellraw_minecraft(
                    mctellraw(
                        text='Passage de %s ➜ %s' % (mcutils.get_srv_param('level-name'), command_dict['args'][1]),
                        color='green')
                )
                mcutils.stop_server()
                mcutils.set_srv_param('level-name', command_dict['args'][1])
                mcutils.start_server()
    else:
        mcutils.tellraw_minecraft(
            mctellraw(text='Usage: %s%s <Map_ID>' % (conf.SYMBOL_COMMAND, command_dict['command']), color='gray')
        )
    return


def command_set_info(command_dict):
    if len(command_dict['args']) > 1:
        str = ' '.join(command_dict['args'][1:])
        mcutils.set_map_info(str)
        mcutils.tellraw_minecraft(
            mctellraw(text='✔ La description de la map %s à bien été mise à jour' % mcutils.get_srv_param('level-name'),
                      color='green')
        )
    else:
        mcutils.tellraw_minecraft(
            mctellraw(text='Usage: %s%s <Description>' % (conf.SYMBOL_COMMAND, command_dict['command']), color='gray')
        )
    return


def command_set_srv_param(command_dict):
    value = ' '.join(command_dict['args'][2:])
    if mcutils.set_srv_param(command_dict['args'][1], value):
        mcutils.tellraw_minecraft(
            mctellraw(text='✔ Le parametre %s à bien été mis à jour' % command_dict['args'][1], color='green')
        )
    else:
        mcutils.tellraw_minecraft(
            mctellraw(text="✖ Le parametre (%s) n'existe pas" % command_dict['args'][1], color='red')
        )
    return

#!/usr/bin/env python
# -*- coding: utf-8 -*-

import config as conf
import subprocess
import json
import time


def get_map_info(map=None):
    maps = json.load(open(conf.MAPINFO_PATH))
    if map:
        try:
            return maps[map]
        except KeyError:
            return None
    else:
        return maps


def set_map_info(str):
    with open(conf.MAPINFO_PATH, 'r') as MapInfo:
        json_copy = json.loads(MapInfo.read())
        json_copy[get_srv_param('level-name')] = str
    with open(conf.MAPINFO_PATH, 'w') as MapInfo:
        json_dump = json.dumps(json_copy, indent=4)
        MapInfo.writelines(json_dump)
    return


def update_map(map_ID):
    # TODO Map update algorithm
    return


def run_cmd(cmd):
    try:
        return subprocess.check_output(cmd, shell=True, cwd=conf.SERVER_DIR)
    except subprocess.CalledProcessError:
        print('Echec de la commande : ' + cmd)
        return


def run_minecraft_cmd(string):
    string = string.replace('"', '\\"')
    run_cmd('screen -p 0 -S %s -X stuff "%s $(printf \\\r)"' % (conf.SCREEN_NAME, string))


def say_minecraft(string):
    run_minecraft_cmd("say %s" % string)


def tellraw_minecraft(string, color=None):
    if not color:
        run_minecraft_cmd('tellraw @a %s' % string)
    else:
        run_minecraft_cmd('tellraw @a {"text":"%s","color":"%s"}' % (string, color))


def stop_server():
    for t in range(15, 0, -5):
        tellraw_minecraft('Stopping in %s ...' % str(t), 'red')
        time.sleep(5)
    run_minecraft_cmd('stop')


def start_server():
    cmd = 'screen -dmS %s java %s -jar %s %s' % (conf.SCREEN_NAME, conf.MINECRAFT_SERVER['javaArgs'],
                                                 conf.MINECRAFT_SERVER['serverJar'], conf.MINECRAFT_SERVER['mcArgs'])
    run_cmd(cmd)


def restart_server():
    tellraw_minecraft("Restarting...", 'gold')
    stop_server()
    start_server()
    time.sleep(30)
    tellraw_minecraft("Server restarted", 'blue')


def get_srv_param(param):
    with open(conf.MINECRAFT_SERVER['serverProperties']) as ServerProperties:
        for line in ServerProperties:
            if param in line:
                return line[line.index('=') + 1:-1]


def set_srv_param(param, value):
    with open(conf.MINECRAFT_SERVER['serverProperties'], 'r') as ServerProperties:
        new_server_properties = ServerProperties.readlines()
        ServerProperties.close()
        i = 0
        for line in new_server_properties:
            i += 1
            if param in line:
                with open('server.properties', 'w') as srvFile:
                    new_line = ("%s=%s" % (param, value))
                    new_server_properties[i - 1] = new_line + '\r'
                    srvFile.writelines(new_server_properties)
                    return True
            else:
                return False

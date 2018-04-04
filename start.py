#!/usr/bin/env python
# -*- coding: utf-8 -*-

from minecraftTellrawGenerator import MinecraftTellRawGenerator as mctellraw
import config as conf
import commands as cmd
import mcutils
import subprocess


def parse_command(string):
    string = string.replace('\n', '')
    split = string.split(conf.SYMBOL_COMMAND)
    command = split[1]
    command_args = command.rsplit(' ')
    return {'command': command_args[0], 'args': command_args}


def read_log(current_line):
    if '> ' + conf.SYMBOL_COMMAND in line:
        command_dict = parse_command(current_line)
        command = command_dict['command']
        print("<COMMAND>: " + str(command_dict))

        if command == 'info':
            cmd.command_info(command_dict)
        if command == 'setinfo':
            cmd.command_set_info(command_dict)
        elif command == 'setsrvparam':
            cmd.command_set_srv_param(command_dict)
        if command == 'swap':
            cmd.command_swap(command_dict)
        elif command == 'stop':
            mcutils.stop_server()
        elif command == 'stopall':
            cmd.stopall()
        elif command == 'restart':
            mcutils.restart_server()


# symbols ✔︎ ✖︎ 𝟵 ➜


if __name__ == '__main__':
    try:
        if conf.START_SERVER_AT_BOOT:
            mcutils.start_server()

        mcutils.say_minecraft("Python script was started")
        mcutils.tellraw_minecraft(mctellraw())
        mcutils.tellraw_minecraft(mctellraw(
            text='Minecraft bot, ready !',
            bold=False,
            color='yellow'))
        mcutils.tellraw_minecraft(mctellraw())
        mcutils.tellraw_minecraft(mctellraw(
            text='This bot is open source, you can contribute on Github (Click!)',
            color='gray',
            url='https://github.com/MyTheValentinus/minecraft-bot',
            hover=mctellraw(text='Click !', bold=True, color='dark_red')
        ))
        f = subprocess.Popen(['tail', '-F', '-n', '0', conf.MINECRAFT_SERVER['latestLog']], stdout=subprocess.PIPE,
                             stderr=subprocess.PIPE)
        while True:
            line = f.stdout.readline().decode('utf-8')
            read_log(line)
    except (KeyboardInterrupt, SystemExit):
        print("Python script was stop")
        mcutils.say_minecraft("Python script was stop")
        exit(0)
    except:
        mcutils.say_minecraft("Python script as crash")
        exit(1)

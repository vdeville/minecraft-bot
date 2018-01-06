BASE_PATH = "/Users/valentin/dev/voxel-pyhton"
MAPINFO_PATH = BASE_PATH + '/MapInfo.json'
SERVER_DIR = BASE_PATH + "/Minecraft/"

MINECRAFT_SERVER = {
    'serverProperties': SERVER_DIR + 'server.properties',
    'latestLog': SERVER_DIR + 'logs/latest.log',
    'serverJar': 'minecraft_server.1.12.2.jar',
    'javaArgs': '-Xmx4096m',
    'mcArgs': 'nogui',
}

SCREEN_NAME = "voxel"
SYMBOL_COMMAND = "!"

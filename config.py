BASE_PATH = "/Users/valentin/Downloads/minecraft"
MAPINFO_PATH = BASE_PATH + '/MapInfo.json'
SERVER_DIR = BASE_PATH + "/mc/"

MINECRAFT_SERVER = {
    'serverProperties': SERVER_DIR + 'server.properties',
    'latestLog': SERVER_DIR + 'logs/latest.log',
    'serverJar': 'server.jar',
    'javaArgs': '-Xmx4096m',
    'mcArgs': 'nogui',
}

SCREEN_NAME = "minecraft"
SYMBOL_COMMAND = "!"
START_SERVER_AT_BOOT = True

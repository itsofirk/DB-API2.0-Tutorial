import configparser

config = configparser.ConfigParser()

if not config.read("config.ini"):
    raise Exception("Failed to parse configuration file.")

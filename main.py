import pyodbc

from factory import config

MYSQL_CONNECTION_FORMAT = "DRIVER=MySQL;SERVER={host};DATABASE={database};UID={username};PWD={password}"


def get_database_credentials():
    return {
        "host": config.get("MySQL", "host"),
        "database": config.get("MySQL", "database"),
        "username": config.get("MySQL", "username"),
        "password": config.get("MySQL", "password")
    }


if __name__ == '__main__':
    with pyodbc.connect(MYSQL_CONNECTION_FORMAT.format(**get_database_credentials())) as conn:
        print("SUCCESS")

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


def compare_users_rows(r1, r2):
    # Do something
    print("Comparing rows...")


if __name__ == '__main__':
    _connection_string = MYSQL_CONNECTION_FORMAT.format(**get_database_credentials())

    # This is a special API in Python, which allows opening a connection for example,")
    # without taking care of closing it. It closes itself outside of its scope.")
    with pyodbc.connect(_connection_string) as conn:
        # In order to query the database we need to create a cursor.")
        # The cursor is part of the db api, which means every database handler uses it.")
        # The cursor is like an open socket inside a connection, so we must ensure to close it")
        with conn.cursor() as cur:
            # Now we can execute queries on the database
            cur.execute("SELECT * FROM {tbl}".format(tbl=config.get("MySQL", "users_table_name")))
            first_row = cur.fetchone()
            second_row = cur.fetchone()  # will return None if no results left to fetch
            # third_row etc...
            other_rows = cur.fetchall()  # will return all the *other* results

        # Let's says we now need to process the results, therefore we should close the cursor. Cursor=Resources
        # So continue writing outside the with-cursor-scope
        compare_users_rows(first_row, second_row)
        compare_users_rows(other_rows[0], other_rows[1])
        # Now we want to insert a row, so we need a cursor
        with conn.cursor() as cur:
            cur.execute(
                "INSERT INTO {tbl} (username, email, password) values ('default', 'default', 'default');"
                .format(tbl=config.get("MySQL", "users_table_name"))
            )
            # Don't forget to commit
            conn.commit()
        # Now to close the connection, we simply write outside the with-connection-scope
        print("Closing database connection")
    print("Exiting...")
    


        

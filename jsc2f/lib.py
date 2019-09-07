"""JSON SQL cell to File utility"""
import json
import mysql.connector as mariadb


def save_to_file(filename, host, user, password, database, column, table,
                 where='', port=3306):
    """Read the json data from the database, save to filename"""
    conn = mariadb.connect(host=host, port=port, user=user, password=password,
                           database=database)
    cursor = conn.cursor()
    read_query = 'SELECT {} from {}{}'.format(column, table, where)
    cursor.execute(read_query)
    data = cursor.fetchone()[0]
    conn.close()
    jdata = json.dumps(json.loads(data), indent=4, sort_keys=True)
    jdata = jdata.rstrip()
    with open(filename, 'w+') as out_file:
        out_file.write(jdata)


def update_from_file(filename, host, user, password, database, column, table,
                     where='', port=3306):
    """Read data from filename, write to database"""
    with open(filename) as json_file:
        jdata = json.load(json_file)
    data = json.dumps(jdata)
    conn = mariadb.connect(host=host, port=port, user=user, password=password,
                           database=database)
    cursor = conn.cursor()
    update_query = "UPDATE {} SET {} = '{}'{}".format(table, column, data,
                                                      where)
    cursor.execute(update_query)
    conn.commit()
    conn.close()

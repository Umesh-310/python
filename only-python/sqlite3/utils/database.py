from .dataBaseConnection import DataBaseConnection


def create_file_table():
    with DataBaseConnection('data.db') as connection:
        cursur = connection.cursor()
        cursur.execute(
            'CREATE TABLE IF NOT EXISTS  data_Info(id integer primary key, name  text, age integer , address text)')


def seve_in_file(id: int, name: str, age: int, address: str):
    with DataBaseConnection('data.db') as connection:
        cursur = connection.cursor()
        cursur.execute(
            'INSERT INTO data_Info VALUES(? , ? , ? , ?)', (id, name, age, address))
    return True


def read_in_file():
    with DataBaseConnection('data.db') as connection:
        cursur = connection.cursor()
        cursur.execute('SELECT * FROM data_Info')
        data = [{'name': row[1], 'age': row[2]}for row in cursur.fetchall()]
    return data


def update_in_file(id: int, name: str, age: int, address: str):
    with DataBaseConnection('data.db') as conn:
        cousur = conn.cursor()
        cousur.execute(
            "UPDATE data_Info SET name = ? , age = ? , address = ? WHERE id = ? ", (name, age, address, id))
    return True


def delete_in_file(id):
    with DataBaseConnection('data.db') as conn:
        cursur = conn.cursor()
        cursur.execute("DELETE FROM data_Info WHERE id = ?", (id))
    return True


def find_in_file(value):
    with DataBaseConnection('data.db') as conn:
        cursur = conn.cursor()
        cursur.execute(
            "SELECT * FROM data_Info WHERE name = ? OR id = ?", (value, value))
        data = [{'name': row[1], 'age': row[2]}for row in cursur.fetchall()]
    return data

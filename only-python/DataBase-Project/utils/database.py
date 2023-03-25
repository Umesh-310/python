book = []


def seve_in_file(content, filename):
    with open(filename, 'a') as file:
        file.write(content)


def read_in_file(fileName):
    with open(fileName, 'r') as file:
        return file.read()


def add_to_pepole(name, age):
    book.append({
        'name': name,
        'age': age,
    })


def list_of_pepole():
    return book

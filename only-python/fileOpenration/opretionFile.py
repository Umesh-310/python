def save_to_file(content, filename):
    with open(filename, 'w') as files:
        files.write(content)


def read_file(fileName):
    with open(fileName, 'r') as file:
        return file.read()

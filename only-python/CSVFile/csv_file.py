
files = open('csv_data.txt', 'r')

lines = files.readlines()

files.close()


lines = [line.strip() for line in lines[1:]]
data = []
for line in lines:
    fname, lname, age, address = line.split(',')
    data.append({
        'firstname': fname,
        'Lastname': lname,
        'Age': age,
        'Address': address,
    })

print(data)

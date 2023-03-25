# my_file_r = open('data.txt', 'r')
# file_content = my_file_r.readlines()
# my_file_r.close()

# print(file_content)

# write_content = input('Enter File content:- ')
# my_file_w = open('newData.txt', 'a')
# my_file_w.write(write_content)
# my_file_w.close()

"""
w	Open a file for writing. Creates a new file if it does not exist or truncates the file if it exists.

a	Open a file for appending at the end of the file without truncating it. Creates a new file if it does not exist.

x	Open a file for exclusive creation. If the file already exists, the operation fails.

+	Open a file for updating (reading and writing)

readlines(n=-1)	Reads and returns a list of lines from the file. Reads in at most n bytes/characters if specified.

"""

# Ask the your list of three friend
# by name tell them the firends city name
# create new file for ecah friend with there name and city


friends = input(
    'Enter three firend name "," Comma sepreted').split(',')

pepole_list = open('pepole.txt', 'r')
friends_list = pepole_list.readlines()
pepole_list.close()

friend_set = set(friends)
friends_list_set = set(name.strip() for name in friends_list)
nearby_friend_set = friend_set.intersection(friends_list_set)

print(nearby_friend_set)
 
new_file_ = open('nearby_friend.txt', 'w')

for friend in nearby_friend_set:
    print(f'{friend} is nearby! Meet up with them.')
    new_file_.write(f'{friend} is nearby! Meet up with them.\n')

new_file_.close()

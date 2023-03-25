# is_programm = True

# movies = []

# while is_programm:
#     user_Enter = input(
#         "a - Add movies\nl - See movies\nf - Find a movie\nq - quit\n Enter any:- ")
#     if user_Enter.lower() == 'a':
#         enterMovies = input('Enter Movies Name:- ')
#         movies.append(enterMovies.title())
#     elif user_Enter.lower() == 'l':
#         for movie in movies:
#             print(f"\t\tMovie name {movie}")
#     elif user_Enter.lower() == 'f':
#         movie = input('Enter movie Name:- ')
#         if movie.title() in movies:
#             print(f'\t\t{movie}')
#         else:
#             print(f'\t\tNo Movie match found of {movie}')
#     elif user_Enter.lower() == 'q':
#         is_programm = False
#     else:
#         print('Enter right value :)')

# from datetime import datetime, timezone, timedelta
# today = datetime.now(timezone.utc)
# print(today + timedelta(days=1))
# print(datetime.now())
# date_string = "21 June, 2018"
# print(datetime.strptime(date_string, "%d %B, %Y"))

# import time
# from threading import Thread


# def user_input():
#     start = time.time()
#     userInput = input('Enter your Name: ')
#     print(f'Hello {userInput}')
#     print(f'user input time is {time.time() - start}')


# def calcu():
#     start = time.time()
#     listof = [x**2 for x in range(20000000)]
#     print(f'calcu time is {time.time() - start}')


# start = time.time()
# user_input()
# calcu()
# print(f'total time is {time.time() - start}')

# thread1 = Thread(target=calcu)
# thread2 = Thread(target=user_input)

# start = time.time()

# thread1.start()
# thread2.start()

# thread1.join()
# thread2.join()

# print(f'thread time is {time.time() - start}')

# from concurrent.futures import ThreadPoolExecuto

# thread and


# list_arr = [1, 2, 3, 4, 5, 6, 7, 8, 9]

# list_arr.append(10)
# print(list_arr)
# print(list_arr.pop())

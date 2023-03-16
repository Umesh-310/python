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
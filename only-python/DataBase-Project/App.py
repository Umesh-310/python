import utils.database as dtb
User_choice = """
Enter :
- 'a' to add a new book
- 'l' to list all book
- 'r' to mark a book as read
- 'q' to quit

Your choice:- """


def prompt_add_entery():
    entered_name = input('Enter your name: - ')
    enter_age = input('Enter your Age:- ')
    dtb.add_to_pepole(entered_name, enter_age)


def list_books():
    print(dtb.list_of_pepole)


is_true = True

while is_true:
    user_input = input(User_choice)

    if user_input.lower() == 'a':
        prompt_add_entery()
    elif user_input.lower() == 'l':
        list_books()
    elif user_input.lower() == 'r':
        print('r')
    elif user_input.lower() == 'q':
        print('q')
        is_true = False
    else:
        print('Wrong Input\nEnter Corrot value')

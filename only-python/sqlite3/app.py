import utils.database as dtb

User_choice = """
Enter :
- 'a' to add a new Entry
- 'l' to list all Entry
- 'u' to Update the Entry
- 'd' to Delete the Entry
- 'f' to find one Entry
- 'q' to quit

Your choice:- """


def prompt_add_entery():

    id: int = input('Enter your id: - ')
    entered_name = input('Enter your name:- ')
    enter_age = input('Enter your Age:- ')
    enter_address = input('Enter your address:- ')
    dtb.seve_in_file(id, 2, enter_age, enter_address)


def list_books():
    data = dtb.read_in_file()
    for val in data:
        print(f'{val["name"]} age is {val["age"]}')


def update_user_entry():
    print("************** Don't Change your id ****************")
    id = input('Enter your old id: - ')
    entered_name = input('Enter your updated name:- ')
    enter_age = input('Enter your updated Age:- ')
    enter_address = input('Enter your updated address:- ')

    dtb.update_in_file(id, entered_name, enter_age, enter_address)


def delete_user_entry():
    print("************** Are you shore you want to delete ****************")
    is_true_d = True
    while is_true_d:
        delete_Qution = input('you shore you want to delete (y/n):- ')
        if delete_Qution.lower() == 'y':
            id = input('Enter your id:- ')
            dtb.delete_in_file(id)
            is_true_d = False
        elif delete_Qution.lower() == 'n':
            is_true_d = False
            return
        else:
            print('Wrong Input\nEnter Corrot value(y/n)')


def find_user_entry():
    value = input('Enter id or name who you want to Find (only one):- ')
    data = dtb.find_in_file(value)
    for val in data:
        print(f'{val["name"]} age is {val["age"]}')


is_true = True

while is_true:
    user_input = input(User_choice)

    if user_input.lower() == 'a':
        prompt_add_entery()
    elif user_input.lower() == 'l':
        list_books()
    elif user_input.lower() == 'u':
        update_user_entry()
    elif user_input.lower() == 'd':
        delete_user_entry()
    elif user_input.lower() == 'f':
        find_user_entry()
    elif user_input.lower() == 'q':
        is_true = False
    else:
        print('Wrong Input\nEnter Corrot value')

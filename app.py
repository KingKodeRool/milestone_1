"""
This needs to have a text base user interface that asks the user what they want to do:
- Add a movie
- See collection of movies
- Find a movie
- Exit the app

Things that need to be done:

[x] Think of where to store movies
[x] How will a movie be formatted
[x] Show user the main text interface and get their input
[] Allow user to add movie(define function)
[] Allow user to see their movies(define function)
[] Allow user to find a movie(define function)
[] Allow user to exit app(define function)
"""


def menu():
    user_interface_input = input('Enter one of the following:'
                                 '\n"add"  -  to add a movie to the collection '
                                 '\n"see"  -  to look at the current collection of movies '
                                 '\n"find" -  to loop up a movie'
                                 '\n"exit" -  to leave out of the application')

    if user_interface_input == 'add':
        add_movie()

    elif user_interface_input == 'see':
        see_movie()

    elif user_interface_input == 'find':
        find_movie()

    elif user_interface_input == 'exit':
        print('Exiting the program.')
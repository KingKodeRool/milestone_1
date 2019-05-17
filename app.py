"""
This needs to have a text base user interface that asks the user what they want to do:
- Add a movie
- See collection of movies
- Find a movie
- Exit the app

Things that need to be done:

[] Think of where to store movies
[] How will a movie be formatted
[x] Show user the main text interface and get their input
[] Allow user to add movie(define function)
[] Allow user to see their movies(define function)
[] Allow user to find a movie(define function)
[x] Allow user to exit app(define function)
"""

movies = []
'''
movie format = 
{
    'title': ... ,
    'director': ... ,
    'year': ... ,
}
'''


# Defined the menu function. This splits up the different parts of our program. Essentially a hub for other functions.
def menu():
    user_interface_input = input('Enter one of the following:'
                                 '\n"add"  -  to add a movie to the collection '
                                 '\n"see"  -  to look at the current collection of movies '
                                 '\n"find" -  to loop up a movie'
                                 '\n"exit" -  to leave out of the application'
                                 '\n')

    while user_interface_input != 'exit':
        if user_interface_input == 'add':
            add_movie()

        elif user_interface_input == 'see':
            see_movie()

        elif user_interface_input == 'find':
            find_movie()

        else:
            print('Invalid input: Please enter a valid option')

        user_interface_input = input('Enter one of the following:'
                                     '\n"add"  -  to add a movie to the collection '
                                     '\n"see"  -  to look at the current collection of movies '
                                     '\n"find" -  to loop up a movie'
                                     '\n"exit" -  to leave out of the application'
                                     '\n')


def add_movie():
    movie_title = input('Enter the title of the movie: ')
    movie_director = input('Enter the director: ')
    movie_year = int(input('Enter the year the movie was released: '))

    movie_data = dict()
    movie_data['Title'] = movie_title
    movie_data['Director'] = movie_director
    movie_data['Year'] = movie_year
    print('You have entered this movie: {}'.format(movie_data))
    movies.append(movie_data)
    '''
    Easier way to make a dictionary and append to list:
    
    movies.append({
        'Title': movie_title,
        'Director': movie_director,
        'Year': movie_year
    })
    '''


menu()
print(movies)

# create function that asks users how they want to look up a movie
def search_movie(attribute):
    attribute = input('What would you like to look up the movie by? ')
    if attribute == 'name':
    user_movie_name = input('What is the name of the movie you want to look up? ')
        for movies in movies_list:
            for name in movies:




movies_list = []

movie_1 = {
    'name': 'The Matrix',
    'director': 'Wachowskis',
    'year': '1994'
}

movies_list.append(movie_1)
print(movies_list)

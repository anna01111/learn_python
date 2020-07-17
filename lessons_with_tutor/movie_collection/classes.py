
class Movie:
    def __init__(self, title: str, year: str, director: str):
        self.title = title
        self.__year = year
        self.director = director

    def __repr__(self):
        return f'<{self.title}> {self.__year} by {self.director}'

    # __year getter
    @property
    def year(self):
        return self.__year

    # __year setter
    @year.setter
    def year(self, year):
        for el in year:
            if el not in '0123456789':
                print('Incorrect year')
                break
        else:
            self.__year = year


class Collection:
    def __init__(self, name: str):
        self.name = name
        self.c = []

    def __repr__(self):
        return f'Collection <{self.name}> : {self.c}'

    def __len__(self):
        return len(self.c)

    def __getitem__(self, i):
        return self.c[i]

    def add_movie(self, movie):
        self.c.append(movie)

    def list_movies(self):
        print(self)
        for movie in self.c:
            print(movie)

    # following method looks for a movie by title
    def find_movie(self, search_query):
        i = 0
        for movie in self.c:
            #  usage of a lower() function here makes it possible to find a movie
            #  even if case in the movie's title and in the search query don't match
            res = movie.title.lower().find(search_query.lower())
            if res != -1:  # find (srt) method returns -1 if there are no matches
                print(self.c[i])
            i += 1


from classes import Movie, Collection


m1 = Movie('She', '2011', 'Deutc')
m2 = Movie('Nauting Hill', '1998', 'Uhjgsgf')
print(m1)
print(m2)
print()
c1 = Collection('my movie collection')
c1.add_movie(m1)
c1.add_movie(m2)
c1.list_movies()
print("RESULTS OF SEARCH")
c1.find_movie('')






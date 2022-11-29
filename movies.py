import sqlite3

import time

class Movie():

    def __init__(self,name,producer,actor,year):

        self.name = name
        self.producer = producer
        self.actor = actor
        self.year = year
        
    def __str__(self):

        return "Film İsmi: {}\nYapımcı: {}\nAktör: {}\nYıl: {}\n".format(self.name,self.producer,self.actor,self.year)


class Library():

    def __init__(self):

        self.connect()

    def connect(self):
        self.baglanti = sqlite3.connect("library.db")
        self.cursor = self.baglanti.cursor()
        sorgu = "Create Table If not exists movies (Name TEXT,Producer TEXT,Actor TEXT,Year INT)"
        self.cursor.execute(sorgu)
        self.baglanti.commit()
        
    def baglantiyi_kes(self):
        self.baglanti.close()

    def show_movies(self):
        sorgu =  "Select * From movies"
        self.cursor.execute(sorgu)
        movies = self.cursor.fetchall()
        if (len(movies) == 0):
            print("There is no movie in libray")
        else:
            for i in movies:
                movie = Movie(i[0],i[1],i[2],i[3])
                print(movie)

    def film_sorgula(self,isim):

        sorgu = "Select * From kitaplar where isim = ?"

        self.cursor.execute(sorgu,(name,))

        movies = self.cursor.fetchall()

        if (len(movies) == 0):
            print("There is no such movie in the library")
        else:
            movie = Movie(movies[0][0],movies[0][1],movies[0][2],movies[0][3],movies[0][4])
            
            print(movie)
    def film_ekle(self,movie):

        sorgu = "Insert into movies Values(?,?,?,?)"

        self.cursor.execute(sorgu,(movie.name,movie.producer,movie.actor,movie.year))

        self.baglanti.commit()

    def film_sil(self,isim):

        sorgu = "Delete From movies where name = ?"

        self.cursor.execute(sorgu,(name,))

        self.baglanti.commit()


print("""

Operations;

1. Show Movies

2. Search For a Movie

3. Add Movie to the Library

4. Delete a Movie From the Library

Press 'q' to exit.
""")

library = Library()

while True:
    işlem = input("Choose the operation.")

    if (işlem == "q"):
        print("Program is being terminated...")
        break
    elif (işlem == "1"):
        library.show_movies()

    elif (işlem == "2"):
        isim = input("Which movie you want to inquire? ")
        print("Movie is being inquired")
        time.sleep(2)

        library.film_sorgula(isim)

    elif (işlem == "3"):
        name = input("Name:")
        producer = input("Producer:")
        actor = input("Main Character:")
        year = int(input("Year: "))

        yeni_film = Movie(name,producer,actor,year)

        print("Movie is being added...")
        time.sleep(2)

        library.film_ekle(yeni_film)
        print("Done.")


    elif (işlem == "4"):
        isim = input("Which movie you'd like to delete?")

        cevap = input("Are you sure ? (Y/N)")
        if (cevap == "Y"):
            print("Movie is being deleted.")
            time.sleep(2)
            library.film_sil(isim)
            print("Done.")

    else:
        print("invalid input.")

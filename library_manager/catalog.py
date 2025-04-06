"""
Модуль `catalog.py
"""
class Book:
    """
    Класс Книга
    Атрибутыж
      Название - строка
      автор - строка
      жанр - строка
    """
    def __init__(self, title : str, author : str, genre : str ):
        self.title = title
        self.author = author
        self.genre =genre
    def __str__(self):
        return(f'Название: {self.title}, автор {self.author}, жанр {self.genre} ')

    def get_title(self):
        """
        полуить название
        :return:
        """
        return self.title

    def get_author(self):
        """
        получить автора
        :return:
        """
        return self.author

    def get_genre(self):
        """
        получить жанр
        """
        return self.genre



class Library:
   """
    - Класс `Library` для управления книгами. Класс должен включать методы для:
    - Добавления книги (с атрибутами: название, автор, жанр).
    - Удаления книги по названию.
    - Поиска книги по названию, автору и жанру.
    - Просмотра всех книг в библиотеке.
    """
   def __init__(self, books : list):
       self.books = books

   def add_book(self, title : str, author : str, genre : str ):
       """
       Добавление книги (с атрибутами: название, автор, жанр)

      """
       new_book = Book (title, author, genre)
       self.books.append(new_book)
       print (f'Книга {new_book} добавлена в библиотеку')
       return

   def del_book(self, title: str):
       """
       Удаление книг по названию.
       """
       books_del = [] #Список удаленных книг
       for bk in self.books:
           if bk.get_title() == title:
              books_del.append(bk)
       if len(books_del) == 0:
           print (f'В библиотеке не найдено книги с названием {title}')
       else:
          print ('Из библиотеки удалено:')
          for bk in books_del:
              print(bk)
              self.books.remove(bk)
       return

   def find_book(self, title : str, author : str, genre: str):
       """
       Поиск книги по названию, автору и жанру.
        return: книга
       """
       book_find = None
       for bk in self.books:
           if bk.get_title() == title and bk.get_author() == author and bk.get_genre() == genre:
               book_find =bk
       if book_find is None:
           print (f'\nКнига по указаннм условиям {title}, {author}, {genre} не найдена')
       else:
           print (f'\nНайдена книга {book_find}')
           return book_find

   def viewing_books(self):
       """
       Просмотр всех книг в библиотеке.
       """
       print ('\nВсе книги в библиотеке на текущий момент:')
       i= 0
       for bk in self.books:
           i +=1
           print (f'Книга №{i} - {bk}')
       return








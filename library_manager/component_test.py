"""
Тестирование компонентов домашенго задания
"""
from library_manager import Library
from library_manager import Book
from library_manager import generate_report
from utils import validate_book_data
from utils import format_book_data

# Создание книг
print('Создание книг ---')
bk1 = Book('Живая математика', 'Яков Перельман', 'матемптика')
print(bk1)
bk2 = Book('Математика для Data Science', 'омас Нилд', 'матемптика')
print(bk2)
bk3 =Book('Фейнмановские лекции по физике.Т. I ', 'Ричард Фейнман','физика')
print(bk3)

#Проверка валидации книги
print('Создание книг'-----------)
validate_book_data(bk1)



books0  = [bk1, bk2, bk3]
#Создание библиотеки
library1 = Library(books0)
library1.viewing_books()
#Добавление книги
library1.add_book('Курс общей физики', 'С. Э. Фриш,А. В. Тиморева', 'учебник')
library1.viewing_books()

# Удаление книги

#Не корректное
library1.del_book('Математика')
# Корректное удаление
library1.del_book('Курс общей физики')
library1.viewing_books()

#Корректный поиск
library1.find_book('Живая математика', 'Яков Перельман', 'матемптика'  )

#Не корректный поиск
library1.find_book('Живая математика', 'Яков Перельман', 'физика'  )

generate_report(library1)
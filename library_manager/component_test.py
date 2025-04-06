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
print(f'Создана книга - {bk1}')
bk2 = Book('Математика для Data Science', 'омас Нилд', 'матемптика')
print(f'Создана книга - {bk2}')
bk3 =Book('Фейнмановские лекции по физике.Т. I ', 'Ричард Фейнман','физика')
print(f'Создана книга - {bk3}')
bkbad =Book(123, 'Ричард Фейнман','физика')
print(f'Создана неправильная книга для провеки валидации {bkbad}')

#Проверка валидации книги
print('\nПроверка валидации книги-----------')
if validate_book_data(bk1):
    print(f'Книга {bk1}  соответствует требованиям ')
else:
    print(f'Книга {bk1} не соответствует требованиям ')

if validate_book_data(bkbad):
    print(f'Книга {bkbad}  соответствует требованиям ')
else:
    print(f'Книга {bkbad} не соответствует требованиям ')

#Создание библиотеки
books0  = [bk1, bk2, bk3]
print ('Создание библиотеки --------------')
library1 = Library(books0)
library1.viewing_books()
#Добавление книги
print('Добавление книги ----------------')
library1.add_book('Курс общей физики', 'С. Э. Фриш,А. В. Тиморева', 'учебник')
library1.viewing_books()

# Удаление книги
#Не корректное удаление
print('\nНе корректное удаление книги -------------')
library1.del_book('Математика')
# Корректное удаление
print('Корректное удаление книги -------------')
library1.del_book('Курс общей физики')
library1.viewing_books()

#Корректный поиск
print('\nКорректный поиск ---------------------')
library1.find_book('Живая математика', 'Яков Перельман', 'матемптика'  )

#Не корректный поиск
print('\n Не лорректный поиск ---------------------')
library1.find_book('Живая математика', 'Яков Перельман', 'физика'  )
# Генерация отчета
print('\nГенерация отчета ---------------------')
generate_report(library1)
# Форматирование
print('Форматирование ---------------')
print(format_book_data(bk2))
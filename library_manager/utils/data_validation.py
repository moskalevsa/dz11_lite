
from library_manager.catalog import Book
def validate_book_data(data: Book) -> bool:
    """
    Проверяет корректность данных книги. Например, проверяет, что все обязательные поля присутствуют и корректны.
    :param data книга
    """
    # Проверка типа аргументов и заполнености
    title_is_correct = isinstance(data.get_title(), str) and (len(data.get_title()) > 0)
    author_is_correct = isinstance(data.get_author(), str) and (len(data.get_author()) > 0)
    genre_is_correct = isinstance(data.get_genre(), str) and (len(data.get_genre()) > 0)
    correct_book = title_is_correct and author_is_correct and genre_is_correct
    if not title_is_correct:
        print(f'Название книги {data.get_title()} заполнено не корректно')
    if not author_is_correct:
        print(f'Автор книги {data.get_author()} заполнен не корректно')
    if not genre_is_correct:
        print(f'жанр книги {data.get_genre()} заполнен не корректно')
    return correct_book


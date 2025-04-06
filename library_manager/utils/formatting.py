
from library_manager import Book
def format_book_data(data: Book) -> str:
    """
    Форматирует данные книги для вывода в отчет
    """
    return data.__str__()

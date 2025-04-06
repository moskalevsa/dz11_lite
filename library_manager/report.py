"""
Модуль `report.py
"""
from library_manager import Library
def generate_report(library: Library):
    """
    Генерирует отчет о всех книгах в библиотеке в формате строки.
    """
    librar = library
    librar.viewing_books()
    return


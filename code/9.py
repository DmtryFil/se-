class Book:
    def __init__(self, title, author, pages, genre, year):
        self.title = title
        self.author = author
        self.pages = pages
        self.genre = genre
        self.year = year
        self.current_page = 0  
    
    def show_info(self):
        print(f"Название: {self.title}")
        print(f"Автор: {self.author}")
        print(f"Страниц: {self.pages}")
        print(f"Жанр: {self.genre}")
        print(f"Год издания: {self.year}")

class LibraryBook(Book):
    def __init__(self, title, author, pages, genre, year, library_code):
        super().__init__(title, author, pages, genre, year)
        self.__library_code = library_code  
        self._is_available = True  
        self.__rental_history = []  
    
    def get_library_code(self):
        return f"Код книги: {self.__library_code}"
    
    def borrow_book(self, reader_name):
        if self._is_available:
            self._is_available = False
            self.__rental_history.append(reader_name)
            print(f"Книга '{self.title}' выдана читателю: {reader_name}")
        else:
            print(f"Книга '{self.title}' уже выдана другому читателю")
    
    def return_book(self):
        self._is_available = True
        self.current_page = 0  
        print(f"Книга '{self.title}' возвращена в библиотеку")
    
    def get_rental_history(self):
        return f"История выдачи: {', '.join(self.__rental_history) if self.__rental_history else 'Нет записей'}"
    
    def show_info(self):
        super().show_info()
        print(f"Доступность: {'Доступна' if self._is_available else 'Выдана'}")
        print(self.get_rental_history())


library_book = LibraryBook("Война и мир", "Лев Толстой", 1225, "Роман-эпопея", 1869, "LIB-001")
library_book.show_info()
print(library_book.get_library_code())
library_book.borrow_book("Иван Петров")
library_book.borrow_book("Мария Сидорова")
library_book.return_book()
library_book.borrow_book("Анна Иванова")
library_book.show_info()
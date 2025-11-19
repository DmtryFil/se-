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
    
    def read_page(self):
        if self.current_page < self.pages:
            self.current_page += 1
            print(f"Читаем страницу {self.current_page} из {self.pages}")
        else:
            print("Книга прочитана!")

class Ebook(Book):
    def __init__(self, title, author, pages, genre, year, file_format, file_size):
        super().__init__(title, author, pages, genre, year)
        self.file_format = file_format
        self.file_size = file_size
        self.is_downloaded = False
    
    def show_info(self):
        super().show_info()
        print(f"Формат: {self.file_format}, Размер: {self.file_size}MB")
        print(f"Статус загрузки: {'Загружена' if self.is_downloaded else 'Не загружена'}")
    
    def download(self):
        self.is_downloaded = True
        print(f"Электронная книга '{self.title}' загружена!")
    
    def read_page(self):
        if self.is_downloaded:
            super().read_page()
        else:
            print("Сначала загрузите книгу!")


ebook = Ebook("1984", "Джордж Оруэлл", 328, "Антиутопия", 1949, "PDF", 5)
ebook.show_info()
ebook.download()
ebook.read_page()
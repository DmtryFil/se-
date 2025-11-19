class Book:
    def __init__(self, title, author, pages, genre, year):
        self.title = title
        self.author = author
        self.pages = pages
        self.genre = genre
        self.year = year
        self.current_page = 0
    
    def show_info(self):
        print(f"Книга: '{self.title}'")
        print(f"Автор: {self.author}")
        print(f"Страниц: {self.pages}")
        print(f"Жанр: {self.genre}")
        print(f"Год издания: {self.year}")
        print(f"Прогресс: {self.current_page}/{self.pages} страниц")
    
    def read_page(self):
        if self.current_page < self.pages:
            self.current_page += 1
            print(f"Прочитана страница {self.current_page}/{self.pages}")
            if self.current_page >= self.pages:
                print("Книга полностью прочитана!")
        else:
            print("Книга уже прочитана!")

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

class AudioBook:
    def __init__(self, title, author, duration):
        self.title = title
        self.author = author
        self.duration = duration
        self.current_time = 0
    
    def show_info(self):
        print(f"Аудиокнига: '{self.title}'")
        print(f"Автор: {self.author}")
        print(f"Длительность: {self.duration} минут")
        print(f"Прогресс: {self.current_time}/{self.duration} минут")
    
    def read_page(self):
        if self.current_time < self.duration:
            self.current_time = min(self.current_time + 10, self.duration)  # Ограничение максимума
            print(f"Прослушано {self.current_time}/{self.duration} минут")
            if self.current_time >= self.duration:
                print("Аудиокнига полностью прослушана!")
        else:
            print("Аудиокнига уже прослушана!")

def test_reading_material(material):
    print(f"\n--- Тестирование материала: {material.title} ---")
    material.show_info()
    material.read_page()
    material.read_page()
    print("--- Тестирование завершено ---")


materials = [
    Book("Гарри Поттер", "Дж. К. Роулинг", 500, "Фэнтези", 1997),
    Ebook("451° по Фаренгейту", "Рэй Брэдбери", 256, "Научная фантастика", 1953, "EPUB", 3),
    AudioBook("Маленький принц", "Антуан де Сент-Экзюпери", 120)
]


materials[1].download()


for material in materials:
    test_reading_material(material)

print("\n" + "=" * 60)
print("ВСЕ ЗАДАНИЯ ВЫПОЛНЕНЫ!")
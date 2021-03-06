books = [] # Список для хранени книг (хранение производится в памяти)
           # В пробвинутом варианте следует использовать БД
           # А вот дл реализации запроса на удаление - 
           # придется придумать способ :) *Подсказка: если данные 
           # не удалять фактически, то реализация удаления будет проще

class Book(): # Описание модели предметной области
    def __init__(self,id, name, author, year):
        self.id = id
        self.name = name
        self.author = author
        self.year = year

def init(): # Метод для первоначального заполнения "базы"
    book = Book(0, "Война и мир", "Толстой Л.Н", 1905)
    books.append(book)
    book = Book(1, "Евгений Онегин", "Пушкин А.С.", 1833)
    books.append(book)

init() # При импорте модул будет произведено заполение списка книг
@@ -1,5 +1,6 @@
class Book:
    """ Базовый класс книги. """
    """Базовый класс книги."""

    def __init__(self, name: str, author: str):
        self.name = name
        self.author = author
@@ -11,21 +12,23 @@ def __repr__(self):
        return f"{self.__class__.__name__}(name={self.name!r}, author={self.author!r})"


class PaperBook:
class PaperBook(Book):
    """Класс бумажной книги."""

    def __init__(self, name: str, author: str, pages: int):
        self.name = name
        self.author = author
        super().__init__(name, author)  # Используем конструктор базового класса
        self.pages = pages

    def __str__(self):
        return f"Книга {self.name}. Автор {self.author}"
    def __repr__(self):
        return f"{self.__class__.__name__}(name={self.name!r}, author={self.author!r}, pages={self.pages})"


class AudioBook:
class AudioBook(Book):
    """Класс аудиокниги."""

    def __init__(self, name: str, author: str, duration: float):
        self.name = name
        self.author = author
        super().__init__(name, author)  # Используем конструктор базового класса
        self.duration = duration

    def __str__(self):
        return f"Книга {self.name}. Автор {self.author}"
    def __repr__(self):
        return f"{self.__class__.__name__}(name={self.name!r}, author={self.author!r}, duration={self.duration})"

class BookShelf:
  def __init__(self, *books) -> None:
    self.books = books

  def __str__(self) -> str:
    return f"BookShelf with {len(self.books)} books."
  
  def show_books(self) -> None:
    for book in self.books:
      print(f"I found {book} on the shelf.")

class Book:
  def __init__(self, name: str) -> None:
    self.name = name

  def __str__(self) -> str:
    return f"Book {self.name}"

harry_potter = Book("Harry Potter")
hobbit = Book("Hobbit")
shelf = BookShelf(harry_potter, hobbit)

print(shelf)
shelf.show_books()
class ClassTest:
  def instance_method(self):
    print(f"Calling instance method of {self}")

  @classmethod
  def class_method(cls):
    print(f"Calling class method of {cls}")

  @staticmethod
  def static_method():
    print(f"Calling static method")

test = ClassTest()
test.instance_method()
ClassTest.class_method()
ClassTest.static_method()

class Book:
  Types = ("hardcover", "paperback")
  
  def __init__(self, name: str, book_type: str, weight: int) -> None:
    self.name = name
    self.book_type = book_type
    self.weight = weight

  def __repr__(self):
    return f"<Book: {self.name}, {self.book_type}, weight: {self.weight}>"

  @classmethod
  def hardcover(cls, name: str, page_weight: int) -> "Book":
    return cls(name, cls.Types[0], page_weight + 100)

  @classmethod
  def paperback(cls, name: str, page_weight: int) -> "Book":
    return cls(name, cls.Types[1], page_weight)

book = Book.hardcover("Harry potter", 1500)
light = Book.paperback("Python 101", 600)

print(book, light)
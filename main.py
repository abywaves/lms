class Library:
  def __init__(self, name, books, users):
    self.name = name
    self.books = books
    self.users = users

class Book:
  def __init__(self, title, author, genre, available):
    self.title = title
    self.author = author
    self.genre = genre
    self.available = available

class User:
  def __init__(self, memberID, name):
    self.memberID = memberID
    self.name = name
    print("I am a user")


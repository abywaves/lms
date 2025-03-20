exit = 0
while exit == 0:
  print("Welcome to the Library Management System")
  print("1. Add New Book")
  print("2. View All Books")
  print("3. Borrow Book")
  print("4. Return Book")
  print("5. View Borrowed Books")
  print("6. Exit")
  M = int(input("Please enter your choice:"))

  if M == 1:
    print("Add New Book\n")
  elif M == 2:
    print("View All Books\n")
  elif M == 3:
    print("Borrow Book\n")
  elif M == 4:  
    print("Return Book\n")
  elif M == 5:
    print("View Borrowed Books\n")
  elif M == 6:
    print("Exit\n")
    exit = 1

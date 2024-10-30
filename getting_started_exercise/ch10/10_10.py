with open("book.txt") as book:
    content = book.read()
    num = content.lower().count("the")
    print(num)
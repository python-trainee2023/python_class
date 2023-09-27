def search_by_author(name):
    try:
        found_books = []
        with open("boo000k.txt", 'r') as file:
            for line in file:
                author, title = line.strip().split(',')
                if author == name:
                    found_books.append(title)

        if found_books:
            print("books by the author ", name)
            for book in found_books:
                print(f"title:{book} ")
        else:
            print("no books found by author ", name)
    # except FileNotFoundError:
    #     print("the file book.txt containing the records doesn't exist")
    except Exception as e:
        print(f"an error had occured:: {str(e)}")


author_name = input("enterthe authors name:")
search_by_author(author_name.lower())

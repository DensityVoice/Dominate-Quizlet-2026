class Book:
    def __init__(self, title, pages):
        self.title = title
        self.pages = pages


class ReadingList:
    def __init__(self):
        self.books = []

    def add_book(self, title, pages):
        self.books.append(Book(title, pages))

    def total_pages(self):
        return sum(book.pages for book in self.books)

    def print_list(self):
        print("Reading List")
        print("============")

        for book in self.books:
            print(f"{book.title} | {book.pages} pages")

        print("============")
        print(f"Total Pages: {self.total_pages()}")


def main():
    reading_list = ReadingList()

    reading_list.add_book("Clean Code", 464)
    reading_list.add_book("The Pragmatic Programmer", 352)
    reading_list.add_book("Design Patterns", 395)
    reading_list.add_book("Refactoring", 448)

    reading_list.print_list()


if __name__ == "__main__":
    main()

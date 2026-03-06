class Library:
    def __init__(self, book_name, author):
        self.book_name = book_name
        self.author = author
        self.is_available = True

    def check_out(self):
        if self.is_available:
            self.is_available = False
            print(f"'{self.book_name}' has been checked out.")
        else:
            print(f"Sorry, '{self.book_name}' is already checked out.")

    def return_book(self):
        if not self.is_available:
            self.is_available = True
            print(f"'{self.book_name}' has been returned.")
        else:
            print(f"'{self.book_name}' was not checked out.")

    def display_book(self):
        status = "Available" if self.is_available else "Not Available"
        print(f"Book Name: {self.book_name}")
        print(f"Author: {self.author}")
        print(f"Status: {status}")
        print("-" * 30)
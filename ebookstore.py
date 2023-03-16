import sqlite3

# Create a database called ebookstore
db = sqlite3.connect('ebookstore')

cursor = db.cursor()

# create a table called books
cursor.execute('''
CREATE TABLE IF NOT EXISTS books(
id INTEGER PRIMARY KEY,
Title TEXT,
Author TEXT,
Qty INTEGER)
''')

# Add entries to the books table
books_ = [(3001, 'A Tale of Two Cities', 'Charles Dickens', 30,),
          (3002, 'Harry Potter and the Philosopher\'s Stone', 'J.K. Rowling', 40,),
          (3003, 'The Lion, the Witch and the Wardrobe', 'C.S. Lewis', 25,),
          (3004, 'The Lord of the Rings', 'J.R.R. Tolkien', 37,),
          (3005, 'Alice in Wonderland', 'Lewis Carroll', 12,)]

cursor.executemany('''
INSERT INTO books VALUES(?,?,?,?)
''', books_)
db.commit()


# Create a function that adds a new book to the database
def enter_book(book_id, book_title, book_author, book_quantity):
    """Add a new book to the database"""
    cursor.execute('''
INSERT INTO books VALUES(?,?,?,?)
''', (book_id, book_title, book_author, book_quantity,))
    db.commit()
    print('The new book has been added.')


# Create a function that updates the information about a book in the database
def update_book(book_id, selection):
    """Update the information about a book in the database"""
    if selection == 't':
        book_title = input('Please enter the book\'s new title: ')
        cursor.execute('''
UPDATE books
SET Title = ? WHERE id = ?
''', (book_title, book_id,))
        db.commit()
        print('The book\'s title has been updated.')
    elif selection == 'a':
        book_author = input('Please enter the book\'s new author: ')
        cursor.execute('''
UPDATE books
SET Author = ? WHERE id = ?
''', (book_author, book_id,))
        db.commit()
        print('The book\'s author has been updated.')
    elif selection == 'q':
        while True:
            try:
                book_quantity = int(input('Please enter the book\'s new quantity: '))
                cursor.execute('''
UPDATE books
SET Qty = ? WHERE id = ?
''', (book_quantity, book_id,))
                db.commit()
                print('The book\'s quantity has been updated.')
                break
            except:
                print('Your input was invalid (e.g. a spelling mistake or the ID already exists), please try again')


# Create a function that deletes a book from the database
def delete_book(book_id):
    """Delete a book from the database"""
    cursor.execute('''
DELETE FROM books 
WHERE id = ?
''', (book_id,))
    db.commit()
    print('The book has been deleted.')


# Create a function that searches for a book in the database
def search_books(selection):
    """Search for a book in the database"""
    if selection == 'i':
        while True:
            try:
                search = int(input('PLease enter the ID you would like to search for: '))
                cursor.execute('''
SELECT * FROM books
WHERE id = ?    
''', (search,))
                books = cursor.fetchall()
                print(f'Here are all the books where the ID is \'{search}\':')
                for row in books:
                    print('ID: {0}\nTitle: {1}\nAuthor: {2}\nQuantity: {3}\n'.format(row[0], row[1], row[2], row[3]))
                break
            except:
                print('Your input was invalid (e.g. a spelling mistake or the ID already exists), please try again')
    if selection == 't':
        while True:
            try:
                search = input('PLease enter the title you would like to search for: ')
                cursor.execute('''
SELECT * FROM books
WHERE Title = ?    
''', (search,))
                books = cursor.fetchall()
                print(f'Here are all the books where the title is \'{search}\':')
                for row in books:
                    print('ID: {0}\nTitle: {1}\nAuthor: {2}\nQuantity: {3}\n'.format(row[0], row[1], row[2], row[3]))
                break
            except:
                print('Your input was invalid (e.g. a spelling mistake or the ID already exists), please try again')
    if selection == 'a':
        while True:
            try:
                search = input('PLease enter the author you would like to search for: ')
                cursor.execute('''
SELECT * FROM books
WHERE Author = ?    
''', (search,))
                books = cursor.fetchall()
                print(f'Here are all the books where the author is \'{search}\':')
                for row in books:
                    print('ID: {0}\nTitle: {1}\nAuthor: {2}\nQuantity: {3}\n'.format(row[0], row[1], row[2], row[3]))
                break
            except:
                print('Your input was invalid (e.g. a spelling mistake or the ID already exists), please try again')
    if selection == 'q':
        while True:
            try:
                search = int(input('PLease enter the quantity you would like to search for: '))
                cursor.execute('''
SELECT * FROM books
WHERE Qty = ?    
''', (search,))
                books = cursor.fetchall()
                print(f'Here are all the books where the quantity is \'{search}\':')
                for row in books:
                    print('ID: {0}\nTitle: {1}\nAuthor: {2}\nQuantity: {3}\n'.format(row[0], row[1], row[2], row[3]))
                break
            except:
                print('Your input was invalid (e.g. a spelling mistake or the ID already exists), please try again')


start = True
while start:
    # Create a menu that the user can choose from
    menu = input('''
Welcome to the ebook store. What would you like to do?
1 - Enter book
2 - Update book
3 - Delete book
4 - Search books
0 - Exit
: ''')
    # Create each option and link to appropriate function
    if menu == '1':
        while True:
            try:
                book_id = int(input('Please enter the new book\'s ID number: '))
                book_title = input('Please enter the new book\'s title: ')
                book_author = input('Please enter the new book\'s author: ')
                book_quantity = int(input('Please enter the new book\'s quantity: '))
                enter_book(book_id, book_title, book_author, book_quantity)
                break
            except:
                print('One of your inputs was invalid (e.g. a spelling mistake or the ID already exists), '
                      'please try again')
    elif menu == '2':
        decision = False
        while not decision:
            while True:
                try:
                    book_id = int(input('Please enter the ID number of the book you would like to update: '))
                    cursor.execute('''
SELECT * FROM books WHERE id = ?
''', (book_id,))
                    book = cursor.fetchone()
                    print(f'ID: {book[0]}\nTitle: {book[1]}\nAuthor: {book[2]}\nQuantity: {book[3]}\n')
                    break
                except:
                    print('Your input was invalid (e.g. a spelling mistake or the ID already exists), please try again')
            choice = input('Is this the book you want to update (y/n)?: ').lower()
            if choice == 'y':
                selection = input('''
What would you like to update:
t - Title of the book
a - author of the book
q - quantity of the book
: ''').lower()
                update_book(book_id, selection)
                choice = input('Would you like to update another book (y/n)?: ').lower()
                if choice == 'y':
                    pass
                elif choice == 'n':
                    decision = True
                else:
                    print('You have made a wrong choice, Please Try again')
            elif choice == 'n':
                decision = True
            else:
                print('You have made a wrong choice, Please Try again')
    elif menu == '3':
        decision = False
        while not decision:
            while True:
                try:
                    book_id = int(input('Please enter the ID number of the book you would like to delete: '))
                    cursor.execute('''
SELECT * FROM books WHERE id = ?
''', (book_id,))
                    book = cursor.fetchone()
                    print(f'ID: {book[0]}\nTitle: {book[1]}\nAuthor: {book[2]}\nQuantity: {book[3]}\n')
                    break
                except:
                    print('Your input was invalid (e.g. a spelling mistake or the ID already exists), please try again')
            choice = input('Is this the book you want to delete (y/n)?: ').lower()
            if choice == 'y':
                delete_book(book_id)
                choice = input('Would you like to delete another book (y/n)?: ').lower()
                if choice == 'y':
                    pass
                elif choice == 'n':
                    decision = True
                else:
                    print('You have made a wrong choice, Please Try again')
            elif choice == 'n':
                decision = True
            else:
                print('You have made a wrong choice, Please Try again')
    elif menu == '4':
        decision = False
        while not decision:
            selection = input('''
What would you like to search for:
i - ID of the book
t - Title of the book
a - author of the book
q - quantity of the book
: ''').lower()
            if selection in ('i', 't', 'a', 'q'):
                search_books(selection)
                decision = True
            else:
                print('You have made a wrong choice, Please Try again')
    # Close program and database
    elif menu == '0':
        print('Goodbye!')
        db.close()
        exit()
    else:
        print('You have made a wrong choice, Please Try again')

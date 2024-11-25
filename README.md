# Book-Nest-Django-App
This is Book Nest, an e-book application where you can explore your favourite books.

## User Types:
1.Regular (registered) user. View the catalog, add some of the books to your favourites, write reviews and manage your profile settings.
2.Staff user. Can do all the things a Regular user can, but also perform CRUD operations on books and authors.
3.Admin user. The most powerful type of user who can perform CRUD operations on books, authors and user profiles.

## In order to use the Book Nest app, follow the steps below:
1.Clone the repository (git clone https://github.com/AndreyKirilov/Book-Nest-Django-App.git)

2.Navigate to the project directory

3.Set up virtual environment (python -m venv venv; venv\Scripts\activate)

4.The user's credentials are located in the 'users' file of the project, but you can also view them here:
  - Admin user: email: admin@gmail.com, password: 12345
  - Staff user: email: andrey@gmail.com, password: softuni1
  - Regular user: email: pesho@gmail.com, password: softuni2
    
  !You can also use the register functionality, but it will create a Regular user which can be assigned as a Staff user from the Admin!

## Dependencies
You can find all the project's dependencies in the "requirements.txt" file. Install them with the command "pip install -r requirements.txt".

## Project Credentials
 - SECRET_KEY - 'django-insecure-r41ktjr+jx^6c8&awvybxorshs7h8&u1!z#8j$4yz3jj#41!-g'
 - DEBUG = True
 - DB_NAME = 'book_nest_db'
 - DB_USER = 'postgres'
 - DB_PASSWORD = 'Andreicho_06'
 - DB_HOST = 'localhost'
 - DB_PORT = '5432'

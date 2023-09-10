# Accuknox Project URL Configuration

#Note that the project is already configured, the model is migrated and sqlite database has the data for all three apps, books, data visualization and students form.
Welcome to the Accuknox Internship project configuration documentation. This Django project is organized into three distinct apps: Books, CSVDB, and Students, each serving a specific purpose within the project.

## Main URLs Configuration

The main `urlpatterns` list in the project's `urls.py` file includes various URL patterns. Let's break down these URL patterns:

### Home

- URL Pattern: `''`
- View: `views.home`
- Name: `home`

This URL pattern maps to the home view of the entire project.

### Books

The Books app retrieves data of books from an SQLite database using a subset of the [Books Dataset](https://www.kaggle.com/datasets/saurabhbagchi/books-dataset) available on Kaggle. It provides a search functionality using a search bar.

- URL Pattern: `'books/'`
- View: `include('books.urls')`

This URL pattern includes the URL patterns defined in the `books` app.

### CSVDB

The CSVDB app allows users to input CSV files containing student marks and provides visualizations of statistics based on the data. It uses the [Students Marksheet Dataset](https://www.kaggle.com/datasets/rohithmahadevan/students-marksheet-dataset) available on Kaggle.

**<span style="color:#007aff; font-size: 25px;">Please Note: To get statistics, use only the "marksheet.csv" file present inside the main/parent root folder of the project when uploading data on the CSVDB pages.</span>**

- URL Pattern: `'csvdb/'`
- View: `include('csvdb.urls')`

This URL pattern includes the URL patterns defined in the `csvdb` app.

### Students

The Students app records student information in the database.

- URL Pattern: `'students/'`
- View: `include('students.urls')`

This URL pattern includes the URL patterns defined in the `students` app.

## Books App URLs

In the `books` app, the following URL patterns are defined:

### Search Books

- URL Pattern: `''`
- View: `views.search_books`
- Name: `books`

This URL pattern allows users to search for books in the database.

### Book Detail

- URL Pattern: `'book/<int:book_id>/'`
- View: `views.book_detail`
- Name: `book_detail`

This URL pattern is used to display detailed information about a specific book.

## CSVDB App URLs

In the `csvdb` app, various URL patterns are defined for handling CSV data and statistics visualization.

## Students App URLs

In the `students` app, various URL patterns are defined for managing student records.

This concludes the documentation for the URL configuration of the Accuknox project.

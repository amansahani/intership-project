# Accuknox Project URL Configuration

Welcome to the Accuknox project URL configuration documentation. This Django project is organized into three distinct apps: Books, CSVDB, and Students, each serving a specific purpose within the project.

## Overview

In Django, the `urlpatterns` list is used to route URLs to views. This configuration determines how different parts of your web application respond to specific URL patterns. Below, we outline the main URL patterns for the entire project and provide a brief overview of each app.

For more detailed information about URL routing in Django, please refer to the [official Django documentation on URL routing](https://docs.djangoproject.com/en/4.2/topics/http/urls/).

## Main URLs Configuration

The main `urlpatterns` list in the project's `urls.py` file includes various URL patterns. Let's break down these URL patterns:

### Home

- URL Pattern: `''`
- View: `views.home`
- Name: `home`

This URL pattern maps to the home view of the entire project.

### Admin

- URL Pattern: `'admin/'`
- View: `admin.site.urls`

This URL pattern is used for the Django admin panel.

### Books

The Books app retrieves data of books from an SQLite database using a subset of the [Books Dataset](https://www.kaggle.com/datasets/saurabhbagchi/books-dataset) available on Kaggle. It provides a search functionality using a search bar.

- URL Pattern: `'books/'`
- View: `include('books.urls')`

This URL pattern includes the URL patterns defined in the `books` app.

### CSVDB

The CSVDB app allows users to input CSV files containing student marks and provides visualizations of statistics based on the data. It uses the [Students Marksheet Dataset](https://www.kaggle.com/datasets/rohithmahadevan/students-marksheet-dataset) available on Kaggle.

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

_[Please provide specific details of URL patterns and views related to the CSVDB app]_

## Students App URLs

In the `students` app, various URL patterns are defined for managing student records.

_[Please provide specific details of URL patterns and views related to the Students app]_

This concludes the documentation for the URL configuration of the Accuknox project. For more detailed information on each app's specific views and functionality, please refer to the respective app's documentation.

For additional information about the project's implementation and usage, please consult the project's main documentation.

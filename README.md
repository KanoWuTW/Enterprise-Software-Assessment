# Django Shopping Web Application

## Overview
This project is a database-driven web application built with Django.  
It allows users to browse products, view details, search items, and interact through a wishlist/basket system.

The application is based on a fictional dataset and focuses on clean structure, usability, and core Django functionality.

---

## Features

- All product list pages, product list by category pages, and detail pages
- User registration and login
- Wishlist / basket functionality
- Search functionality (keyword-based)
- Data validation and error handling
- 3 Automated tests 
- Deployed on PythonAnywhere

---

## Data

- Dataset: Created manually and by GenAI(Copilot), and from no real-world data source
- Records: 150 entries
- Five related models:
  - Product
  - Category
  - Profile
  - Wishlist
  - Basket


---

## Technologies Used

- Python
- Django
- SQLite
- HTML
- CSS
- JavaScript
- Bootstrap

---

## Installation

```bash
git clone https://github.com/KanoWuTW/Enterprise-Software-Assessment.git
cd a_shoping_site

python -m venv .venv
source .venv/bin/activate  # Windows: .venv\Scripts\activate

pip install -r requirements.txt

python manage.py migrate
python manage.py loaddata category.json
python manage.py loaddata product.json

python manage.py test # Runtest

python manage.py runserver
```

## Using the system

1. Open a browser
2. Vist URL http://127.0.0.1:8000/ (Local host) or https://t02cw25.pythonanywhere.com/ (PythonAnywhere)

### Looking items
1. On the home page, use the left and right arrow buttons to browse all the items.
2. Click the category name (e.g. Food) to see items by category.
3. Click the item name to view item details.
4. Type keywords in the search bar to find items.

### User account
To use the basket and wishlist features, users must register and sign in to an account.

1. Click the “Account” dropdown menu, and sign up to get an account.
2. Once the user has an account, the Log Out and Sign In buttons are available.

### Basket and wishlist
Once you are signed in, you can click the “Add to basket” button to add items to your basket. You can click the same items multiple times to add the quantity you need. Wishlist works similarly to a basket, but it does not track item quantities.


## Project Structure
a_shoping_site/
├── account/                # User account app (registration, login, profile)
│   ├── admin.py
│   ├── apps.py
│   ├── migrations/
│   ├── models.py
│   ├── tests.py
│   ├── urls.py
│   ├── views.py
│   └── __init__.py
├── a_shoping_site/         # Django project settings and root URLs
│   ├── asgi.py
│   ├── settings.py
│   ├── urls.py
│   ├── wsgi.py
│   └── __init__.py
├── items/                  # Product and category app
│   ├── admin.py
│   ├── apps.py
│   ├── migrations/
│   ├── models.py
│   ├── tests.py
│   ├── urls.py
│   ├── views.py
│   └── __init__.py
├── user/                   # Basket and wishlist app
│   ├── admin.py
│   ├── apps.py
│   ├── migrations/
│   ├── models.py
│   ├── tests.py
│   ├── urls.py
│   ├── views.py
│   └── __init__.py
├── static/                 # Static files (JS, CSS, images)
│   └── scripts/
├── templates/              # HTML templates
│   ├── 404.html
│   ├── basket.html
│   ├── item_list_template.html
│   ├── item_template.html
│   ├── search_result.html
│   ├── signin.html
│   ├── signup.html
│   ├── wishlist.html
│   └── index.html
├── category.json           # Category fixture data
├── product.json            # Product fixture data
├── db.sqlite3              # SQLite database
├── manage.py               # Django management script
├── requirements.txt        # Python dependencies
└── README.md               # Project documentation
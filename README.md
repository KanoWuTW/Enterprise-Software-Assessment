# Django Shopping Web Application

## Overview
This project is a database-driven web application built with Django.  
It allows users to browse products, view details, search items, and interact through a wishlist/basket system.

The application is based on a fictional dataset and focuses on clean structure, usability, and core Django functionality.

---

## Features

- All product list page, product list by category page, and detail page
- User registration and login
- Wishlist / basket functionality
- Search functionality (keyword-based)
- Data validation and error handling
- 3 Automated tests 
- Deployed on PythonAnywhere

---

## Data

- Dataset: Created mannually and by GenAI(Copilot) and from no real-world data source
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
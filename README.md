# Flask E-commerce Market

A full-stack e-commerce application built with **Python** and **Flask**. This project simulates a marketplace where users can create accounts, manage their budget, and buy/sell items in real-time.

## Key Features

* **User Authentication**: Secure registration and login system using `Flask-Login` and `Bcrypt` for password hashing.
* **Marketplace Logic**:
    * **Purchase**: Users can buy items if they have sufficient funds; ownership transfers immediately.
    * **Sell**: Users can sell items back to the market to reclaim funds.
* **Database Management**: Relational data handling between Users and Items using **SQLAlchemy** (One-to-Many relationship).
* **Interactive UI**: Responsive design using **Bootstrap**, featuring modal confirmations for transactions and dynamic Flash messaging for user feedback.
* **Form Validation**: Robust input validation using `Flask-WTF` to prevent invalid data entry and ensure security.

## Tech Stack

* **Language**: Python 3
* **Framework**: Flask
* **Database**: SQLite, SQLAlchemy (ORM)
* **Frontend**: HTML5, CSS3, Bootstrap, Jinja2
* **Forms & Security**: Flask-WTF, Flask-Login, Flask-Bcrypt

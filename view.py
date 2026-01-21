from market import app
from market.models import Item, User

with app.app_context():
    print('Item:')
    for i in Item.query.all():
        print(f'ID: {i.id}, Name: {i.name}, Price: {i.price}, Barcode: {i.barcode}, Description: {i.description}')
        print('-' * 83)

    print('User:')
    for x in User.query.all():
        print(f'ID: {x.id}, Name: {x.username}, Email: {x.email}, password: {x.password}, Budget: {x.budget}')
        print('-' * 83)

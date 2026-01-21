from market import app, db
from market.models import Item, User
import random

choice = ['Phone', 'Tablet', 'Camera', 'Keyboard', 'Mouse', 'Monitor']

with app.app_context():
    for i in choice:
        price = random.randint(100000, 500000)
        barcode = str(random.randint(100000000000, 999999999999))

        item1 = Item(name=i, price=price, barcode=barcode, description='description')
        db.session.add(item1)
        db.session.commit()
        print(f'{i} commit successfully')
from market import db, login_manager
from market import bcrypt
from flask_login import UserMixin

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

class User(db.Model, UserMixin):
    id = db.Column(db.Integer(), primary_key=True)
    username = db.Column(db.String(length=20), nullable=False, unique=True)
    email = db.Column(db.String(length=30), nullable=False, unique=True)
    password_hash = db.Column(db.String(length=30), nullable=False)
    budget = db.Column(db.Integer(), nullable=False, default=1000000)
    items = db.relationship('Item', backref='owned_user', lazy=True)

    @property
    def prettier_budget(self):
        return f'£{self.budget:,}'

    @property
    def password(self):
        return self.password_hash

    @password.setter
    def password(self, password):
        self.password_hash = bcrypt.generate_password_hash(password).decode('utf-8')

    def check_correction(self, attempt_password):
        return bcrypt.check_password_hash(self.password_hash, attempt_password)

    def can_purchase(self, item_obj):
        return self.budget >= item_obj.price

    def can_discard(self,item_obj):
        return item_obj in self.items

class Item(db.Model):
    id = db.Column(db.Integer(), primary_key=True)
    name = db.Column(db.String(length=30), nullable=False)
    price = db.Column(db.Integer(), nullable=False)
    barcode = db.Column(db.String(length=12), nullable=False, unique = True)
    description = db.Column(db.String(length=1024), nullable=False)
    owner = db.Column(db.Integer(), db.ForeignKey('user.id'))

    def __repr__(self):
        return f'{self.name}'

    def buy(self, user):
        self.owner = user.id
        user.budget -= self.price
        db.session.commit()

    def discard(self, user):
        self.owner = None
        user.budget += self.price
        db.session.commit()
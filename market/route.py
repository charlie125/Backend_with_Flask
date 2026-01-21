from market import app, db
from flask import render_template, redirect, url_for, flash, request
from market.models import Item, User
from market.form import RegisterForm, LoginForm, PurchaseForm, DiscardForm
from flask_login import login_user, logout_user, login_required, current_user


@app.route('/')
@app.route('/home')
def main_page():
    return render_template('home_page.html')


@app.route('/register', methods=['GET', 'POST'])
def regiser_page():
    form = RegisterForm()
    if form.validate_on_submit():
        user = User(username=form.username.data, email=form.email.data, password=form.password1.data)
        db.session.add(user)
        db.session.commit()

        login_user(user)
        flash(f'Account created successfully, you are now logged in as {form.username.data}', category='success')
        return redirect(url_for('market_page'))

    if form.errors != {}:
        for err_msg in form.errors.values():
            flash(f'There is some error {err_msg}', category='danger')
    return render_template('regiser_page.html', form=form)


@app.route('/market', methods=['POST', 'GET'])
@login_required
def market_page():
    purchase_form = PurchaseForm()
    discard_form = DiscardForm()

    if request.method == 'POST':
        # purchase algo
        purchased_item = request.form.get('purchased_item')
        purchased_object = Item.query.filter_by(name=purchased_item).first()
        if purchased_object:
            if current_user.can_purchase(purchased_object):
                purchased_object.buy(current_user)
                flash(f'Congratulation! you just purchased {purchased_object.name} for £{purchased_object.price}.',
                      category='success')
            else:
                flash(f'Balance not enough for {purchased_object.name}', category='warning')

        # discard algo
        discard_item = request.form.get('discard_item')
        discard_item_obj = Item.query.filter_by(name=discard_item).first()
        if discard_item_obj:
            if current_user.can_discard(discard_item_obj):
                discard_item_obj.discard(current_user)
                flash(f'Congratulation! you just discard {discard_item_obj.name} for £{discard_item_obj.price}',
                      category='success')
            else:
                flash(f'There is no item name {discard_item_obj.name} is your basket.', category='warning')
        return redirect(url_for('market_page'))

    if request.method == 'GET':
        items = Item.query.filter_by(owner=None)
        owned_items = Item.query.filter_by(owner=current_user.id)
        return render_template('market_page.html', items=items, purchase_form=purchase_form, owned_items=owned_items,
                               discard_form=discard_form)


@app.route('/login', methods=['GET', 'POST'])
def login_page():
    form = LoginForm()
    if form.validate_on_submit():
        attempted_user = User.query.filter_by(username=form.username.data).first()
        if attempted_user and attempted_user.check_correction(form.password.data):
            login_user(attempted_user)
            flash(f'Success! You are logged in as: {attempted_user.username}', category='success')
            return redirect(url_for('market_page'))
        else:
            flash('Username or password are incorrect! Please try again.', category='danger')

    return render_template('login_page.html', form=form)


@app.route('/logout')
def logout_page():
    logout_user()
    flash(f'You have been logged out', category='warning')
    return redirect(url_for('main_page'))

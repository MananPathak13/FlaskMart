from flask import Flask, render_template, redirect, url_for, request
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager, UserMixin, login_user, login_required, current_user
import stripe

app = Flask(__name__)
app.config['SECRET_KEY'] = 'your_secret_key'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
db = SQLAlchemy(app)
login_manager = LoginManager(app)

stripe.api_key = "your_stripe_secret_key"

from models import User, Product
from forms import RegistrationForm, CheckoutForm

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

@app.route("/")
def home():
    products = Product.query.all()
    return render_template('home.html', products=products)

@app.route("/register", methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        user = User(username=form.username.data, email=form.email.data)
        db.session.add(user)
        db.session.commit()
        login_user(user)
        return redirect(url_for('home'))
    return render_template('register.html', form=form)

@app.route("/checkout/<int:product_id>", methods=['GET', 'POST'])
@login_required
def checkout(product_id):
    product = Product.query.get_or_404(product_id)
    form = CheckoutForm()
    if form.validate_on_submit():
        try:
            charge = stripe.Charge.create(
                amount=int(product.price * 100),
                currency='usd',
                description=product.name,
                source=form.stripe_token.data
            )
            return render_template('success.html')
        except stripe.error.CardError as e:
            return render_template('checkout.html', form=form, error=e.user_message)
    return render_template('checkout.html', form=form, product=product)

if __name__ == "__main__":
    app.run(debug=True)

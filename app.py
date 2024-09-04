from flask import Flask, render_template, request, send_from_directory, redirect, url_for, flash, session,jsonify
from swiggy_module import Swiggy
from Zomato.zomato_module import Zomato
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app = Flask(__name__, static_folder='static', template_folder='templates')
app.secret_key = 'root'

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///price_compare.db'
db = SQLAlchemy(app)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(255), nullable=False)

class Feedback(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    review_text = db.Column(db.String(500), nullable=False)
    rating = db.Column(db.Integer, nullable=False)

class Contact(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)
    email = db.Column(db.String(120), nullable=False)
    message = db.Column(db.Text, nullable=False)
    date_submitted = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)

with app.app_context():
    db.create_all()

@app.route("/")
def home():
    return render_template("home.html")

@app.route("/home")
def home_page():
    return render_template("home.html")

@app.route("/login_page.html")
def login_page():
    return render_template("login.html")

@app.route("/contact_page.html")
def contact():
    return render_template("contact.html")

@app.route("/about_us")  
def about_us():
    return render_template("about_us.html")

@app.route("/register", methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        email = request.form['email']
        password = request.form['password']

        existing_user = User.query.filter_by(email=email).first()
        if existing_user:
            flash('Email already exists. Please use a different email.')
        else:
            new_user = User(username=username, email=email, password=password)
            db.session.add(new_user)
            db.session.commit()
            flash('Registration successful. You can now log in.')

    return redirect(url_for('login_page'))
   
@app.route("/login", methods=['POST'])
def login():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']

        user = User.query.filter_by(email=email, password=password).first()

        if user:
            session['user_id'] = user.id
            flash('Login successful.')
            return redirect(url_for('search'))
        else:
            flash('Invalid email or password.')

    return redirect(url_for('login_page'))

@app.route("/search_page.html", methods=['POST', 'GET'])
def search():
    if request.method == "POST":
        city = request.form['city']
        food = request.form['food']
        site = request.form['site']
        
        if site == "zomato":
            dish = Zomato(food, city)
            hotel_info = dish.get_hotel_data()
            #print("Zomato")
        else:
            dish = Swiggy(food, city)
            hotel_info = dish.get_category_dishes()
        print(hotel_info)
        return render_template("result.html", info = hotel_info)
    return render_template("search.html")

@app.route('/Images/<filename>')
def get_image(filename):
    image_dir = 'D:\BE_Group_15_Project_work\Code\PriceCompare_modified\Images'
    return send_from_directory(image_dir, filename)

@app.route("/submit_review", methods=['POST'])
def submit_review():
    if 'user_id' not in session:
        flash('You need to log in to leave a review.')
        return redirect(url_for('login_page'))

    user_id = session['user_id']
    review_text = request.form['application-review']
    rating = int(request.form['star-rating'])

    new_review = Feedback(user_id=user_id, review_text=review_text, rating=rating)
    db.session.add(new_review)
    db.session.commit()

    flash('Review submitted successfully.')
    return redirect(url_for('search'))

@app.route("/submit_contact", methods=['POST'])
def submit_contact():
    data = request.get_json()
    name = data.get('name')
    email = data.get('email')
    message = data.get('message')

    new_contact = Contact(name=name, email=email, message=message)
    db.session.add(new_contact)
    db.session.commit()
    
    return jsonify({'success': True}), 200

if __name__ == '__main__':
    app.run(debug=True)

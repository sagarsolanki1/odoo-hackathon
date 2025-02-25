from flask import Flask, render_template, request, redirect, url_for, session
from datetime import timedelta
import pymongo
import bcrypt
from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()

# MongoDB connection
mongo_uri = os.getenv('MONGO_URI')
client = pymongo.MongoClient(mongo_uri)
db = client["nutrition"]
collection = db["values"]
users_collection = db["users"]  # MongoDB collection for users

app = Flask(__name__)
app.secret_key = os.getenv('SECRET_KEY')
app.permanent_session_lifetime = timedelta(minutes=5)  # Set session timeout to 5 minutes

# Function to calculate BMR and TDEE
def calculate_caloric_intake(age, gender, height, weight, activity_level, disease):
    if gender.lower() == 'male':
        bmr = 88.362 + (13.397 * weight) + (4.799 * height) - (5.677 * age)
    else:
        bmr = 447.593 + (9.247 * weight) + (3.098 * height) - (4.330 * age)

    activity_factors = {
        'sedentary': 1.2,
        'lightly active': 1.375,
        'moderately active': 1.55,
        'very active': 1.725
    }

    tdee = bmr * activity_factors.get(activity_level.lower(), 1.9)
    return tdee

# Function to generate meal plan
def generate_meal_plan(tdee):
    # Sample food items from MongoDB based on some criteria (e.g., calories, macronutrients)
    breakfast_items = list(collection.aggregate([{ '$sample': { 'size': 5 } }]))
    lunch_items = list(collection.aggregate([{ '$sample': { 'size': 5 } }]))
    dinner_items = list(collection.aggregate([{ '$sample': { 'size': 5 } }]))

    # Function to format meal plan output
    def format_meal_plan(items):
        meal_plan = '\n'.join([f"{i+1}. {item['Shrt_Desc']} - Calories: {item['Energ_Kcal']}, Protein: {item['Protein_(g)']}, Carbs: {item['Carbohydrt_(g)']}" for i, item in enumerate(items)])
        return meal_plan

    # Select food items for each meal
    breakfast = format_meal_plan(breakfast_items)
    lunch = format_meal_plan(lunch_items)
    dinner = format_meal_plan(dinner_items)

    return breakfast, lunch, dinner

# Route for home page and meal plan generation
@app.route('/', methods=['GET', 'POST'])
def home():
    if 'user' not in session:
        return redirect(url_for('login'))
    session.permanent = True  # Extend the session lifetime with each request

    if request.method == 'POST':
        # Retrieve form data
        age = int(request.form['age'])
        gender = request.form['gender']
        height = int(request.form['height'])
        weight = int(request.form['weight'])
        activity_level = request.form['activity_level']
        disease = request.form['disease']

        # Calculate required caloric intake
        tdee = calculate_caloric_intake(age, gender, height, weight, activity_level, disease)

        # Generate meal plan
        breakfast, lunch, dinner = generate_meal_plan(tdee)

        # Render template with meal plan results
        return render_template('meal_plan.html', 
                               age=age, gender=gender, height=height, weight=weight,
                               activity_level=activity_level, disease=disease,
                               breakfast=breakfast, lunch=lunch, dinner=dinner)

    # Render the initial form template
    return render_template('index.html')

# Route for user registration
@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        # Retrieve form data
        name = request.form['name']
        email = request.form['email']
        password = request.form['password']

        # Check if the email is already registered
        if users_collection.find_one({'email': email}):
            return "Email already exists. Please use a different email."

        # Hash the password for security
        hashed_password = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())

        # Insert the user into the database
        users_collection.insert_one({
            'name': name,
            'email': email,
            'password': hashed_password,
            'role': 'user'  # Default role for new users
        })

        return redirect(url_for('login'))  # Redirect to login page after registration

    return render_template('register.html')

# Route for user login
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        # Retrieve form data
        email = request.form['email']
        password = request.form['password']

        # Check if the email exists in the database
        user = users_collection.find_one({'email': email})

        if user and bcrypt.checkpw(password.encode('utf-8'), user['password']):
            # Authentication successful, set session variables
            session['user'] = user['email']
            session['role'] = user['role']
            session.permanent = True  # Set the session as permanent to use the timeout

            # Redirect to home page or protected route
            return redirect(url_for('home'))
        else:
            # Invalid credentials
            return "Invalid login credentials. Please try again."

    return render_template('login.html')

# Logout route
@app.route('/logout')
def logout():
    session.clear()  # Clear session variables
    return redirect(url_for('login'))

if __name__ == '__main__':
    app.run(debug=True)

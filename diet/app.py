from flask import Flask, render_template, request
import pymongo

client = pymongo.MongoClient("mongodb+srv://prathamdoshi42:vJdq24J7ZfTqfvRR@cluster0.vsfywjg.mongodb.net/")
db = client["nutrition"]  # Replace with your database name
collection = db["values"]

app = Flask(__name__)

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

if __name__ == '__main__':
    app.run(debug=True)

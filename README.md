Personalized Meal Planner
This web application calculates your Total Daily Energy Expenditure (TDEE) based on your age, gender, height, weight, activity level, and health conditions. It then generates a personalized meal plan using nutrition data stored in MongoDB.

Features
Calculation of TDEE: Based on user inputs, the application calculates the Total Daily Energy Expenditure using the Mifflin-St Jeor Equation adjusted for gender and activity level.

Meal Plan Generation: Once TDEE is calculated, the application fetches food items from MongoDB to generate a meal plan divided into breakfast, lunch, and dinner. Each meal includes food items along with their calorie, carbohydrate, fat, and protein content.

Technologies Used
Flask: Python web framework used for backend development.
MongoDB: NoSQL database used to store and retrieve nutrition data.
HTML/CSS: Frontend templates and styling for user interface.

Run app.py for web application.

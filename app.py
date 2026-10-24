#Fitness Calorie Calculator 
#July 10, 2026

import streamlit as st
import sys
from io import StringIO

st.title("Fitness Calorie Calculator")

#Gather information from the user 
age = st.number_input("What is your age?",min_value=1, value=25)
weight = st.number_input("Please input your weight in pounds",min_value=1.0, value=150.0)
height = st.number_input("Please input your height in inches",min_value=1.0, value=65.0)
gender_answer = st.selectbox("What is your gender?",["Male", "Female"])

activity_level = st.selectbox("How active are you?",["Sedentary (little to no exercise)", "Moderately Active (exercise 3-5 days/week)", "Active (exercise 6-7 days/week)"])

final_goal = st.selectbox("What is your goal?",["Lose weight", "Maintain your weight", "Build muscle"])

if final_goal == "Lose weight":
    intensity = st.selectbox("How quick are you looking to lose weight?",["1 pound per week", "2 pounds per week"])
    
#Mifflin St Jeor equation utilized for calculating the BMR
if st.button("Run Calculator"):
    if gender_answer == "Male":
        BMR = (4.536 * weight) + (15.88 * height) - (4.92 * age) + 5
    else:
        BMR = (4.536 * weight) + (15.88 * height) - (4.92 * age) - 161
    
#Multiplier depending on one's activity level
    if activity_level == "Sedentary (little to no exercise)":
        multiplier = 1.2
    elif activity_level == "Moderately Active (exercise 3-5 days/week)":
        multiplier = 1.55
    else:
        multiplier = 1.725
    
#Product of the BMR and the multiplier
    if final_goal == "Lose weight":
        if intensity == "1 pound per week":
            total_calories = int((BMR * multiplier) - 500)
        else:
            total_calories = int((BMR * multiplier) - 1000)
    elif final_goal == "Maintain your weight":
        total_calories = int((BMR * multiplier))
    else:
        total_calories = int((BMR * multiplier) + 250)

#Calculate the amount of calories from carbs, fats, and protein
    carbohydrates_calories = total_calories * 0.40
    fats_calories = total_calories * 0.30
    proteins_calories = total_calories * 0.30

#Calculate the amount of carbs, fats, and protein in grams one should eating
    carbohydrates = int(carbohydrates_calories // 4)
    fats = int(fats_calories // 9)
    proteins = int(proteins_calories // 4)

#Prints the final calories for the user
    st.write(f"You should be eating {total_calories} calories every day with "
        f"{carbohydrates} grams of carbohydrates, "
        f"{proteins} grams of protein, and "
        f"{fats} grams of fat!")      

#Prints meal plan suggestions based on calorie ranges
    st.subheader("Suggested Daily Meal Plan")

    if total_calories < 1000:
        st.write("Your calorie target is below 1,000 calories. Please consult a healthcare professional before following this plan.")

    elif total_calories < 1500:
        st.write("Breakfast: 1/2 cup dry oatmeal, 1/2 cup blueberries, and 3/4 cup Greek yogurt")
        st.write("Lunch: 3 oz grilled chicken, 2 cups salad greens, 1 slice whole wheat bread, and 1 tablespoon dressing")
        st.write("Dinner: 3 oz baked salmon, 1/2 cup cooked brown rice, and 1 cup steamed broccoli")
        st.write("Snack: 1 small apple and 1 tablespoon peanut butter")

    elif total_calories < 2000:
        st.write("Breakfast: 2 eggs, 2 slices whole wheat toast, and 1 medium banana")
        st.write("Lunch: 4 oz grilled chicken, 1 cup cooked rice, and 1 cup vegetables")
        st.write("Dinner: 4 oz baked salmon, 3/4 cup cooked brown rice, and 1 cup roasted vegetables")
        st.write("Snack: 1 cup Greek yogurt, 1/4 cup granola, and 1 medium apple")

    elif total_calories < 2500:
        st.write("Breakfast: 3 eggs, 2 slices whole wheat toast, 1 medium banana, and 1 tablespoon peanut butter")
        st.write("Lunch: 5 oz grilled chicken, 1.5 cups cooked rice, and 1 cup vegetables")
        st.write("Dinner: 5 oz lean beef, 1 medium baked potato, and 1 cup vegetables")
        st.write("Snack: 1 cup Greek yogurt, 1/4 cup granola, and 1 oz almonds")

    elif total_calories < 3000:
        st.write("Breakfast: 1 cup cooked oatmeal, 3 eggs, 1 banana, and 2 tablespoons peanut butter")
        st.write("Lunch: 6 oz grilled chicken, 2 cups cooked rice, and 1 cup vegetables")
        st.write("Dinner: 6 oz lean beef, 1.5 cups cooked potatoes, and 1 cup vegetables")
        st.write("Snack: 1 protein shake made with 1 cup milk, 1 banana, and 1/4 cup almonds")
        st.write("Extra meal: 1 turkey sandwich with 2 slices whole wheat bread and 2 oz turkey")

    elif total_calories < 3500:
        st.write("Breakfast: 1.5 cups cooked oatmeal, 3 eggs, 1 banana, and 2 tablespoons peanut butter")
        st.write("Lunch: 7 oz grilled chicken, 2 cups cooked rice, and 1 cup vegetables")
        st.write("Dinner: 7 oz lean beef, 2 cups cooked potatoes, and 1 cup vegetables")
        st.write("Snack: 1 protein shake with 1.5 cups milk, 1 banana, and 1/4 cup almonds")
        st.write("Extra meal: Turkey sandwich with 2 slices whole wheat bread, 3 oz turkey, and 1 slice cheese")

    elif total_calories <= 4000:
        st.write("Breakfast: 2 cups cooked oatmeal, 4 eggs, 1 banana, and 2 tablespoons peanut butter")
        st.write("Lunch: 8 oz grilled chicken, 2.5 cups cooked rice, and 1 cup vegetables")
        st.write("Dinner: 8 oz lean beef, 2 cups cooked potatoes, and 1.5 cups vegetables")
        st.write("Snack: Protein shake with 2 cups milk, 1 banana, and 1/4 cup almonds")
        st.write("Extra meal 1: Turkey sandwich with 2 slices whole wheat bread, 3 oz turkey, and 1 slice cheese")
        st.write("Extra meal 2: 1 cup Greek yogurt, 1/2 cup granola, and 1/2 cup berries")

    else:
        st.write("Your calorie target is above 4,000 calories. Consider consulting a registered dietitian for a personalized meal plan.")

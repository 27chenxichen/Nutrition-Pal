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

from langchain_core.tools import tool
import re

@tool(description="Calculate BMI using weight in kg and height in meters.")
def calculate_bmi(weight_kg: float, height_m: float) -> str:
    bmi = weight_kg / (height_m ** 2)
    
    if bmi < 18.5:
        category = "Underweight"
    elif 18.5 <= bmi < 24.9:
        category = "Normal weight"
    elif 25.0 <= bmi < 29.9:
        category = "Overweight"
    else:
        category = "Obesity"
        
    return f"BMI: {bmi:.2f} (Category: {category})"

@tool(description="Calculate BMR using weight in kg, height in cm, age, and gender.")
def calculate_bmr(weight_kg: float, height_cm: float, age: int, gender: str) -> str:
    if gender.lower() == 'male':
        bmr = 10 * weight_kg + 6.25 * height_cm - 5 * age + 5
    else:
        bmr = 10 * weight_kg + 6.25 * height_cm - 5 * age - 161
        
    return f"BMR: {bmr:.2f} calories/day (This is your resting energy expenditure)"

@tool(description="Calculate BMI and fitness info from a query string containing weight and height.")
def fitness_tool(query: str) -> str:
    try:
        numbers = re.findall(r"\d+\.?\d*", query)
        
        if len(numbers) < 2:
            return "Please provide both weight (kg) and height (cm)."
        
        weight = float(numbers[0])
        height_cm = float(numbers[1])
        height_m = height_cm / 100
        bmi = weight / (height_m ** 2)
        
        if bmi < 18.5:
            category = "Underweight"
        elif 18.5 <= bmi < 25:
            category = "Normal Weight"
        elif 25 <= bmi <= 30:
            category = "Overweight"
        else:
            category = "Obese"
            
        return (
            f"Your BMI is {bmi:.2f}, which falls under '{category}'."
            "Maintain a balanced diet and regular exercise."
        )
        
    except Exception:
        return "Could not process the input. Please provide valid weight and height."

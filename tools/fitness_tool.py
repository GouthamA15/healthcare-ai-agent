from langchain_core.tools import tool

@tool
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

@tool
def calculate_bmr(weight_kg: float, height_cm: float, age: int, gender: str) -> str:
    if gender.lower() == 'male':
        bmr = 10 * weight_kg + 6.25 * height_cm - 5 * age + 5
    else:
        bmr = 10 * weight_kg + 6.25 * height_cm - 5 * age - 161
        
    return f"BMR: {bmr:.2f} calories/day (This is your resting energy expenditure)"

from langchain.tools import tool
import re

@tool
def fitness_tool(query: str) -> str:
    """
    Use this tool to calculate BMI and assess basic fitness. 
    Input should include weight (kg) and height (cm).
    """
    
    try:
        #Extract numbers from query
        numbers = re.findall(r"\d+\.?\d*", query)
        
        if len(numbers) < 2:
            return "Please provide both weight (kg) and height (cm)."
        
        weight = float(numbers[0])
        height_cm = float(numbers[1])
        
        #Convert height to meters
        height_m = height_cm / 100
        
        #BMI formula
        bmi = weight / (height_m ** 2)
        
        #Classification
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
    
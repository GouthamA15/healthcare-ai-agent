from langchain_core.tools import tool

INTERACTIONS = {
    "aspirin": ["warfarin", "clopidogrel", "ibuprofen"],
    "metformin": ["contrast medium", "alcohol"],
    "lisinopril": ["potassium supplements", "spironolactone"],
    "warfarin": ["aspirin", "vitamin k", "cranberry juice"],
    "simvastatin": ["grapefruit juice", "erythromycin", "itraconazole"]
}

@tool
def check_drug_interaction(drug1: str, drug2: str) -> str:
    drug1, drug2 = drug1.lower().strip(), drug2.lower().strip()
    
    if drug1 in INTERACTIONS and drug2 in INTERACTIONS[drug1]:
        return f"Warning: Potential interaction between {drug1} and {drug2} found. Please consult a doctor."
    if drug2 in INTERACTIONS and drug1 in INTERACTIONS[drug2]:
        return f"Warning: Potential interaction between {drug1} and {drug2} found. Please consult a doctor."
        
    return f"No common interaction found between {drug1} and {drug2} in our simple database. Always verify with a healthcare professional."

@tool
def get_medication_info(med_name: str) -> str:
    med_database = {
        "metformin": "A medication for type 2 diabetes that helps control blood sugar levels.",
        "lisinopril": "An ACE inhibitor used to treat high blood pressure and heart failure.",
        "simvastatin": "A statin used to lower cholesterol and prevent heart disease.",
        "aspirin": "A pain reliever, fever reducer, and anti-inflammatory drug; often used for heart health."
    }
    
    med_name = med_name.lower().strip()
    return med_database.get(med_name, "Medication not found in simple database. Use the medical knowledge tool for more details.")

from langchain_core.tools import tool

INTERACTIONS = {
    "aspirin": ["warfarin", "clopidogrel", "ibuprofen"],
    "metformin": ["contrast medium", "alcohol"],
    "lisinopril": ["potassium supplements", "spironolactone"],
    "warfarin": ["aspirin", "vitamin k", "cranberry juice"],
    "simvastatin": ["grapefruit juice", "erythromycin", "itraconazole"]
}

# Simple static database (can upgrade later)
MEDICATION_DB = {
    "paracetamol": {
        "use": "Used to treat fever and mild to moderate pain.",
        "dosage": "Typically 500mg–1000mg every 4–6 hours (max 4g/day).",
        "warning": "Avoid overdose as it may cause liver damage."
    },
    "ibuprofen": {
        "use": "Used for pain relief, inflammation, and fever.",
        "dosage": "200–400mg every 6–8 hours.",
        "warning": "Avoid if you have stomach ulcers or kidney issues."
    },
    "amoxicillin": {
        "use": "Antibiotic used to treat bacterial infections.",
        "dosage": "Prescribed by doctor (varies by condition).",
        "warning": "Complete full course; do not stop early."
    }
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

@tool
def medication_tool(query: str) -> str:
    """
    Use this tool to get basic information about medications,
    including usage, dosage, and warnings.
    """

    query = query.lower()

    for med in MEDICATION_DB:
        if med in query:
            info = MEDICATION_DB[med]
            return (
                f"{med.capitalize()}:\n"
                f"- Use: {info['use']}\n"
                f"- Dosage: {info['dosage']}\n"
                f"- Warning: {info['warning']}"
            )

    return "Sorry, I don’t have information about that medication."

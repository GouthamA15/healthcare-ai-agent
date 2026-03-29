from langchain.tools import tool


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
from tools.medication_tool import medication_tool


def main():
    query = "What is amoxicillin used for?"

    result = medication_tool.invoke(query)

    print("\nQuery:", query)
    print("\nResult:\n", result)


if __name__ == "__main__":
    main()
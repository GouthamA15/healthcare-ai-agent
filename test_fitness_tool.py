from tools.fitness_tool import fitness_tool


def main():
    query = "My weight is 54kg and height is 170cm"

    result = fitness_tool.invoke(query)

    print("\nQuery:", query)
    print("\nResult:", result)


if __name__ == "__main__":
    main()
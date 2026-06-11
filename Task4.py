def validate_brackets(code: str) -> bool:
    stack = []

    opening = "([{"
    closing = ")]}"

    for char in code:
        if char in opening:
            stack.append(char)
        elif char in closing:
            if len(stack) == 0:
                return False
            top = stack.pop()
            if opening.index(top) != closing.index(char):
                return False

    return len(stack) == 0


def main():
    print("Enter the code to validate.")
    code = input()

    if validate_brackets(code):
        print("Brackets are valid.")
    else:
        print("Brackets are invalid, the empire isn't happy.") # 😈


main()
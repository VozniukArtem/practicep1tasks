def search_dictionary(dictionary: list, word: str) -> str:
    Left = 0
    Right = len(dictionary) - 1

    while Left <= Right:
        middle = (Left + Right) // 2
        middle_value = dictionary[middle][0]

        if str.lower(middle_value) == str.lower(word):
            return dictionary[middle][1]
        elif str.lower(middle_value) < str.lower(word):
            Left = middle + 1
        else:
            Right = middle - 1

    return "Word not found."


def main():
    dictionary = [
        ("five",  "five^2"),
        ("four",  "four^2"),
        ("one",   "one^2"),
        ("six",   "six^2"),
        ("three", "three^2"),
        ("two",   "two^2"),
    ]

    print("Dictionary:")
    for word, definition in dictionary:
        print(f"{word}: {definition}")

    print("Enter the word you want to search for.")
    word = input()

    while len(word) == 0:
        print("Please enter a valid word.")
        word = input()

    result = search_dictionary(dictionary, word)
    print(result)


main()
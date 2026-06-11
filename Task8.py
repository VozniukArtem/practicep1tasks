class Deque:
    def __init__(self):
        self.items = []

    def add_front(self, item):
        self.items.insert(0, item)

    def add_rear(self, item):
        self.items.append(item)

    def remove_front(self):
        return self.items.pop(0)

    def remove_rear(self):
        return self.items.pop()

    def is_empty(self) -> bool:
        return len(self.items) == 0


def is_palindrome(phrase: str) -> bool:
    deque = Deque()

    for char in phrase:
        if char.isalpha() or char.isdigit():
            deque.add_rear(char.lower())

    while not deque.is_empty():
        if len(deque.items) == 1:
            break
        if deque.remove_front() != deque.remove_rear():
            return False

    return True


def main():
    print("Enter a phrase to check if it's a palindrome.")
    phrase = input()

    if is_palindrome(phrase):
        print(f"'{phrase}' is a palindrome.")
    else:
        print(f"'{phrase}' is not a palindrome.")


main()
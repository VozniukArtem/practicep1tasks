class PhoneBook:
    def __init__(self, capacity: int = 8):
        self.capacity = capacity
        self.size = 0
        self.table = [[] for _ in range(self.capacity)]

    def _hash(self, key: str) -> int:
        hash_value = 0
        for i in range(len(key)):
            hash_value = hash_value * 31 + ord(key[i])
        return hash_value % self.capacity

    def _resize(self):
        old_table = self.table
        self.capacity = self.capacity * 2
        self.table = [[] for _ in range(self.capacity)]
        self.size = 0

        for bucket in old_table:
            for name, phone in bucket:
                self.add(name, phone)

    def add(self, name: str, phone: str):
        if self.size / self.capacity > 0.75:
            self._resize()

        index = self._hash(name)
        bucket = self.table[index]

        for i in range(len(bucket)):
            if bucket[i][0] == name:
                bucket[i] = (name, phone)
                return

        bucket.append((name, phone))
        self.size += 1

    def get(self, name: str) -> str:
        index = self._hash(name)
        bucket = self.table[index]

        for i in range(len(bucket)):
            if bucket[i][0] == name:
                return bucket[i][1]

        return "Contact not found."

    def remove(self, name: str):
        index = self._hash(name)
        bucket = self.table[index]

        for i in range(len(bucket)):
            if bucket[i][0] == name:
                bucket.pop(i)
                self.size -= 1
                return

        print("Contact not found.")

    def contains(self, name: str) -> bool:
        index = self._hash(name)
        bucket = self.table[index]

        for i in range(len(bucket)):
            if bucket[i][0] == name:
                return True

        return False

    def count(self) -> int:
        return self.size


def main():
    pb = PhoneBook()

    pb.add("User1",   "+380-93-145-2106")
    pb.add("User2",   "+380-93-145-2107")
    pb.add("User3",   "+380-93-145-2108")
    pb.add("User4",   "+380-93-145-2109")
    pb.add("User5",   "+380-93-145-2110")
    pb.add("User6",   "+380-93-145-2111")
    pb.add("User7",   "+380-93-145-2112")

    print(f"\nTotal contacts: {pb.count()}")
    print(f"\nUser1's number: {pb.get('User1')}")

    print(f"\nContains User2: {pb.contains('User2')}")
    print("Updating User2's number.")
    pb.add("User2", "+380-93-145-2113")
    print(f"User2's new number: {pb.get('User2')}")

    print("\nRemoving User7.")
    pb.remove("User7")
    print(f"Contains User7: {pb.contains('User7')}")
    print(f"\nTotal contacts: {pb.count()}")

    print(f"\nUnknown contact: {pb.get('Unknown')}")


main()

def list_find(itemslist: list, target: str) -> list:
    Items = []

    for i in range(len(itemslist)):
        if str.lower(itemslist[i]) == str.lower(target):
            Items.append(i + 1)

    return Items

def main():
    print("Enter the list of products(SEPARATED BY SPACES) :")
    table = input().split(" ")

    print("Enter the product you want to find.")
    target = input()

    while (len(target) == 0):
        print("Please enter a valid product name.")
        target = input()

    result = list_find(table, target)

    if (len(result) > 0):
        print(f"The product was found at position(s): {result}")
    else:
        print(f"{target} is not found in the list.")

main()
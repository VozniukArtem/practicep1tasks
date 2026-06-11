def rate_students(studentslist: list, reverse: bool = False) -> list:
    result = list(studentslist)

    for i in range(len(result)):
        max_index = i
        for j in range(i + 1, len(result)):
            if reverse:
                if result[j][1] < result[max_index][1]:
                    max_index = j
            else:
                if result[j][1] > result[max_index][1]:
                    max_index = j

        result[i], result[max_index] = result[max_index], result[i]

    return result


def main():
    studentslist = [
        ("Student1", 70),
        ("Student2", 80),
        ("Student3", 90),
        ("Student4", 40),
        ("Student5", 50),
        ("Student6", 60),
        ("Student7", 20),
    ]

    print("1 for from highest to lowest")
    print("2 for from lowest to highest")

    print("\n")

    choice = input()

    while choice not in ["1", "2"]:
        print("\nInvalid input, it's not that hard to type 1 or 2 I swear😭")
        choice = input()

    if choice == "1":
        print("Student rating sorted from highest to lowest:")
    elif choice == "2":
        print("Student rating sorted from lowest to highest:")
    else:
        print("\n ????? howd this even happen")
        return




    rating = rate_students(studentslist, choice == "2")

    for i in range(len(rating)):
        print(f"{i + 1}. {rating[i][0]} — {rating[i][1]}")


main()
def merge_orders(web_orders: list, app_orders: list) -> list:
    result = []
    i = 0
    j = 0

    while i < len(web_orders) and j < len(app_orders):
        if web_orders[i][1] <= app_orders[j][1]:
            result.append(web_orders[i])
            i += 1
        else:
            result.append(app_orders[j])
            j += 1

    while i < len(web_orders):
        result.append(web_orders[i])
        i += 1

    while j < len(app_orders):
        result.append(app_orders[j])
        j += 1

    return result


def main():
    web_orders = [
        ("WEB-001", "2026-06-10 23:09"),
        ("WEB-002", "2026-06-10 23:10"),
        ("WEB-003", "2026-06-10 23:17"),
        ("WEB-004", "2026-06-10 23:18"),
    ]

    app_orders = [
        ("APP-001", "2026-06-10 23:06"),
        ("APP-002", "2026-06-10 23:11"),
        ("APP-003", "2026-06-10 23:12"),
        ("APP-004", "2026-06-10 23:16"),
    ]

    merged = merge_orders(web_orders, app_orders)

    print("Merged orders:")
    for order in merged:
        print(f"  {order[1]}  {order[0]}")


main()
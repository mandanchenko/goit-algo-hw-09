import random
import timeit

coins = [50, 25, 10, 5, 2, 1]


def find_coins_greedy(sum_: int):
    sorted_coins = sorted(coins, reverse=True)
    count_coins = {}
    for coin in sorted_coins:
        count = sum_ // coin
        if count > 0:
            count_coins[coin] = count
        sum_ = sum_ - coin * count
    return count_coins


def find_min_coins(sum_):
    # Тут індекс це сума
    min_coins_required = [0] + [float("inf")] * sum_  # мінімальна кілкість монет
    last_coin_used = [0] * (sum_ + 1)  # остання монета для цієї суми

    for s in range(1, sum_ + 1):
        for coin in coins:
            if s >= coin and min_coins_required[s - coin] + 1 < min_coins_required[s]:
                min_coins_required[s] = min_coins_required[s - coin] + 1
                last_coin_used[s] = coin

    count_coins = {}
    current_sum = sum_
    while current_sum > 0:
        coin = last_coin_used[current_sum]
        count_coins[coin] = count_coins.get(coin, 0) + 1
        current_sum = current_sum - coin

    return count_coins


if __name__ == "__main__":
    # Число менше за принаймні одну монету - від 1 до 49
    random_number_1_to_49 = random.randint(1, 49)
    # Число більше за всі монети - від 51 до 99
    random_number_51_to_99 = random.randint(51, 99)
    # Велике число - від 100 до 1000
    random_number_100_to_1000 = random.randint(100, 1000)

    # Визначаємо час роботи та результати жадібного алгоритму:
    time_small_greedy = timeit.timeit(lambda: find_coins_greedy(random_number_1_to_49), number=5)
    time_medium_greedy = timeit.timeit(lambda: find_coins_greedy(random_number_51_to_99), number=5)
    time_large_greedy = timeit.timeit(lambda: find_coins_greedy(random_number_100_to_1000), number=5)

    # Визначаємо час роботи та результати динамічного програмування:
    time_small_min = timeit.timeit(lambda: find_min_coins(random_number_1_to_49), number=5)
    time_medium_min = timeit.timeit(lambda: find_min_coins(random_number_51_to_99), number=5)
    time_large_min = timeit.timeit(lambda: find_min_coins(random_number_100_to_1000), number=5)

    print("Данні по часу алгоритмів:")
    print(
        f"{'Назва алгоритму': <23} | {'Число': <20} | {'Час алгоритму': <20}"
    )
    print(f":{'-'*22} | :{'-'*19} | :{'-'*19}")
    print(
        f"{'Жадібний алгоритм': <23} | {random_number_1_to_49: <20} | {time_small_greedy:<20} | "
    )
    print(
        f"{'Динамічне програмування': <23} | {random_number_1_to_49: <20} | {time_small_min:<20} | "
    )
    print(
        f"{'Жадібний алгоритм': <23} | {random_number_51_to_99: <20} | {time_medium_greedy:<20} | "
    )
    print(
        f"{'Динамічне програмування': <23} | {random_number_51_to_99: <20} | {time_medium_min:<20} | "
    )
    print(
        f"{'Жадібний алгоритм': <23} | {random_number_100_to_1000: <20} | {time_large_greedy:<20} | "
    )
    print(
        f"{'Динамічне програмування': <23} | {random_number_100_to_1000: <20} | {time_large_min:<20} | "
    )

    print("Результати алгоритмів: ")
    print("Жадібний алгоритм: ")
    print(random_number_1_to_49, find_coins_greedy(random_number_1_to_49))
    print(random_number_51_to_99, find_coins_greedy(random_number_51_to_99))
    print(random_number_100_to_1000, find_coins_greedy(random_number_100_to_1000))
    print("Динамічне програмування: ")
    print(random_number_1_to_49, find_min_coins(random_number_1_to_49))
    print(random_number_51_to_99, find_min_coins(random_number_51_to_99))
    print(random_number_100_to_1000, find_min_coins(random_number_100_to_1000))
    
def find_coins_greedy(amount, coins=[50, 25, 10, 5, 2, 1]):
    """
    Видає решту за допомогою жадібного алгоритму.
    
    Аргументи:
        amount (int): Сума, яку потрібно видати.
        coins (list): Список номіналів монет, відсортований у порядку спадання.
    
    Повертає:
        dict: Словник з кількістю монет кожного номіналу.
    """
    result = {}
    for coin in coins:
        if amount == 0:
            break
        if amount >= coin:
            count = amount // coin
            result[coin] = count
            amount %= coin
    return result

# Приклад використання
print("--- Жадібний алгоритм ---")
amount_greedy = 113
change_greedy = find_coins_greedy(amount_greedy)
print(f"Сума: {amount_greedy}")
print(f"Видача: {change_greedy}")
print(f"Загальна кількість монет: {sum(change_greedy.values())}")

def find_min_coins(amount, coins=[1, 2, 5, 10, 25, 50]):
    """
    Знаходить мінімальну кількість монет для видачі суми
    за допомогою динамічного програмування.
    
    Аргументи:
        amount (int): Сума, яку потрібно видати.
        coins (list): Список номіналів монет.
    
    Повертає:
        dict: Словник з кількістю монет кожного номіналу.
    """
    # Ініціалізуємо масиви для зберігання мінімальної кількості монет
    # та останньої використаної монети для кожної суми
    min_coins = [0] + [float('inf')] * amount
    last_coin = [0] * (amount + 1)
    
    for i in range(1, amount + 1):
        for coin in coins:
            if coin <= i and min_coins[i - coin] + 1 < min_coins[i]:
                min_coins[i] = min_coins[i - coin] + 1
                last_coin[i] = coin
    
    # Реконструюємо рішення
    result = {}
    current_amount = amount
    while current_amount > 0:
        coin = last_coin[current_amount]
        result[coin] = result.get(coin, 0) + 1
        current_amount -= coin
    
    return result

# Приклад використання
print("\n--- Алгоритм динамічного програмування ---")
amount_dp = 113
change_dp = find_min_coins(amount_dp)
print(f"Сума: {amount_dp}")
print(f"Видача: {change_dp}")
print(f"Загальна кількість монет: {sum(change_dp.values())}")
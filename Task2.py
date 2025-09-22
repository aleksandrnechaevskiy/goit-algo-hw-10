import numpy as np

# Визначення функції та меж інтегрування
def f(x):
    return x ** 2

a = 0  # Нижня межа
b = 2  # Верхня межа

# Кількість випадкових точок
num_points = 1_000_000

# Визначення площі прямокутника, в якому будуть генеруватися точки
# Висота прямокутника - це максимальне значення функції на інтервалі [0, 2]
max_y = f(b) 
area_of_box = (b - a) * max_y

# Генеруємо випадкові координати x та y
x_rand = np.random.uniform(a, b, num_points)
y_rand = np.random.uniform(0, max_y, num_points)

# Підраховуємо кількість точок, що потрапили під криву
points_under_curve = np.sum(y_rand <= f(x_rand))

# Обчислюємо значення інтеграла
integral_monte_carlo = (points_under_curve / num_points) * area_of_box

print(f"Інтеграл методом Монте-Карло: {integral_monte_carlo}")
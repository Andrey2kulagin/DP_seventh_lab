import math
import statistics
import numpy as np
import matplotlib.pyplot as plt


def graph_with_trend(input_x, input_y, lbl, trend_y, formula):  # Функция построения графика с линией тренда
    plt.scatter(input_x, input_y)  # Задание точечной диаграммы
    plt.text(900, 7.7, formula)
    plt.plot(range(max(input_x)+1), trend_y)
    plt.ylabel('y')  # Название оси y
    plt.xlabel('x')  # Название оси x
    plt.title(lbl)  # Название графика
    plt.show()  # Вывод графика


def func_obr_xt_x(xt_matrix):
    x_matrix = xt_matrix.transpose().copy()
    xt_x = xt_matrix.dot(x_matrix)
    obr_xt_x = np.linalg.inv(xt_x)
    return obr_xt_x


def signs(fit, sign):
    for j in range(len(sign)):
        if fit[j] < 0:
            sign[j] = '-'
            fit[j] = fit[j] * (-1)
    return sign


# 1. Стадия выбора
choice = input("Для работы с конкретными данными введите 1. В ином случае будет работа со случайными данными...\n")
if choice == '1':
    yT_column = np.fromfile('7_y_data.txt', float, sep=" ")  # Создание строки yT из файла
    yT_graph_column = np.copy(yT_column)
    xT_column = np.fromfile('7_x_data.txt', int, sep=" ")  # Создание строки xT из файла
else:
    length = 70
    xT_column = np.random.randint(2, 2200, length)
    xT_column = np.sort(xT_column)
    yT_column = np.random.random(length)
    for i in range(length):
        yT_column[i] += 5 * math.sin(xT_column[i] / 250)

length = len(xT_column)
XT_matrix_4 = np.ones((5, length))

# 1. Полином 4-го порядка
for i in range(length):
    XT_matrix_4[1][i] = xT_column[i]
    XT_matrix_4[2][i] = xT_column[i]**2
    XT_matrix_4[3][i] = xT_column[i]**3
    XT_matrix_4[4][i] = xT_column[i]**4
obr_XT_X_4 = func_obr_xt_x(XT_matrix_4)
fit_4 = np.polynomial.polynomial.polyfit(xT_column, yT_column, 4)
trend_y_4 = []
i = 0
while i <= max(xT_column):
    trend_y_4.append(fit_4[0] + fit_4[1]*i + fit_4[2]*(i**2) + fit_4[3]*(i**3) + fit_4[4]*(i**4))
    i += 1
signs_4 = ['+', '+', '+', '+']
signs_4 = signs(fit_4, signs_4)
formula_4 = f"y = {round(fit_4[4],3)}x^4 {signs_4[3]}{round(fit_4[3],3)}x^3 {signs_4[2]}{round(fit_4[2],3)}x^2 " \
            f"{signs_4[1]}{round(fit_4[1],3)}x {signs_4[0]}{round(fit_4[0],3)}"

# 2. Полином 3-го порядка
XT_matrix_3 = np.copy(XT_matrix_4[0:4])
obr_XT_X_3 = func_obr_xt_x(XT_matrix_3)
fit_3 = np.polynomial.polynomial.polyfit(xT_column, yT_column, 3)
trend_y_3 = []
for i in range(max(xT_column)+1):
    trend_y_3.append(fit_3[0] + fit_3[1]*i + fit_3[2]*(i**2) + fit_3[3]*(i**3))
pluses = ['+', '+', '+']
signs_3 = signs(fit_3, pluses)
formula_3 = f"y = {round(fit_3[3],3)}x^3 {signs_3[2]}{round(fit_3[2],3)}x^2 {signs_3[1]}{round(fit_3[1],3)}x " \
            f"{signs_3[0]}{round(fit_3[0],3)}"

# 3. Полином 2-го порядка
XT_matrix_2 = np.copy(XT_matrix_4[0:3])
obr_XT_X_2 = func_obr_xt_x(XT_matrix_2)
fit_2 = np.polynomial.polynomial.polyfit(xT_column, yT_column, 2)
trend_y_2 = []
for i in range(max(xT_column)+1):
    trend_y_2.append(fit_2[0] + fit_2[1]*i + fit_2[2]*(i**2))
pluses = ['+', '+']
signs_2 = signs(fit_2, pluses)
formula_2 = f"y = {round(fit_2[2], 3)}x^2 {signs_2[1]}{round(fit_2[1], 3)}x {signs_2[0]}{round(fit_2[0], 3)}"

# 4. Вывод графиков
graph_with_trend(xT_column, yT_column, "Полином 4-го порядка", trend_y_4, formula_4)
graph_with_trend(xT_column, yT_column, "Полином 3-го порядка", trend_y_3, formula_3)
graph_with_trend(xT_column, yT_column, "Полином 2-го порядка", trend_y_2, formula_2)

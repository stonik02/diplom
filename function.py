from utils import *

t = 4e-7  # Один отрезок времени Время все сильно меняет 0.002-0.005
c = 1500  # Скорость звука
# f = 600  # Гц(частота             Частота все сильно меняет 200-300
H_Start = 100  # Глубина начальная сильно все меняет 20-...
isto4nik = [0, 5000]
l_moda = 2  # Номер моды
pi = 3.14
# x = []
# y = []

num_rays = 50  # Число лучей
steps = 5000  # Число шагов в цикле

# Wk = 2 * pi * f
#
# ql0 = ql(Wk, c, pi, H_Start, l_moda)

# priemnik = [2121, 7788]
result_lych_x = []
result_lych_y = []
result_alfa = 0
min_dist = float('inf')


def main_function(priemnik, f):
    Wk = 2 * pi * f
    ql0 = ql(Wk, c, pi, H_Start, l_moda)

    distance_min = float('inf')
    lines_x = []
    lines_y = []
    flag = False
    for i in range(num_rays):
        alfa = i * pi / num_rays
        k = [ql0 * math.cos(alfa), ql0 * math.sin(alfa)]
        r = isto4nik
        x_arr = []  # Список для координат x текущей линии
        y_arr = []  # Список для координат y текущей линии
        for j in range(steps):
            n = refractive_index_v2(r[1], Wk, c, l_moda, ql0, pi)
            # gradient_n = gradient(r)
            gradient_n = gradient_v2(r, ql0, Wk, c, l_moda, pi)
            # print("gradient_n = ", gradient_n)
            k = dk(Wk, n, gradient_n, t, k)
            # print("k = ", k)
            r = dr(c, Wk, k, t, r)
            # print("r = ", r)

            # A[i] = r
            x_point = r[0] * 1000
            # x_point = r[0]
            y_point = r[1]
            x_arr.append(x_point)
            y_arr.append(y_point)
            distance_points = distance_between_points(x_point, y_point, priemnik[0], priemnik[1])
            if distance_points < distance_min:
                global min_dist
                min_dist = distance_points
                distance_min = distance_points
                flag = True

        if flag:
            flag = False
            global result_alfa
            result_alfa = alfa
            result_lych_x.clear()
            result_lych_y.clear()
            result_lych_x.append(x_arr)
            result_lych_y.append(y_arr)
        lines_x.append(x_arr)
        lines_y.append(y_arr)

    return [lines_x, lines_y], [result_lych_x, result_lych_y, result_alfa]
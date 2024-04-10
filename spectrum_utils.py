import numpy as np

from utils import *


def f_k(steps, t):
    fd = 1/t
    delfa_f = fd/steps
    fk = []  # Объявляем массив fk и потом заполняем fk = i * delfa_f

    for i in range(steps):
        fk.append(i * delfa_f)
    return fk


def w_k(steps, pi, fk):
    wk_result = []  # Объявляем массив фазовых набегов и заполняем его

    for i in range(steps):
        wk_result.append(2 * pi * fk[i])
    return wk_result


def ray_path_calculation_v2(h_k, l_moda, receiver, w, inception, c, pi, v_dna, t):

    result_ray_x = []
    result_ray_y = []
    result_alfa = 0

    y_min = float('inf')

    h_start = depth(inception[1], h_k)
    try:
        ql0 = ql(w, c, pi, h_start, l_moda)
    except:
        return [0,0], 0

    distance_min = float('inf')

    flag = False
    i = 0
    alfa_grad = 0


    while True:
        zna4enie_y_v_to4ke_x_priemnika = 0
        i+=1
        alfa = alfa_grad * pi / 180
        # print("угол = {}".format(alfa))
        k = [ql0 * math.cos(alfa), ql0 * math.sin(alfa)]
        r = inception
        x_arr = []
        y_arr = []


        while True:
            h_point = depth(r[1], h_k)
            try:
                ql_point = ql(w, c, pi, h_point, l_moda)
            except:
                break
            if ql_point == 0:
                break
            c_point = w / ql_point
            # Проверяем, если звук уходит в дно, то заканчиваем его рассчет
            if c_point > v_dna:
                break
            n = refractive_index_v2(r[1], w, c, l_moda, ql0, pi, h_k)
            try:
                gradient_n = gradient_v2(r, ql0, w, c, l_moda, pi, h_k)
            except:
                break
            k = dk(w, n, gradient_n, t, k)
            r = dr(c, w, k, t, r)

            x_point = r[0]
            y_point = r[1]

            if x_point < 0:
                break

            x_arr.append(x_point)
            y_arr.append(y_point)

            if x_point - receiver[0] > 0:
                # print(x_arr)
                # print(y_arr)
                break
            # if y_point - receiver[0] > 0:
            #     # print(x_point)
            #     # print(y_point)
            #     break
        if i > 50:
            print("Невозможно подойти к приемнику ближе, чем на {} метров".format(np.abs(int(zna4enie_y_v_to4ke_x_priemnika - receiver[1]))))

            break
        try:
            zna4enie_x_v_to4ke_x_priemnika = min(x_arr, key=lambda x: abs(x - receiver[0]))
            index_x_v_to4ke_x_priemnika = x_arr.index(zna4enie_x_v_to4ke_x_priemnika)
            zna4enie_y_v_to4ke_x_priemnika = y_arr[index_x_v_to4ke_x_priemnika]
            # print("alfa_grad = {} y = {}".format(alfa_grad, zna4enie_y_v_to4ke_x_priemnika))
            # print("zna4enie_y_v_to4ke_x_priemnika - receiver[1] = {}".format(zna4enie_y_v_to4ke_x_priemnika - receiver[1]))
            if zna4enie_y_v_to4ke_x_priemnika - receiver[1] > 100:
                if zna4enie_y_v_to4ke_x_priemnika - receiver[1] > 1000:
                    alfa_grad -= 5
                    continue
                # print(">")
                # print(zna4enie_y_v_to4ke_x_priemnika - receiver[1])
                alfa_grad -= 1
                continue
            if zna4enie_y_v_to4ke_x_priemnika - receiver[1] < -100:
                if zna4enie_y_v_to4ke_x_priemnika - receiver[1] < 1000:
                    alfa_grad += 5
                    continue
                # print("-")
                # print(zna4enie_y_v_to4ke_x_priemnika - receiver[1])
                alfa_grad += 1
                continue
            else:
                print("Попыток было затрачено {}".format(i))
                break
        except ValueError:
            alfa_grad += 1
            continue



    return [x_arr, y_arr], alfa_grad * pi / 180


def ray_path_calculation_v1(h_k, l_moda, receiver, w, inception, c, pi, v_dna, t):

    x_lines = []
    y_lines = []
    result_alfa = 0

    y_min = float('inf')

    h_start = depth(inception[1], h_k)
    try:
        ql0 = ql(w, c, pi, h_start, l_moda)
    except:
        return [0,0], 0

    distance_min = float('inf')

    flag = False
    i = 0
    alfa_grad = 0


    while True:
        zna4enie_y_v_to4ke_x_priemnika = 0
        i+=1
        alfa = alfa_grad * pi / 180
        # print("угол = {}".format(alfa))
        k = [ql0 * math.cos(alfa), ql0 * math.sin(alfa)]
        r = inception
        x_arr = []
        y_arr = []


        while True:
            h_point = depth(r[1], h_k)
            try:
                ql_point = ql(w, c, pi, h_point, l_moda)
            except:
                break
            if ql_point == 0:
                break
            c_point = w / ql_point
            # Проверяем, если звук уходит в дно, то заканчиваем его рассчет
            if c_point > v_dna:
                break
            n = refractive_index_v2(r[1], w, c, l_moda, ql0, pi, h_k)
            try:
                gradient_n = gradient_v2(r, ql0, w, c, l_moda, pi, h_k)
            except:
                break
            k = dk(w, n, gradient_n, t, k)
            r = dr(c, w, k, t, r)

            x_point = r[0]
            y_point = r[1]

            if x_point < 0:
                break

            x_arr.append(x_point)
            y_arr.append(y_point)

            if x_point - receiver[0] > 0:
                # print(x_arr)
                # print(y_arr)
                y_lines.append(y_arr)
                x_lines.append(x_arr)
                break
            # if y_point - receiver[0] > 0:
            #     # print(x_point)
            #     # print(y_point)
            #     break
        if i > 50:

            print("Невозможно подойти к приемнику ближе, чем на {} метров. Wk = {}".format(np.abs(int(zna4enie_y_v_to4ke_x_priemnika - receiver[1])), w))
            if zna4enie_y_v_to4ke_x_priemnika == 0:
                return [0, 0], 0

        try:
            zna4enie_x_v_to4ke_x_priemnika = min(x_arr, key=lambda x: abs(x - receiver[0]))
            index_x_v_to4ke_x_priemnika = x_arr.index(zna4enie_x_v_to4ke_x_priemnika)
            zna4enie_y_v_to4ke_x_priemnika = y_arr[index_x_v_to4ke_x_priemnika]
            # print("alfa_grad = {} y = {}".format(alfa_grad, zna4enie_y_v_to4ke_x_priemnika))
            # print("zna4enie_y_v_to4ke_x_priemnika - receiver[1] = {}".format(zna4enie_y_v_to4ke_x_priemnika - receiver[1]))
            if zna4enie_y_v_to4ke_x_priemnika - receiver[1] > 100:
                if zna4enie_y_v_to4ke_x_priemnika - receiver[1] > 1000:
                    alfa_grad -= 5
                    continue
                # print(">")
                # print(zna4enie_y_v_to4ke_x_priemnika - receiver[1])
                alfa_grad -= 1
                continue
            if zna4enie_y_v_to4ke_x_priemnika - receiver[1] < -100:
                if zna4enie_y_v_to4ke_x_priemnika - receiver[1] < 1000:
                    alfa_grad += 5
                    continue
                # print("-")
                # print(zna4enie_y_v_to4ke_x_priemnika - receiver[1])
                alfa_grad += 1
                continue
            else:
                print("Попыток было затрачено {}".format(i))
                break
        except ValueError:
            alfa_grad += 1
            continue



    return [x_arr, y_arr],  alfa_grad * pi / 180


def fi_wk(wk, h_k, c, pi, l_moda, receiver, inception, v_dna, t):
    fi_wk_arr = []
    print(wk)
    for i in range(int(len(wk)/2)):
        if i < 1:
            fi_wk_arr.append(0)
            continue
        wi = wk[i]
        fi_wk_res = 0
        delta_ll = []
        line, alfa = ray_path_calculation_v1(h_k, l_moda, receiver, wi, inception, c, pi, v_dna, t)
        # print(line)
        x_arr = line[0]
        y_arr = line[1]
        if x_arr == 0:
            fi_wk_arr.append(0)
            continue
        for point in range(len(x_arr)):  # По кол-ву точек
            x_point = x_arr[point]
            y_point = y_arr[point]
            delta_l = 0
            if point != 0:
                # Расстояние между нашей точкой и предыдущей
                delta_l = distance_between_points(x_point, y_point, x_arr[point - 1],
                                                  y_arr[point - 1], )
            h_point = depth(y_point, h_k)
            try:
                ql_point = ql(wi, c, pi, h_point, l_moda)
            except:
                ql_point = 0
            fi_wk = ql_point * delta_l
            fi_wk_res += fi_wk
            delta_ll.append(delta_l)
        fi_wk_arr.append(fi_wk_res)
        print("Луч номер {} fi_wk_arr = {} угол = {}".format(i, fi_wk_res, alfa))
        # print(delta_ll)
    return fi_wk_arr

# def obrezaem_ly4(ray, receiver):
#     result_ray_x = []
#     result_ray_y = []
#
#     dist_min = float('inf')
#     for i in range(len(ray[0])):
#         dist = distance_between_points(ray[0][i], ray[1][i], receiver[0], receiver[1])
#         if dist < dist_min:
#             dist_min = dist
#             result_ray_x.append(ray[0][i])
#             result_ray_y.append(ray[1][i])
#     return [result_ray_x, result_ray_y]
#
# def take_points_result_ray(alfa, h_k, f, l_moda, steps):
#     h_start = depth(inception[1], h_k)
#     w = 2 * pi * f
#     ql0 = ql(w, c, pi, h_start, l_moda)
#     k = [ql0 * math.cos(alfa), ql0 * math.sin(alfa)]
#     r = inception
#     x_arr = []  # Список для координат x текущей линии
#     y_arr = []  # Список для координат y текущей линии
#     for j in range(steps):
#         h_point = depth(r[1], h_k)
#         try:
#             ql_point = ql(w, c, pi, h_point, l_moda)
#         except:
#             break
#
#         c_point = w / ql_point
#         # Проверяем, если звук уходит в дно, то заканчиваем его рассчет
#         if c_point > v_dna:
#             break
#         n = refractive_index_v2(r[1], w, c, l_moda, ql0, pi, h_k)
#         try:
#             gradient_n = gradient_v2(r, ql0, w, c, l_moda, pi, h_k)
#         except:
#             break
#         k = dk(w, n, gradient_n, t_signal, k)
#         r = dr(c, w, k, t_signal, r)
#
#         x_point = r[0]
#         y_point = r[1]
#
#
#         x_arr.append(x_point)
#         y_arr.append(y_point)
#
#     return [x_arr, y_arr]

# def t_full():
#     t_full = []
#     time = 0
#     for i in range(steps):
#         time += t
#         t_full.append(time)
#     return t_full
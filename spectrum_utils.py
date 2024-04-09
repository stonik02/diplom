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


def fi_wk(wk, result_ray, h_k, c, pi, l_moda):
    fi_wk_arr = []

    for i in range(int(len(wk)/2)):
        wi = wk[i]
        fi_wk_res = 0
        delta_ll = []
        for point in range(len(result_ray[0][0])):  # По кол-ву точек
            x_point = result_ray[0][0][point]
            y_point = result_ray[1][0][point]
            delta_l = 0
            if point != 0:
                # Расстояние между нашей точкой и предыдущей
                delta_l = distance_between_points(x_point, y_point, result_ray[0][0][point - 1],
                                                  result_ray[1][0][point - 1], )
            h_point = depth(y_point, h_k)
            try:
                ql_point = ql(wi, c, pi, h_point, l_moda)
            except:
                ql_point = 0
            fi_wk = ql_point * delta_l
            fi_wk_res += fi_wk
            delta_ll.append(delta_l)
        fi_wk_arr.append(fi_wk_res)
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
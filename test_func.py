import numpy as np

from signal import signal
from utils import *
from spectrum_utils import *
from scipy.fft import fft, ifft
import cmath

# t = 1e-3  # Один отрезок времени
t = 1e-3  # Один отрезок времени
steps = 6000  # Число шагов в цикле
t_signal = 8e-4  # Один отрезок времени
steps_signal = 1000  # Число шагов в цикле
c = 1500  # Скорость звука
inception = [0, 3000]   # Источник
pi = 3.14
v_dna = 1800   # Скорость звука в дне


def ray_path_calculation(h_k, l_moda, f, receiver, num_rays):
    result_ray_x = []
    result_ray_y = []
    result_alfa = 0

    y_min = float('inf')

    h_start = depth(inception[1], h_k)
    w = 2 * pi * f
    ql0 = ql(w, c, pi, h_start, l_moda)

    distance_min = float('inf')
    lines_x = []
    lines_y = []
    flag = False
    i = 0
    for i in range(num_rays):
        i += 1
        alfa = i * pi / (num_rays / 2)
        k = [ql0 * math.cos(alfa), ql0 * math.sin(alfa)]
        r = inception
        x_arr = []  # Список для координат x текущей линии
        y_arr = []  # Список для координат y текущей линии
        for j in range(steps):
            h_point = depth(r[1], h_k)
            try:
                ql_point = ql(w, c, pi, h_point, l_moda)
            except:
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

            if y_point < y_min:
                y_min = y_point

            # Берем только правую половину графика
            # if x_point < 0 or x_point > receiver[0]:

            if x_point < 0:
                break
            x_arr.append(x_point)
            y_arr.append(y_point)

            distance_points = distance_between_points(x_point, y_point, receiver[0], receiver[1])
            if distance_points < distance_min and distance_points < 200:
                distance_min = distance_points
                result_alfa = alfa
                result_ray_x.clear()
                result_ray_y.clear()
                result_ray_x.append(x_arr)
                result_ray_y.append(y_arr)
                if distance_points < 70:
                    break

        lines_x.append(x_arr)
        lines_y.append(y_arr)
    steps_res = len(result_ray_y[0])
    return [lines_x, lines_y], [result_ray_x, result_ray_y, result_alfa], y_min, distance_min, steps_res


def main_func(h_k, l_moda, f, receiver, num_rays):
    lines, result_ray, y_min, distance_min, steps_res = ray_path_calculation(h_k, l_moda, f, receiver, num_rays)

    signal_arr, t_arr = signal(f, t_signal, steps_res)
    signal_fft = fft(signal_arr)  # Фурье сигнала

    fk_arr = f_k(steps_res, t)
    wk_arr = w_k(steps_res, pi, fk_arr)   # Объявляем массив фазовых набегов и заполняем его
    fi_wk_res = fi_wk(wk_arr, result_ray, h_k, c, pi, l_moda)   # Считаем fi_wk = ql(wk) * delta_l

    # Считаем пришедший на приемник ряд фурье
    signal_fft_receiver1 = []
    for i in range(int(len(signal_fft)/2)):
        c_res = signal_fft[i] * cmath.exp((0+1j) * fi_wk_res[i])
        signal_fft_receiver1.append(c_res)
    signal_fft_receiver2 = []
    for i in reversed(signal_fft_receiver1):
        signal_fft_receiver2.append(i.conjugate())
    signal_fft_receiver_result = signal_fft_receiver1 + signal_fft_receiver2

    signal_on_receiver = ifft(signal_fft_receiver_result)   # Обратный фурье

    #
    # print("LEN: signal = {} fft = {} fk = {} wk = {} fi_wk = {} signal_fft_receiver_result = {}".
    #       format(len(signal_arr), len(signal_fft), len(fk), len(wk), len(fi_wk_res), len(signal_fft_receiver_result)))

    return signal_arr, signal_on_receiver, t_arr, lines, result_ray, y_min, distance_min







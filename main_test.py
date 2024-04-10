from matplotlib import pyplot as plt
import numpy as np

from test_func import *

h_k = 0.09
l_moda = 6
f = 800
receiver = [100, 3200]
num_rays = 400
wk = 2*pi*f

t = 4e-3  # Один отрезок времени
steps = 1000  # Число шагов в цикле
t_signal = 8e-4  # Один отрезок времени
steps_signal = 1000  # Число шагов в цикле
c = 1500  # Скорость звука
inception = [0, 3000]   # Источник
pi = 3.14
v_dna = 1800   # Скорость звука в дне
if __name__ == '__main__':

    # result_ray, lines, alfa = ray_path_calculation_v1(h_k, l_moda, receiver, wk, inception, c, pi, v_dna, t)
    #
    # if alfa != 0:
    #     plt.figure(figsize=(7, 5))
    #     # for x, y in zip(lines[0], lines[1]):
    #     #     plt.plot(x, y, color='black')
    #     # plt.title("График x y")
    #
    #     plt.grid()
    #     plt.xlabel("x")
    #     plt.ylabel("y")
    #
    #     x_coords = result_ray[0]
    #     y_coords = result_ray[1]
    #     plt.plot(x_coords, y_coords, color='red', label='')
    #     plt.scatter(receiver[0], receiver[1], color='green', label='Приемник')
    #     plt.show()









    signal_arr, signal_on_receiver, t_arr = main_func(h_k, l_moda, f, receiver)
    plt.figure(figsize=(20, 5))
    plt.plot(t_arr, np.abs(signal_arr))
    plt.title("Исходный сигнал")
    plt.xlabel("t")
    plt.ylabel("s")

    plt.figure(figsize=(20, 5))
    plt.plot(t_arr, np.abs(signal_on_receiver))
    plt.title("Принятый сигнал")
    plt.xlabel("t")
    plt.ylabel("s")

    plt.show()








    # ray = ray_path_calculation_v2(h_k, l_moda, receiver, wk, inception, c, pi, v_dna, t)
    # plt.figure(figsize=(7, 5))
    # plt.plot(ray[0], ray[1], color='black')
    # plt.scatter(receiver[0], receiver[1], color='green', label='Приемник')
    # plt.grid()
    # plt.xlabel("x")
    # plt.ylabel("y")
    # plt.show()
    # alfa_grad = 0
    # for i in range(50):
    #     print("alfa_grad * pi / 180 = {} alfa_grad = {}".format((alfa_grad * pi / 180), alfa_grad))
    #     alfa_grad +=3


#     plt.figure(figsize=(7, 5))
#     for x, y in zip(lines[0], lines[1]):
#         plt.plot(x, y, color='black')
#     plt.title("График x y")
#
#     plt.grid()
#     plt.xlabel("x")
#     plt.ylabel("y")
#     x_coords = []
#     y_coords = []
#     if len(result_ray) == 3:
#         x_coords = [coord for sublist in result_ray[0] for coord in sublist]
#         y_coords = [coord for sublist in result_ray[1] for coord in sublist]
#         print("Дистанция от луча до приемника = {}".format(distance_min))
#         plt.plot(x_coords, y_coords, color='red', label='')
#         plt.scatter(inception[0], inception[1], color='green', label='Приемник')
# #     plt.show()



    # plt.figure(figsize=(7, 5))
    # plt.plot(x_coords, y_coords, color='black')
    #
    # plt.grid()
    # plt.xlabel("x")
    # plt.ylabel("y")
    # plt.show()







    # lines, result_ray, y_min, distance_min = ray_path_calculation(h_k, l_moda, f, inception, num_rays)
    # plt.figure(figsize=(7, 5))
    # for x, y in zip(lines[0], lines[1]):
    #     plt.plot(x, y, color='black')
    # plt.title("График x y")
    #
    # plt.grid()
    # plt.xlabel("x")
    # plt.ylabel("y")
    #
    # if len(result_ray) == 3:
    #     x_coords = [coord for sublist in result_ray[0] for coord in sublist]
    #     y_coords = [coord for sublist in result_ray[1] for coord in sublist]
    #     print("Дистанция от луча до приемника = {}".format(distance_min))
    #     plt.plot(x_coords, y_coords, color='red', label='')
    #     plt.scatter(inception[0], inception[1], color='green', label='Приемник')
    # plt.show()
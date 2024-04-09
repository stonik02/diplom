from matplotlib import pyplot as plt
import numpy as np

from test_func import ray_path_calculation, main_func

h_k = 0.03
l_moda = 2
f = 300
inception = [2300, 4000]
num_rays = 100

if __name__ == '__main__':
    signal_arr, signal_on_receiver, t_arr, lines, result_ray, y_min, distance_min = main_func(h_k, l_moda, f, inception, num_rays)

    plt.figure(figsize=(7, 5))
    for x, y in zip(lines[0], lines[1]):
        plt.plot(x, y, color='black')
    plt.title("График x y")

    plt.grid()
    plt.xlabel("x")
    plt.ylabel("y")
    x_coords = []
    y_coords = []
    if len(result_ray) == 3:
        x_coords = [coord for sublist in result_ray[0] for coord in sublist]
        y_coords = [coord for sublist in result_ray[1] for coord in sublist]
        print("Дистанция от луча до приемника = {}".format(distance_min))
        plt.plot(x_coords, y_coords, color='red', label='')
        plt.scatter(inception[0], inception[1], color='green', label='Приемник')
#     plt.show()

    plt.figure(figsize=(20, 5))
    plt.plot(t_arr,  np.abs(signal_arr))
    plt.title("Исходный сигнал")
    plt.xlabel("t")
    plt.ylabel("s")

    plt.figure(figsize=(20, 5))
    plt.plot(t_arr, np.abs(signal_on_receiver))
    plt.title("Принятый сигнал")
    plt.xlabel("t")
    plt.ylabel("s")

    plt.figure(figsize=(7, 5))
    plt.plot(x_coords, y_coords, color='black')

    plt.grid()
    plt.xlabel("x")
    plt.ylabel("y")
    plt.show()







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
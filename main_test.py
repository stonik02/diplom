from matplotlib import pyplot as plt

from test_func import main_function_test

pi = 3.14
f = 300
Wk = 2 * pi * f
# ql0 = ql(Wk, 1500, pi, 5000*0.02, 2)
# print(ql0)

if __name__ == '__main__':
    n_arr, r_arr, gradient_arr, dk_arr, dr_arr, lines, h_arr = main_function_test([5000, 5000], 300)

    # y_array = list(range(200, 10000, 100))
    # n_test_array = []
    # for y in y_array:
    #     n = refractive_index_v2(y, Wk, 1500, 2, ql0, pi)
    #     n_test_array.append(n)

    plt.figure(figsize=(7, 5))
    for x, y in zip(lines[0], lines[1]):
        plt.plot(x, y)
    plt.title("График x y")

    plt.grid()
    plt.xlabel("x")
    plt.ylabel("y")

    plt.show()


    # plt.figure(figsize=(7, 5))
    # plt.plot(r_arr, h_arr, color='black')
    # plt.title("Зависимость h от y")
    #
    # plt.xlabel("y")
    # plt.ylabel("H")

    # plt.figure(figsize=(12, 10))
    # plt.subplot(2, 2, 1)
    # plt.plot(r_arr, n_arr, color='black')
    # plt.title("Зависимость n от y")
    #
    # plt.xlabel("y")
    # plt.ylabel("n")
    #
    # plt.subplot(2, 2, 3)
    # plt.plot( r_arr, gradient_arr, color='black')
    # plt.title("Зависимость градиента от y")
    #
    # plt.xlabel("y")
    # plt.ylabel("gradient")
    #
    # plt.subplot(2, 2, 2)
    # plt.plot(r_arr, dr_arr, color='black')
    # plt.title("Зависимость dr от y")
    #
    # plt.xlabel("y")
    # plt.ylabel("dr")
    #
    # plt.subplot(2, 2, 4)
    # plt.plot(r_arr, dk_arr, color='black')
    # plt.title("Зависимость dk от y")
    #
    # plt.xlabel("y")
    # plt.ylabel("dk")
    #
    #
    # plt.figure(figsize=(7, 5))
    # for x, y in zip(lines[0], lines[1]):
    #     plt.plot(x, y)
    # plt.title("График x y")
    # plt.xlabel("x")
    # plt.ylabel("y")
    #
    # plt.figure(figsize=(7, 5))
    # plt.plot(y_array, n_test_array, color='black')
    # plt.title("Зависимость n от y TEST")
    #
    # plt.xlabel("y")
    # plt.ylabel("n")
    # plt.show()


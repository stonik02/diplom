from matplotlib import pyplot as plt

from test_func import main_function_test

if __name__ == '__main__':
    n_arr, r_arr, gradient_arr, dk_arr, dr_arr, lines = main_function_test([5000, 5000], 300)

    plt.figure(figsize=(12, 10))
    plt.subplot(2, 2, 1)
    plt.plot(r_arr, n_arr, color='black')
    plt.title("Зависимость n от y")

    plt.xlabel("y")
    plt.ylabel("n")

    plt.subplot(2, 2, 3)
    plt.plot( r_arr, gradient_arr, color='black')
    plt.title("Зависимость градиента от y")

    plt.xlabel("y")
    plt.ylabel("gradient")

    plt.subplot(2, 2, 2)
    plt.plot(r_arr, dr_arr, color='black')
    plt.title("Зависимость dr от y")

    plt.xlabel("y")
    plt.ylabel("dr")

    plt.subplot(2, 2, 4)
    plt.plot(r_arr, dk_arr, color='black')
    plt.title("Зависимость dk от y")

    plt.xlabel("y")
    plt.ylabel("dk")


    plt.figure(figsize=(7, 5))
    for x, y in zip(lines[0], lines[1]):
        plt.plot(x, y)
    plt.title("График x y")
    plt.xlabel("x")
    plt.ylabel("y")
    plt.show()

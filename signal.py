import math

# s = sin(2*pi*f*t)

pi = 3.14


def signal_point(f, t):
    return math.sin(2*pi*f*t)


def signal(f, t, steps):
    signal_arr = []
    t_arr = []
    time = t
    for i in range(steps):
        signal_arr.append(signal_point(f, time))
        time += t
        t_arr.append(time)
    return signal_arr, t_arr

from tkinter import messagebox

from function import main_function

from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure
from tkinter import *


'''
1) Почему-то изменение частоты ни на что не влияет
2) Сейчас координата y умножается на 1000 для удобства расчетов, но
я так и не понял, почему она такая маленькая
3) Так и не сделал градиент для n (не получается(  )


pip install -r requirements.txt


'''


def _quit():
    root.quit()  # остановка цикла
    root.destroy()  # закрытие приложения


# Создание canvas и графика
def generate_scatter_chart(priemnik, f):
    global canvas
    lines, result_lych = main_function(priemnik, f)
    if canvas:
        canvas.get_tk_widget().destroy()
    fig = Figure(dpi=100)
    grafik = fig.add_subplot(111)


    for x, y in zip(lines[0], lines[1]):
        grafik.plot(x, y, color='black')
    if len(result_lych) == 3:
        x_coords = [coord for sublist in result_lych[0] for coord in sublist]
        y_coords = [coord for sublist in result_lych[1] for coord in sublist]
        grafik.plot(x_coords, y_coords, color='red', label='Луч, выпущенный под {} градусов попадает в приемник'.format(result_lych[2] * 180 / 3.14))
        grafik.scatter(priemnik[0], priemnik[1], color='green', label='Приемник')
    grafik.legend()

    canvas = FigureCanvasTkAgg(fig, master = frame_canvas)
    canvas.draw()
    canvas.get_tk_widget().pack(expand=True, fill="both")
    root.after(200, None)


# Получение данных из формы и создание графика
def draw_graph():
    """
        Нужно еще обработать ошибки
    """

    try:
        f = int(txt_f.get())
    except ValueError:
        messagebox.showinfo('Ошибка', 'Необходимо ввести число')
        return

    try:
        priemnik = txt_priemnik.get()
        priemtik_arr = [float(x) for x in priemnik.split(",")]
        if priemtik_arr[0] < 0 or priemtik_arr[1] < 0 or priemtik_arr[0] > 10000 or priemtik_arr[1] > 10000:
            messagebox.showinfo('Ошибка', 'Необходимо ввести неотрицательные числа в диапазоне 5000-1000')

    except ValueError:
        messagebox.showinfo('Ошибка', 'Необходимо ввести числа в формате 1234, 4321')

        return

    if f > 1000 or f < 10:
        messagebox.showinfo('Ошибка', 'Необходимо ввести числа в интервале 10-1000')

    generate_scatter_chart(priemtik_arr, f)


# Очистка графика
def clear_canvas():
    global canvas
    if canvas:
        canvas.get_tk_widget().destroy()
        canvas = FigureCanvasTkAgg(None, master = frame_canvas)


if __name__ == '__main__':
    # Создание основного окна
    root = Tk()
    root.wm_title("Моделирование сигналов")
    root.geometry("1200x800")



    # Создание фрейма для графика
    canvas = None
    frame_canvas = Frame(master=root, width=700, height=600, borderwidth=1, relief=SOLID, padx=5, pady=5)
    # frame_canvas = Frame(master=root, width=900, height=900, borderwidth=1, relief=SOLID, padx=5, pady=5)
    frame_canvas.pack(anchor='center', side='right', padx=20, pady=20)
    frame_canvas.pack_propagate(False)  # Фиксирует размер Frame
    frame_canvas.grid_propagate(False)

    # Создание единого фрейма для кнопок и полей
    frame_main = Frame(root, borderwidth=1, relief=SOLID,)
    frame_main.pack(anchor='center', side='left', padx=20, pady=20)

    # Создаем фрейма для текстовых полей
    frame_entrys = Frame(frame_main, width=550, height=40, padx=1, pady=1)
    frame_entrys.pack(anchor='center', side='top', pady=20)
    frame_entrys.pack_propagate(False)

    # Создаем фрейма для кнопок
    frame_canvas_button = Frame(frame_main, width=450, height=40, padx=1, pady=1)
    frame_canvas_button.pack(anchor='center', side='top', pady=20)
    frame_canvas_button.pack_propagate(False)


    # Кнопка отрисовки графика
    btn_paint = Button(
        master=frame_canvas_button,
        text='Отрисовать график',
        command=draw_graph,
        width=17,
        height=2
    )
    btn_paint.grid(row=0, column=0, padx=5, sticky="nsew")


    # Кнопка очистки графика
    btn_clear_canvas = Button(
        master=frame_canvas_button,
        text='Очистить график',
        command=clear_canvas,
        width=17,
        height=2
    )
    btn_clear_canvas.grid(row=0, column=1, padx=5, sticky="nsew")

    # Текстовое поле и описание получения f
    lbl_f = Label(frame_entrys, text="Укажите частоту", font=("Arial Bold", 10))
    lbl_f.grid(row=0, column=0, padx=5, sticky="nsew")
    txt_f = Entry(frame_entrys, width=10)
    txt_f.grid(row=0, column=1, padx=5, pady=10, sticky="nsew")
    txt_f.insert(0, '300')

    # Текстовое поле и описание получения координат приемника
    lbl_priemnik = Label(frame_entrys, text="Укажите координаты приемника в формате x,y", font=("Arial Bold", 10))
    lbl_priemnik.grid(row=1, column=0, padx=5, sticky="nsew")
    txt_priemnik = Entry(frame_entrys, width=10)
    txt_priemnik.grid(row=1, column=1, padx=5, pady=15, sticky="nsew")
    txt_priemnik.insert(0, '2121, 7788')

    # Отрисовка основного окна
    root.mainloop()

    # x, y = main_function()

    # closest_ray = find_closest_ray(x, y, priemnik)

    # for x, y in zip(x, y):
    #     plt.plot(x, y)
    # if len(result_lych_y) == 1:
    #     plt.plot(result_lych_x[0], result_lych_y[0], color='red',
    #              label='Луч {} попадает в приемник'.format(result_alfa * 180 / pi))
    # plt.scatter(priemnik[0], priemnik[1], color='green', label='Приемник')
    # plt.legend(title='Минимальное расстояние до приемника = {}'.format(min_dist))
    # plt.show()

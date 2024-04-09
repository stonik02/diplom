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
def generate_scatter_chart(h_k, l_moda, f, inception, num_rays):
    global canvas
    global description
    lines, result_lych, y_min, distance_min = main_function(h_k, l_moda, f, inception, num_rays)
    if canvas:
        canvas.get_tk_widget().destroy()
    if description:
        description.destroy()
    fig = Figure(dpi=100)
    grafik = fig.add_subplot(111)
    for x, y in zip(lines[0], lines[1]):
        grafik.plot(x, y, color='black')
    if len(result_lych) == 3:
        x_coords = [coord for sublist in result_lych[0] for coord in sublist]
        y_coords = [coord for sublist in result_lych[1] for coord in sublist]
        grafik.plot(x_coords, y_coords, color='red', label='')
        grafik.scatter(inception[0], inception[1], color='green', label='Приемник')
    grafik.legend()

    canvas = FigureCanvasTkAgg(fig, master = frame_canvas)
    canvas.draw()
    canvas.get_tk_widget().pack(expand=True,
                                fill="both"
                                )
    description = Label(frame_description,
                        text="1. Луч, выпущенный под {} градусов попадает в приемник. На графике он отображен {} цветом. \n\n"
                             "Расстояние от луча до приемника = {} метров. \n\n"
                             "2. Лучи подходят к берегу на расстояние = {} метров. \n\n".format(int(result_lych[2] * 180 / 3.14), "Красным", int(distance_min), int(y_min)),
                        font=("Arial Bold", 10),
                        pady=15
                        )

    description.pack()
    root.after(200, None)


# Получение данных из формы и создание графика
def draw_graph():
    try:
        l_moda = int(txt_l_moda.get())
    except ValueError:
        messagebox.showinfo('Неверное значение моды', 'Необходимо ввести число')
        return

    try:
        h_k = float(txt_h_k.get())
    except ValueError:
        messagebox.showinfo('Неверное значение коэффициента глубины', 'Необходимо ввести дробное число')
        return

    try:
        num_rays = int(txt_num_rays.get())
        num_rays = num_rays * 2
    except ValueError:
        messagebox.showinfo('Неверное значение кол-ва лучей', 'Необходимо ввести число')
        return

    try:
        f = int(txt_f.get())
    except ValueError:
        messagebox.showinfo('Неверное значение частоты', 'Необходимо ввести число')
        return

    try:
        inception = txt_inception.get()
        inception_arr = [float(x) for x in inception.split(",")]

    except ValueError:
        messagebox.showinfo('Неверное значение координат приемника', 'Необходимо ввести числа в формате 1234, 4321')
        return

    if inception_arr[0] < 0 or inception_arr[1] < 0 or inception_arr[0] > 30000 or inception_arr[1] > 30000:
        messagebox.showinfo('Неверное значение координат приемника', 'Необходимо ввести неотрицательные числа в диапазоне 5000-30000')

    if f > 1000 or f < 10:
        messagebox.showinfo('Неверное значение частоты', 'Необходимо ввести число в интервале 10-1000')

    if l_moda > 7 or l_moda < 1:
        messagebox.showinfo('Неверное значение моды', 'Необходимо ввести число в интервале 1-7')

    # Для отрисовки в половине графиков всех лучей мы их * 2
    if num_rays > 200 or num_rays < 60:
        messagebox.showinfo('Неверное значение кол-ва лучей', 'Необходимо ввести число в интервале 30-100')

    if h_k > 1000 or h_k < 0.004:
        messagebox.showinfo('Неверное значение коэффициента глубины', 'Необходимо ввести число в интервале 0.02 - 0.06')

    generate_scatter_chart(h_k, l_moda, f, inception_arr, num_rays)


# Очистка графика
def clear_canvas():
    global canvas
    global description
    if canvas:
        canvas.get_tk_widget().destroy()
        canvas = FigureCanvasTkAgg(None, master = frame_canvas)

    if description:
        description.destroy()
        description = Label()


if __name__ == '__main__':
    # Создание основного окна
    root = Tk()
    root.wm_title("Моделирование сигналов")
    root.geometry("1200x800")
    # root.geometry("1000x600")
    root.resizable(False, False)


    # Создание фрейма для графика
    canvas = None
    description = None
    frame_canvas_description = Frame(master=root,
                         padx=5,
                         pady=5
                         )
    frame_canvas_description.pack(
                      side='right',
                      padx=20,
                      pady=20
                      )

    frame_canvas = Frame(master=frame_canvas_description,
                         width=600,
                         height=500,
                         borderwidth=1,
                         relief=SOLID,
                         padx=5,
                         pady=5
                         )
    frame_canvas.pack(
                      side='top',
                      padx=20,
                      pady=20

                      )
    frame_canvas.pack_propagate(False)  # Фиксирует размер Frame
    frame_canvas.grid_propagate(False)

    frame_description = Frame(master=frame_canvas_description,
                              width=600,
                              height=300,
                              borderwidth=1,
                              relief=SOLID,
                              padx=5,
                              pady=5
                              )
    frame_description.pack(
                      side='bottom',
                      padx=20,
                      pady=20

                      )

    # Создание единого фрейма для кнопок и полей
    frame_main = Frame(root,
                       borderwidth=1,
                       relief=SOLID,
                       padx=5,
                       pady=5
                       )
    frame_main.pack(
                    side='left',
                    padx=20,
                    pady=20
                    )


    # # Создаем пустой фрейм для отступа
    # frame_null = Frame(master=root,
    #                           width=50,
    #                           height=300,
    #                           )
    # # frame_canvas = Frame(master=root, width=900, height=900, borderwidth=1, relief=SOLID, padx=5, pady=5)
    # frame_null.pack(side='top',
    #                 padx=40,
    #                 pady=20
    #                 )
    # frame_null.pack_propagate(False)  # Фиксирует размер Frame

    # Создаем фрейма вывода описания графика
    # frame_description = Frame(master=root,
    #                           width=1000,
    #                           height=100,
    #                           borderwidth=1,
    #                           relief=SOLID,
    #                           padx=1,
    #                           pady=1
    #                           )
    # # frame_canvas = Frame(master=root, width=900, height=900, borderwidth=1, relief=SOLID, padx=5, pady=5)
    # frame_description.pack(
    #                        side='bottom',
    #                        pady=20
    #                        )
    # frame_description.pack_propagate(False)  # Фиксирует размер Frame

    # Создаем фрейма для текстовых полей ввода
    frame_entrys = Frame(frame_main,
                         width=450,
                         height=40,
                         padx=1,
                         pady=1
                         )
    frame_entrys.grid( row=1,
                       column=1
                      # side='top',
                      # pady=20
                      )
    frame_entrys.pack_propagate(False)

    # Создаем фрейма для кнопок
    frame_canvas_button = Frame(frame_main,
                                width=450,
                                height=40,
                                padx=1,
                                pady=1
                                )
    frame_canvas_button.grid( row=2,
                              column=1
                             # side='bottom',
                             # pady=20
                             )
    frame_canvas_button.pack_propagate(False)





    # Кнопка отрисовки графика
    btn_paint = Button(
        master=frame_canvas_button,
        text='Отрисовать график',
        command=draw_graph,
        width=17,
        height=2
    )
    btn_paint.grid(row=0,
                   column=0,
                   padx=5,
                   sticky="nsew"
                   )


    # Кнопка очистки графика
    btn_clear_canvas = Button(
        master=frame_canvas_button,
        text='Очистить график',
        command=clear_canvas,
        width=17,
        height=2
    )
    btn_clear_canvas.grid(row=0,
                          column=1,
                          padx=5,
                          sticky="nsew"
                          )

    # Текстовое поле и описание получения f
    lbl_f = Label(frame_entrys,
                  text="Укажите частоту",
                  font=("Arial Bold", 10))
    lbl_f.grid(row=0,
               column=0,
               padx=5,
               sticky="nsew"
               )
    txt_f = Entry(frame_entrys,
                  width=10
                  )
    txt_f.grid(row=0,
               column=1,
               padx=5,
               pady=10,
               sticky="nsew"
               )
    txt_f.insert(0,
                 '300'
                 )

    # Текстовое поле и описание получения координат приемника
    lbl_inception = Label(frame_entrys,
                          text="Укажите координаты приемника в формате x,y",
                          font=("Arial Bold", 10))
    lbl_inception.grid(row=1,
                       column=0,
                       padx=5,
                       sticky="nsew"
                       )
    txt_inception = Entry(frame_entrys,
                          width=15
                          )
    txt_inception.grid(row=1,
                       column=1,
                       padx=5,
                       pady=15,
                       sticky="nsew"
                       )
    txt_inception.insert(0, '2121, 7788')

    # Текстовое поле и описание получения номер моды
    l_moda_ = Label(frame_entrys,
                    text="Укажите номер моды 1-7",
                    font=("Arial Bold", 10)
                    )
    l_moda_.grid(row=2,
                 column=0,
                 padx=5,
                 sticky="nsew"
                 )
    txt_l_moda = Entry(frame_entrys,
                       width=10
                       )
    txt_l_moda.grid(row=2, column=1, padx=5, pady=15, sticky="nsew")
    txt_l_moda.insert(0, '3')

    # Текстовое поле и описание получения кол-ва лучей
    num_rays = Label(frame_entrys,
                     text="Укажите колличество лучей 30-100",
                     font=("Arial Bold", 10)
                     )
    num_rays.grid(row=3,
                  column=0,
                  padx=5,
                  sticky="nsew"
                  )
    txt_num_rays = Entry(frame_entrys,
                         width=10)
    txt_num_rays.grid(row=3,
                      column=1,
                      padx=5,
                      pady=15,
                      sticky="nsew"
                      )
    txt_num_rays.insert(0, '50')

    # Текстовое поле и описание получения коэффициента H
    """
    Сделать выпадающим списком
    """
    h_k_inception = Label(frame_entrys, text="Укажите коэффициент глубины 0.004-1000", font=("Arial Bold", 10))
    h_k_inception.grid(row=4,
                      column=0,
                      padx=5,
                      sticky="nsew"
                      )
    txt_h_k = Entry(frame_entrys,
                    width=10
                    )
    txt_h_k.grid(row=4,
                 column=1,
                 padx=5,
                 pady=15,
                 sticky="nsew"
                 )
    txt_h_k.insert(0, '0.03')

    # txt_description = Label(frame_description,
    #                    text="Укажите коэффициент глубины 0.02-0.06 Укажите коэффициент глубины 0.02-0.06 Укажите коэффициент глубины 0.02-0.06", font=("Arial Bold", 10)
    #                    )
    # txt_description.pack(padx=5, pady=15)


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

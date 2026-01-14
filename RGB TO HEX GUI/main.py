#импортируем библиотеки
import flet as ft

#импортируем файлы с функциями
import rgb_to_hex

#основная функция
def main(page: ft.Page):
    #настройка окна
    page.title = "RGB TO HEX"   #название программы
    page.theme_mode = 'dark'    #начальная тема
    page.vertical_alignment = ft.MainAxisAlignment.CENTER   #расположение элементов по вертикали
    page.horizontal_alignment = ft.MainAxisAlignment.CENTER     #расположение элементов по горизонтали
    page.window.width = 700     #ширина
    page.window.height = 1100   #высота
    page.window.min_height = 510    #минимальная высота
    page.window.min_width = 700     #минимальная ширина
    page.scroll = ft.ScrollMode.AUTO    #режим прокрутки окна

    #функция для перевода RGB в HEX
    def rgba1(e):
        try:
            rgbzz = rgbz.value  #то что ввёл пользователь
            hexes = str(rgb_to_hex.rgba(str(rgbzz)))    #перевод ввода
            vyvod.value = "HEX code: " + hexes  #вывод кода
            rgbz.value = ''     #отсистка поля ввода
            buttonrgb.disabled = True   #отключение кнопки блокировки
            clean_btn.disabled = False  #включение кнопки отчистки
            vyvod_container.disabled = False    #включение кнопки копирования
            #отображаем цвет вводы/вывода
            hexes = hexes.replace('#', '')
            if len(hexes) > 6:
                o = hexes[:-2]
                hexes = "#"+hexes+o
            if len(hexes) <= 6:
                hexes = "#ff"+hexes #не убирать, иначе контейнер не окраситься и будет прозрачным!
            vyvod_container.bgcolor = hexes
            page.open(ft.SnackBar(ft.Text('Color:'), bgcolor=hexes))
            page.update() #обновляем информацию на странице
        except:
            #если не удалось перевести
            vyvod.value = 'Error: incorrect input'  #выводим ощибку
            rgbz.value = ''     #очищаем поле ввода
            buttonrgb.disabled = True   #выключаем кнопку перевода
            clean_btn.disabled = False  #включаем кнопку отчистки
            vyvod_container.disabled = True     #выключаем возможность скопировать ввывод
            page.open(ft.SnackBar(ft.Text('Error: incorrect input'), bgcolor="#80a11c1c"))  #открываем снекбар с ошибкой
            vyvod_container.bgcolor = '#80a11c1c'   #задаём красный цвет для вывода цвета
            page.update()   #обновляем информацию на старнице

    #функция для перевода HEX в RGB
    def hex1(e):
        try:
            rgbzz = HEXa.value.replace('#', '')     #убираем не нужное для перевода
            hexes = rgb_to_hex.HEX(str(rgbzz))      #перевводим
            vyvod2.value = "RGB code: " + str(hexes)    #ввыводим ответ
            HEXa.value = ''     #отчищаем поле ввода
            buttonhex.disabled = True   #выключаем кнопку отправки ввода
            clean_btn.disabled = False      #включаем кнопку отчитки
            vyvod2_container.disabled = False   #включаем возможность скопировать ввывод
            #выводим введёный цвет
            if len(rgbzz) > 6:
                o = rgbzz[:-2]
                rgbzz = rgbzz+o
            rgbzz = str('#'+str(rgbzz))
            vyvod2_container.bgcolor = rgbzz
            page.open(ft.SnackBar(ft.Text('Color:'), bgcolor=rgbzz))
            page.update() #обновляем информацию на странице
        except:
            #если не получилось перевести
            vyvod2.value = 'Error: incorrect input'  #ввыодим ошибку
            HEXa.value = ''     #отчищаем поле ввода
            buttonhex.disabled = True   #блокируем кнопку перевода
            clean_btn.disabled = False      #разрешаем отчистить поле вывода
            vyvod2_container.disabled = True    #запрещаем копирование вывода
            page.open(ft.SnackBar(ft.Text('Error: incorrect input'), bgcolor="#80a11c1c"))      #открываем снекбар с ошибкой
            vyvod2_container.bgcolor = '#80a11c1c'      #задаём цвет поля вывода цвета
            page.update()   #обновляем информацию об ошибках

    #смена темы
    def theme_switch(e):
        if page.theme_mode == 'dark':
            theme_btn.icon = ft.Icons.DARK_MODE #меняем иконку
            RGB_to_HEX.bgcolor = "#80811EAC"    #выставляем правильный цвет для светлой темы
            HEX_to_RGB.bgcolor = "#80811EAC"    #выставляем правильный цвет для светлой темы
            MAIN_RGB_TO_HEX.bgcolor = "#80760DA0"   #выставляем правильный цвет для светлой темы
            buttonrgb.bgcolor= {ft.ControlState.DISABLED: "#80682486", ft.ControlState.DEFAULT: "#7F22A7"}  #выставляем правильный цвет для светлой темы
            buttonhex.bgcolor={ft.ControlState.DISABLED: '#80682486', ft.ControlState.DEFAULT: '#7F22A'}    #выставляем правильный цвет для светлой темы
            page.update()   #обновляем страницу
            page.theme_mode = 'light'   #меняем тему на светлую
        else:
            theme_btn.icon = ft.Icons.LIGHT_MODE #меняем иконку
            RGB_to_HEX.bgcolor = "#804D245E"    #выставляем правильный цвет для светлой темы
            HEX_to_RGB.bgcolor = "#804D245E"    #выставляем правильный цвет для светлой темы
            MAIN_RGB_TO_HEX.bgcolor = "#802E0C3C"   #выставляем правильный цвет для светлой темы
            buttonhex.bgcolor={ft.ControlState.DISABLED: '#805f3b6f', ft.ControlState.DEFAULT: '#5f3b6f'}   #выставляем правильный цвет для светлой темы
            buttonrgb.bgcolor={ft.ControlState.DISABLED: '#805f3b6f', ft.ControlState.DEFAULT: '#5f3b6f'}   #выставляем правильный цвет для светлой темы
            page.update()   #обновляем страницу
            page.theme_mode ='dark'     #меняем тему на тёмную
        page.update()   #обновляем все изменения

    #проверка кнопки перевода в rgb
    def varidate_hex(e):
        #проверяем нужно ли отивирорвать кнопку для перевода
        if all([HEXa.value]):
            buttonhex.disabled = False      #активируем
        else:
            buttonhex.disabled = True       #не активируем
        page.update()   #обновляем страницу
    
    #проверка кнопки перевода в hex
    def varidate_rgb(e):
        #проверяем нужно ли отивирорвать кнопку для перевода
        if all([rgbz.value]):   
            buttonrgb.disabled = False      #активируем
        else:
            buttonrgb.disabled = True       #не активируем
        page.update()   #обновляем страницу

    #отчиска результатов
    def clean(e):
        vyvod.value = ''    #отчищаем результат
        vyvod2.value = ''   #отчищаем результат 2
        vyvod_container.bgcolor = '#80FFFFFF'   #меняем вывод на основной цвет
        vyvod2_container.bgcolor = '#80FFFFFF'  #тоже самое, но для другого вывода
        clean_btn.disabled = True   #блокируем кнопку отчиски 1
        clean_btn_hex.disabled = True   #блокируем кнопку отчистки 2
        clean_btn_rgb.disabled = True   #блокируем кнопку отчистки all
        vyvod2_container.disabled = True    #блокируем копирование
        vyvod_container.disabled = True     #тоже самое, для другого контейнера
        page.open(ft.SnackBar(ft.Text('All results was successfully cleared'), bgcolor='#804ab818'))    #открываем снекбар в честь успешной отчистки
        page.update()   #обновляем страницу
    
    #отчиска результата hex
    def cleanhex(e):
        vyvod.value = ''    #отчищаем
        vyvod_container.bgcolor = '#80FFFFFF'   #меняем на основной цвет
        clean_btn_hex.disabled = True       #запрещаем отчищать это поле
        vyvod_container.disabled = True     #запрещаем копировать вывод
        page.open(ft.SnackBar(ft.Text('The result was successfully cleared'), bgcolor='#804ab818'))     #выводим снекбар об успешной отчистке
        page.update()   #обновляем страницу

    #проверка clean HEX result
    def clean_btn_hex_data(e):
        #проверяем кнопочку
        if all([vyvod.value]):
            clean_btn_hex.disabled = False  #активируем
        else:
            clean_btn_hex.disabled = True   #деактивируем
        page.update()   #обновляем страницу

    #отчистка результата rgb
    def cleanrgb(e):
        vyvod2.value = ''   #отчищаем
        vyvod2_container.bgcolor = '#80FFFFFF'  #меняем на основной цвет
        clean_btn_rgb.disabled = True   #запрещаем отчищать это поле
        vyvod2_container.disabled = True    #запрещаем копировать вывод
        page.open(ft.SnackBar(ft.Text('The result was successfully cleared'), bgcolor="#804ab818")) #выводим снекбар об успешной отчистке
        page.update()   #обновляем страницу

    #проверка clean RGB result
    def clean_btn_rgb_data(e):
        #проверяем кнопку
        if all([vyvod2.value]):
            clean_btn_rgb.disabled = False      #активируем
        else:
            clean_btn_rgb.disabled = True   #деактивируем
        page.update()   #обновляем страницу

    #проверка clean all result
    def clean_btn_data(e):
        #проверяем
        if clean_btn_hex.disabled or clean_btn_rgb.disabled == True:
            #активируем
            clean_btn.disabled = True
        else:
            #деактивируем
            clean_btn.disabled = False
        page.update()   #обновляем страницу

    #копирование hex 
    def copy_result_hex(e):
        b = vyvod.value.replace("HEX code: ", "")   #удаляем лишнее
        page.set_clipboard(str(b))  #копируем
        page.open(ft.SnackBar(ft.Text('Result is copied')))     #открываем снекбар о успешном копирование
        page.update()   #обновляем страницу

    #копирование rgb
    def copy_result_rgb(e):
        z = vyvod2.value.replace("RGB code: ", "")     #удаляем лишнее  
        page.set_clipboard(str(z))  #копируем
        page.open(ft.SnackBar(ft.Text('Result is copied')))  #выводим сообщение о успешном копирование
        page.update()   #обновляем страницу
    

    #поле ввода rgb
    rgbz = ft.TextField(label='Enter the RGB (for example: 128, 128, 128, 1 or 128, 128, 128)', color='#e4e4e4', label_style=ft.TextStyle(color="#e4e4e4"), width=500, text_align=ft.TextAlign.CENTER, on_change=varidate_rgb, on_submit=rgba1)

    #поле ввода hex
    HEXa = ft.TextField(label='Enter the HEX (for example: 80808080 or 808080)', color='#e4e4e4', label_style=ft.TextStyle(color="#e4e4e4"), width=410, text_align=ft.TextAlign.CENTER, on_change=varidate_hex, on_submit=hex1)

    #кнопка конвертирования в hex
    buttonrgb = ft.ElevatedButton(text='Convert RGB to HEX', bgcolor={ft.ControlState.DISABLED: '#805f3b6f', ft.ControlState.DEFAULT: '#5f3b6f'}, color={ft.ControlState.DISABLED: "#80292929", ft.ControlState.DEFAULT: "#e4e4e4"}, on_click=rgba1, disabled=True, on_blur=clean_btn_hex_data)

    #кнопка конвертирования в rgb
    buttonhex = ft.ElevatedButton(text='Convert HEX to RGB', bgcolor={ft.ControlState.DISABLED: '#805f3b6f', ft.ControlState.DEFAULT: '#5f3b6f'}, color={ft.ControlState.DISABLED: "#80292929", ft.ControlState.DEFAULT: "#e4e4e4"}, on_click=hex1, disabled=True, on_blur=clean_btn_rgb_data)
    
    #вывод hex
    vyvod = ft.Text('', color="#e4e4e4")

    #вывод rgb
    vyvod2 = ft.Text('', color="#e4e4e4")

    #кнопка отчистки всех результатов
    clean_btn = ft.OutlinedButton(text='Clean all results', on_click=clean, disabled=True)

    #отчистка результата hex
    clean_btn_hex = ft.OutlinedButton(text='Clean result',  style=ft.ButtonStyle(color={ft.ControlState.DISABLED: "#80292929", ft.ControlState.DEFAULT: "#e4e4e4"}, text_style=ft.TextStyle(size=10)), height=20, width=80, on_click=cleanhex, on_blur=clean_btn_data, disabled=True)

    #отчистка результата rgb
    clean_btn_rgb = ft.OutlinedButton(text='Clean result', style=ft.ButtonStyle(color={ft.ControlState.DISABLED: "#80292929", ft.ControlState.DEFAULT: "#e4e4e4"}, text_style=ft.TextStyle(size=10)), height=20, width=80, on_click=cleanrgb, on_blur=clean_btn_data, disabled=True)

    #кнопка смены темы
    theme_btn = ft.IconButton(icon=ft.Icons.LIGHT_MODE, on_click=theme_switch)

    #вывод с цветом hex
    vyvod_container = ft.Container(     #открываем контейнер
        content=ft.Row([vyvod], alignment=ft.MainAxisAlignment.CENTER), #что выводим
        tooltip='Copy result',  #что показывваем при наведении
        margin=10,  #отступы наружние
        padding=10, #внутрение отступы
        alignment=ft.alignment.center,  #где располагем элементы
        bgcolor='#80FFFFFF',    #основной цвет
        width=300,  #ширина
        height=50,  #высота
        border_radius=10,   #радиус закругления
        on_click=copy_result_hex,   #что делаем при нажатии на контейнер
        disabled=True   #выключен ли клик по нему?
    )

    #вывод с цветом rgb
    vyvod2_container = ft.Container(    #открываем контейнер
        content=ft.Row([vyvod2], alignment=ft.MainAxisAlignment.CENTER),    #что выводим
        tooltip='Copy result',  #что показывваем при наведении
        margin=10,  #отступы наружние
        padding=10, #внутрение отступы
        alignment=ft.alignment.center,  #где располагем элементы
        bgcolor='#80FFFFFF',    #основной цвет
        width=300,  #ширина
        height=50,  #высота
        border_radius=10,   #радиус закругления
        on_click=copy_result_rgb,   #что делаем при нажатии на контейнер
        disabled=True   #выключен ли клик по нему?
    )

    #основной текст первого контейнера
    main_text_rgb_to_hex = ft.Container(    #открываем контейнер
        content=ft.Column(      #что выводим
            [
                ft.Row([ft.Text('RGB to HEX', size=25, color="#000b31")], alignment=ft.MainAxisAlignment.CENTER)
            ], alignment=ft.MainAxisAlignment.CENTER
        ),
        margin=10,      #отступы наружние
        padding=2.5,    #внутрение отступы
        alignment=ft.alignment.center,      #где располагем элементы
        bgcolor="#7994eb",      #основной цвет
        border_radius=10    #радиус закругления
    )

    #основной текст второго контейнера
    main_text_hex_to_rgb = ft.Container(    #открываем контейнер
        content=ft.Column(      #что выводим
            [
                ft.Row([ft.Text('HEX to RGB', size=25, color="#000b31")], alignment=ft.MainAxisAlignment.CENTER)
            ], alignment=ft.MainAxisAlignment.CENTER
        ),
        margin=10,  #наружние отступы
        padding=2.5,    #внутрение отступы
        alignment=ft.alignment.center,  #где располагем элементы
        bgcolor="#7994eb",  #основной цвет
        border_radius=10    #радиус закругления
    )

    #первый контейнер
    RGB_to_HEX = ft.Container(  #открываем контейнер
        content=ft.Column(   #что выводим
            [
                ft.Row([main_text_rgb_to_hex], alignment=ft.MainAxisAlignment.CENTER),
                ft.Row([ft.Text('Enter the RGB:', color='#e4e4e4')], alignment=ft.MainAxisAlignment.CENTER),
                ft.Row([rgbz], alignment=ft.MainAxisAlignment.CENTER),
                ft.Row([buttonrgb, clean_btn_hex], alignment=ft.MainAxisAlignment.CENTER),
                ft.Row([vyvod_container], alignment=ft.MainAxisAlignment.CENTER),
            ], alignment=ft.MainAxisAlignment.CENTER
        ),
        margin=10,  #наружние отступы
        padding=10, #внутрение отступы
        alignment=ft.alignment.center,  #где располагем элементы
        bgcolor="#804D245E",    #основной цвет
        width=550,  #ширина
        height=350, #высота
        border_radius=10    #радиус закругления
    )

    #второй контейнер
    HEX_to_RGB = ft.Container(  #открываем контейнер
        content=ft.Column(  #что выводим
            [
                ft.Row([main_text_hex_to_rgb], alignment=ft.MainAxisAlignment.CENTER),
                ft.Row([ft.Text('Enter the HEX:', color='#e4e4e4')], alignment=ft.MainAxisAlignment.CENTER),
                ft.Row([HEXa], alignment=ft.MainAxisAlignment.CENTER),
                ft.Row([buttonhex, clean_btn_rgb], alignment=ft.MainAxisAlignment.CENTER),
                ft.Row([vyvod2_container], alignment=ft.MainAxisAlignment.CENTER),
            ], alignment=ft.MainAxisAlignment.CENTER
        ),
        margin=10,  #наружние отступы
        padding=10, #внутрение отступы
        alignment=ft.alignment.center,  #где располагем элементы
        bgcolor="#804D245E",    #основной цвет
        width=550,  #ширина
        height=350, #высота
        border_radius=10    #радиус закругления
    )

    #фон и основное поле
    MAIN_RGB_TO_HEX = ft.Container( #открываем контейнер
        content=ft.Column(  #что выводим
            [
                ft.Row([theme_btn], alignment=ft.MainAxisAlignment.END),
                ft.Row([RGB_to_HEX], alignment=ft.MainAxisAlignment.CENTER),
                ft.Row([HEX_to_RGB], alignment=ft.MainAxisAlignment.CENTER),
                ft.Row([clean_btn], alignment=ft.MainAxisAlignment.END)
            ], alignment=ft.MainAxisAlignment.CENTER
        ),
        margin=10,  #наружние отступы
        padding=10, #внутрение отступы
        alignment=ft.alignment.center,  #где распологаем элементы
        bgcolor="#802E0C3C",    #основной цвет
        border_radius=10    #радиус закругления
    )

    #отрисовка приложения    
    page.add(
        #основное поле
        MAIN_RGB_TO_HEX
    )

#старт программы
ft.app(port=25565,      #какой порт используем, если это web прриложение или сайт
       target=main,     #какую функцию исполняем
       view=ft.AppView.FLET_APP     #как отбражаем приложение 
    )
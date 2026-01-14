import flet as ft
import rgb_to_hex

def main(page: ft.Page):
    #настройка окна
    page.title = "RGB TO HEX"
    page.theme_mode = 'dark' 
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.MainAxisAlignment.CENTER
    page.window.width = 700
    page.window.height = 1100
    page.window.min_height = 510
    page.window.min_width = 700
    page.scroll = ft.ScrollMode.AUTO

    #функция для перевода RGB в HEX
    def rgba1(e):
        try:
            rgbzz = rgbz.value
            hexes = str(rgb_to_hex.rgba(str(rgbzz)))
            vyvod.value = "HEX code: " + hexes
            rgbz.value = ''
            buttonrgb.disabled = True
            clean_btn.disabled = False
            vyvod_container.disabled = False
            hexes = hexes.replace('#', '')
            if len(hexes) > 6:
                o = hexes[:-2]
                hexes = "#"+hexes+o
            if len(hexes) <= 6:
                hexes = "#ff"+hexes
            vyvod_container.bgcolor = hexes
            page.open(ft.SnackBar(ft.Text('Color:'), bgcolor=hexes))
            page.update()
        except:
            vyvod.value = 'Error: incorrect input'
            rgbz.value = ''
            buttonrgb.disabled = True
            clean_btn.disabled = False
            vyvod_container.disabled = True
            page.open(ft.SnackBar(ft.Text('Error: incorrect input'), bgcolor="#80a11c1c"))
            vyvod_container.bgcolor = '#80a11c1c'
            page.update()

    #функция для перевода HEX в RGB
    def hex1(e):
        try:
            rgbzz = HEXa.value.replace('#', '')
            hexes = rgb_to_hex.HEX(str(rgbzz))
            vyvod2.value = "RGB code: " + str(hexes)
            HEXa.value = ''
            buttonhex.disabled = True
            clean_btn.disabled = False
            vyvod2_container.disabled = False
            if len(rgbzz) > 6:
                o = rgbzz[:-2]
                rgbzz = rgbzz+o
            rgbzz = str('#'+str(rgbzz))
            vyvod2_container.bgcolor = rgbzz
            page.open(ft.SnackBar(ft.Text('Color:'), bgcolor=rgbzz))
            page.update()
        except:
            vyvod2.value = 'Error: incorrect input'
            HEXa.value = ''
            buttonhex.disabled = True
            clean_btn.disabled = False
            vyvod2_container.disabled = True
            page.open(ft.SnackBar(ft.Text('Error: incorrect input'), bgcolor="#80a11c1c"))
            vyvod2_container.bgcolor = '#80a11c1c'
            page.update()

    #смена темы
    def theme_switch(e):
        if page.theme_mode == 'dark':
            theme_btn.icon = ft.Icons.DARK_MODE
            RGB_to_HEX.bgcolor = "#80811EAC"
            HEX_to_RGB.bgcolor = "#80811EAC"
            MAIN_RGB_TO_HEX.bgcolor = "#80760DA0"
            buttonrgb.bgcolor= {ft.ControlState.DISABLED: "#80682486", ft.ControlState.DEFAULT: "#7F22A7"}
            buttonhex.bgcolor={ft.ControlState.DISABLED: '#80682486', ft.ControlState.DEFAULT: '#7F22A'}
            page.update()
            page.theme_mode = 'light'
        else:
            theme_btn.icon = ft.Icons.LIGHT_MODE
            RGB_to_HEX.bgcolor = "#804D245E"
            HEX_to_RGB.bgcolor = "#804D245E"
            MAIN_RGB_TO_HEX.bgcolor = "#802E0C3C"
            buttonhex.bgcolor={ft.ControlState.DISABLED: '#805f3b6f', ft.ControlState.DEFAULT: '#5f3b6f'}
            buttonrgb.bgcolor={ft.ControlState.DISABLED: '#805f3b6f', ft.ControlState.DEFAULT: '#5f3b6f'}
            page.update()
            page.theme_mode ='dark'
        page.update()

    #проверка кнопки перевода в rgb
    def varidate_hex(e):
        if all([HEXa.value]):
            buttonhex.disabled = False
        else:
            buttonhex.disabled = True
        page.update()
    
    #проверка кнопки перевода в hex
    def varidate_rgb(e):
        if all([rgbz.value]):
            buttonrgb.disabled = False
        else:
            buttonrgb.disabled = True
        page.update()

    #отчиска результатов
    def clean(e):
        vyvod.value = ''
        vyvod2.value = ''
        vyvod_container.bgcolor = '#80FFFFFF'
        vyvod2_container.bgcolor = '#80FFFFFF'
        clean_btn.disabled = True
        clean_btn_hex.disabled = True
        clean_btn_rgb.disabled = True
        vyvod2_container.disabled = True
        vyvod_container.disabled = True
        page.open(ft.SnackBar(ft.Text('All results was successfully cleared'), bgcolor='#804ab818'))
        page.update()
    
    #отчиска результата hex
    def cleanhex(e):
        vyvod.value = ''
        vyvod_container.bgcolor = '#80FFFFFF'
        clean_btn_hex.disabled = True
        vyvod_container.disabled = True
        page.open(ft.SnackBar(ft.Text('The result was successfully cleared'), bgcolor='#804ab818'))
        page.update()

    #проверка clean HEX result
    def clean_btn_hex_data(e):
        if all([vyvod.value]):
            clean_btn_hex.disabled = False
        else:
            clean_btn_hex.disabled = True
        page.update()

    #отчистка результата rgb
    def cleanrgb(e):
        vyvod2.value = ''
        vyvod2_container.bgcolor = '#80FFFFFF'
        clean_btn_rgb.disabled = True
        vyvod2_container.disabled = True
        page.open(ft.SnackBar(ft.Text('The result was successfully cleared'), bgcolor="#804ab818"))
        page.update()

    #проверка clean RGB result
    def clean_btn_rgb_data(e):
        if all([vyvod2.value]):
            clean_btn_rgb.disabled = False
        else:
            clean_btn_rgb.disabled = True
        page.update()

    #проверка clean all result
    def clean_btn_data(e):
        if clean_btn_hex.disabled and clean_btn_rgb.disabled == True:
            clean_btn.disabled = True
        else:
            clean_btn.disabled = False
        page.update()

    #копирование hex 
    def copy_result_hex(e):
        b = vyvod.value.replace("HEX code: ", "")
        page.set_clipboard(str(b))
        page.open(ft.SnackBar(ft.Text('Result is copied')))
        page.update()

    #копирование rgb
    def copy_result_rgb(e):
        z = vyvod2.value.replace("RGB code: ", "")
        page.set_clipboard(str(z))
        page.open(ft.SnackBar(ft.Text('Result is copied')))
        page.update()
    

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
    vyvod_container = ft.Container(
        content=ft.Row([vyvod], alignment=ft.MainAxisAlignment.CENTER),
        tooltip='Copy result',
        margin=10,
        padding=10,
        alignment=ft.alignment.center,
        bgcolor='#80FFFFFF',
        width=300,
        height=50,
        border_radius=10,
        on_click=copy_result_hex,
        disabled=True
    )

    #вывод с цветом rgb
    vyvod2_container = ft.Container(
        content=ft.Row([vyvod2], alignment=ft.MainAxisAlignment.CENTER),
        tooltip='Copy result',
        margin=10,
        padding=10,
        alignment=ft.alignment.center,
        bgcolor='#80FFFFFF',
        width=300,
        height=50,
        border_radius=10,
        on_click=copy_result_rgb,
        disabled=True
    )

    #основной текст первого контейнера
    main_text_rgb_to_hex = ft.Container(
        content=ft.Column(
            [
                ft.Row([ft.Text('RGB to HEX', size=25, color="#000b31")], alignment=ft.MainAxisAlignment.CENTER)
            ], alignment=ft.MainAxisAlignment.CENTER
        ),
        margin=10,
        padding=2.5,
        alignment=ft.alignment.center,
        bgcolor="#7994eb",
        border_radius=10
    )

    #основной текст второго контейнера
    main_text_hex_to_rgb = ft.Container(
        content=ft.Column(
            [
                ft.Row([ft.Text('HEX to RGB', size=25, color="#000b31")], alignment=ft.MainAxisAlignment.CENTER)
            ], alignment=ft.MainAxisAlignment.CENTER
        ),
        margin=10,
        padding=2.5,
        alignment=ft.alignment.center,
        bgcolor="#7994eb",
        border_radius=10
    )

    #первый контейнер
    RGB_to_HEX = ft.Container(
        content=ft.Column(
            [
                ft.Row([main_text_rgb_to_hex], alignment=ft.MainAxisAlignment.CENTER),
                ft.Row([ft.Text('Enter the RGB:', color='#e4e4e4')], alignment=ft.MainAxisAlignment.CENTER),
                ft.Row([rgbz], alignment=ft.MainAxisAlignment.CENTER),
                ft.Row([buttonrgb, clean_btn_hex], alignment=ft.MainAxisAlignment.CENTER),
                ft.Row([vyvod_container], alignment=ft.MainAxisAlignment.CENTER),
            ], alignment=ft.MainAxisAlignment.CENTER
        ),
        margin=10,
        padding=10,
        alignment=ft.alignment.center,
        bgcolor="#804D245E",
        width=550,
        height=350,
        border_radius=10
    )

    #второй контейнер
    HEX_to_RGB = ft.Container(
        content=ft.Column(
            [
                ft.Row([main_text_hex_to_rgb], alignment=ft.MainAxisAlignment.CENTER),
                ft.Row([ft.Text('Enter the HEX:', color='#e4e4e4')], alignment=ft.MainAxisAlignment.CENTER),
                ft.Row([HEXa], alignment=ft.MainAxisAlignment.CENTER),
                ft.Row([buttonhex, clean_btn_rgb], alignment=ft.MainAxisAlignment.CENTER),
                ft.Row([vyvod2_container], alignment=ft.MainAxisAlignment.CENTER),
            ], alignment=ft.MainAxisAlignment.CENTER
        ),
        margin=10,
        padding=10,
        alignment=ft.alignment.center,
        bgcolor="#804D245E",
        width=550,
        height=350,
        border_radius=10
    )

    #фон и основное поле
    MAIN_RGB_TO_HEX = ft.Container(
        content=ft.Column(
            [
                ft.Row([theme_btn], alignment=ft.MainAxisAlignment.END),
                ft.Row([RGB_to_HEX], alignment=ft.MainAxisAlignment.CENTER),
                ft.Row([HEX_to_RGB], alignment=ft.MainAxisAlignment.CENTER),
                ft.Row([clean_btn], alignment=ft.MainAxisAlignment.END)
            ], alignment=ft.MainAxisAlignment.CENTER
        ),
        margin=10,
        padding=10,
        alignment=ft.alignment.center,
        bgcolor="#802E0C3C",
        border_radius=10
    )

    #отрисовка приложения    
    page.add(
        #основное поле
        MAIN_RGB_TO_HEX
    )

#старт программы
ft.app(port=25565, target=main, view=ft.AppView.FLET_APP)
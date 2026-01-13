import flet as ft
import rgb_to_hex

clr = ''

def main(page: ft.Page):
    #настройка окна
    page.title = "RGB TO HEX"
    page.theme_mode = 'dark' 
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.window.width = 550
    page.window.height = 700

    #функция для перевода RGB в HEX
    def rgba1(e):
        try:
            rgbzz = rgbz.value
            hexes = str(rgb_to_hex.rgba(str(rgbzz)))
            vyvod.value = "HEX code: " + hexes
            rgbz.value = ''
            buttonrgb.disabled = True
            clean_btn.disabled = False
            copy_btn_hex.disabled = False
            if len(hexes) > 7:
                hexes = hexes[:-2]
                global clr
                clr = hexes
            page.open(ft.SnackBar(ft.Text('Color:'), bgcolor=f'{hexes}'))
            page.update()
        except:
            vyvod.value = 'Error: incorrect input'
            rgbz.value = ''
            buttonrgb.disabled = True
            clean_btn.disabled = False
            copy_btn_hex.disabled = True
            page.open(ft.SnackBar(ft.Text('Error: incorrect input'), bgcolor="#a11c1c"))
            global clr
            clr = ''
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
            copy_btn_rgb.disabled = False
            rgbzz = str('#'+str(rgbzz))
            if len(rgbzz) > 7:
                rgbzz = rgbzz[:-2]
                global clr
                clr = rgbzz
            page.open(ft.SnackBar(ft.Text('Color:'), bgcolor=rgbzz))
            page.update()
        except:
            vyvod2.value = 'Error: incorrect input'
            HEXa.value = ''
            buttonhex.disabled = True
            clean_btn.disabled = False
            copy_btn_rgb.disabled = True
            page.open(ft.SnackBar(ft.Text('Error: incorrect input'), bgcolor="#a11c1c"))
            global clr
            clr = ''
            page.update()

    #смена темы
    def theme_switch(e):
        page.theme_mode = 'light' if page.theme_mode == 'dark' else 'dark'
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
        clean_btn.disabled = True
        clean_btn_hex.disabled = True
        clean_btn_rgb.disabled = True
        copy_btn_hex.disabled = True
        copy_btn_rgb.disabled = True
        page.open(ft.SnackBar(ft.Text('All results was successfully cleared'), bgcolor='#4ab818'))
        page.update()
    
    #отчиска результата hex
    def cleanhex(e):
        vyvod.value = ''
        clean_btn_hex.disabled = True
        copy_btn_hex.disabled = True
        page.open(ft.SnackBar(ft.Text('The result was successfully cleared'), bgcolor='#4ab818'))
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
        clean_btn_rgb.disabled = True
        copy_btn_rgb.disabled = True
        page.open(ft.SnackBar(ft.Text('The result was successfully cleared'), bgcolor="#4ab818"))
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
    rgbz = ft.TextField(label='Enter the RGB (for example: 128, 128, 128, 1 or 128, 128, 128)', width=500, text_align=ft.TextAlign.CENTER, on_change=varidate_rgb, on_submit=rgba1)

    #поле ввода hex
    HEXa = ft.TextField(label='Enter the HEX (for example: 80808080 or 808080)', width=410, text_align=ft.TextAlign.CENTER, on_change=varidate_hex, on_submit=hex1)

    #кнопка конвертирования в hex
    buttonrgb = ft.ElevatedButton(text='Convert RGB to HEX', on_click=rgba1, disabled=True, on_blur=clean_btn_hex_data)

    #кнопка конвертирования в rgb
    buttonhex = ft.ElevatedButton(text='Convert HEX to RGB', on_click=hex1, disabled=True, on_blur=clean_btn_rgb_data)
    
    #вывод hex
    vyvod = ft.Text('')

    #вывод rgb
    vyvod2 = ft.Text('')

    #кнопка отчистки всех результатов
    clean_btn = ft.OutlinedButton(text='Clean all results', on_click=clean, disabled=True)

    #отчистка результата hex
    clean_btn_hex = ft.OutlinedButton(text='Clean result', style=ft.ButtonStyle(text_style=ft.TextStyle(size=10)), height=20, width=80, on_click=cleanhex, on_blur=clean_btn_data, disabled=True)

    #отчистка результата rgb
    clean_btn_rgb = ft.OutlinedButton(text='Clean result', style=ft.ButtonStyle(text_style=ft.TextStyle(size=10)), height=20, width=80, on_click=cleanrgb, on_blur=clean_btn_data, disabled=True)

    #копирование результата hex
    copy_btn_hex = ft.IconButton(icon=ft.Icons.COPY, tooltip='Copy result', on_click=copy_result_hex, disabled=True)

    #копирование результата rgb
    copy_btn_rgb = ft.IconButton(icon=ft.Icons.COPY, tooltip='Copy result', on_click=copy_result_rgb, disabled=True)
    

    #отрисовка приложения    
    page.add(
        #кнопка смены темы
        ft.Row([ft.IconButton(ft.Icons.SUNNY, on_click=theme_switch)], alignment=ft.MainAxisAlignment.END),

        
        #перевод в hex
        ft.Row([ft.Text('RGB to HEX', color="#7994eb")], alignment=ft.MainAxisAlignment.CENTER),
        ft.Row([ft.Text('Enter the RGB:')], alignment=ft.MainAxisAlignment.CENTER),
        ft.Row([rgbz], alignment=ft.MainAxisAlignment.CENTER),
        ft.Row([copy_btn_hex, buttonrgb, clean_btn_hex], alignment=ft.MainAxisAlignment.CENTER),
        ft.Row([vyvod], alignment=ft.MainAxisAlignment.CENTER),

        ft.Row([],alignment=ft.MainAxisAlignment.CENTER),
        ft.Row([],alignment=ft.MainAxisAlignment.CENTER),
        ft.Row([],alignment=ft.MainAxisAlignment.CENTER),

        #перевод в rgb
        ft.Row([ft.Text('HEX to RGB', color="#7994eb")], alignment=ft.MainAxisAlignment.CENTER),
        ft.Row([ft.Text('Enter the HEX:')], alignment=ft.MainAxisAlignment.CENTER),
        ft.Row([HEXa], alignment=ft.MainAxisAlignment.CENTER),
        ft.Row([copy_btn_rgb, buttonhex, clean_btn_rgb], alignment=ft.MainAxisAlignment.CENTER),
        ft.Row([vyvod2], alignment=ft.MainAxisAlignment.CENTER),

        ft.Row([],alignment=ft.MainAxisAlignment.CENTER),

        #кнопка отчистки всех результатов
        ft.Row([clean_btn], alignment=ft.MainAxisAlignment.END)

        
    )

#старт программы
ft.app(port=25565, target=main, view=ft.AppView.FLET_APP)
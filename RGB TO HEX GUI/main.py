import flet as f
import rgb_to_hex

def main(page: f.Page):
    page.title = "RGB TO HEX"
    page.theme_mode = 'dark' 
    page.vertical_alignment = f.MainAxisAlignment.CENTER
    page.window.width = 550
    page.window.height = 700

    #функция для перевода RGB to HEX
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
            page.open(f.SnackBar(f.Text('Color:'), bgcolor=f'{hexes}'))
            page.update()
        except:
            vyvod.value = 'Error: incorrect input'
            rgbz.value = ''
            buttonrgb.disabled = True
            clean_btn.disabled = False
            copy_btn_hex.disabled = True
            page.open(f.SnackBar(f.Text('Error: incorrect input'), bgcolor="#a11c1c"))
            page.update()

    #функция для перевода HEX to RGB
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
            page.open(f.SnackBar(f.Text('Color:'), bgcolor=rgbzz))
            page.update()
        except:
            vyvod2.value = 'Error: incorrect input'
            HEXa.value = ''
            buttonhex.disabled = True
            clean_btn.disabled = False
            copy_btn_rgb.disabled = True
            page.open(f.SnackBar(f.Text('Error: incorrect input'), bgcolor="#a11c1c"))
            page.update()

    def theme_switch(e):
        page.theme_mode = 'light' if page.theme_mode == 'dark' else 'dark'
        page.update()

    def varidate_hex(e):
        if all([HEXa.value]):
            buttonhex.disabled = False
        else:
            buttonhex.disabled = True
        page.update()
    
    def varidate_rgb(e):
        if all([rgbz.value]):
            buttonrgb.disabled = False
        else:
            buttonrgb.disabled = True
        page.update()

    def clean(e):
        vyvod.value = ''
        vyvod2.value = ''
        clean_btn.disabled = True
        clean_btn_hex.disabled = True
        clean_btn_rgb.disabled = True
        copy_btn_hex.disabled = True
        copy_btn_rgb.disabled = True
        page.open(f.SnackBar(f.Text('All results was successfully cleared'), bgcolor='#4ab818'))
        page.update()
    
    def cleanhex(e):
        vyvod.value = ''
        clean_btn_hex.disabled = True
        copy_btn_hex.disabled = True
        page.open(f.SnackBar(f.Text('The result was successfully cleared'), bgcolor='#4ab818'))
        page.update()

    def clean_btn_hex_data(e):
        if all([vyvod.value]):
            clean_btn_hex.disabled = False
        else:
            clean_btn_hex.disabled = True
        page.update()

    def cleanrgb(e):
        vyvod2.value = ''
        clean_btn_rgb.disabled = True
        copy_btn_rgb.disabled = True
        page.open(f.SnackBar(f.Text('The result was successfully cleared'), bgcolor="#4ab818"))
        page.update()

    def clean_btn_rgb_data(e):
        if all([vyvod2.value]):
            clean_btn_rgb.disabled = False
        else:
            clean_btn_rgb.disabled = True
        page.update()

    def clean_btn_data(e):
        if clean_btn_hex.disabled and clean_btn_rgb.disabled == True:
            clean_btn.disabled = True
        else:
            clean_btn.disabled = False
        page.update()

    def copy_result_hex(e):
        b = vyvod.value.replace("HEX code: ", "")
        page.set_clipboard(str(b))
        page.open(f.SnackBar(f.Text('Result is copied')))
        page.update()

    def copy_result_rgb(e):
        z = vyvod2.value.replace("RGB code: ", "")
        page.set_clipboard(str(z))
        page.open(f.SnackBar(f.Text('Result is copied')))
        page.update()


    rgbz = f.TextField(label='Enter the RGB (for example: 128, 128, 128, 1 or 128, 128, 128)', width=500, text_align=f.TextAlign.CENTER, on_change=varidate_rgb, on_submit=rgba1)
    HEXa = f.TextField(label='Enter the HEX (for example: 80808080 or 808080)', width=410, text_align=f.TextAlign.CENTER, on_change=varidate_hex, on_submit=hex1)
    buttonrgb = f.ElevatedButton(text='Convert RGB to HEX', on_click=rgba1, disabled=True, on_blur=clean_btn_hex_data)
    buttonhex = f.ElevatedButton(text='Convert HEX to RGB', on_click=hex1, disabled=True, on_blur=clean_btn_rgb_data)
    vyvod = f.Text('')
    vyvod2 = f.Text('')
    clean_btn = f.OutlinedButton(text='Clean all results', on_click=clean, disabled=True)
    clean_btn_hex = f.OutlinedButton(text='Clean result', style=f.ButtonStyle(text_style=f.TextStyle(size=10)), height=20, width=80, on_click=cleanhex, on_blur=clean_btn_data, disabled=True)
    clean_btn_rgb = f.OutlinedButton(text='Clean result', style=f.ButtonStyle(text_style=f.TextStyle(size=10)), height=20, width=80, on_click=cleanrgb, on_blur=clean_btn_data, disabled=True)
    copy_btn_hex = f.IconButton(icon=f.Icons.COPY, tooltip='Copy result', on_click=copy_result_hex, disabled=True)
    copy_btn_rgb = f.IconButton(icon=f.Icons.COPY, tooltip='Copy result', on_click=copy_result_rgb, disabled=True)
    

    
    page.add(
        f.Row([f.IconButton(f.Icons.SUNNY, on_click=theme_switch)], alignment=f.MainAxisAlignment.END),
        f.Row([f.Text('RGB to HEX', color="#7994eb")], alignment=f.MainAxisAlignment.CENTER),
        f.Row([f.Text('Enter the RGB:')], alignment=f.MainAxisAlignment.CENTER),
        f.Row([rgbz], alignment=f.MainAxisAlignment.CENTER),
        f.Row([copy_btn_hex, buttonrgb, clean_btn_hex], alignment=f.MainAxisAlignment.CENTER),
        f.Row([vyvod], alignment=f.MainAxisAlignment.CENTER),

        f.Row([],alignment=f.MainAxisAlignment.CENTER),
        f.Row([],alignment=f.MainAxisAlignment.CENTER),
        f.Row([],alignment=f.MainAxisAlignment.CENTER),

        f.Row([f.Text('HEX to RGB', color="#7994eb")], alignment=f.MainAxisAlignment.CENTER),
        f.Row([f.Text('Enter the HEX:')], alignment=f.MainAxisAlignment.CENTER),
        f.Row([HEXa], alignment=f.MainAxisAlignment.CENTER),
        f.Row([copy_btn_rgb, buttonhex, clean_btn_rgb], alignment=f.MainAxisAlignment.CENTER),
        f.Row([vyvod2], alignment=f.MainAxisAlignment.CENTER),

        f.Row([],alignment=f.MainAxisAlignment.CENTER),

        f.Row([clean_btn], alignment=f.MainAxisAlignment.END)
    )


f.app(port=25565, target=main, view=f.AppView.WEB_BROWSER)
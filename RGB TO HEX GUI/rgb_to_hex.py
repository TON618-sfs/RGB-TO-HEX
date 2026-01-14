#функция для перевода числа в от 0 до 1 из от 0 до 255
def maps(value):
    d = float(value)
    return d / 255.0

#функция для перевода числа от 0 да 255 из 0 до 1 
def mapps(value):
    d = float(value)
    return d * 255.0

#функция для деления по кол-ву символов
def splited(text, chunk_size):
    return [text[i:i + chunk_size] for i in range(0, len(text), chunk_size)]

#перевод rgb/rgba в hex
def rgba(rgb):
    r = rgb.replace(" ", ",").replace(",,", ",").split(',')     #разложение полученых данных в массив

    c = "#"+str(hex(int(r[0])).replace('0x', '').zfill(2))+str(hex(int(r[1])).replace('0x', '').zfill(2))+str(hex(int(r[2])).replace('0x', '').zfill(2))    #перевод данных в hex
    #если  с alpha каналом то
    if len(r) > 3:
        #переводим с ним
        q = int(round(mapps(float(r[3])), 0))
        return c+str(hex(q).replace('0x', '').zfill(2)) #отправляем данные
    else:
        #иначе
        return c    #отправляем данные

#переводим hex в rgb/rgba
def HEX(h):
    v = splited(h, 2)   #разделяем строку по два элемента в массив
    c = str(int(v[0], 16))+", "+str(int(v[1], 16))+", "+str(int(v[2], 16))  #переводим без alpha канала
    #если есть альфа канал переводим с ним
    if len(v) > 3:
        b = str(round(maps(int(v[3], 16)), 2))
        return c+", "+b #отправляем результат с альфа каналом
    else:
        return c    #отправляем результат без альфа канала



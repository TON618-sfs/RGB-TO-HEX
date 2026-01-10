def maps(value):
    d = float(value)
    return d / 255.0

def mapps(value):
    d = float(value)
    return d * 255.0

def splited(text, chunk_size):
    return [text[i:i + chunk_size] for i in range(0, len(text), chunk_size)]


def rgba(rgb):
    r = rgb.replace(" ", "").split(',')

    c = "#"+str(hex(int(r[0])).replace('0x', '').zfill(2))+str(hex(int(r[1])).replace('0x', '').zfill(2))+str(hex(int(r[2])).replace('0x', '').zfill(2))
    if len(r) > 3:
        q = int(round(mapps(float(r[3])), 0))
        return c+str(hex(q).replace('0x', '').zfill(2))
    else:
        return c


def HEX(h):
    v = splited(h, 2)
    c = str(int(v[0], 16))+", "+str(int(v[1], 16))+", "+str(int(v[2], 16))
    if len(v) > 3:
        b = str(round(maps(int(v[3], 16)), 2))
        return c+", "+b
    else:
        return c



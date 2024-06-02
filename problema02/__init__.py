from package.letterformat import get_fonts, fig_letter

def __init__() :
    fonts = get_fonts()
    while True : 
        font = input('Digite la fuente que desea utilizar, digite 1 si desea ver las fuentes disponibles\n -> ')
        if font == '1' :
            print(fonts)
            continue
        text = input('Digite el texto para aplicar fuente\n -> ')
        break
    res = fig_letter(text, font)
    print(res)

if __name__ == '__main__' :
    __init__()
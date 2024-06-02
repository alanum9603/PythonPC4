from pyfiglet import Figlet
import random

figlet = Figlet()

def get_fonts() : 
    fonts = figlet.getFonts()
    return fonts

def random_font() :
    fonts = get_fonts()
    index = random.randint(1, len(fonts))
    font = fonts[index]
    return font

def fig_letter(text, font) :
    err1 = ''
    err2 = ''
    try :
        figlet.setFont(font=font)
    except :
        font = random_font()
        figlet.setFont(font=font)
        err1 = 'Fuente no reconocida, se tomó una fuente aleatoria\n'  
    try : 
        res = figlet.renderText(text)
    except :
        res = figlet.renderText('Hello, World')
        err2 = 'Texto inválido, se usará una frase predeterminada\n'  
    return f'{err1}{err2}Fuente: {font}\nTexto:\n{res}'

def main() :
    print(fig_letter('Hello, World', 'tubular'))

if __name__ == '__main__' :
    main()

from PPlay.gameimage import *
from PPlay.sprite import *
from PPlay.window import*


def interface(janela, pontos, vidas, fase):
    mousee = Window.get_mouse()

    # Barra
    barra = GameImage('Interface/barra.png')
    barra.y = -2

    # Fase
    fase1 = GameImage('Interface/fase1.png')
    fase2 = GameImage('Interface/fase2.png')
    fase3 = GameImage('Interface/fase3.png')
    fase1.y = 0
    fase1.x = 20

    # Menu
    menu = Sprite('Interface/menu.png')
    menu.x = 650-(menu.width/2)
    menu.y = 12.5 - (menu.height/2)
    # Sair
    sair = Sprite('Interface/sair.png')
    sair.x = 750-(sair.width/2)
    sair.y = 12.5 - (sair.height/2)

    # Notch
    notch = GameImage('Interface/notch.png')
    notch.x = 240

    # Vidas
    vida1 = Sprite('Interface/vida1.png')
    vida2 = Sprite('Interface/vida2.png')
    vida3 = Sprite('Interface/vida1.png')
    vida4 = Sprite('Interface/vida2.png')
    vida5 = Sprite('Interface/vida1.png')
    vida6 = Sprite('Interface/vida2.png')

    vida1.y = vida2.y = vida3.y = vida4.y = vida5.y = vida6.y = 25 - vida1.height/2
    vida1.x = 317 - vida1.width
    vida2.x = 328 - vida2.width
    vida3.x = 346 - vida3.width
    vida4.x = 357 - vida4.width
    vida5.x = 375.3 - vida5.width
    vida6.x = 386.3 - vida6.width

    # Pontos
    score = Sprite('Interface/score.png')
    score.y = 25 - score.height/2
    score.x = 443 - score.width/2

    d1 = {0: Sprite("interface/0.png"), 1: Sprite("interface/1.png"), 2: Sprite("interface/2.png"), 3: Sprite("interface/3.png"), 4: Sprite("interface/4.png"), 5: Sprite("interface/5.png"), 6: Sprite("interface/6.png"), 7: Sprite("interface/7.png"), 8: Sprite("interface/8.png"), 9: Sprite("interface/9.png")}
    d2 = {0: Sprite("interface/0.png"), 1: Sprite("interface/1.png"), 2: Sprite("interface/2.png"), 3: Sprite("interface/3.png"), 4: Sprite("interface/4.png"), 5: Sprite("interface/5.png"), 6: Sprite("interface/6.png"), 7: Sprite("interface/7.png"), 8: Sprite("interface/8.png"), 9: Sprite("interface/9.png")}
    d3 = {0: Sprite("interface/0.png"), 1: Sprite("interface/1.png"), 2: Sprite("interface/2.png"), 3: Sprite("interface/3.png"), 4: Sprite("interface/4.png"), 5: Sprite("interface/5.png"), 6: Sprite("interface/6.png"), 7: Sprite("interface/7.png"), 8: Sprite("interface/8.png"), 9: Sprite("interface/9.png")}
    d4 = {0: Sprite("interface/0.png"), 1: Sprite("interface/1.png"), 2: Sprite("interface/2.png"), 3: Sprite("interface/3.png"), 4: Sprite("interface/4.png"), 5: Sprite("interface/5.png"), 6: Sprite("interface/6.png"), 7: Sprite("interface/7.png"), 8: Sprite("interface/8.png"), 9: Sprite("interface/9.png")}
    d5 = {0: Sprite("interface/0.png"), 1: Sprite("interface/1.png"), 2: Sprite("interface/2.png"), 3: Sprite("interface/3.png"), 4: Sprite("interface/4.png"), 5: Sprite("interface/5.png"), 6: Sprite("interface/6.png"), 7: Sprite("interface/7.png"), 8: Sprite("interface/8.png"), 9: Sprite("interface/9.png")}

    dig1 = (d5.get(int(pontos / 10000)))
    dig2 = (d4.get(int((pontos % 10000) / 1000)))
    dig3 = (d3.get(int((pontos % 1000) / 100)))
    dig4 = (d2.get(int((pontos % 100) / 10)))
    dig5 = (d1.get(int((pontos % 10))))

    dig1.y = dig2.y = dig3.y = dig4.y = dig5.y = 25 - dig1.height/2
    dig1.x = 482.2 - dig1.width/2
    dig2.x = 494.1 - dig2.width/2
    dig3.x = 505.3 - dig3.width/2
    dig4.x = 516.5 - dig4.width/2
    dig5.x = 527.7 - dig5.width/2

    barra.draw()
    notch.draw()

    menu.draw()
    sair.draw()
    dig1.draw()
    dig2.draw()
    dig3.draw()
    dig4.draw()
    dig5.draw()
    score.draw()

    # Fase
    if fase == 1:
        fase1.draw()
    elif fase == 2:
        fase2.draw()
    elif fase == 3:
        fase3.draw()

    # Vidas
    if vidas == 6:
        vida1.draw()
        vida2.draw()
        vida3.draw()
        vida4.draw()
        vida5.draw()
        vida6.draw()
    elif vidas == 5:
        vida1.draw()
        vida2.draw()
        vida3.draw()
        vida4.draw()
        vida5.draw()
    elif vidas == 4:
        vida1.draw()
        vida2.draw()
        vida3.draw()
        vida4.draw()
    if vidas == 3:
        vida1.draw()
        vida2.draw()
        vida3.draw()
    elif vidas == 2:
        vida1.draw()
        vida2.draw()
    elif vidas == 1:
        vida1.draw()

    if mousee.is_button_pressed(1):
        if mousee.is_over_object(menu):
            return 5
        if mousee.is_over_object(sair):
            janela.close()

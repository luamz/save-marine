from PPlay.gameimage import *
from PPlay.sprite import *
from PPlay.sound import*


def menu(janela):
    mouse = janela.get_mouse()

    jogar = Sprite('Menu/play.png')
    fase = Sprite('Menu/fases.png')
    manual = Sprite('Menu/manual.png')
    sair = Sprite('Menu/sair.png')
    fundo = GameImage('Menu/bg_menu.png')

    jogar.x = manual.x = fase.x = sair.x = 405 - jogar.width / 2
    jogar.y, manual.y, fase.y, sair.y = 335, 385, 435, 485

    som = Sound("Sons/be2.ogg")
    som2 = Sound("Sons/som_menu.ogg")
    som.set_volume(5)
    som2.set_volume(10)

    pressionado = True
    while True:
        som.play()
        som2.play()
        som.set_repeat(True)
        som2.set_repeat(True)
        if mouse.is_button_pressed(1) is False:
            pressionado = False
        if pressionado is False:
            if mouse.is_over_object(jogar) and mouse.is_button_pressed(1):
                som.stop()
                som2.stop()
                return 1
            if mouse.is_over_object(fase) and mouse.is_button_pressed(1):
                time_ms = 10000
                som.fadeout(time_ms)
                som2.fadeout(time_ms)
                return 4
            if mouse.is_over_object(manual) and mouse.is_button_pressed(1):
                time_ms = 10000
                som.fadeout(time_ms)
                som2.fadeout(time_ms)
                return 5
            if mouse.is_over_object(sair) and mouse.is_button_pressed(1):
                som.stop()
                som2.stop()
                return 10
            fundo.draw()
            jogar.draw()
            manual.draw()
            fase.draw()
            sair.draw()
        janela.update()


def sel_fase(janela):
    mouse = janela.get_mouse()
    fase1 = Sprite('Menu/1.png')
    fase2 = Sprite('Menu/2.png')
    fase3 = Sprite('Menu/3.png')
    fundo = GameImage('Menu/bg_menu.png')
    sair = Sprite('Menu/voltar.png')

    fase1.x = fase2.x = fase3.x = sair.x = 405 - fase1.width / 2
    fase1.y, fase2.y, fase3.y, sair.y = 335, 385, 435, 485

    pressionado = True
    while True:
        if mouse.is_button_pressed(1) is False:
            pressionado = False
        if pressionado is False:
            if mouse.is_over_object(sair) and mouse.is_button_pressed(1):
                return 0
            if mouse.is_over_object(fase1) and mouse.is_button_pressed(1):

                return 1
            if mouse.is_over_object(fase2) and mouse.is_button_pressed(1):

                return 2
            if mouse.is_over_object(fase3) and mouse.is_button_pressed(1):

                return 3
            fundo.draw()
            fase1.draw()
            fase2.draw()
            fase3.draw()
            sair.draw()
        janela.update()


def derrota(janela):
    mouse = janela.get_mouse()

    jogar = Sprite('Menu/replay.png')
    sair = Sprite('Menu/sair.png')
    fundo = GameImage('Menu/derrota.png')

    jogar.y = sair.y = 500 - jogar.height / 2
    jogar.x = 290 - jogar.width/2
    sair.x = 510 - sair.width/2

    som = Sound("Sons/be2.ogg")
    som2 = Sound("Sons/som_menu.ogg")
    som.set_volume(5)
    som2.set_volume(10)

    pressionado = True
    while True:
        som.play()
        som2.play()
        som.set_repeat(True)
        som2.set_repeat(True)
        if mouse.is_button_pressed(1) is False:
            pressionado = False
        if pressionado is False:
            if mouse.is_over_object(jogar) and mouse.is_button_pressed(1):
                som.stop()
                som2.stop()
                return 0
            if mouse.is_over_object(sair) and mouse.is_button_pressed(1):
                som.stop()
                som2.stop()
                return 10
            fundo.draw()
            jogar.draw()
            sair.draw()
        janela.update()


def passa_fase1(janela):
    teclado = janela.get_keyboard()
    fundo = GameImage('Menu/passa_fase1.png')
    while True:
        if teclado.key_pressed('space') is True:
            return 2
        fundo.draw()
        janela.update()


def passa_fase2(janela):
    teclado = janela.get_keyboard()
    fundo = GameImage('Menu/passa_fase2.png')
    while True:
        if teclado.key_pressed('space') is True:
            return 3
        fundo.draw()
        janela.update()


def vitoria(janela):
    mouse = janela.get_mouse()

    jogar = Sprite('Menu/replay.png')
    sair = Sprite('Menu/sair.png')
    fundo = GameImage('Menu/vitoria.png')

    jogar.y = sair.y = 500 - jogar.height / 2
    jogar.x = 290 - jogar.width/2
    sair.x = 510 - sair.width/2

    som = Sound("Sons/be2.ogg")
    som2 = Sound("Sons/som_menu.ogg")
    som.set_volume(5)
    som2.set_volume(10)

    pressionado = True
    while True:
        som.play()
        som2.play()
        som.set_repeat(True)
        som2.set_repeat(True)
        if mouse.is_button_pressed(1) is False:
            pressionado = False
        if pressionado is False:
            if mouse.is_over_object(jogar) and mouse.is_button_pressed(1):
                som.stop()
                som2.stop()
                return 0

            if mouse.is_over_object(sair) and mouse.is_button_pressed(1):
                som.stop()
                som2.stop()
                return 10
            fundo.draw()
            jogar.draw()
            sair.draw()
        janela.update()


def manual(janela):
    mouse = janela.get_mouse()

    jogar = Sprite('Menu/play.png')
    sair = Sprite('Menu/voltar.png')
    fundo = GameImage('Menu/bg_manual.png')

    jogar.y, sair.y = 450, 500
    jogar.x = 250 - jogar.width/2
    sair.x = 250 - sair.width/2

    som = Sound("Sons/be2.ogg")
    som2 = Sound("Sons/som_menu.ogg")
    som.set_volume(5)
    som2.set_volume(10)

    pressionado = True
    while True:
        som.play()
        som2.play()
        som.set_repeat(True)
        som2.set_repeat(True)
        if mouse.is_button_pressed(1) is False:
            pressionado = False
        if pressionado is False:
            if mouse.is_over_object(jogar) and mouse.is_button_pressed(1):
                som.stop()
                som2.stop()
                return 1

            if mouse.is_over_object(sair) and mouse.is_button_pressed(1):
                som.stop()
                som2.stop()
                return 0
            fundo.draw()
            jogar.draw()
            sair.draw()
        janela.update()

from PPlay.gameimage import *
from PPlay.sprite import *
import funcs as func
import interface as inter
import random
from PPlay.sound import*

pontos = 0


def fase1(janela):
    # Teclado
    teclado = janela.get_keyboard()

    # Vetor para obstáculos
    obst = []
    # Vetor para animais
    pex = []
    # Vetor para recolhíveis
    rec = []
    # Vetor para algas e corais
    obj = []
    # Vetor de spawns de peixes
    spawns1 = [1, 2, 5, 6, 8, 9]
    # Vetor de spawns de rochas
    spawns2 = [1, 2, 4]

    # Submarino
    sub = Sprite("Objetos/Submarino.png")
    sub.x, sub.y = 0, (janela.height / 2) - (sub.height / 2)
    imune = Sprite('Objetos/animacaosub.png', 9)
    imune.set_total_duration(3000)
    imune.x, imune.y = 0, (janela.height / 2) - (sub.height / 2)

    # Fundos
    fundo1 = GameImage('Fundos/bg_fase1.png')
    fundo2 = GameImage('Fundos/bg_fase1.png')

    # Sons
    som = Sound("Sons/vitoria.ogg")
    som.set_volume(10)

    # Velocidades
    velspaw = velcolid = 4
    velscroll = 280
    velsub = 300

    global pontos
    vida = 6
    direc = direc2 = 1
    while True:
        # Scroll
        func.scroll(fundo1, fundo2, velscroll, janela)

        # Spawns
        if velspaw >= 2:
            velspaw = 0
            func.obst_spawn(spawns2[random.randint(0, 2)], janela, obst)
            func.pex_spawn(spawns1[random.randint(0, 5)], janela, pex)
            func.rec_spawn(random.randint(1, 18), janela, rec)
            func.obj_spawn(random.randint(1, 8), janela, obj)
        velspaw += janela.delta_time()

        # Submarino
        if 0 <= velcolid < 3:
            imune.x, imune.y = sub.x, sub.y
            imune.update()
            imune.draw()
        else:
            sub.draw()

        # Movimentos
        valor = func.rec_move(rec, velscroll, janela, direc2)
        if type(valor) == int:
            direc2 = valor
        func.obts_move(janela, velscroll, obst)
        valor = func.pex_move(janela, velscroll, pex, direc)
        if type(valor) == int:
            direc = valor
        func.obj_move(janela, velscroll, obj)
        func.sub_move(janela, sub, velsub)

        # Pontos
        conta = func.coleta(rec, sub)
        if type(conta) == int:
            pontos += conta

        #  Vidas
        if vida <= 0:
            return 6
        if velcolid >= 3:
            conta = func.colisao(obst, pex, sub)
            if type(conta) == int:
                if conta == 1:
                    vida -= 1
                    velcolid = 0
                else:
                    vida -= 2
                    velcolid = 0
        velcolid += janela.delta_time()

        # Direciona pro menu
        dic = inter.interface(janela, pontos, vida, 1)
        if teclado.key_pressed("esc") or dic == 5:
            pontos = 0
            return 0

        # Direciona pra fase 2
        if vida > 0 and pontos >= 900:
            som.play()
            return 7

        janela.update()


def fase2(janela):
    global pontos
    # Teclado
    teclado = janela.get_keyboard()

    # Vetor para obstáculos
    obst = []
    # Vetor para animais
    pex = []
    # Vetor para recolhíveis
    rec = []
    # Vetor para algas e corais
    obj = []
    # Vetor de spawns de peixes
    spawns1 = [3, 4, 7, 9, 11, 13, 15]
    # Vetor de spawns de rochas
    spawns2 = [1, 2, 4, 5, 6]

    # Submarino
    sub = Sprite("Objetos/Submarino.png")
    sub.x, sub.y = 0, (janela.height / 2) - (sub.height / 2)
    imune = Sprite('Objetos/animacaosub.png', 9)
    imune.set_total_duration(3000)
    imune.x, imune.y = 0, (janela.height / 2) - (sub.height / 2)

    # Fundos
    fundo1 = GameImage('Fundos/bg_fase2.png')
    fundo2 = GameImage('Fundos/bg_fase2.png')

    # Sons
    som = Sound("Sons/vitoria.ogg")
    som.set_volume(10)

    # Velocidades
    velspaw = velcolid = 3.5
    velscroll = 290
    velsub = 250

    global pontos
    vida = 6
    direc = direc2 = 1
    while True:
        # Scroll
        func.scroll(fundo1, fundo2, velscroll, janela)

        # Spawns
        if velspaw >= 2:
            velspaw = 0
            func.obst_spawn(spawns2[random.randint(0, 4)], janela, obst)
            func.pex_spawn(spawns1[random.randint(0, 6)], janela, pex)
            func.rec_spawn(random.randint(1, 18), janela, rec)
            func.obj_spawn(random.randint(1, 8), janela, obj)
        velspaw += janela.delta_time()

        # Submarino
        if 0 <= velcolid < 3:
            imune.x, imune.y = sub.x, sub.y
            imune.update()
            imune.draw()
        else:
            sub.draw()

        # Movimentos
        valor = func.rec_move(rec, velscroll, janela, direc2)
        if type(valor) == int:
            direc2 = valor
        func.obts_move(janela, velscroll, obst)
        valor = func.pex_move(janela, velscroll, pex, direc)
        if type(valor) == int:
            direc = valor
        func.obj_move(janela, velscroll, obj)
        func.sub_move(janela, sub, velsub)

        # Pontos
        conta = func.coleta(rec, sub)
        if type(conta) == int:
            pontos += conta

        #  Vidas
        if vida <= 0:
            return 6
        if velcolid >= 3:
            conta = func.colisao(obst, pex, sub)
            if type(conta) == int:
                if conta == 1:
                    vida -= 1
                    velcolid = 0
                else:
                    vida -= 2
                    velcolid = 0
        velcolid += janela.delta_time()

        # Direciona pro menu
        dic = inter.interface(janela, pontos, vida, 2)
        if teclado.key_pressed("esc") or dic == 5:
            pontos = 0
            return 0

        # Direciona pra fase 3
        if vida > 0 and pontos >= 1500:
            som.play()
            return 8

        janela.update()


def fase3(janela):
    global pontos
    # Teclado
    teclado = janela.get_keyboard()

    # Vetor para obstáculos
    obst = []
    # Vetor para animais
    pex = []
    # Vetor para recolhíveis
    rec = []
    # Vetor para algas e corais
    obj = []
    # Vetor de spawns de peixes
    spawns1 = [2, 3, 6, 10, 12, 13, 14, 15, 16]
    # Vetor de spawns de rochas
    spawns2 = [1, 2, 3, 5, 6, 7]

    # Submarino
    sub = Sprite("Objetos/Submarino.png")
    sub.x, sub.y = 0, (janela.height / 2) - (sub.height / 2)
    imune = Sprite('Objetos/animacaosub.png', 9)
    imune.set_total_duration(3000)
    imune.x, imune.y = 0, (janela.height / 2) - (sub.height / 2)

    # Fundos
    fundo1 = GameImage('Fundos/bg_fase3.png')
    fundo2 = GameImage('Fundos/bg_fase3.png')

    # Sons
    som = Sound("Sons/vitoria.ogg")
    som.set_volume(10)

    # Velocidades
    velspaw = velcolid = 3
    velscroll = 400
    velsub = 300

    global pontos
    vida = 6
    direc = direc2 = 1
    while True:
        # Scroll
        func.scroll(fundo1, fundo2, velscroll, janela)

        # Spawns
        if velspaw >= 2:
            velspaw = 0
            func.obst_spawn(spawns2[random.randint(0, 5)], janela, obst)
            func.pex_spawn(spawns1[random.randint(0, 8)], janela, pex)
            func.rec_spawn(random.randint(1, 18), janela, rec)
            func.obj_spawn(random.randint(1, 8), janela, obj)
        velspaw += janela.delta_time()

        # Submarino
        if 0 <= velcolid < 3:
            imune.x, imune.y = sub.x, sub.y
            imune.update()
            imune.draw()
        else:
            sub.draw()

        # Movimentos
        valor = func.rec_move(rec, velscroll, janela, direc2)
        if type(valor) == int:
            direc2 = valor
        func.obts_move(janela, velscroll, obst)
        valor = func.pex_move(janela, velscroll, pex, direc)
        if type(valor) == int:
            direc = valor
        func.obj_move(janela, velscroll, obj)
        func.sub_move(janela, sub, velsub)

        # Pontos
        conta = func.coleta(rec, sub)
        if type(conta) == int:
            pontos += conta

        #  Vidas
        if vida <= 0:
            pontos = 0
            return 6
        if velcolid >= 3:
            conta = func.colisao(obst, pex, sub)
            if type(conta) == int:
                if conta == 1:
                    vida -= 1
                    velcolid = 0
                else:
                    vida -= 2
                    velcolid = 0
        velcolid += janela.delta_time()

        # Direciona pro menu
        dic = inter.interface(janela, pontos, vida, 3)
        if teclado.key_pressed("esc") or dic == 5:
            pontos = 0
            return 0

        # Direciona pro fim
        if vida > 0 and pontos >= 2500:
            pontos = 0
            som.play()
            return 9

        janela.update()

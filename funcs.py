from PPlay.sprite import *
import random
from PPlay.sound import*

# Sons
som1 = Sound("Sons/coleta.ogg")
som1.set_volume(10)
som2 = Sound("Sons/choque.ogg")
som2.set_volume(10)


def scroll(bg_right, bg_left, roll_speed, janela):

    # Movimenta o fundo horizontalmente
    bg_left.x -= roll_speed * janela.delta_time()
    bg_right.x -= roll_speed * janela.delta_time()

    # Se a primeira imagem já tiver sido completamente exibida,
    # retorna ambas imagens às suas posições iniciais
    if bg_left.x >= 0:
        bg_right.x = 800
        bg_left.x = 0

    # Conserto do erro do fundo borrado
    if bg_right.x <= 0:
        bg_left.x = 800

    # Draws
    bg_left.draw()
    bg_right.draw()


def rocha_baixo_spawn(vet, janela):
    altura = 600
    inc = random.uniform(0, janela.width - 1)+janela.width
    rocha1 = Sprite("Objetos/Obstáculos/Rochas/Rocha1/Rocha1.png")
    rocha1.x, rocha1.y = 0 + inc, altura - rocha1.height
    vet.append(rocha1)

    rocha2 = Sprite("Objetos/Obstáculos/Rochas/Rocha1/Rocha2.png")
    rocha2.x, rocha2.y = 24+inc, altura - rocha2.height
    rocha2.draw()
    vet.append(rocha2)

    rocha3 = Sprite("Objetos/Obstáculos/Rochas/Rocha1/Rocha3.png")
    rocha3.x, rocha3.y = 59+inc, altura - rocha3.height
    rocha3.draw()
    vet.append(rocha3)

    rocha4 = Sprite("Objetos/Obstáculos/Rochas/Rocha1/Rocha4.png")
    rocha4.x, rocha4.y = 101+inc, altura - rocha4.height
    rocha4.draw()
    vet.append(rocha4)

    rocha5 = Sprite("Objetos/Obstáculos/Rochas/Rocha1/Rocha5.png")
    rocha5.x, rocha5.y = 145+inc, altura - rocha5.height
    rocha5.draw()
    vet.append(rocha5)

    rocha6 = Sprite("Objetos/Obstáculos/Rochas/Rocha1/Rocha6.png")
    rocha6.x, rocha6.y = 164+inc, altura - rocha6.height
    rocha6.draw()
    vet.append(rocha6)

    rocha7 = Sprite("Objetos/Obstáculos/Rochas/Rocha1/Rocha7.png")
    rocha7.x, rocha7.y = 245+inc, altura - rocha7.height
    rocha7.draw()
    vet.append(rocha7)

    rocha8 = Sprite("Objetos/Obstáculos/Rochas/Rocha1/Rocha8.png")
    rocha8.x, rocha8.y = 274+inc, altura - rocha8.height
    rocha8.draw()
    vet.append(rocha8)

    rocha9 = Sprite("Objetos/Obstáculos/Rochas/Rocha1/Rocha9.png")
    rocha9.x, rocha9.y = 322+inc, altura - rocha9.height
    rocha9.draw()
    vet.append(rocha9)

    rocha10 = Sprite("Objetos/Obstáculos/Rochas/Rocha1/Rocha10.png")
    rocha10.x, rocha10.y = 342+inc, altura - rocha10.height
    rocha10.draw()
    vet.append(rocha10)


def rocha_cima_spawn(vet, janela):
    altura = 0
    inc = random.uniform(0, janela.width - 1)+janela.width

    rocha1 = Sprite("Objetos/Obstáculos/Rochas/Rocha1/Rocha-1.png")
    rocha1.x, rocha1.y = 0+inc, altura
    vet.append(rocha1)

    rocha2 = Sprite("Objetos/Obstáculos/Rochas/Rocha1/Rocha-2.png")
    rocha2.x, rocha2.y = 24+inc, altura
    vet.append(rocha2)

    rocha3 = Sprite("Objetos/Obstáculos/Rochas/Rocha1/Rocha-3.png")
    rocha3.x, rocha3.y = 59+inc, altura
    vet.append(rocha3)

    rocha4 = Sprite("Objetos/Obstáculos/Rochas/Rocha1/Rocha-4.png")
    rocha4.x, rocha4.y = 101+inc, altura
    vet.append(rocha4)

    rocha5 = Sprite("Objetos/Obstáculos/Rochas/Rocha1/Rocha-5.png")
    rocha5.x, rocha5.y = 145+inc, altura
    vet.append(rocha5)

    rocha6 = Sprite("Objetos/Obstáculos/Rochas/Rocha1/Rocha-6.png")
    rocha6.x, rocha6.y = 164+inc, altura
    vet.append(rocha6)

    rocha7 = Sprite("Objetos/Obstáculos/Rochas/Rocha1/Rocha-7.png")
    rocha7.x, rocha7.y = 245+inc, altura
    vet.append(rocha7)

    rocha8 = Sprite("Objetos/Obstáculos/Rochas/Rocha1/Rocha-8.png")
    rocha8.x, rocha8.y = 274+inc, altura
    vet.append(rocha8)

    rocha9 = Sprite("Objetos/Obstáculos/Rochas/Rocha1/Rocha-9.png")
    rocha9.x, rocha9.y = 322+inc, altura
    vet.append(rocha9)

    rocha10 = Sprite("Objetos/Obstáculos/Rochas/Rocha1/Rocha-10.png")
    rocha10.x, rocha10.y = 342+inc, altura
    vet.append(rocha10)


# Instancia obstáculos
def obst_spawn(num, janela, vet):
    # Cria Rocha1 em baixo
    if num == 1:
        rocha_baixo_spawn(vet, janela)

    # Cria Rocha1 em cima
    if num == 2:
        rocha_cima_spawn(vet, janela)

    # Cria Rocha2 em baixo
    if num == 3:
        ob = Sprite('Objetos/Obstáculos/Rochas/Rocha2.png')
        ob.set_position(random.randint(0, janela.width - 1)+janela.width, janela.height - ob.height)
        vet.append(ob)

    # Cria Rocha3 em baixo
    if num == 4:
        ob = Sprite('Objetos/Obstáculos/Rochas/Rocha3.png')
        ob.set_position(random.randint(0, janela.width - 1)+janela.width, janela.height - ob.height)
        vet.append(ob)

    # Cria Rocha4 em cima
    if num == 5:
        ob = Sprite('Objetos/Obstáculos/Rochas/Rocha4.png')
        ob.set_position(random.randint(0, janela.width - 1)+janela.width, 0)
        vet.append(ob)

    # Cria Navio1 em baixo
    if num == 6:
        ob = Sprite('Objetos/Obstáculos/Barcos-afundados/Navio1.png', dan=1)
        ob.set_position(random.randint(0, janela.width - 1) + janela.width, janela.height - ob.height)
        vet.append(ob)

    # Cria Navio2 em baixo
    if num == 7:
        ob = Sprite('Objetos/Obstáculos/Barcos-afundados/Navio2.png', dan=1)
        ob.set_position(random.randint(0, janela.width - 1) + janela.width, janela.height - ob.height)
        vet.append(ob)


# Movimento dos obstáculos
def obts_move(janela, velscroll, vet):
    for ob in vet:
        ob.x -= velscroll*janela.delta_time()
        ob.draw()
        if ob.x <= ob.x-ob.width/2:
            vet.remove(ob)


# Instancia animais
def pex_spawn(num, janela, vet):
    # Cria Peixe1
    if num == 1:
        ob = Sprite('Objetos/Obstáculos/Animais/Peixe1.png')
        ob.set_position(janela.width+ob.width, random.randint(int(ob.height/2)+150, int(janela.height-ob.height/2)-150))
        vet.append(ob)

    # Cria Peixe2
    if num == 2:
        ob = Sprite('Objetos/Obstáculos/Animais/Peixe2.png', mov=1)
        ob.set_position(janela.width+ob.width, random.randint(int(ob.height/2)+150, int(janela.height-ob.height/2)-150))
        vet.append(ob)

    # Cria Peixe3
    if num == 3:
        ob = Sprite('Objetos/Obstáculos/Animais/Peixe3.png')
        ob.set_position(janela.width+ob.width, random.randint(int(ob.height/2)+150, int(janela.height-ob.height/2)-150))
        vet.append(ob)

    # Cria Peixe4
    if num == 4:
        ob = Sprite('Objetos/Obstáculos/Animais/Peixe4.png')
        ob.set_position(janela.width+ob.width, random.randint(int(ob.height/2)+150, int(janela.height-ob.height/2)-150))
        vet.append(ob)

    # Cria Peixe5
    if num == 5:
        ob = Sprite('Objetos/Obstáculos/Animais/Peixe5.png', mov=1)
        ob.set_position(janela.width+ob.width, random.randint(int(ob.height/2)+150, int(janela.height-ob.height/2)-150))
        vet.append(ob)

    # Cria Cardume1
    if num == 6:
        ob = Sprite('Objetos/Obstáculos/Animais/Cardume1.png')
        ob.set_position(janela.width+ob.width, random.randint(int(ob.height/2)+150, int(janela.height-ob.height/2)-150))
        vet.append(ob)

    # Cria Cardume2
    if num == 7:
        ob = Sprite('Objetos/Obstáculos/Animais/Cardume2.png')
        ob.set_position(janela.width+ob.width, random.randint(int(ob.height/2)+150, int(janela.height-ob.height/2)-150))
        vet.append(ob)

    # Cria Cavalo-marinho
    if num == 8:
        ob = Sprite('Objetos/Obstáculos/Animais/Cavalo-marinho.png', mov=1)
        ob.set_position(janela.width+ob.width, random.randint(int(ob.height/2)+150, int(janela.height-ob.height/2)-150))
        vet.append(ob)

    # Cria Estrela-do-mar1
    if num == 9:
        ob = Sprite('Objetos/Obstáculos/Animais/Estrela-do-mar1.png')
        ob.set_position(janela.width+ob.width, random.randint(int(ob.height/2)+150, int(janela.height-ob.height/2)-150))
        vet.append(ob)

    # Cria Estrela-do-mar2
    if num == 10:
        ob = Sprite('Objetos/Obstáculos/Animais/Estrela-do-mar2.png', mov=1)
        ob.set_position(janela.width+ob.width, random.randint(int(ob.height/2)+150, int(janela.height-ob.height/2)-150))
        vet.append(ob)

    # Cria Tartaruga1
    if num == 11:
        ob = Sprite('Objetos/Obstáculos/Animais/Tartaruga1.png', mov=1, dan=1)
        ob.set_position(janela.width+ob.width, random.randint(int(ob.height/2)+150, int(janela.height-ob.height/2)-150))
        vet.append(ob)

    # Cria Tartaruga2
    if num == 12:
        ob = Sprite('Objetos/Obstáculos/Animais/Tartaruga2.png', mov=1, dan=1)
        ob.set_position(janela.width+ob.width, random.randint(int(ob.height/2)+150, int(janela.height-ob.height/2)-150))
        vet.append(ob)

    # Cria Golfinho
    if num == 13:
        ob = Sprite('Objetos/Obstáculos/Animais/Golfinho.png', dan=1)
        ob.set_position(janela.width+ob.width, random.randint(int(ob.height/2)+150, int(janela.height-ob.height/2)-150))
        vet.append(ob)

    # Cria Baleia
    if num == 14:
        ob = Sprite('Objetos/Obstáculos/Animais/Baleia.png', mov=1, dan=1)
        ob.set_position(janela.width+ob.width, random.randint(int(ob.height/2)+150, int(janela.height-ob.height/2)-150))
        vet.append(ob)

    # Cria Tubarão1
    if num == 15:
        ob = Sprite('Objetos/Obstáculos/Animais/Tubarão1.png', dan=1)
        ob.set_position(janela.width+ob.width, random.randint(int(ob.height/2)+150, int(janela.height-ob.height/2)-150))
        vet.append(ob)

    # Cria Tubarão2
    if num == 16:
        ob = Sprite('Objetos/Obstáculos/Animais/Tubarão2.png', dan=1)
        ob.set_position(janela.width+ob.width, random.randint(int(ob.height/2)+150, int(janela.height-ob.height/2)-150))
        vet.append(ob)


# Movimento dos animais
def pex_move(janela, velscroll, vet, direc):
    for ob in vet:
        ob.x -= velscroll * janela.delta_time()*1.5
        if ob.get_move() == 1:
            ob.y += (velscroll-100)*janela.delta_time()*direc
            if ob.y <= ob.height/2 or ob.y >= 600-ob.height/2:
                return direc*-1
        if ob.x <= -ob.width/2:
            vet.remove(ob)
        ob.draw()


# Instancia recolhiveis
def rec_spawn(num, janela, vet):
    # Cria Canudo
    if num == 1:
        ob = Sprite('Objetos/Recolhíveis/Lixo/Canudo.png', pts=150)
        ob.set_position(janela.width + ob.width, random.randint(int(ob.height / 2), int(janela.height - ob.height / 2)))
        vet.append(ob)

    # Cria Garrafa1.1
    if num == 2:
        ob = Sprite('Objetos/Recolhíveis/Lixo/Garrafa1.1.png', pts=50)
        ob.set_position(janela.width + ob.width, random.randint(int(ob.height / 2), int(janela.height - ob.height / 2)))
        vet.append(ob)

    # Cria Garrafa1.2
    if num == 3:
        ob = Sprite('Objetos/Recolhíveis/Lixo/Garrafa1.2.png', pts=50)
        ob.set_position(janela.width + ob.width, random.randint(int(ob.height / 2), int(janela.height - ob.height / 2)))
        vet.append(ob)

    # Cria Garrafa2
    if num == 4:
        ob = Sprite('Objetos/Recolhíveis/Lixo/Garrafa2.png', mov=1, pts=50)
        ob.set_position(janela.width + ob.width, random.randint(int(ob.height / 2), int(janela.height - ob.height / 2)))
        vet.append(ob)

    # Cria Graveto1
    if num == 5:
        ob = Sprite('Objetos/Recolhíveis/Lixo/Graveto1.png', mov=1, pts=50)
        ob.set_position(janela.width + ob.width, random.randint(int(ob.height / 2), int(janela.height - ob.height / 2)))
        vet.append(ob)

    # Cria Graveto2
    if num == 6:
        ob = Sprite('Objetos/Recolhíveis/Lixo/Graveto2.png', mov=1, pts=50)
        ob.set_position(janela.width + ob.width, random.randint(int(ob.height / 2), int(janela.height - ob.height / 2)))
        vet.append(ob)

    # Cria Graveto3
    if num == 7:
        ob = Sprite('Objetos/Recolhíveis/Lixo/Graveto3.png', pts=100)
        ob.set_position(janela.width + ob.width, random.randint(int(ob.height / 2), int(janela.height - ob.height / 2)))
        vet.append(ob)

    # Cria Lata1.1
    if num == 8:
        ob = Sprite('Objetos/Recolhíveis/Lixo/Lata1.1.png', pts=100)
        ob.set_position(janela.width + ob.width, random.randint(int(ob.height / 2), int(janela.height - ob.height / 2)))
        vet.append(ob)

    # Cria Lata1.2
    if num == 9:
        ob = Sprite('Objetos/Recolhíveis/Lixo/Lata1.2.png', pts=100)
        ob.set_position(janela.width + ob.width, random.randint(int(ob.height / 2), int(janela.height - ob.height / 2)))
        vet.append(ob)

    # Cria Lata2
    if num == 10:
        ob = Sprite('Objetos/Recolhíveis/Lixo/Lata2.png', mov=1, pts=100)
        ob.set_position(janela.width + ob.width, random.randint(int(ob.height / 2), int(janela.height - ob.height / 2)))
        vet.append(ob)

    # Cria Saco1
    if num == 11:
        ob = Sprite('Objetos/Recolhíveis/Lixo/Saco1.png', mov=1, pts=150)
        ob.set_position(janela.width + ob.width, random.randint(int(ob.height / 2), int(janela.height - ob.height / 2)))
        vet.append(ob)

    # Cria Saco2
    if num == 12:
        ob = Sprite('Objetos/Recolhíveis/Lixo/Saco2.png', mov=1, pts=150)
        ob.set_position(janela.width + ob.width, random.randint(int(ob.height / 2), int(janela.height - ob.height / 2)))
        vet.append(ob)

    # Cria Saco3
    if num == 13:
        ob = Sprite('Objetos/Recolhíveis/Lixo/Saco3.png', mov=1, pts=150)
        ob.set_position(janela.width + ob.width, random.randint(int(ob.height / 2), int(janela.height - ob.height / 2)))
        vet.append(ob)

    # Cria Saco4
    if num == 14:
        ob = Sprite('Objetos/Recolhíveis/Lixo/Saco4.png', mov=1, pts=150)
        ob.set_position(janela.width + ob.width, random.randint(int(ob.height / 2), int(janela.height - ob.height / 2)))
        vet.append(ob)

    # Cria TV
    if num == 15:
        ob = Sprite('Objetos/Recolhíveis/Lixo/TV.png', pts=200)
        ob.set_position(janela.width + ob.width, random.randint(int(ob.height / 2), int(janela.height - ob.height / 2)))
        vet.append(ob)

    # Cria Concha1
    if num == 16:
        ob = Sprite('Objetos/Recolhíveis/Conchas/Concha1.png', mov=1, pts=400)
        ob.set_position(janela.width + ob.width, random.randint(int(ob.height / 2), int(janela.height - ob.height / 2)))
        vet.append(ob)

    # Cria Concha2
    if num == 17:
        ob = Sprite('Objetos/Recolhíveis/Conchas/Concha2.png', pts=350)
        ob.set_position(janela.width + ob.width,
                        random.randint(int(ob.height / 2), int(janela.height - ob.height / 2)))
        vet.append(ob)

    # Cria Concha3
    if num == 18:
        ob = Sprite('Objetos/Recolhíveis/Conchas/Concha3.png', pts=300)
        ob.set_position(janela.width + ob.width,
                        random.randint(int(ob.height / 2), int(janela.height - ob.height / 2)))
        vet.append(ob)


# Movimento dos materiais recolhiveis
def rec_move(vet, velscroll, janela, direc):
    for ob in vet:
        ob.x -= velscroll*janela.delta_time()*2
        if ob.get_move() == 1:
            ob.y += (velscroll-100)*janela.delta_time()*direc
            if ob.y <= ob.height/2 or ob.y >= 600-ob.height/2:
                return direc*-1
        ob.draw()
        if ob.x <= -ob.width/2:
            vet.remove(ob)


# Instancia vegetação
def obj_spawn(num, janela, vet):
    # Cria Alga1.1
    if num == 1:
        ob = Sprite('Objetos/Obstáculos/Vegetação/Alga1.1.png')
        ob.set_position(random.uniform(0, janela.width - 1) + janela.width, janela.height - ob.height)
        vet.append(ob)

    # Cria Alga1.2
    if num == 1:
        ob = Sprite('Objetos/Obstáculos/Vegetação/Alga1.2.png')
        ob.set_position(random.randint(0, janela.width - 1) + janela.width, 0)
        vet.append(ob)

    # Cria Alga2
    if num == 3:
        ob = Sprite('Objetos/Obstáculos/Vegetação/Alga2.png')
        ob.set_position(random.uniform(0, janela.width - 1) + janela.width, janela.height - ob.height)
        vet.append(ob)

    # Cria Alga3
    if num == 4:
        ob = Sprite('Objetos/Obstáculos/Vegetação/Alga3.png')
        ob.set_position(random.uniform(0, janela.width - 1) + janela.width, janela.height - ob.height)
        vet.append(ob)

    # Cria Alga4
    if num == 5:
        ob = Sprite('Objetos/Obstáculos/Vegetação/Alga4.png')
        ob.set_position(random.uniform(0, janela.width - 1) + janela.width, janela.height - ob.height)
        vet.append(ob)

    # Cria Coral1
    if num == 6:
        ob = Sprite('Objetos/Obstáculos/Vegetação/Coral1.png')
        ob.set_position(random.uniform(0, janela.width - 1) + janela.width, janela.height - ob.height)
        vet.append(ob)

    # Cria Coral2
    if num == 7:
        ob = Sprite('Objetos/Obstáculos/Vegetação/Coral2.png')
        ob.set_position(random.uniform(0, janela.width - 1) + janela.width, janela.height - ob.height)
        vet.append(ob)

    # Cria Coral3
    if num == 8:
        ob = Sprite('Objetos/Obstáculos/Vegetação/Coral3.png')
        ob.set_position(random.uniform(0, janela.width - 1) + janela.width, janela.height - ob.height)
        vet.append(ob)


# Movimento dos obstáculos
def obj_move(janela, velscroll, vet):
    for ob in vet:
        ob.x -= velscroll*janela.delta_time()
        ob.draw()
        if ob.x <= ob.x-ob.width/2:
            vet.remove(ob)


# Adiciona pontos
def coleta(vetrec, sub):
    for ob in vetrec:
        if sub.collided(ob):
            vetrec.remove(ob)
            som1.play()
            return int(ob.get_pontos())


# Retira vida
def colisao(vetobst, vetpex, sub):
    for ob in vetobst:
        if sub.collided(ob):
            som2.play()
            if ob.get_dano() == 1:
                return 2
            else:
                return 1

    for px in vetpex:
        if sub.collided(px):
            som1.play()
            vetpex.remove(px)
            if px.get_dano() == 1:
                return 2
            else:
                return 1


# Movimento do submarino
def sub_move(janela, sub, velsub):
    sub.move_key_x(velsub * janela.delta_time())
    sub.move_key_y(velsub * janela.delta_time())
    # Limites
    if sub.width + sub.x > janela.width or sub.x < 0:
        sub.move_key_x(-velsub * janela.delta_time())
    if sub.height + sub.y > janela.height or sub.y < 0:
        sub.move_key_y(-velsub * janela.delta_time())

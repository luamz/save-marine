# Imports
from PPlay.window import*
import menu as menu
import exec as ex

# Inicializa janela
janela = Window(800, 600)
janela.set_title('SaveMarine')

teclado = janela.get_keyboard()

game_state = 0

# Iniciação do Jogo
while True:
    if game_state == 0:
        game_state = menu.menu(janela)
    if game_state == 1:
        game_state = ex.fase1(janela)
    if game_state == 2:
        game_state = ex.fase2(janela)
    if game_state == 3:
        game_state = ex.fase3(janela)
    if game_state == 4:
        game_state = menu.sel_fase(janela)
    if game_state == 5:
        game_state = menu.manual(janela)
    if game_state == 6:
        game_state = menu.derrota(janela)
    if game_state == 7:
        game_state = menu.passa_fase1(janela)
    if game_state == 8:
        game_state = menu.passa_fase2(janela)
    if game_state == 9:
        game_state = menu.vitoria(janela)
    if game_state == 10:
        janela.close()

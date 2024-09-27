import pygame

# Definindo as constantes de cores com o sistema RGB
PRETO = (0,0,0)
BRANCO = (255,255,255)
VERMELHO = (255,0,0)
VERDE = (0,255,0)
AZUL = (0,0,255)

# Definindo constante com valor PI (Utilizado para o cálculo na criação das figuras)
PI = 3.1416

# Inicializando os módulos do Pygame
pygame.init()

# Criando a janela de tamanho 800x600 e com título "Figuras e Texto"
janela = pygame.display.set_mode((800,600))
pygame.display.set_caption("Figuras e texto")

# Utilizando método fill() para aplicar a cor da superfície
janela.fill(BRANCO)

# A mudança de cor da superfície acima somente será aplicada quando rodar o código abaixo
pygame.display.update()

# Trabalhando com texto
fonte = pygame.font.Font(None,48)

# Utilizar o método render() para renderizar o texto a apresentar
texto = fonte.render("Olá mundo!", True, BRANCO, AZUL)
janela.blit(texto, [30,150])

# Utilizando o método line() para desenhar uma linha na tela
pygame.draw.line(janela, VERDE, [60,260], [420,260], 4)

# Utilizando o método polygon() para desenhar um polígono na tela
pygame.draw.polygon(janela, PRETO, ([191,206], [236,277], [156,277]), 0)

# Utilizando o método circle() para desenhar um polígono na tela
pygame.draw.circle(janela, AZUL, (300,250), 25, 0)

# Utilizando o método elipse() para desenhar um polígono na tela
pygame.draw.ellipse(janela, VERMELHO, (300,500,40,80), 1)

# Utilizando o método rect() para desenhar um polígono na tela
pygame.draw.rect(janela, VERDE, (20,20,6,40), 0)

# Utilizando o método arc() para desenhar um arco na tela
pygame.draw.arc(janela, VERMELHO, (250,75,150,125),PI/2,3*PI,2)
pygame.draw.arc(janela, PRETO,(250,75,150,125),-PI/2,PI/2,2)

pygame.display.update()


deve_continuar = True

while deve_continuar:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            deve_continuar = False

# Fechar os módulos de pygame
pygame.quit()


#Jogo da velha com Heuristica
import pygame as pg

#Configurações
largura, altura = 500, 513
celula = largura // 3

#Cores
branco = (255, 255, 255)
preto = (0, 0, 0)
vermelho = (200, 0,0)

#Matriz 3x3
matriz = [[0 for l in range(3)] for c in range(3)]

debug = True

def desenhar_velha(tela):

    tela.fill(preto)

    #Linhas
    pg.draw.line(tela, branco, (celula, 0), (celula, altura), 1)
    pg.draw.line(tela, branco, (celula*2, 0), (celula*2, altura), 1)

    #Colunas
    pg.draw.line(tela, branco, (0, celula), (largura, celula), 1)
    pg.draw.line(tela, branco, (0, celula*2), (largura, celula*2), 1)

def desenhar_jogada(tela):

    #Leitura da matriz
    for l in range(3):
        for c in range(3):
            
            #Desenha um x
            if matriz[l][c] == 1:
                pg.draw.line(tela, vermelho, (c*celula+20, l*celula+20), ((c+1)*celula-20, (l+1)*celula-20), 3)
                pg.draw.line(tela, vermelho, ((c+1)*celula-20, l*celula+20), (c*celula+20, (l+1)*celula-20), 3)
            
            #Desenha um o  
            elif matriz[l][c] == 2:
                pg.draw.circle(tela, vermelho, (c*celula + celula//2, l*celula + celula//2), celula//2 - 15, 3)

def checar_vitoria(jogada): 

    '''

    Return True p/ vitória
    Return False se não encotrado parametros de vitória
    
    '''

    # checa linhas
    for l in range(3):
        if matriz[l][0] == jogada and matriz[l][1] == jogada and matriz[l][2] == jogada:
            return True

    # checa colunas
    for c in range(3):
        if matriz[0][c] == jogada and matriz[1][c] == jogada and matriz[2][c] == jogada:
            return True

    # diagonais
    if matriz[0][0] == jogada and matriz[1][1] == jogada and matriz[2][2] == jogada:
        return True
    if matriz[0][2] == jogada and matriz[1][1] == jogada and matriz[2][0] == jogada:
        return True

def jogada_ia():

            #Troca espaços vazios por sua jogada e verifica ganha
            for l in range(3):
                for c in range(3):
                    if matriz[l][c] == 0:
                        matriz[l][c] = 2
                        if checar_vitoria(2):
                            return
                        matriz[l][c] = 0

            #Bloqueia se jogador pode vencer
            for l in range(3):
                for c in range(3):
                    if matriz[l][c] == 0:
                        matriz[l][c] = 1
                        if checar_vitoria(1):
                            matriz[l][c] = 2
                            return
                        matriz[l][c] = 0

            #Se não outras requisições joga nessas
            #centro
            if matriz[1][1] == 0:
                matriz[1][1] = 2
                return

            #cantos
            for l, c in [(0,0), (0,2), (2,0), (2,2)]:
                if matriz[l][c] == 0:
                    matriz[l][c] = 2
                    return

            #laterais
            for l, c in [(0,1), (1,0), (1,2), (2,1)]:
                if matriz[l][c] == 0:
                    matriz[l][c] = 2
                    return
def main():

    pg.init()
    pg.display.set_caption("Jogo da Velha")
    tela = pg.display.set_mode((largura,altura))

    loop = True
    while loop:
        
        for eventos in pg.event.get():
            
            #Mouse
            if eventos.type == pg.MOUSEBUTTONDOWN:
                x, y = pg.mouse.get_pos()
                linha = y // celula
                coluna = x // celula
                
                if 0 <= linha < 3 and 0 <= coluna < 3:
                    
                    #Jogada do usuário -> X
                    if matriz[linha][coluna] == 0:  
                        matriz[linha][coluna] = 1                                  
                        
                        if not checar_vitoria(1) == True:
                            jogada_ia()
                            
                            if debug == True:
                                print('x:',x,'y:',y,'coluna:', coluna, 'linha:', linha)
                                print(matriz) 
                                print('Vitória Jogador: ', checar_vitoria(1), '\nVitória Máquina:', checar_vitoria(2))
                                
            #Exit
            if eventos.type == pg.QUIT:
                loop= False
                
        desenhar_velha(tela)
        desenhar_jogada(tela)
        pg.display.update()

    pg.quit()

#Execução
if __name__ == "__main__":
    main()



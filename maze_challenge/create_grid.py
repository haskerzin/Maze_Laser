import random, time, os
import numpy as np

class Grid:

    def __init__(self):
        self.size = 12
        self.origem_laser = (0,1)
        self.__saida = (11,1)
        self.espelhos = []
        self.__bombas = []
        self.tipo = 0

    
    # Método para gerar os índices da parte superior do grid
    def gera_indices(self):
        
        indice = '   '
        num = 1
        for i in range(self.size - 2):
            indice += ' ' + str(num) + ' '
            num += 1
        
        
        print(indice)
    
    # Método para definir onde ficará a origem do laser
    def laser(self):
        self.origem_laser = (0, random.randint(1, self.size - 2))

    # Método para definir por onde o laser deve sair
    def saida(self):
        self.__saida =  (self.size-1, random.randint(1, self.size - 2))
    
    # Método de colocação das bombas
    def coloca_bombas(self, n_bombas, laser, saida):
        self.__bombas = []
        while len(self.__bombas) < n_bombas:
            biribinha = (random.randint(1,10), random.randint(1,10))
            if biribinha not in self.__bombas and biribinha != (laser[0] + 1,laser[1]) and biribinha != (saida[0] - 1, saida[1]):
                self.__bombas.append(biribinha)

    def checa_inteiro(self, valor):
        try:
            int(valor)
            return True
        except:
            return False
    
    # Metodo que verifica se uma posicao dada esta dentro dos limites do grid
    def verifica_posicao(self, posicao):
        verifica = 0
        for p in posicao:
            if (1 <= p <= self.size - 1) == False:
                verifica += 1
        
        if verifica != 0:
            return False
        else:
            return True

    ########################## Metodos dos espelhos ################################################################################################################################
    
    # Metodo de escolher o tipo de espelho
    def tipo_espelho(self):
        # print('Digite 1 para espelho \ e 2 para espelho /')
        tipo = input('Digite 1 para espelho \ e 2 para espelho /: ')
        
        verifica = False

        while verifica == False:
            if self.checa_inteiro(tipo) == True:
                if int(tipo) in (1,2):
                    verifica = True

                else:
                    # print('Valor inválido. Digite 1 para espelho \ e 2 para espelho /')
                    tipo = input('Entrada inválida. \n Digite 1 para espelho \ e 2 para espelho /: ')
            else:
                # print('Valor inválido. Digite 1 para espelho \ e 2 para espelho /')
                tipo = input('Entrada inválida. \n Digite 1 para espelho \ e 2 para espelho /: ')

        self.tipo = int(tipo)
    
    # Metodo de receber input da posicao dos espelhos
    def posicao_espelho(self):
        x_espelho = input("Coluna do espelho: ")
        y_espelho = input("Linha do espelho: ")

        while (self.checa_inteiro(x_espelho) == False)  or (self.checa_inteiro(y_espelho) == False):
            # print('Valores inválidos!')
            x_espelho = input("Valor inválido. \n Coluna do espelho: ")
            y_espelho = input("Linha do espelho: ")

        x_espelho = int(x_espelho)
        y_espelho = int(y_espelho)

        return (x_espelho, y_espelho)
    
    # Metodo que adiciona a posicao de um espelho na lista de espelhos
    def espelho(self):
        
        posicao_espelho = self.posicao_espelho()

        while (posicao_espelho in self.__bombas) or (self.verifica_posicao(posicao_espelho) == False):
            # print('Posição inválida. Digite novamente.')
            posicao_espelho = self.posicao_espelho()
        
        self.espelhos.append(posicao_espelho)

    ################################################################################################################################################################################

    ########################## Metodos do raio #####################################################################################################################################

    # Método de desenho do caminho do laser
    def raio(self, origem_laser):
        caminho_laser = []
        for i in range(10):
            caminho_laser.append((origem_laser[0] + 1 + i, origem_laser[1]))
        
        return caminho_laser

    # Novo método de desenho do caminho do laser
    def raio_novo(self):
        caminho_laser = []
        posicao_x = self.origem_laser[0]+1
        posicao_y = self.origem_laser[1]
        for i in range(10):
            # Identificando colisao com bombas
            if (self.origem_laser[0] + 1 + i, self.origem_laser[1]) in self.__bombas:
                print('Game Over')
                break

            elif self.origem_laser[0] + 1 + i == 11:
                pass
            
            elif (self.origem_laser[0] + 1 + i, self.origem_laser[1]) in self.espelhos:
                pass

            
            else:
                caminho_laser.append((self.laser_origem[0] + 1 + i, self.laser_origem[1]))
        
        return caminho_laser
    
    # Novo método de desenho do caminho do laser
    def raio_2(self):
        caminho_laser = []
        posicao_x = self.origem_laser[0]+1
        posicao_y = self.origem_laser[1]
        for i in range(10):
            # Identificando colisao com bombas
            if (posicao_x + 1, posicao_y) in self.espelhos:
                pass

            elif self.origem_laser[0] + 1 + i == 11:
                pass
            
            elif (self.origem_laser[0] + 1 + i, self.origem_laser[1]) in self.espelhos:
                pass

            
            else:
                caminho_laser.append((self.laser_origem[0] + 1 + i, self.laser_origem[1]))
        
        return caminho_laser

    ################################################################################################################################################################################

    # Metodo para definir as posicoes da origem e saida do laser e das bombas antes de chamar a funcao para desenhar a tela
    def define_aparatos(self):
        self.laser()
        self.saida()
        self.coloca_bombas(5, self.__laser, self.__saida)
    
    # Método de desenho da grade
    def draw_grid(self):
        
        blank = '   '
        wall = ' w '
        ponto = ''
        linha = 1
        # laser = self.laser()
        # saida = self.saida()
        # Essa chamada do método self.bombas() terá que sair do método self.draw_grid() pois
        # após iniciar o jogo a posição das bombas não mudam
        # bombas = self.coloca_bombas(5, laser, saida)
        caminho_laser = self.raio_novo(self.__laser, self.__bombas)
        self.gera_indices()
        
        for i in range(self.size):
            ponto =''
            for j in range(self.size+1):
                
                # Desenhando a origem do self.__laser
                if (j,i) == self.__laser:
                    ponto += ' = '
                
                # Desenhando a saída 
                elif (j,i) == self.__saida:
                    ponto += '   '

                # Desenhando a bomba
                elif (j,i) in self.__bombas:
                    ponto += ' B '
                
                # Desenhando os espelhos
                elif (j,i) in self.espelhos:
                    if self.tipo == 1:
                        ponto += ' \ '
                    else:
                        ponto += ' / '

                # Desenhando o caminho do laser
                elif (j,i) in caminho_laser:
                    ponto += ' - '

                else:

                    if (i in [0, self.size-1] or j in [0,self.size-1]) and j != self.size:
                        ponto += wall

                    elif j == self.size and (i == 0 or i == self.size-1):
                        ponto += blank
                    
                    elif j == self.size:
                        ponto += str(linha)
                        linha += 1
                    else:
                        ponto += blank
                
            print(ponto)

    
    ###################### Metodo para rodar o jogo #######################################

    def joga(self):
        jogando = True
        # Definindo as posicoes de entrada e saida do laser e das bombas
        self.define_aparatos()

        while jogando == True:
            # Desenhando o campo
            self.draw_grid()

            ################## Inputs do jogador ###########################
            # Selecionando o tipo de espelho
            self.tipo_espelho()

            # Selecionando a posicao do espelho
            self.espelho()
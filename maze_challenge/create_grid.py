import random, time, os

class Grid:

    def __init__(self):
        self.size = 12
        self.__laser = (0,1)

    
    # Método para gerar os Ã­ndices da parte superior do grid
    def gera_indices(self):
        
        indice = '   '
        num = 1
        for i in range(self.size - 2):
            indice += ' ' + str(num) + ' '
            num += 1
        
        
        print(indice)
    
    # Método para definir onde ficarÃ¡ a origem do laser
    def laser(self):
        self.__laser = (0, random.randint(1, self.size - 2))
        return self.__laser

    # Método para definir por onde o laser deve sair
    def saida(self):
        return (self.size-1, random.randint(1, self.size - 2))
    
    # Método de colocação das bombas
    def bombas(self, n_bombas, laser, saida):
        bombas = []
        while len(bombas) < n_bombas:
            biribinha = (random.randint(1,10), random.randint(1,10))
            if biribinha not in bombas and biribinha != (laser[0] + 1,laser[1]) and biribinha != (saida[0] - 1, saida[1]):
                bombas.append(biribinha)

        return bombas

    # Método de colocação dos espelhos
    def espelhos(self):
        linha = input('Digite a linha do espelho: ')
        coluna = input('Digite a coluna do espelho: ')
        return (linha, coluna)

    # Método de desenho do caminho do laser
    def raio(self, origem_laser):
        caminho_laser = []
        for i in range(10):
            caminho_laser.append((origem_laser[0] + 1 + i, origem_laser[1]))
        
        return caminho_laser

    # Novo método de desenho do caminho do laser
    def raio_novo(self, origem_laser, bombas):
        caminho_laser = []
        for i in range(10):
            if (origem_laser[0] + 1 + i, origem_laser[1]) in bombas:
                print('Game Over')
                break
            else:
                caminho_laser.append((origem_laser[0] + 1 + i, origem_laser[1]))
        
        return caminho_laser


    # Método de desenho da grade
    def draw_grid(self):
        
        blank = '   '
        wall = ' w '
        ponto = ''
        linha = 1
        laser = self.laser()
        saida = self.saida()
        # Essa chamada do Método self.bombas() terÃ¡ que sair do Método self.draw_grid() pois
        # apÃ³s iniciar o jogo a posiÃ§Ã£o das bombas nÃ£o mudam
        bombas = self.bombas(3, laser, saida)
        caminho_laser = self.raio_novo(laser, bombas)
        self.gera_indices()

        for i in range(self.size):
            ponto =''
            for j in range(self.size+1):
                
                # Desenhando a origem do laser
                if (j,i) == laser:
                    ponto += ' = '
                
                # Desenhando a saÃ­da 
                elif (j,i) == saida:
                    ponto += '   '

                # Desenhando a bomba
                elif (j,i) in bombas:
                    ponto += ' B '
                
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
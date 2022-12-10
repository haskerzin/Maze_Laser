import random, time, os

class Grid:

    def __init__(self):
        self.size = 12
        self.__laser = (0,1)

    
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

    # Método de desenho do caminho do laser
    def raio(self, origem_laser):
        caminho_laser = []
        for i in range(10):
            caminho_laser.append((origem_laser[0] + 1 + i, origem_laser[1]))
        
        return caminho_laser


    # Método de desenho da grade
    def draw_grid(self):
        
        blank = '   '
        wall = ' w '
        ponto = ''
        self.gera_indices()
        linha = 1
        laser = self.laser()
        saida = self.saida()
        # Essa chamada do método self.bombas() terá que sair do método self.draw_grid() pois
        # após iniciar o jogo a posição das bombas não mudam
        bombas = self.bombas(3, laser, saida)
        caminho_laser = self.raio(laser)

        for i in range(self.size):
            ponto =''
            for j in range(self.size+1):
                
                # Desenhando a origem do laser
                if (j,i) == laser:
                    ponto += ' = '
                
                # Desenhando a saída 
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
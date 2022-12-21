# Novo maze
import pygame
from sys import exit
import random
import math
 
 

class Laser:

    def __init__(self):
        self.width = 800
        self.height = 600
        self.pos_x = 0
        self.pos_y = 300
        self.speed = 10
        self.velocity = [self.speed,0]
        self.new_velocity = [self.speed,0]
        self.direction = 1
        self.position_vector = [[0,300], [10,300], [20,300], [30,300], [40,300], [50,300], [60,300]]
        self.orange = (255,69,0)
        self.blue = (72,61,139)
        self.primeiro = len(self.position_vector)
        self.mudou_direcao = False
        self.food = []
        self._screen = pygame.display.set_mode([self.width, self.height])
        self.velocity_vector = []
        self.define_velocity()


    def move_snake(self):

        # self.add_velocity()
        if self.mudou_direcao == True:
            self.velocity_vector.append(self.new_velocity)
            del self.velocity_vector[0]
            self.primeiro -= 1

        if self.primeiro == 0:
            self.mudou_direcao = False
            self.velocity = self.new_velocity
            self.define_velocity()
        
        for i in range(len(self.position_vector)):
            self.position_vector[i][0] += self.velocity_vector[i][0]
            self.position_vector[i][1] += self.velocity_vector[i][1]



        # Torus topology
        for i in range(len(self.position_vector)):
            if self.position_vector[i][0] in (0, self.width):
                self.position_vector[i][0] = abs(self.width - self.position_vector[i][0])
            if self.position_vector[i][1] in (0, self.height):
                self.position_vector[i][1] = abs(self.height - self.position_vector[i][1])
        
    
            
    def move_vector(self):
        for i in range(len(self.position_vector)):
            if i >= self.primeiro:
                self.position_vector[i][0] += self.new_velocity[0]
                self.position_vector[i][1] += self.new_velocity[1]
            else:
                self.position_vector[i][0] += self.velocity[0]
                self.position_vector[i][1] += self.velocity[1]
            

        for i in range(len(self.position_vector)):
            if self.position_vector[i][0] in (0, self.width):
                self.position_vector[i][0] = abs(self.width - self.position_vector[i][0])
            if self.position_vector[i][1] in (0, self.height):
                self.position_vector[i][1] = abs(self.height - self.position_vector[i][1])

        if self.mudou_direcao == True:
            self.primeiro -= 1
        
        if self.primeiro == 0:
            self.primeiro = len(self.position_vector)
            self.velocity = self.new_velocity
            self.new_velocity = [0,0]
            self.mudou_direcao = False

    
    def generate_food(self):
        if len(self.food) == 0:
            self.food.append((random.randint(1,self.width), random.randint(1, self.height)))
    
    def draw_food(self):
        for food in self.food:
            pygame.draw.rect(self._screen, self.blue, (food[0], food[1], 20,20))

    def distance(self, x, y):
        return math.sqrt(abs(x[0] - y[0])**2 + abs(x[1] - y[1])**2)
    
    def eat_food(self):
        for food in self.food:
            if self.distance(self.position_vector[-1], food) < 10:
                self.position_vector.insert(0, [self.position_vector[0][0] - self.velocity[0], self.position_vector[0][1] - self.velocity[1]])
                self.food = []
        


    def draw_character(self):
        for i in range(len(self.position_vector)):
            pygame.draw.rect(self._screen, self.orange, (self.position_vector[i][0], self.position_vector[i][1], 10,10))


    def get_input(self, event):
        # event = pygame.event.wait()
        if event.key == pygame.K_w:
            self.new_velocity[0] = 0
            self.new_velocity[1] = -self.speed

        if event.key == pygame.K_a:
            self.new_velocity[0] = -self.speed
            self.new_velocity[1] = 0

        if event.key == pygame.K_s:
            self.new_velocity[0] = 0
            self.new_velocity[1] = self.speed

        if event.key == pygame.K_d:
            self.new_velocity[0] = self.speed
            self.new_velocity[1] = 0
        
        # Vetor para marcar que mudamos de direção
        self.primeiro = len(self.position_vector)
        self.mudou_direcao = True


    
    def define_velocity(self):
        vetor = []
        for i in range(len(self.position_vector)):
            vetor.append(self.velocity)
        
        self.velocity_vector = vetor


    def add_velocity(self):
        # Adding the self.new_velocity to the self.velocity_vector
        self.velocity_vector.append(self.new_velocity)
        del self.velocity_vector[0]
        






    def play(self):

        # Initialize the pygame library
        pygame.init()

        # Set up the drawing window
        self._screen
        # Run until the user asks to quit
        running = True
        while running:

            # Did the user click the window close button?
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

                if event.type == pygame.KEYDOWN:
                    self.get_input(event)

            # Fill the background with black
            self._screen.fill((0, 0, 0))
            # self.generate_food()
            # self.draw_food()
            # self.eat_food()
            self.move_snake()
            self.draw_character()
            # self.move_vector()
            
            pygame.time.wait(100)

            # Flip the display
            pygame.display.flip()

        # Done! Time to quit.
        pygame.quit()
        exit()

# Novo maze
import pygame
from sys import exit
# import numpy 
 

class Laser:

    def __init__(self):
        self.width = 800
        self.height = 600
        self.pos_x = 0
        self.pos_y = 300
        self.velocity_x = 10
        self.velocity_y = 0
        self.direction = 1
        self.position_vector = [[0,300], [10, 300], [20, 300]]
        self.orange = (255,69,0)

    def move_vector(self):
        for i in range(len(self.position_vector)):
            self.position_vector[i][0] += self.velocity_x
            self.position_vector[i][1] += self.velocity_y

        for i in range(len(self.position_vector)):
            if self.position_vector[i][0] in (0, self.width):
                self.velocity_x *= -1
            if self.position_vector[i][1] in (0, self.height):
                self.velocity_y *= -1

    def draw_character(self, screen):
        for i in range(len(self.position_vector)):
            pygame.draw.rect(screen, self.orange, (self.position_vector[i][0], self.position_vector[i][1], 10,10))


    def get_input(self, event):
        # event = pygame.event.wait()
        if event.key == pygame.K_w:
            self.velocity_x = 0
            self.velocity_y = -10

        if event.key == pygame.K_a:
            self.velocity_x = -10
            self.velocity_y = 0

        if event.key == pygame.K_s:
            self.velocity_x = 0
            self.velocity_y = 10

        if event.key == pygame.K_d:
            self.velocity_x = 10
            self.velocity_y = 0



    def move(self):
        self.pos_x += self.direction*self.velocity

        if self.pos_x in (0, self.width):
            self.direction *= -1

    def play(self):

        # Initialize the pygame library
        pygame.init()

        # Set up the drawing window
        screen = pygame.display.set_mode([self.width, self.height])

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
            screen.fill((0, 0, 0))
            self.draw_character(screen)
            self.move_vector()
            pygame.time.wait(10)

            # Flip the display
            pygame.display.flip()

        # Done! Time to quit.
        pygame.quit()
        exit()

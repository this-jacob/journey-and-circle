import pygame, os, color

size = width, height = 720, 480

#Start initializing the game
pygame.init()
screen = pygame.display.set_mode(size)
clock = pygame.time.Clock()

def main():

    #Game Loop
    while True:
        ###
        # EVENT HANDLING
        ###

        #preset event handler
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()

        ###
        # DRAWING CODE
        ###

        #clear screen
        screen.fill(color.BLACK)

        #render entities

        #flip and lock display
        pygame.display.flip()
        clock.tick(60)

if __name__ == '__main__':
    main()

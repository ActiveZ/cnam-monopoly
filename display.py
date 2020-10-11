import pygame
from data import cases_data


class Display:

    def __init__(self):
        # initialisation graphique du plateau
        successes, failures = pygame.init()
        print("Initializing pygame: {0} successes and {1} failures.".format(successes, failures))

        self.screen = pygame.display.set_mode((700, 700))
        clock = pygame.time.Clock()
        FPS = 60
        # BLACK = (0, 0, 0)
        # WHITE = (255, 255, 255)

        self.img_plateau = pygame.image.load("images/board.png").convert()
        self.screen.blit(self.img_plateau,(0,0))
        pygame.display.update()


    def display_players(self, players): # doublon avec update board ?
        self.screen.blit(self.img_plateau,(0,0))
        for p in players:
            self.screen.blit(p.image, p.rect)
        pygame.display.update()  # Or pygame.display.flip()


    def update_board(self, j, progress, players):
        for i in range (progress + 1):
            pos = j.position + i
            c = cases_data[pos] if pos < 40 else cases_data [pos - 40]
            while j.rect.centerx != c["x"] or j.rect.centery != c["y"]:
                if j.rect.centerx < c["x"]: j.velocity[0] = +1
                elif j.rect.centerx > c["x"]: j.velocity[0] = -1
                else: j.velocity[0] = 0

                if j.rect.centery < c["y"]: j.velocity[1] = +1
                elif j.rect.centery > c["y"]: j.velocity[1] = -1
                else: j.velocity[1] = 0

                j.rect.move_ip(*j.velocity)

                # print("c:", c, "x:", j.rect.centerx, "y:", j.rect.centery, "dt:", dt) # affiche les coordonnées du centre du pion

                self.screen.blit(self.img_plateau,(0,0))
                self.screen.blit(j.image, j.rect)
                for p in players: self.screen.blit(p.image, p.rect) # a optimiser ?
                pygame.display.update()  # Or pygame.display.flip()
import pygame
from data import cases_data


successes, failures = pygame.init()
print("Initializing pygame: {0} successes and {1} failures.".format(successes, failures))

screen = pygame.display.set_mode((700, 700))
clock = pygame.time.Clock()
FPS = 60

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

img_plateau = pygame.image.load("images/board.png").convert()

screen.blit(img_plateau,(0,0))
# pygame.display.update()


class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        # self.image = pygame.Surface((32, 32))
        # self.image.fill(WHITE)
        self.image = pygame.image.load("images/pion_chapeau.png")
        self.rect = self.image.get_rect()  # Get rect of some size as 'image'.
        self.rect.center = (cases_data[0]["x"], cases_data[0]["y"]) # case départ

        self.velocity = [0, 0] # [x, y]

    def update(self):
        self.rect.move_ip(*self.velocity)


player = Player()
running = False
# running = True
while running:
    dt = clock.tick(FPS) / 1000  # Returns milliseconds between each call to 'tick'. The convert time to seconds.
    # screen.fill(BLACK)  # Fill the screen with background color.

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_z or event.key == pygame.K_UP:
                player.velocity[1] = -200 * dt  # 200 pixels per second
            elif event.key == pygame.K_s or event.key == pygame.K_DOWN:
                player.velocity[1] = 200 * dt
            elif event.key == pygame.K_q or event.key == pygame.K_LEFT:
                player.velocity[0] = -200 * dt
            elif event.key == pygame.K_d or event.key == pygame.K_RIGHT:
                player.velocity[0] = 200 * dt
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_z or event.key == pygame.K_s or event.key == pygame.K_DOWN or event.key == pygame.K_UP:
                player.velocity[1] = 0
            elif event.key == pygame.K_q or event.key == pygame.K_d or event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                player.velocity[0] = 0

    player.velocity[0] = -200 * dt  # X 200 pixels per second
    running = player.rect.centerx != cases_data[10]["x"] # simple visite
    # player.velocity[1] = -200 * dt  # Y 200 pixels per second


    player.update()
    print("x:", player.rect.centerx, "y:", player.rect.centery) # affiche les coordonnées du centre du pion

    screen.blit(img_plateau,(0,0))
    screen.blit(player.image, player.rect)
    pygame.display.update()  # Or pygame.display.flip()


running = True
running = False
while running:
    dt = clock.tick(FPS) / 1000  # Returns milliseconds between each call to 'tick'. The convert time to seconds.


    for c in cases_data:
        if c == 40: break # on saute la case prison: à regler en envoyant directement
        for event in pygame.event.get(): running = event.type != pygame.QUIT

        while player.rect.centerx != cases_data[c]["x"] or player.rect.centery != cases_data[c]["y"]:
            if player.rect.centerx < cases_data[c]["x"]: player.velocity[0] = +1
            elif player.rect.centerx > cases_data[c]["x"]: player.velocity[0] = -1
            else: player.velocity[0] = 0

            if player.rect.centery < cases_data[c]["y"]: player.velocity[1] = +1
            elif player.rect.centery > cases_data[c]["y"]: player.velocity[1] = -1
            else: player.velocity[1] = 0

            player.update()

            print("c:", c, "x:", player.rect.centerx, "y:", player.rect.centery, "dt:", dt) # affiche les coordonnées du centre du pion

            screen.blit(img_plateau,(0,0))
            screen.blit(player.image, player.rect)
            pygame.display.update()  # Or pygame.display.flip()


# running = True
dt = clock.tick(FPS) / 1000  # Returns milliseconds between each call to 'tick'. The convert time to seconds.
c1 = 7
c2 = 24
player.rect.centerx = cases_data[7]["x"]
player.rect.centery = cases_data[7]["y"]
print("x:", player.rect.centerx, "y:", player.rect.centery, "dt:", dt) # affiche les coordonnées du centre du pion

# while running:
for c in [cases_data[7], cases_data[24]]:
    while player.rect.centerx != c["x"] or player.rect.centery != c["y"]:
        if player.rect.centerx < c["x"]: player.velocity[0] = +1
        elif player.rect.centerx > c["x"]: player.velocity[0] = -1
        else: player.velocity[0] = 0

        if player.rect.centery < c["y"]: player.velocity[1] = +1
        elif player.rect.centery > c["y"]: player.velocity[1] = -1
        else: player.velocity[1] = 0

        player.update()

        print("x:", player.rect.centerx, "y:", player.rect.centery, "dt:", dt) # affiche les coordonnées du centre du pion

        screen.blit(img_plateau,(0,0))
        screen.blit(player.image, player.rect)
        pygame.display.update()  # Or pygame.display.flip()



print("Exited the game loop. Game will quit...")
quit()
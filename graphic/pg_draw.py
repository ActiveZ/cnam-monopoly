import pygame

background_colour = (255,255,255) # White color
(width, height) = (300, 200) # Screen size
color1=(0,0,0) # black for retangle
color2=(255,0,0) # red for circle

screen = pygame.display.set_mode((width, height)) #Setting Screen
pygame.display.set_caption('Drawing') #Window Name
screen.fill(background_colour)#Fills white to screen

# pygame.draw.rect(screen, color, (x,y,width,height), thickness)
pygame.draw.rect(screen, color1, (100,50,30,40), 1) #Drawing the rectangle

# pygame.draw.circle(screen, color, (x,y), radius, thickness)
pygame.draw.circle(screen, color2, (150,100), 80, 1) # center of screen

pygame.display.update()

#Loop
running = True
while running:
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      running = False
      pygame.quit()
 
def Buttonify(Picture, coords, surface):
    image = pygame.image.load(Picture)
    imagerect = image.get_rect()
    imagerect.topright = coords
    surface.blit(image,imagerect)
    return (image,imagerect)


Image = Buttonify('YOUR_PICTURE.png',THE_COORDS_OF_THE_BUTTON'S_TOP_RIGHT_CORNER, THE_NAME_OF_THE_SURFACE)

if event.type == MOUSEBUTTONDOWN and event.button == 1:
     mouse = pygame.mouse.getpos
     if Image[1].collidrect(mouse):
        #code if button is pressed goes here

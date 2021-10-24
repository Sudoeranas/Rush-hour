from board import *

pygame.init()
board = Board()
board.prepare_stage()

slide_sound = pygame.mixer.Sound("./sons/son_mouvement.wav") # Un son pour chaque mouvement slide d'un véhicule
level_sound = pygame.mixer.Sound("./sons/gagné.wav") # Quand le niveau est fini il y aura un son de level clear

slide_sound.set_volume(0.1) #Régler le volume
level_sound.set_volume(0.3)

w = 900 # largeur 
h = 800 # hauteur 

stride_x  = 100
stride_y = 100

screen = pygame.display.set_mode((w, h))

imagee = pygame.image.load("./img/board_img.jpg")

imagee = pygame.transform.scale(imagee, (w,h)) #Redimensionner le jeu 

pygame.display.set_caption("Rush hour") #Titre de la fenêtre

font = pygame.font.SysFont(None, 32) # 32 pixels 

textLevelImg = font.render('Niveau: '+ str(board.level+1), True, (255,255,255))
textLevelRect = textLevelImg.get_rect()

textLevelRect.center = (800,250)
textClearImg = font.render('Gagné !', True, (0,255,0), (0,0,255)) #Couleur et fond du mot gagné

textClearRect = textClearImg.get_rect()

textClearRect.center = (w//2,h//2)


running = True

sel_vechle = ""
levClear = False
time_levUp = 0

while running:
    for event in pygame.event.get():
        if event.type == QUIT:
            running = False # arrêter la boucle 
       
        elif event.type == pygame.KEYDOWN: # Keydowns càd Si une touche a été pressée
            
            if not levClear: # Tout simplement si aucune touche n'a été pressée
                
                #Si la touche correspondante a été pressée donc on sélectionne l'image avec la touche convenable
                
                if event.key == K_a: 
                    sel_vechle = "a"
                elif event.key == K_b:
                    sel_vechle = "b"
                elif event.key == K_c:
                    sel_vechle = "c"
                elif event.key == K_d:
                    sel_vechle = "d"
                elif event.key == K_e:
                    sel_vechle = "e"
                elif event.key == K_f:
                    sel_vechle = "f"
                elif event.key == K_g:
                    sel_vechle = "g"
                elif event.key == K_h:
                    sel_vechle = "h"
                elif event.key == K_i:
                    sel_vechle = "i"
                elif event.key == K_j:
                    sel_vechle = "j"
                elif event.key == K_k:
                    sel_vechle = "k"
                elif event.key == K_o:
                    sel_vechle = "o"
                elif event.key == K_p:
                    sel_vechle = "p"
                elif event.key == K_q:
                    sel_vechle = "q"
                elif event.key == K_r:
                    sel_vechle = "r"
                elif event.key == K_x:
                    sel_vechle = "x"
                
                elif event.key == pygame.K_LEFT: # Si la touche de mouvement gauche est apuyée
                    if board.sur_tableau(sel_vechle):
                        if board.vechles[sel_vechle].dir == 'h': #si la direction est horizontale
                            if board.move(sel_vechle, -1):# La gauche est toujours -1 
                                pygame.mixer.Sound.play(slide_sound) # Jouer le son du mouvement
                            
                elif event.key == pygame.K_RIGHT: # Même chose pour les 4 autres touches !!
                    if board.sur_tableau(sel_vechle):
                        if board.vechles[sel_vechle].dir == 'h':#Horizontal 
                            if board.move(sel_vechle, 1):
                                pygame.mixer.Sound.play(slide_sound)
                
                elif event.key == pygame.K_UP:
                    if board.sur_tableau(sel_vechle):
                        if board.vechles[sel_vechle].dir == 'v':
                            if board.move(sel_vechle, -1):
                                pygame.mixer.Sound.play(slide_sound)
                
                elif event.key == pygame.K_DOWN:
                    if board.sur_tableau(sel_vechle):
                        if board.vechles[sel_vechle].dir == 'v':
                            if board.move(sel_vechle, 1):#
                                pygame.mixer.Sound.play(slide_sound)

    # print(board)
    screen.blit(imagee, (0,0))
    
    
    for v in board.vechles:
        curr_v = board.vechles[v] 
        screen.blit(curr_v.image, (curr_v.pos[0] * stride_x + 100  , curr_v.pos[1] * stride_y + 100))       
    
    textLevelImg = font.render('Niveau: '+ str(board.level+1), True, (255,255,255))
    screen.blit(textLevelImg, textLevelRect)
    pygame.display.update()


    if levClear == False:
        levClear = board.isLevelCleared()
    
    time_levUp = pygame.time.get_ticks()
    if levClear:
        pygame.mixer.Sound.play(level_sound)
        screen.blit(textClearImg, textClearRect)
        pygame.display.update()
        while pygame.time.get_ticks() - time_levUp < 4000:
            continue

        board.level += 1
        levClear = False
        board.prepare_stage()

    pygame.display.update()
pygame.quit()
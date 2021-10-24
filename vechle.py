MAX_COLS = 6 # --> Colonnes en total
MAX_LIGNES = 6# --> Lignes en total

import pygame
from pygame.locals import *

class Vechle:
    def __init__(self, nom, pos, dir):  # pos --> position et dir --> direction
        if type(nom) is str:
            self.nom = nom
           
            if self.nom == "x": #La voiture rouge principale à faire sortir on la nomme x
                
                self.img_name = "./img/x.png" #référence de l'image à choisir est celle qu'on a entré 
                
                self.len = 2 # Chaque véhicule a une certaine longueur puisque x est une voiture donc c'est 2 
            
            elif self.nom == "a":
                self.img_name = "./img/a.png" # Même chose pour les autres ..
                self.len = 2
            
            elif self.nom == "b":
                self.img_name = "./img/b.png"
                self.len = 2
            
            elif self.nom == "c":
                self.img_name = "./img/c.png"
                self.len = 2
            
            elif self.nom == "d":
                self.img_name = "./img/d.png"
                self.len = 2
            
            elif self.nom == "e":
                self.img_name = "./img/e.png"
                self.len = 2
            
            elif self.nom == "f":
                self.img_name = "./img/f.png"
                self.len = 2
            
            elif self.nom == "g":
                self.img_name = "./img/g.png"
                self.len = 2
            
            elif self.nom == "h":
                self.img_name = "./img/h.png"
                self.len = 2
            
            elif self.nom == "i":
                self.img_name = "./img/i.png"
                self.len = 2
            
            elif self.nom == "j":
                self.img_name = "./img/j.png"
                self.len = 2
            
            elif self.nom == "k":
                self.img_name = "./img/k.png"
                self.len = 2
            
            elif self.nom == "o":
                self.img_name = "./img/o.png"
                #La longueur de ce véhicule sera 3 car c'est un bus ou camion
                self.len = 3
            
            elif self.nom == "p":
                self.img_name = "./img/p.png"
                self.len = 3
            
            elif self.nom == "q":
                self.img_name = "./img/q.png"
                self.len = 3
            
            elif self.nom == "r":
                self.img_name = "./img/r.png"
                self.len = 3
            
            else:
                raise Exception(nom , " n'existe pas dans la liste des noms entrés")
        else:
            raise Exception(nom, " n'est même pas un type str")

        if dir == "h" or  dir == "v": # Direction doit être soit horizontale soit verticale
            self.dir = dir
        
        else:
            raise Exception("La direction doit être soit 0 ou 1")


        if type(pos) is list:
            
            if pos[0] >= 0 and  pos[0] <= MAX_COLS - 1 and \
                pos[1] >= 0 and pos[1] <= MAX_LIGNES - 1:
                self.pos = [pos[0], pos[1]]
            
            else:
                raise Exception("Ceci n'est pas un nombre valide")


        self.image = pygame.image.load(self.img_name) # Charger les images ...
        
        self.image = pygame.transform.scale(self.image, (self.len * 100, 100)) 
        # Rendimentionner car verticalement chaque image doit avoir une unité et en longeur c'est soit 3 unités soit 2
        
        
        if self.dir == 'v': # Si La direction est vericale On doit faire une rotation ...
            self.image = pygame.transform.rotate(self.image, 90) 
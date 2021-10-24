from vechle import *

problème ="./problems/problem_set.txt"


class Board:
    def __init__(self, lignes=6, cols=6): 
        self.lignes= lignes
        self.cols = cols
        
        self.grille = [] # Grille 2D de base 
        
        self.creer_grille(self.lignes + 1)
        
        self.level = 0
        
        self.vechles = {} # Dictionnaire car il aide et facilite de classifier les charactères de l'alphabet
        
        self.stages = []
            
        with open(problème, "r") as stageFile: # ouverture du fichier problème en lecture seule
            # stageFile --> considéré comme un fichier temporaire
            
            for ligne in stageFile: # lignes des positions des voitures du fichier problem_set.txt
                mots = ligne.split(" ") #séparer les positions des véhicules par un espace
                stage = []
                
                for mot in mots:
                    mot = mot.strip() # retirer tous les espaces non nécessaires
                    block = []
                    
                    for lettre in mot: #on commence à traiter les lettres
                        
                        if lettre.isdigit():# On traite les parties des mots dont il y a des nombres avec la fonction "is_digit()"
                            block.append(int(lettre))
                        
                        else:
                            block.append(lettre)
                    stage.append(block)
                self.stages.append(stage)
    
    def __str__(self):
        ret_str = "\n"
        for i in range(self.lignes):
            for j in range(self.cols):
                ret_str += str(self.grille[j][i])
                ret_str += " "
            ret_str += "\n"
        ret_str += "\n"
        return ret_str

    def creer_grille(self, size): # fonction méthode
        """
        Fonction qui sert à créer une grille vide 
        """
        for i in range(size):
            self.grille.append([0]*size) #Chaque ligne a 6 éléments 0 (colonnes)


    def prepare_stage(self):
        """
        Quand le niveau est O quand la grille est crée, tout est vide et commence la première
        situation, mais dès qu'on passe au niveau 2 , on doit tout rénitialiser à 0
        """
        
        self.clearGrid()
        self.vechles = {} # Les véhicules doivent être vides 
        
        level_courant = self.stages[self.level]
        
        for v in level_courant:
            self.pushVechle(Vechle(v[0], [v[1], v[2]], v[3])) # 3 éléments dont j'ai besoin
            
    def pushVechle(self, vechle):
        """
        
        """
        vPos = vechle.pos #Position du véhicule
        vLen = vechle.len #Longueur du véhicule
        vDir = vechle.dir #Direction du véhicule
        vNom = vechle.nom #Nom du véhicule 

        check = True

        if vNom in self.vechles: # Si il est déjà sur le board(tableau)
            return False
                
        """
        Première partie : traiter les cas horizontaux
        
        """
        if vDir == 'h':
            if vPos[0] < 0 and vPos[0] > self.cols - 1 - vLen and\
                vPos[1] < 0 and vPos[1] > self.lignes - 1:          # par exemple s'il est plus large que 5 donc il est plus large que le tableau
                return False                                        # --> cas impossible .
            
            for i in range(vPos[0], vPos[0] + vLen):
                if self.grille[i][vPos[1]] != 0: # si la position prochaine n'est pas égale 
                    check = False            # à 0 donc un autre objet a occupé cette place
                    return False                 #donc tu peux pas push ce vehicule .

            
            if check: # Donc on peux faire un push au vehicule au cas True!
                self.vechles[vNom] = vechle
                for i in range(vPos[0], vPos[0] + vLen):
                    self.grille[i][vPos[1]] = vNom
                return True

        
        #Deuxième partie : traiter les cas verticals même chose comme le cas horizontal
        #Que le 0 qui doit être changé car 0--> vertical et 1 --> horizontal 
        
        elif vDir == 'v':
            if vPos[0] < 0 and vPos[0] > self.cols - 1 and \
                vPos[1] < 0 and vPos[1] > self.lignes - 1 - vLen : # On retraite les mêmes cas 
                return False                    #pour le cas horizontal on a qu'à changer le 0 avec un 1

            for i in range(vPos[1], vPos[1] + vLen):
                if self.grille[vPos[0]][i] != 0:
                    check = False
                    return False

            if check:
                self.vechles[vNom] = vechle
                for i in range(vPos[1], vPos[1] + vLen):
                    self.grille[vPos[0]][i] = vNom # Déplacement possible !!
                return True

    def clearGrid(self):
        """
        La fonction sert tout simplement à remplir notre matrice avec des 0 
        """
        for i in range(len(self.grille)):
            for j in range(len(self.grille[0])):
                self.grille[i][j] = 0

    def sur_tableau(self, nom):
        """
        Pour vérifier l'appartenance du nom de véhicules dans le disctionnaire contenant
        le total des véhicules disponibles 
        """
        if nom not in self.vechles:
            return False
        else:
            return True

    
    def move(self, nom, val):
        """
        Fonction principale pour bouger 
        """

        if nom not in self.vechles:
            return False

        vechle = self.vechles[nom]
        vPos = vechle.pos
        vLen = vechle.len
        vDir = vechle.dir
        vNom = vechle.nom

        check = True

        if nom == 'x' and vPos[0] ==  4: # 'x' car c'est la voiture rouge principale !
            self.vechles['x'].pos = (6,2) # la position finale pour gagner 
            return True

        """
        Pour le cas horizontal 
        """
        if vDir == 'h':
            if vPos[0] + val < 0 or vPos[0] + val > self.cols - vLen or \
                vPos[1]  < 0 or vPos[1] > self.lignes - 1:
                return False

            for i in range(vPos[0] + val, vPos[0]+val + vLen):
                if self.grille[i][vPos[1]] != 0:
                    if self.grille[i][vPos[1]] != vNom:
                        check = False
                        return False

            if check: 
                if val > 0:
                    self.grille[vPos[0]][vPos[1]] = 0 # quand tu bouges a droit donc la position doit être filée avec des 0
                else:
                    self.grille[vPos[0] + vLen - 1][vPos[1]] = 0 
                    
                self.vechles[vNom].pos[0] += val #implémenter le dictionnaire de véhicules
                
                vPos = vechle.pos # Remettre à jour la variable initiale

                for i in range(vPos[0], vPos[0] + vLen):
                    self.grille[i][vPos[1]] = vNom
                
                return True

        
        #Sinon pour le cas vertical il suffit de remettre à jour les valeurs entre 0 et 1 de l'alignementcomme toujours 

        elif vDir == 'v':
            if vPos[0] < 0 or vPos[0] > self.cols - 1 or \
                vPos[1] + val < 0 or vPos[1] + val > self.lignes - vLen :
                return False

            for i in range(vPos[1] +val, vPos[1]+val + vLen):
                if self.grille[vPos[0]][i] != 0:
                    if self.grille[vPos[0]][i] != vNom:
                        check = False
                        return False

            if check:
                if val > 0:
                    self.grille[vPos[0]][vPos[1]] = 0
                else:
                    self.grille[vPos[0]][vPos[1]+vLen - 1]=0
                self.vechles[vNom].pos[1] += val
                vPos = vechle.pos
                self.grille[vPos[0]][vPos[1] - val] = 0
                for i in range(vPos[1], vPos[1] + vLen):
                    self.grille[vPos[0]][i] = vNom
                return True
    
    
    def isLevelCleared(self):
        """
        Si le niveau est fait et terminé on doit créer la position finale
        du véhicule x (voiture rouge)
        """
        vechle_x = self.vechles['x']
        
        if vechle_x.pos[0] >= 4 and vechle_x.pos[1] == 2: # Quand il dépasse la case 4 c'est déjà la case finale 5 ou 6
            self.vechles['x'].pos = (6,2)
            return True # Bingo !
        else:
            return False
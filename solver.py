import vechle
import board
from vechle import *
from board import *


def chercher_solution(self):
    '''Tente de trouver une solution, ne s'arrêtera qu'après avoir trouvé ou tout essayé.'''
    
    grille  = Board.grille()
    
    a_tester = [self]
        
    while len(a_tester) > 0:
        
        prochain = a_tester.pop(0)
        grille .append(prochain)
        prochain.afficher_grille()
        print('déjà faits :\t',len(grille ), '\nà tester   :\t', len(a_tester))
        
        if prochain.victoire():
            return prochain
        
        for vehicule, deplacements in prochain.lister_deplacements().items():
            for deplacement in deplacements:
                next_to_try = prochain.copier_grille_deplacement(vehicule, deplacement)
                if not next_to_try in grille  + a_tester:
                    a_tester.append(next_to_try)

def afficher_deplacements(self):
    '''Affiche l'historique des déplacements sur cette grille.'''
    for deplacement in self._deplacements:
        print(deplacement)

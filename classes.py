"""Classes du jeu de Labyrinthe MacGyver"""

import pygame
import random
from pygame.locals import * 
from constantes import *


class Niveau:
	"""Classe permettant de créer un niveau"""
	def __init__(self, fichier):
		self.fichier = fichier
		self.structure = 0
	
	
	def generer(self):
		"""Méthode permettant de générer le niveau en fonction du fichier.
		On crée une liste générale, contenant une liste par ligne à afficher"""	
		#On ouvre le fichier
		with open(self.fichier, "r") as fichier:
			structure_niveau = []
			#On parcourt les lignes du fichier
			for ligne in fichier:
				ligne_niveau = []
				#On parcourt les sprites (lettres) contenus dans le fichier
				for sprite in ligne:
					#On ignore les "\n" de fin de ligne
					if sprite != '\n':
						#On ajoute le sprite à la liste de la ligne
						ligne_niveau.append(sprite)
				#On ajoute la ligne à la liste du niveau
				structure_niveau.append(ligne_niveau)
			#On sauvegarde cette structure
			self.structure = structure_niveau
	
	
	def afficher(self, fenetre):
		"""Méthode permettant d'afficher le niveau en fonction 
		de la liste de structure renvoyée par generer()"""
		#Chargement des images 
		mur = pygame.image.load(image_mur).convert()
		arrivee = pygame.image.load(image_arrivee).convert_alpha()

		#On parcourt la liste du niveau
		num_ligne = 0
		for ligne in self.structure:
			#On parcourt les listes de lignes
			num_case = 0
			for sprite in ligne:
				#On calcule la position réelle en pixels
				x = num_case * taille_sprite
				y = num_ligne * taille_sprite
				if sprite == 'm':		   #m = Mur
					fenetre.blit(mur, (x,y))
				elif sprite == 'd':		   #d = Départ
					fenetre.blit(depart, (x,y))
				elif sprite == 'a':		   #a = Arrivée
					fenetre.blit(arrivee, (x,y))
				num_case += 1
			num_ligne += 1
			
			
			
			
class MacGyver:
	"""Classe permettant de créer le personnage MacGyver"""
	def __init__(self, droite, gauche):
		#Sprites du personnage
		self.droite = pygame.image.load(mg_droite).convert_alpha()
		self.gauche = pygame.image.load(mg_gauche).convert_alpha()
		#Position du personnage en cases et en pixels
		self.case_x = 0
		self.case_y = 5
		self.x = 0
		self.y = 0
		#Direction par défaut
		self.direction = self.droite
		#Niveau dans lequel le personnage se trouve 
		self.niveau = niveau
		
	
	
	def deplacer(self, direction):
		"""Methode permettant de déplacer le personnage"""
		
		#Déplacement vers la droite
		if direction == 'droite':
			#Pour ne pas dépasser l'écran
			if self.case_x < (nombre_sprite_cote - 1):
				#On vérifie que la case de destination n'est pas un mur
				if self.niveau.structure[self.case_y][self.case_x+1] != 'm':
					#Déplacement d'une case
					self.case_x += 1
					#Calcul de la position "réelle" en pixel
					self.x = self.case_x * taille_sprite
			#Image dans la bonne direction
			self.direction = self.droite
		
		#Déplacement vers la gauche
		if direction == 'gauche':
			if self.case_x > 0:
				if self.niveau.structure[self.case_y][self.case_x-1] != 'm':
					self.case_x -= 1
					self.x = self.case_x * taille_sprite
			self.direction = self.gauche
		
		#Déplacement vers le haut
		if direction == 'haut':
			if self.case_y > 0:
				if self.niveau.structure[self.case_y-1][self.case_x] != 'm':
					self.case_y -= 1
					self.y = self.case_y * taille_sprite
		
		#Déplacement vers le bas
		if direction == 'bas':
			if self.case_y < (nombre_sprite_cote - 1):
				if self.niveau.structure[self.case_y+1][self.case_x] != 'm':
					self.case_y += 1
					self.y = self.case_y * taille_sprite




class Gardien:
	"""Classe permettant de créer le personnage Gardien"""
	def __init__(self, fixe):
		#Image fixe du gardien
		self.fixe = pygame.image.load(image_gardien).convert_alpha()
		#Position du personnage en cases et en pixels
		self.case_x = 13
		self.case_y = 5
		self.x = 0
		self.y = 0
		#Niveau dans lequel le personnage se trouve 
		self.niveau = niveau




class Aiguille:
	"""Classe permettant de créer l'objet Aiguille"""
	def __init__(self, fixe ):
		#Image fixe de l'objet
		self.fixe = pygame.image.load(image_aiguille).convert_alpha()
		#calcul de la position de l'objet
		for self.x_aleatoire in random.randint(1, 12)
			#On vérifie que la case de destination n'est pas un mur ou autres
			if self.niveau.structure[self.case_y][self.case_x] != 'm, d, g, a, tube.case_x, ether.case_x':
			#Affichage sur la case
			elif self.case_x = 0
				 self.case_y = 0
		#Calcul de la position en pixel
		self.x = 0
		self.y = 0
		for self.y_aleatoire in random.randint(0, 10)
			#On vérifie que la case de destination n'est pas un mur ou autres
			if self.niveau.structure[self.case_y][self.case_x] != 'm, d, g, a, tube.case_y, ether.case_y':
			#Affichage sur la case
			elif self.case_x = 0
				 self.case_y = 0
		#Calcul de la position en pixel
		self.x = 0
		self.y = 0
		#Niveau dans lequel l'objet se trouve 
		self.niveau = niveau




class Tube:
	"""Classe permettant de créer l'objet Tube"""
	def __init__(self, fixe):
		#Image fixe de l'objet
		self.fixe = pygame.image.load(image_tube).convert_alpha()
		#calcul de la position de l'objet
		for self.x_aleatoire in random.randint(1, 12)
			#On vérifie que la case de destination n'est pas un mur ou autres
			if self.niveau.structure[self.case_y][self.case_x] != 'm, d, g, a, aiguille.case_x, ether.case_x':
			#Affichage sur la case
			elif self.case_x = 0
				 self.case_y = 0
		#Calcul de la position en pixel
		self.x = 0
		self.y = 0
		for self.y_aleatoire in random.randint(0, 10)
			#On vérifie que la case de destination n'est pas un mur ou autres
			if self.niveau.structure[self.case_y][self.case_x] != 'm, d, g, a, aiguille.case_y, ether.case_y':
			#Affichage sur la case
			elif self.case_x = 0
				 self.case_y = 0
		#Calcul de la position en pixel
		self.x = 0
		self.y = 0
		#Niveau dans lequel l'objet se trouve 
		self.niveau = niveau




class Ether:
	"""Classe permettant de créer l'objet Ether"""
	def __init__(self, fixe):
		#Image fixe de l'objet
		self.fixe = pygame.image.load(image_ether).convert_alpha()
		#calcul de la position de l'objet
		for self.x_aleatoire in random.randint(1, 12)
			#On vérifie que la case de destination n'est pas un mur ou autres
			if self.niveau.structure[self.case_y][self.case_x] != 'm, d, g, a, aiguille.case_x, tube.case_x':
			#Affichage sur la case
			elif self.case_x = 0
				 self.case_y = 0
		#Calcul de la position en pixel
		self.x = 0
		self.y = 0
		for self.y_aleatoire in random.randint(0, 10)
			#On vérifie que la case de destination n'est pas un mur ou autres
			if self.niveau.structure[self.case_y][self.case_x] != 'm, d, g, a, aiguille.case_y, tube.case_y':
			#Affichage sur la case
			elif self.case_x = 0
				 self.case_y = 0
		#Calcul de la position en pixel
		self.x = 0
		self.y = 0
		#Niveau dans lequel l'objet se trouve 
		self.niveau = niveau




class Seringue:
	"""Classe permettant de créer l'objet Seringue"""
	def __init__(self, fixe):
		#Image fixe de l'objet
		self.fixe = pygame.image.load(image_seringue).convert_alpha()
		#Niveau dans lequel l'objet se trouve 
		self.niveau = niveau

	def generer(self, inventaire):
		"""Méthode permettant de générer l'objet quand les 3 éléments sont réunis"""
		
		if inventaire{} == 'aiguille, tube, ether'
			print("Vous créez l'objet seringue")



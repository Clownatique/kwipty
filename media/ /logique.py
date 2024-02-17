import random
from math import sqrt
#import sympy

class Point:
    def __init__(self, name = 'A', randomCoo = True, x=None, y=None, z=None):
        self.nom = name
        if randomCoo:
            self.x = random.randint(-5,5)
            self.y = random.randint(-5,5)
            self.z = random.randint(-5,5)
            
        else:
            self.x = x
            self.y = y
            self.z = z
    
    def __str__(self, latex=False):
        if latex:
            return f'''{self.nom} \begin{pmatrix} 1 \\ 2 \\ 3 \end{pmatrix} '''
        else:
            return f''' {self.nom} de coordonnées ({self.x},{self.y},{self.z})'''
        
    def longueur(self,Point) -> int:
        return sqrt((Point.x - self.x) ** 2 + (Point.y - self.y) ** 2 + (Point.z - self.z) ** 2) 
    
    def alignees(self,Point,Point2) -> bool :
        vecteur1 = Vecteur(self, Point)
        vecteur2 = Vecteur(self, Point2)
        return vecteur.colineaire(vecteur2)
    
    def coplanaire(self, Point, Point2):
        pass
    
    def intersection(self):
        pass

class Vecteur:
    def __init__(self, nom_vecteur = 'AB', randomVecteur=False, x=None, y=None, z=None, PointB=None, PointA=None):
        '''Définis un vecteur:
                On peut définir un vecteur
                -avec ces coordonées //ALEATOIRE OU NON
                -ou bien deux points //ALEATOIRE OU NON
        '''
        if randomVecteur:
            self.x = random.randint(-5,5)
            self.y = random.randint(-5,5)
            self.z = random.randint(-5,5) 
        if x is not None and y is not None and z is not None:
            self.x = x
            self.y = y
            self.z = z
            self.name = nom_vecteur
        if PointB is not None and PointA is not None:
            self.x= PointB.x - PointA.x
            self.y= PointB.y - PointA.y
            self.z= PointB.z - PointA.z
            self.name = PointA.nom + PointB.nom
            
    def orthogonal(self, Vecteur) -> bool:
        if self.produit_scalaire(Vecteur):
            return True
        else:
            return False
            
    def chasles(self, Vecteur):
        pass
        
    def produit_scalaire(self, Vecteur) -> int:
        return self.x * Vecteur.x + self.y* Vecteur.y + self.z * Vecteur.z
    
    def colineaire(self, Vecteur) -> bool:       
        if self.x / Vecteur.x != self.y / Vecteur.y or self.y / Vecteur.y != self.z / Vecteur.z:
            return False
        else:
            return True
    
    def coplanaire(self):
        pass
        
class Droite:
    def __init__(self, Point1 = None, Point2= None, Vecteur= None):
        self.point1 = Point1
        self.point2 = Point2
        self.vecteur_directeur = Vecteur
        t = symbols("t")
        x, y, z = symbols("x y z")
        x = self.point1.x + self.vecteur_directeur.x * t
        y = self.point1.y + self.vecteur_directeur.y * t
        z = self.point1.z + self.vecteur_directeur.z * t
        self.equation_parametrique = f"x(t) = {x}\ny(t) = {y} \nz(t) = {z}"
    
    def equation_parametrique(self):
        return self.equation_parametrique
    
    def intersection_plan(self,Plan) -> bool:
        solve(self.equation_parametrique, Plan.equation_cartesienne)
        
    def intersection_droite(self,Droite) -> Point:
        pass
        
    def position_relative(self, Droite, Plan)-> str:
        pass

class Plan:
    
    def __init__(self, plane_name, Point1=None, Point2=None, Point3=None, VecteurNormale=None):
        ''' Initializes a plane with the name 'plane_name'.
            Can be defined by:
                - 3 points given by the user with no vector
                - 1 point given by the user and 1 vector given by the user
                - 3 random points
                - 1 random vector and 1 random point
        '''
        self.name = plane_name
        self.vecteur_normale = []     #Il peut en avoir une infinité
        self.points = []              #Il peut en avoir une infinité
        self.equation_cartesienne = []#Il peut en avoir une infinité
        if random == True:
            # If no points are provided, generate 3 random points
            self.troispoints = [Point('A', randomCoo=True), Point('B', randomCoo=True), Point('C', randomCoo=True)]
        elif Point1 is not None and Point2 is not None and Point3 is not None:
            self.troispoints = [Point1, Point2, Point3]
            #Vecteur(PointA = Point1,PointB = Point2) ## génère un vecteur du plan
            #TODO : un moyen de trouver un autre vecteur dont le produit scalaire avec celui au dessus est nul
            #self.vecteur_normale = Vecteur
            

        elif any(point is not None for point in [Point1, Point2, Point3]) and VecteurNormale is not None:
            # If user provides 1 point and 1 normal vector, define the plane
            provided_point = next((point for point in [Point1, Point2, Point3] if point is not None), None)
            self.troispoints = [provided_point, Point('B', randomCoo=True), Point('C', randomCoo=True)]
            self.vecteur_normale.append(VecteurNormale)
        else:
            print('Invalid parameters')
    
    def __str__(self):
        reponse = f'{self.name} est un plan définis par les points:\n'
        for point in self.troispoints:
            reponse += f' {point}\n'
        
        VecteurNormale = self.vecteur_normale
        reponse+= f'et par le vecteur {self.vecteur_normale.name} normale de coordonées {self.vecteur_normale.x, self.vecteur_normale.y, self.vecteur_normale.z} '
        return reponse
    
    def verifier_si_point_in_plan(self, Point) -> bool:
        x, y, z, d = symbols("x y z d")
        equation_modifiee = solve(self.equation_cartesienne, d)[0]
        return equation_modifiee
    
    def verifier_vecteur_normal(self,Vecteur) -> bool:
        if Vecteur.produit_scalaire(self.vecteur_normale) == 0 :
            return True
        else:
            return False
    
    def calculer_equation_cartesienne(self, VecteurNormale : Vecteur, Point : Point): # Réfléchir sur la verbosité des fonctions : 
        x, y, z, d = symbols("x y z d")#donner le raisonnement pour la réponse ou pas
        if VecteurNormale is None or VecteurNormale.produit_scalaire(VecteurNormale, Vecteur(nom="cache",x = Point.x, y = Point.y, z = Point.z)) != 0:
            assert(f'''Le vecteur fourni n'est pas vecteur au plan {self.name}''')

        if Vecteur is None:
            assert("Pas de vecteur normal donnée.")
        elif Vecteur is not None and Point is None:
            equa = f'''{Vecteur.x}*x + {Vecteur.y} * y + {Vecteur.z} * z +  d'''
            return equa.solve()
        elif Vecteur is not None and Point is not None:
            x, y, z, d = symbols("x y z d")
        else:
            return "test"
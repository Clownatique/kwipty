from logique.logique import Point, Vecteur, Plan

def technique1_chapitre6():
    xml = []
    c = Point(name = 'C')
    n = Vecteur(nom_vecteur = 'n', randomVecteur=True)
    p = Plan('p', Point1 = c, VecteurNormale = n)
    question1 = f'''On considère le plan P qui passe par le point C{(c.x, c.y, c.z)} et dont le vecteur n{(n.x, n.y, n.z)} est un vecteur normal. Déterminer une equation cartésienne de ce plan.'''
    xml.append(question1)
    correction1 = f'''D’après le cours, n{(n.x, n.y, n.z)} est un vecteur normal, donc P admet une equation cartésienne de la forme , ou d est un réel.
                      De plus C(3; −2; 5) appartient à P, donc les coordonnées du point C vérifient l’´equation ci-dessus.
                      Cela donne −5 × 3 + 3 × (−2) + 5 + d = 0 ⇔ −16 + d = 0 ⇔ d = 16.
                      Donc, une équation cart´esienne de P est −5x + 3y + z + 16 = 0.
                      {p.calculer_equation_cartesienne(n,c)}'''
    xml.append(correction1)
    return str(xml)
    
print(technique1_chapitre6())

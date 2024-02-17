from logique import Point, Vecteur, Plan

def technique1_chapitre6():
    xml = []
    c = Point(name = 'C')
    n = Vecteur(nom_vecteur = 'n', randomVecteur=True)
    p = Plan('p', Point1 = c, VecteurNormale = n)
    question1 = f'''On considère le plan P qui passe par le point C{(c.x, c.y, c.z)} et dont le vecteur n{(n.x, n.y, n.z)} est un vecteur normal. Déterminer une equation cartésienne de ce plan.'''
    xml.append(question1)
    correction1 = f'''D’apr`es le cours, n{(n.x, n.y, n.z)} est un vecteur normal, donc P admet une equation cart´esienne de la forme , o`u d est un r´eel.
De plus C(3; −2; 5) appartient `a P, donc les coordonn´ees du point C v´erifient l’´equation ci-dessus.
Cela donne −5 × 3 + 3 × (−2) + 5 + d = 0 ⇔ −16 + d = 0 ⇔ d = 16.
Donc, une ´equation cart´esienne de P est −5x + 3y + z + 16 = 0.'''
    
    xml.append(p.equation_cartesienne(n,c))
    return xml 
    
print(technique1_chapitre6())
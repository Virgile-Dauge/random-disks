# Dépendances

# [[file:readme.org::*Dépendances][Dépendances:1]]
import cairo
import argparse
import uuid

from typing import List, Tuple
from random import randint
from math import pi, sqrt
# Dépendances:1 ends here

# Générer une liste de disques


# [[file:readme.org::*Générer une liste de disques][Générer une liste de disques:1]]
def intersection(a: Tuple[int, int], b: Tuple[int, int], r: float) -> bool:
    (xa, ya), (xb, yb) = a, b
    return sqrt((xa - xb)**2 + (ya - yb)**2) <= 2 * r

def random_disks(c: int, n: int, r: float) -> List[Tuple[int, int]]:
    a, b = 0 + round(r), round(c - r)
    l: List[Tuple[int, int]] = []
    while len(l) < n:
        t = (randint(a, b), randint(a, b))

        if any([intersection(t, o, r) for o in l]):
            continue

        l += [t]
    return l
# Générer une liste de disques:1 ends here

# Génération d'un nom de fichier

# [[file:readme.org::*Génération d'un nom de fichier][Génération d'un nom de fichier:1]]
def filenamer(p: int, d: float, n: int, ext: str='svg') -> str:
    return f"disks_p{p}_n{n}_d{d}_{str(uuid.uuid4().hex)}.{ext}"
# Génération d'un nom de fichier:1 ends here

# Parser les options

# [[file:readme.org::*Parser les options][Parser les options:1]]
def options() -> Tuple[int, int, int, int]:
    parser = argparse.ArgumentParser()
    parser.add_argument('--t', '-tirages', type=int, default=1,
                        help="Combien d'images faut-il générer ?")
    parser.add_argument('--p', '-pixels', type=int, required=True,
                        help="La taille d'un coté de l'image en pixels")
    parser.add_argument('--d', '-diametre', type=int, required=True,
                        help="Le diamètre en pixels des disques")
    parser.add_argument('--n', '-disques', type=int, required=True,
                        help="Combien de disques faut il générer par image ?")
    args = parser.parse_args()
    return args.t, args.p, args.d, args.n
# Parser les options:1 ends here

# Fonction principale

# [[file:readme.org::*Fonction principale][Fonction principale:1]]
def main():
    t, p, d, n = options()

    for _ in range(t):
        with cairo.SVGSurface(filenamer(p, d, n), p, p) as surface:
            l = random_disks(p, n, d/2)

            cr = cairo.Context(surface)
            for (x, y) in l:
                cr.arc(x, y, d/2, 0, 2 * pi)
                cr.fill()
            ...
# Fonction principale:1 ends here

# [[file:readme.org::*Fonction principale][Fonction principale:2]]
if __name__=='__main__':
    main()
# Fonction principale:2 ends here

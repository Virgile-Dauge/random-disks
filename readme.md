- [Description du projet](#org7f5273e)
- [Prototype](#org85736f8)
  - [Dessiner un disque](#orgfae34f2)
  - [Générer une liste de disques](#orgd89b2ef)
  - [Dessiner la liste des disques](#orgb4890e9)


<a id="org7f5273e"></a>

# Description du projet

On veut générer une image carrée de coté **c**, contenant **n** disques de même diamètre **d** (ou un rayon **r**), diposés aléatoirement dans l'espace libre. Les disques ne doivent pas avoir d'intersection commune.

Idée d'algo :

-   **Initialisation:** Générer un espace vide de ****c**** par ****c**** pixels
-   **Remplissage:** Tirer pour chaque axe *x* et *y* une valeur aléatoire entre $0 + r$ et $c - r$. Tester une possible intersection avec chacun des autres disques, recommencer si intersection.


<a id="org85736f8"></a>

# Prototype

```python
import cairo
from IPython.display import Image, display

from math import pi
from io import BytesIO

def disp(draw_func):
    c, n, r = 1000, 20, 50
    surface = cairo.ImageSurface(cairo.FORMAT_ARGB32, c, c)
    ctx = cairo.Context(surface)
    draw_func(ctx, c, n, r)
    with BytesIO() as fileobj:
	surface.write_to_png(fileobj)
	display(Image(fileobj.getvalue(), width=c))
```


<a id="orgfae34f2"></a>

## Dessiner un disque

```python
def circle_path(cr: cairo.Context, x: int, y: int, r: float) -> cairo.Context:
    # draw cricle
    cr.arc(x, y, r, 0, 2 * pi)
    cr.close_path()
    return cr
```

```python
@disp
def draw(cr: cairo.Context, c: int, n: int, r: float) -> None:
    cr.scale(c, c)
    cr = circle_path(cr, x=0.5, y=0.5, r=0.5)
    cr.fill()
```


<a id="orgd89b2ef"></a>

## Générer une liste de disques

```python
from typing import List, Tuple
from random import randint
from math import pi, sqrt

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
```


<a id="orgb4890e9"></a>

## Dessiner la liste des disques

```python
@disp
def draw(cr: cairo.Context, c: int, n: int, r: float) -> None:
    l = random_disks(c, n, r)

    for (x, y) in l:
	cr.arc(x, y, r, 0, 2 * pi)
	cr.fill()
```
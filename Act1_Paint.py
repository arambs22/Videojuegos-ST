"""Paint, for drawing shapes.

Exercises

1. Add a color.
2. Complete circle.
3. Complete rectangle.
4. Complete triangle.
5. Add width parameter.
"""

import turtle

from turtle import *

from freegames import vector

# Dibuja una línea entre dos puntos.
def line(start, end):
    """Draw line from start to end."""
    up()
    goto(start.x, start.y)
    down()
    goto(end.x, end.y)

# Dibuja un cuadrado.
def square(start, end):
    """Draw square from start to end."""
    up()
    goto(start.x, start.y)
    down()
    begin_fill()

    for count in range(4):
        forward(end.x - start.x)
        left(90)

    end_fill()

# Dibuja un círculo.
def circle(start, end):
    """Draw circle from start to end."""
    up()
    goto(start.x, start.y)
    down()
    begin_fill()

    # Calculate the radius as the distance between the start and end points
    radius = ((end.x - start.x) ** 2 + (end.y - start.y) ** 2) ** 0.5

    # Draw the circle using the calculated radius
    turtle.circle(radius)

    end_fill()

# Dibuja un rectángulo.
def rectangle(start, end):
    """Draw rectangle from start to end."""
    up()
    goto(start.x, start.y)
    down()
    begin_fill()

    for count in range(2):
        forward(end.x - start.x)
        left(90)
        forward(end.y - start.y)
        left(90)

    end_fill()

# Dibuja un triángulo.
def triangle(start, end):
    """Draw triangle from start to end."""
    up()
    goto(start.x, start.y)
    down()
    begin_fill()

    for count in range(3):
        forward(end.x - start.x)
        left(120)

    end_fill()

# Maneja los clics para almacenar el punto de inicio o dibujar la forma.
def tap(x, y):
    """Store starting point or draw shape."""
    start = state['start']

    if start is None:
        state['start'] = vector(x, y)
    else:
        shape = state['shape']
        end = vector(x, y)
        shape(start, end)
        state['start'] = None

# Almacena un valor en el estado.
def store(key, value):
    """Store value in state at key."""
    state[key] = value

# Estado inicial y configuración de la ventana.
state = {'start': None, 'shape': line}
setup(420, 420, 370, 0)
onscreenclick(tap) # Asocia la función tap a los clics del ratón.
listen()# Comienza a escuchar eventos de teclado.

# Configura las teclas para cambiar colores y formas.
onkey(undo, 'u')
onkey(lambda: color('black'), 'K')
onkey(lambda: color('white'), 'W')
onkey(lambda: color('green'), 'G')
onkey(lambda: color('blue'), 'B')
onkey(lambda: color('red'), 'R')
onkey(lambda: color('orange'), 'O')
onkey(lambda: store('shape', line), 'l')
onkey(lambda: store('shape', square), 's')
onkey(lambda: store('shape', circle), 'c')
onkey(lambda: store('shape', rectangle), 'r')
onkey(lambda: store('shape', triangle), 't')

done() # Finaliza y muestra la ventana gráfica.
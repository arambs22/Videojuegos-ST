"""Cannon, hitting targets with projectiles.

Exercises

1. Keep score by counting target hits.
2. Vary the effect of gravity.
3. Apply gravity to the targets.
4. Change the speed of the ball.
"""

from random import randrange
from turtle import *
from freegames import vector

# Inicializa la posición de la bola y su velocidad
ball = vector(-200, -200)
speed = vector(0, 0)
targets = []


def tap(x, y):
    """Respond to screen tap."""
    if not inside(ball):
        # Resetea la bola en la posición inicial y establece su velocidad
        ball.x = -199
        ball.y = -199
        speed.x = (x + 350) / 25
        speed.y = (y + 350) / 25


def inside(xy):
    """Return True if xy within screen."""
    return -200 < xy.x < 200 and -200 < xy.y < 200


def draw():
    """Draw ball and targets."""
    clear()

    for target in targets:
        # Dibuja cada target en su posición
        goto(target.x, target.y)
        dot(20, 'blue')
    
    if inside(ball):
        # Dibuja cada target en su posición
        goto(ball.x, ball.y)
        dot(6, 'red')

    update()


def move():
    """Move ball and targets."""
    if randrange(40) == 0:
         # Genera un nuevo target de forma aleatoria
        y = randrange(-150, 150)
        target = vector(200, y)
        targets.append(target)

    for target in targets:
        # Mueve los targets hacia la izquierda
        target.x -= 0.5

        if target.x < -200:
            # Reposiciona el target al lado derecho de la pantalla
            target.x = 200
            target.y = randrange(-150, 150)  # Nueva posición Y aleatoria

    if inside(ball):
        speed.y -= 0.35
        ball.move(speed)

    dupe = targets.copy()
    targets.clear()

    for target in dupe:
        # Mantiene solo los targets que están lo suficientemente lejos de la bola
        if abs(target - ball) > 13:
            targets.append(target)

    draw()

    ontimer(move, 15)

# Configuración inicial del juego
setup(420, 420, 370, 0)
hideturtle()
up()
tracer(False)
onscreenclick(tap)
move()
done()
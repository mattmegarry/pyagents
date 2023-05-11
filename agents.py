import random
import math
from js import window, document, setInterval  # type: ignore
from pyodide.ffi import create_proxy  # type: ignore

CANVAS_HEIGHT = window.canvasAttributes.height
CANVAS_WIDTH = window.canvasAttributes.width
N = 100
agents = []


def update_rotation(current_rotation, degrees):
    new_rotation = (current_rotation + degrees) % 360
    if new_rotation < 0:
        new_rotation += 360
    return new_rotation


class Agent:
    def __init__(self):
        self.x = random.randint(0, CANVAS_WIDTH)
        self.y = random.randint(0, CANVAS_HEIGHT)
        self.rotation = random.randint(0, 360)

    def draw_body(self, ctx):
        ctx.beginPath()
        ctx.arc(self.x, self.y, 3, 0, 2 * math.pi)
        ctx.stroke()

    def update(self):
        self.rotation = update_rotation(self.rotation, random.randint(-10, 10))
        angle_rad = math.radians(self.rotation)
        delta_x = math.cos(angle_rad)
        delta_y = math.sin(angle_rad)
        self.x += delta_x
        self.y += delta_y

    def render(self, ctx):
        self.draw_body(ctx)


def update(ctx, canvas):
    ctx.clearRect(0, 0, canvas.width, canvas.height)
    for agent in agents:
        agent.update()
        agent.render(ctx)


def init():
    canvas = document.getElementById("canvas")
    ctx = canvas.getContext("2d")
    for i in range(N):
        agents.append(Agent())
    update(ctx, canvas)
    updateProxy = create_proxy(update)
    setInterval(updateProxy, 17, ctx, canvas)


init()

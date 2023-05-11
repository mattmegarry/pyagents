import random
import math
from js import window, document, setInterval  # type: ignore
from pyodide.ffi import create_proxy  # type: ignore

CANVAS_HEIGHT = window.canvasAttributes.height
CANVAS_WIDTH = window.canvasAttributes.width
N = 100
agents = []


def degToRad(degrees):
    return (degrees * math.pi) / 180


class Agent:
    def __init__(self):
        self.x = random.randint(0, CANVAS_WIDTH)
        self.y = random.randint(0, CANVAS_HEIGHT)
        self.rotation = random.randint(0, 360)

    def draw_body(self, ctx):
        ctx.beginPath()
        ctx.arc(self.x, self.y, 3, 0, 2 * math.pi)
        ctx.stroke()

    def render(self, ctx):
        self.draw_body(ctx)


def renderFrame(ctx, canvas):
    ctx.clearRect(0, 0, canvas.width, canvas.height)
    for agent in agents:
        agent.render(ctx)


def init():
    canvas = document.getElementById("canvas")
    ctx = canvas.getContext("2d")
    for i in range(N):
        agents.append(Agent())
    renderFrame(ctx, canvas)
    renderFrameProxy = create_proxy(renderFrame)
    setInterval(renderFrameProxy, 17, ctx, canvas)


init()

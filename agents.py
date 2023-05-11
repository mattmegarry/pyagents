import random
import math
from js import window, document, setInterval  # type: ignore
from pyodide.ffi import create_proxy  # type: ignore

CANVAS_HEIGHT = window.canvasAttributes.height
CANVAS_WIDTH = window.canvasAttributes.width


def degToRad(degrees):
    return (degrees * math.pi) / 180


class Agent:
    def __init__(self, ctx):
        self.x = random.randint(0, CANVAS_WIDTH)
        self.y = random.randint(0, CANVAS_HEIGHT)
        self.rotation = random.randint(0, 360)

    def draw_body(self, ctx):
        ctx.beginPath()
        ctx.arc(self.x, self.y, 3, 0, 2 * math.pi)
        ctx.stroke()

    def render(self, ctx):
        self.draw_body(ctx)


def renderFrame(ctx, canvas, agents):
    ctx.clearRect(0, 0, canvas.width, canvas.height)
    agents[0].render(ctx)


def init():
    canvas = document.getElementById("canvas")
    ctx = canvas.getContext("2d")
    agents = [Agent(ctx)]
    renderFrame(ctx, canvas, agents)
    drawThingsProxy = create_proxy(renderFrame)
    setInterval(drawThingsProxy, 17, ctx, canvas)


init()

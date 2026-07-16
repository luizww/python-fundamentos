import math
import random
import tkinter as tk

# ----------------------------------------------------
#   Simulador simples de partículas com gravidade
# ----------------------------------------------------

WIDTH, HEIGHT = 800, 600
NUM_PARTICLES = 40
G = 0.4  # intensidade da gravidade

class Particle:
    def __init__(self):
        self.x = random.uniform(100, WIDTH - 100)
        self.y = random.uniform(100, HEIGHT - 100)
        self.vx = random.uniform(-1, 1)
        self.vy = random.uniform(-1, 1)
        self.mass = random.uniform(5, 20)

    def update(self, particles):
        ax = ay = 0
        for p in particles:
            if p is self:
                continue
            dx = p.x - self.x
            dy = p.y - self.y
            dist = math.sqrt(dx*dx + dy*dy) + 0.1
            force = G * self.mass * p.mass / (dist*dist)
            ax += force * dx / dist
            ay += force * dy / dist

        self.vx += ax / self.mass
        self.vy += ay / self.mass
        self.x += self.vx
        self.y += self.vy

        # limites da tela
        if self.x < 0 or self.x > WIDTH:
            self.vx *= -1
        if self.y < 0 or self.y > HEIGHT:
            self.vy *= -1

def draw():
    canvas.delete("all")
    for p in particles:
        canvas.create_oval(
            p.x - 3, p.y - 3, p.x + 3, p.y + 3,
            fill="white"
        )
    root.after(16, update)

def update():
    for p in particles:
        p.update(particles)
    draw()

root = tk.Tk()
root.title("Simulação Gravitacional")
canvas = tk.Canvas(root, width=WIDTH, height=HEIGHT, bg="black")
canvas.pack()

particles = [Particle() for _ in range(NUM_PARTICLES)]
draw()
root.mainloop()

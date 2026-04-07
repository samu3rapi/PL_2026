import pygame as p

p.init()
screen = p.display.set_mode((1000, 700))



SKY = (85, 85, 85)
GROUND = (0, 0, 0)
CLOUD = (55, 55, 55)
HOUSE_BASE = (58, 48, 15)
WINDOW_OFF = (40, 20, 10)
WINDOW_ON = (215, 175, 0)
GHOST_BODY = (180, 180, 180)
GHOST_EYE = (135, 206, 235)


def draw_house(x, y, scale=1.0, light_on=False):

    w, h = 250 * scale, 130 * scale
    p.draw.rect(screen, HOUSE_BASE, (x, y, w, h))

    p.draw.rect(screen, (30, 30, 30), (x - 10 * scale, y, w + 20 * scale, 20 * scale))
    p.draw.rect(screen, (30, 30, 30), (x - 10 * scale, y + 45 * scale, w + 20 * scale, 15 * scale))

    for i in range(5):
        p.draw.rect(screen, (45, 40, 25),
                         (x + 15 * scale + i * 45 * scale, y + 10 * scale, 30 * scale, 35 * scale))

    p.draw.rect(screen, WINDOW_OFF, (x + 20 * scale, y + 75 * scale, 40 * scale, 30 * scale))
    p.draw.rect(screen, WINDOW_OFF, (x + 80 * scale, y + 75 * scale, 40 * scale, 30 * scale))
    p.draw.rect(screen, WINDOW_ON if light_on else WINDOW_OFF,
                     (x + 140 * scale, y + 75 * scale, 40 * scale, 30 * scale))


def draw_ghost(x, y, scale=1.0):
    """Функция отрисовки привидения"""
    points = [
        (x, y), (x + 40 * scale, y - 20 * scale), (x + 100 * scale, y - 30 * scale),
        (x + 180 * scale, y + 10 * scale), (x + 140 * scale, y + 50 * scale), (x + 40 * scale, y + 40 * scale)
    ]
    p.draw.polygon(screen, GHOST_BODY, points)
    # Глаза
    p.draw.ellipse(screen, GHOST_EYE, (x + 60 * scale, y - 10 * scale, 18 * scale, 10 * scale))
    p.draw.ellipse(screen, GHOST_EYE, (x + 90 * scale, y - 5 * scale, 18 * scale, 10 * scale))


running = True
while running:
    for event in p.event.get():
        if event.type == p.QUIT:
            running = False

    screen.fill(SKY)


    p.draw.circle(screen, (240, 240, 240), (880, 80), 55)
    clouds = [(500, 40, 600), (0, 100, 800), (450, 200, 700), (200, 450, 900)]
    for cx, cy, cw in clouds:
        p.draw.ellipse(screen, CLOUD, (cx, cy, cw, 50))


    p.draw.rect(screen, GROUND, (0, 400, 1000, 300))


    draw_house(680, 280, scale=1, light_on=True)
    draw_house(330, 350, scale=1, light_on=True)
    draw_house(20, 460, scale=1, light_on=True)


    draw_ghost(800, 580, 0.6)
    draw_ghost(830, 630, 0.7)
    draw_ghost(650, 640, 1.4)
    draw_ghost(560, 650, 0.6)

    draw_ghost(100, 650, 0.7)
    draw_ghost(130, 600, 0.8)

    p.display.flip()

p.quit()

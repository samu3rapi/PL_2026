import pygame as p


p.init()
screen = p.display.set_mode((800, 600))



SKY_GRAY = (80, 80, 80)
GROUND_BLACK = (0, 0, 0)
HOUSE_BROWN = (60, 45, 10)
WINDOW_DARK = (40, 20, 10)
WINDOW_LIGHT = (210, 170, 0)
GHOST_WHITE = (200, 200, 200)
ROOF_BLACK = (30, 30, 30)
CLOUD_GRAY = (60, 60, 60)

running = True
while running:
    for event in p.event.get():
        if event.type == p.QUIT:
            running = False


    screen.fill(SKY_GRAY)
    p.draw.rect(screen, GROUND_BLACK, (0, 300, 800, 300))


    p.draw.circle(screen, (240, 240, 240), (700, 80), 40)
    p.draw.ellipse(screen, CLOUD_GRAY, (150, 100, 600, 40))
    p.draw.ellipse(screen, CLOUD_GRAY, (450, 200, 500, 50))


    p.draw.rect(screen, HOUSE_BROWN, (160, 200, 350, 400))


    p.draw.rect(screen, ROOF_BLACK, (130, 200, 410, 30))
    p.draw.rect(screen, ROOF_BLACK, (130, 350, 410, 50))

    for i in range(5):
        p.draw.rect(screen, (40, 35, 20), (180 + i * 70, 230, 40, 120))


    p.draw.rect(screen, WINDOW_DARK, (200, 450, 70, 70))
    p.draw.rect(screen, WINDOW_DARK, (300, 450, 70, 70))
    p.draw.rect(screen, WINDOW_LIGHT, (400, 450, 70, 70))

    # 6. Привидение (рисуем через многоугольник для формы «простыни»)
    ghost_eyes = [(550, 550), (600, 510), (650, 500), (720, 520), (830, 580), (650, 620)]
    p.draw.polygon(screen, GHOST_WHITE, ghost_eyes)
    # Глаза привидения
    p.draw.ellipse(screen, (150, 180, 220), (605, 520, 15, 10))
    p.draw.ellipse(screen, (150, 180, 220), (630, 525, 15, 10))

    p.display.flip()

p.quit()

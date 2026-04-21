import pygame as p

def init_game(width, height):
    p.init()
    screen = p.display.set_mode((width, height))
    return screen

def draw_background(screen, sky_color, ground_color, ground_y):
    """Рисует небо и землю"""
    screen.fill(sky_color)
    p.draw.rect(screen, ground_color, (0, ground_y, screen.get_width(), screen.get_height() - ground_y))

def draw_moon(screen, color, x, y, radius):
    """Рисует луну"""
    p.draw.circle(screen, color, (x, y), radius)

def draw_cloud(screen, color, x, y, width, height):
    """Рисует одно облако в виде эллипса"""
    p.draw.ellipse(screen, color, (x, y, width, height))

def draw_clouds(screen, color, clouds):
    """Рисует несколько облаков из списка (x, y, width, height)"""
    for (x, y, w, h) in clouds:
        draw_cloud(screen, color, x, y, w, h)

def draw_house(screen, house_color, x, y, width, height):
    """Рисует основную часть дома"""
    p.draw.rect(screen, house_color, (x, y, width, height))

def draw_roof_section(screen, roof_color, x, y, width, height):
    """Рисует одну секцию крыши"""
    p.draw.rect(screen, roof_color, (x, y, width, height))

def draw_roof(screen, roof_color, sections):
    """Рисует крышу из нескольких секций"""
    for (x, y, w, h) in sections:
        draw_roof_section(screen, roof_color, x, y, w, h)

def draw_vertical_segments(screen, color, x_start, y, width, height, count, spacing):
    """Рисует вертикальные полосы (секции стены)"""
    for i in range(count):
        p.draw.rect(screen, color, (x_start + i * spacing, y, width, height))

def draw_window(screen, dark_color, light_color, x, y, size):
    """Рисует одно окно (тёмный квадрат со светлым окном внутри)"""
    p.draw.rect(screen, dark_color, (x, y, size, size))
    p.draw.rect(screen, light_color, (x + 10, y + 10, size - 20, size - 20))

def draw_windows(screen, dark_color, light_color, windows):
    """Рисует несколько окон из списка (x, y, size)"""
    for (x, y, size) in windows:
        draw_window(screen, dark_color, light_color, x, y, size)

def draw_ghost(screen, ghost_color, points, eye1, eye2):
    """Рисует приведение по точкам многоугольника и глаза"""
    p.draw.polygon(screen, ghost_color, points)
    (ex1, ey1, ew1, eh1) = eye1
    (ex2, ey2, ew2, eh2) = eye2
    p.draw.ellipse(screen, (150, 180, 220), (ex1, ey1, ew1, eh1))
    p.draw.ellipse(screen, (150, 180, 220), (ex2, ey2, ew2, eh2))

def finish_game():
    p.display.flip()
    running = True
    while running:
        for event in p.event.get():
            if event.type == p.QUIT:
                running = False
    p.quit()

# ==================== ОСНОВНАЯ ПРОГРАММА ====================

screen = init_game(800, 600)

# Цвета
SKY_GRAY = (80, 80, 80)
GROUND_BLACK = (0, 0, 0)
HOUSE_BROWN = (60, 45, 10)
WINDOW_DARK = (40, 20, 10)
WINDOW_LIGHT = (210, 170, 0)
GHOST_WHITE = (200, 200, 200)
ROOF_BLACK = (30, 30, 30)
CLOUD_GRAY = (60, 60, 60)
MOON_COLOR = (240, 240, 240)

# 1. Фон
draw_background(screen, SKY_GRAY, GROUND_BLACK, 300)

# 2. Луна
draw_moon(screen, MOON_COLOR, 700, 80, 40)

# 3. Облака
clouds = [
    (150, 100, 600, 40),
    (450, 200, 500, 50)
]
draw_clouds(screen, CLOUD_GRAY, clouds)

# 4. Дом
draw_house(screen, HOUSE_BROWN, 160, 200, 350, 400)

# 5. Крыша
roof_sections = [
    (130, 200, 410, 30),
    (130, 350, 410, 50)
]
draw_roof(screen, ROOF_BLACK, roof_sections)

# 6. Вертикальные секции
draw_vertical_segments(screen, (40, 35, 20), 180, 230, 40, 120, 5, 70)

# 7. Окна
windows = [
    (200, 450, 70),
    (300, 450, 70),
    (400, 450, 70)
]
draw_windows(screen, WINDOW_DARK, WINDOW_LIGHT, windows)

# 8. Привидение
ghost_points = [(550, 550), (600, 510), (650, 500), (720, 520), (830, 580), (650, 620)]
eye1 = (605, 520, 15, 10)
eye2 = (630, 525, 15, 10)
draw_ghost(screen, GHOST_WHITE, ghost_points, eye1, eye2)

# 9. Завершение
finish_game()
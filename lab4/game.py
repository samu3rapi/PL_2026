import pygame
from pygame.draw import *
from random import randint
import math

pygame.init()

FPS = 60
WIDTH = 1200
HEIGHT = 900
screen = pygame.display.set_mode((WIDTH, HEIGHT))

RED = (255, 0, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
GREEN = (0, 255, 0)
MAGENTA = (255, 0, 255)
CYAN = (0, 255, 255)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
COLORS = [RED, BLUE, YELLOW, GREEN, MAGENTA, CYAN]

font = pygame.font.Font(None, 36)

# Глобальные переменные
score = 0
level = 1
combo_counter = 0
no_hit_timer = 0
balls = []

class Ball:
    def __init__(self, x, y, r, vx, vy, color):
        self.x = x
        self.y = y
        self.r = r
        self.vx = vx
        self.vy = vy
        self.color = color
    
    def move(self):
        self.x += self.vx
        self.y += self.vy
        if self.x - self.r <= 0 or self.x + self.r >= WIDTH:
            self.vx = -self.vx
        if self.y - self.r <= 0 or self.y + self.r >= HEIGHT:
            self.vy = -self.vy
    
    def draw(self):
        circle(screen, self.color, (int(self.x), int(self.y)), self.r)
        circle(screen, BLACK, (int(self.x), int(self.y)), self.r, 2)
    
    def contains_point(self, pos):
        return math.hypot(pos[0] - self.x, pos[1] - self.y) <= self.r

def new_ball():
    """Создаёт новый шарик со случайными параметрами"""
    r = randint(20, 50)
    x = randint(r, WIDTH - r)
    y = randint(r, HEIGHT - r)
    vx = randint(-5, 5)
    while vx == 0:
        vx = randint(-5, 5)
    vy = randint(-5, 5)
    while vy == 0:
        vy = randint(-5, 5)
    color = COLORS[randint(0, len(COLORS) - 1)]
    return Ball(x, y, r, vx, vy, color)

def click(event):
    """Обрабатывает клик мыши"""
    global score, combo_counter, no_hit_timer, balls
    hit = False
    for ball in balls[:]:
        if ball.contains_point(event.pos):
            multiplier = get_combo_multiplier(combo_counter)
            score += 1 * multiplier
            combo_counter += 1
            no_hit_timer = 0
            hit = True
            balls.remove(ball)
            for _ in range(2):
                balls.append(new_ball())
            break
    if not hit:
        combo_counter = 0

def get_combo_multiplier(cnt):
    """Возвращает множитель очков в зависимости от комбо"""
    if cnt >= 10:
        return 10
    elif cnt >= 5:
        return 5
    elif cnt >= 3:
        return 3
    elif cnt >= 2:
        return 2
    return 1

def get_balls_count(lvl):
    """Количество шариков в зависимости от уровня"""
    return [2, 4, 6, 8, 10][lvl - 1]

def get_timer_limit(lvl):
    """Лимит времени бездействия (секунды)"""
    return max(10 - (lvl - 1) * 1.5, 3)

def draw_score():
    """Отображает счёт, уровень и комбо на экране"""
    text = font.render(f"Score: {score}", True, WHITE)
    screen.blit(text, (10, 10))
    text = font.render(f"Level: {level}", True, WHITE)
    screen.blit(text, (10, 50))
    text = font.render(f"Combo: x{get_combo_multiplier(combo_counter)}", True, WHITE)
    screen.blit(text, (10, 90))
    if combo_counter > 0:
        text = font.render(f"Combo streak: {combo_counter}", True, YELLOW)
        screen.blit(text, (10, 130))

def check_level_up():
    """Проверяет, нужно ли перейти на следующий уровень"""
    global level, score, combo_counter, no_hit_timer, balls
    required_score = level * 10
    if score >= required_score and level < 5:
        level += 1
        combo_counter = 0
        no_hit_timer = 0
        balls = []
        for _ in range(get_balls_count(level)):
            balls.append(new_ball())

def update_timer():
    """Обновляет таймер бездействия и взрывает все шары при его истечении"""
    global no_hit_timer, balls, combo_counter
    no_hit_timer += 1 / FPS
    if no_hit_timer >= get_timer_limit(level):
        balls = []
        for _ in range(get_balls_count(level)):
            balls.append(new_ball())
        no_hit_timer = 0
        combo_counter = 0

# Основная программа
clock = pygame.time.Clock()
finished = False

for _ in range(get_balls_count(level)):
    balls.append(new_ball())

while not finished:
    clock.tick(FPS)
    
    update_timer()
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True
        elif event.type == pygame.MOUSEBUTTONDOWN:
            click(event)
    
    check_level_up()
    
    for ball in balls:
        ball.move()
    
    screen.fill(BLACK)
    for ball in balls:
        ball.draw()
    draw_score()
    
    pygame.display.update()

pygame.quit()
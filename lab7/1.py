import pygame
import sys
import math
from datetime import datetime

pygame.init()

width, height = 400, 400
clock_radius = 150
center = (width // 2, height // 2)
bg_color = (255, 255, 255)
hand_color = (0, 0, 0)

screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Clock")

def draw_hand(length, angle):
    end_pos = (
        center[0] + length * math.cos(math.radians(angle - 90)),
        center[1] + length * math.sin(math.radians(angle - 90))
    )
    pygame.draw.line(screen, hand_color, center, end_pos, 5)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    screen.fill(bg_color)

    current_time = datetime.now().time()
    minutes_angle = (current_time.minute / 60) * 360
    seconds_angle = (current_time.second / 60) * 360

    draw_hand(clock_radius * 0.5, minutes_angle)
    draw_hand(clock_radius * 0.8, seconds_angle)

    pygame.display.flip()

    pygame.time.Clock().tick(60)
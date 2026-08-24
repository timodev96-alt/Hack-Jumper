import pygame

import main
def calculate_render_rect(win_w,win_h):
    current_ratio = win_w / win_h
    if current_ratio > main.TARGET_RATIO:
        render_h = win_h
        render_w = (win_w / main.TARGET_RATIO)
    else:
        render_w = win_h
        render_h = int(win_w/main.TARGET_RATIO)
    render_x = (win_w - render_w) // 2
    render_y = (win_h - render_h) // 2
    return pygame.Rect(render_x, render_y, render_w, render_h)
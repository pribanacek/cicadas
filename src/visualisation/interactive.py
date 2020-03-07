import threading
import os
os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = "hide"

import pygame as pg

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
FPS = 30
graph = None
screen_size = (640, 640)
graph_dimensions = (1, 1)

NODE_RADIUS = 5

pg.font.init()
font = pg.font.SysFont('Ubuntu', 15)
line_spacing = 15

held_node = None
mouse_pos = (0, 0)
energy_stat_surfaces = []

clock = pg.time.Clock()

def graph_to_screen_pos(pos):
    x, y = pos
    dim_x, dim_y = graph_dimensions
    size_x, size_y = screen_size
    x = (x / dim_x + 0.5) * size_x
    y = (0.5 - y / dim_y) * size_y
    return (int(round(x)), int(round(y)))

def screen_to_graph_pos(pos):
    x, y = pos
    dim_x, dim_y = graph_dimensions
    size_x, size_y = screen_size
    x = (x / size_x - 0.5) * dim_x
    y = (y / size_y - 0.5) * -dim_y
    return (x, y)

def draw_node(screen, position):
    pg.draw.circle(screen, BLACK, position, NODE_RADIUS)

def draw_edge(screen, start, end):
    pg.draw.line(screen, BLACK, start, end)

def reset_energy_stats(stats):
    global energy_stat_surfaces
    items = [('ENERGY', sum(stats.values()))] + list(stats.items())
    l = []
    for k, v in items:
        text = str(k) + ": " + str(round(v))
        surface = font.render(text, True, BLACK)
        l.append(surface)
    energy_stat_surfaces = l

def draw(screen):
    global graph, graph_dimensions, held_node, mouse_pos, energy_stat_surfaces, line_spacing
    screen.fill(WHITE)
    for i in range(len(energy_stat_surfaces)):
        screen.blit(energy_stat_surfaces[i], (5, i * line_spacing))
    if graph == None:
        return
    graph_dimensions = graph.dimensions
    positions = graph.get_positions()
    for node_id, pos in positions.items():
        screen_pos = graph_to_screen_pos(pos)
        if node_id == held_node:
            screen_pos = mouse_pos
        draw_node(screen, screen_pos)
    for start, end, _, _ in graph.edge_data:
        start_pos = graph_to_screen_pos(positions[start])
        end_pos = graph_to_screen_pos(positions[end])
        if start == held_node:
            start_pos = mouse_pos
        elif end == held_node:
            end_pos = mouse_pos
        draw_edge(screen, start_pos, end_pos)

def mouse_move(pos):
    global mouse_pos
    mouse_pos = pos

def mouse_down(pos):
    global held_node
    positions = graph.get_positions()
    for node_id, node_pos in positions.items():
        node_x, node_y = graph_to_screen_pos(node_pos)
        mouse_x, mouse_y = pos
        d2 = (node_x - mouse_x) ** 2 + (node_y - mouse_y) ** 2
        if d2 < (NODE_RADIUS * 5) ** 2:
            held_node = node_id
            break

def mouse_up(pos):
    global held_node, energy_stat_surface
    if held_node != None:
        graph_pos = screen_to_graph_pos(pos)
        graph.set_node_position(held_node, graph_pos)
        held_node = None
        reset_energy_stats(graph.energy_stats())

def run():
    pg.init()
    screen = pg.display.set_mode(screen_size)
    screen.fill(WHITE)

    while True:
        clock.tick(FPS)
        for event in pg.event.get():
            if event.type in (pg.QUIT, pg.KEYDOWN):
                return
            if event.type == pg.MOUSEBUTTONDOWN:
                mouse_down(pg.mouse.get_pos())
            if event.type == pg.MOUSEBUTTONUP:
                mouse_up(pg.mouse.get_pos())
            if event.type == pg.MOUSEMOTION:
                mouse_move(pg.mouse.get_pos())
        draw(screen)
        pg.display.update()
    pg.quit()

def start_animation_thread(g):
    global graph
    graph = g
    reset_energy_stats(graph.energy_stats())
    x = threading.Thread(target = run)
    x.start()

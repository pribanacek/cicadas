import threading
import pygame as pg

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

graphs = []
i = 0
screen_size = (640, 640)
graph_dimensions = (1, 1)

clock = pg.time.Clock()

def scale_position(pos):
    x, y = pos
    dim_x, dim_y = graph_dimensions
    size_x, size_y = screen_size
    x = (x / dim_x) * size_x + size_x / 2
    y = -(y / dim_y) * size_y + size_y / 2
    return (int(round(x)), int(round(y)))

def draw_node(screen, position):
    coords = scale_position(position)
    pg.draw.circle(screen, BLACK, coords, 5)

def draw_edge(screen, start, end):
    start = scale_position(start)
    end = scale_position(end)
    pg.draw.line(screen, BLACK, start, end)

def draw(screen):
    global i, graphs, graph_dimensions
    screen.fill(WHITE)
    if len(graphs) == 0:
        return
    graph = graphs[i]
    graph.recentre_nodes() # this is bad
    graph_dimensions = graph.dimensions
    positions = graph.get_positions()
    for _, pos in positions.items():
        draw_node(screen, pos)
    for start, end, _, _ in graph.edge_data:
        start_pos = positions[start]
        end_pos = positions[end]
        draw_edge(screen, start_pos, end_pos)
    i = (i + 1) % len(graphs)


def run():
    pg.init()
    screen = pg.display.set_mode(screen_size)
    screen.fill(WHITE)

    while True:
        clock.tick(30)
        for event in pg.event.get():
            if event.type in (pg.QUIT, pg.KEYDOWN):
                return
        draw(screen)
        pg.display.update()
    pg.quit()

def start_animation_thread(graph_array):
    global graphs
    graphs = graph_array
    x = threading.Thread(target = run)
    x.start()

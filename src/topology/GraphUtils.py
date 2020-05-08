def new_node_id(node_name, node_counts):
    uid = node_counts[node_name]
    node_counts[node_name] += 1
    return node_name + '-' + str(uid)

def add_node_instance(graph, node, node_counts, regions = None):
    node_id = new_node_id(node.node_name, node_counts)
    region_list = frozenset() if regions == None else frozenset(regions)
    graph.add_node(node_id, data = node, pos = (0, 0), regions = region_list)
    return node_id

def add_edge(graph, edge, node_counts, start = None, end = None, regions = None):
    start_node = edge.start
    end_node = edge.end
    start_node_id = start if start != None else add_node_instance(graph, start_node, node_counts, regions = regions)
    end_node_id = end if end != None else add_node_instance(graph, end_node, node_counts, regions = regions)
    graph.add_edge(start_node_id, end_node_id, edge.edgeId, data = edge)
    return (start_node_id, end_node_id)

def add_path(graph, path, node_counts, start = None, end = None, loop = False, regions = None):
    path_start_node = path[0].start
    path_end_node = path[-1].end
    path_start_id = start if start != None else add_node_instance(graph, path_start_node, node_counts, regions = regions)
    path_end_id = None
    if loop:
        path_end_id = path_start_id
    elif end != None:
        path_end_id = end
    else:
        path_end_id = add_node_instance(graph, path_end_node, node_counts, regions = regions)

    path_ids = [path_start_id]
    for i in range(len(path) - 1):
        edge_id = path[i]
        (_, edge_end_id) = add_edge(graph, edge_id, node_counts, start = path_ids[-1])
        path_ids.append(edge_end_id)
    add_edge(graph, path[-1], node_counts, start = path_ids[-1], end = path_end_id, regions = regions)
    path_ids.append(path_end_id)
    return path_ids

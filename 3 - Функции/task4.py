#!/bin/env python
'''
4. На вход функции передается строка с xml документом (тэги без аттрибутов, корневой элемент только один).
   Нужно выполнить следующее преобразование и вывести максимальную вложенность.
   Пример:
        a = '<root><element1 /><element2 /><element3><element4 /></element3></root>'
        foo(a) ->
        {
            'name': 'root',
            'children': [
                {'name': 'element1', 'children': []},
                {'name': 'element2', 'children': []},
                {
                    'name': 'element3',
                    'children': [
                        {'name': 'element4', 'children': []}
                    ]
                }
            ]
        }, 2
      в данном случае у element4 тэга вложенность/глубина 2
'''
nodes = []
parentId = 0
ck = 0
g_max = 0

def open_tag(x):
    global nodes, parentId, ck
    ck += 1
    nodes.append({'id': ck, 'parentId': parentId, 'node': x})
    parentId = ck

def getParentId(node):
    global nodes
    for i in range(len(nodes)-1, 0, -1):
        if nodes[i]['node'] == node:
            return nodes[i]['parentId']
    return 0

def close_tag(x):
    global parentId
    parentId = getParentId(x)

def make_nodes(xml):
    # 1 - ищем начало тега
    # 2 - имя тега
    stage = 1
    for char in xml:
        if stage == 2:
            if char == '>' or char == ' ':
                if tag_name[0] == '/':
                    close_tag(tag_name[1:]);
                else:
                    open_tag(tag_name);
                stage = 1
            else: tag_name += char
        if stage == 1:
            if char == '/': close_tag(tag_name)
            if char == '<': stage = 2; tag_name = ''

def get_children_ids(parentId):
    global nodes
    res = []
    for i in range(len(nodes)):
        if nodes[i]['parentId'] == parentId:
            res.append(i)
    return res

def get_by_id(id):
    global nodes
    for node in nodes:
        if node['id'] == id: return node
    return None

def make_tree(id, level=0):
    global nodes, g_max
    node = nodes[id]
    res = {'name': node['node'], 'children': []}
    if g_max < level: g_max = level
    for id in get_children_ids(node['id']):
        res['children'].append(make_tree(id, level+1))
    return res

def foo(xml):
    global g_max
    make_nodes(xml)
    return make_tree(0), g_max

print(foo('<root><element1 /><element2 /><element3><element4 /></element3></root>'))

# список всех нод
for i in nodes: print(i)

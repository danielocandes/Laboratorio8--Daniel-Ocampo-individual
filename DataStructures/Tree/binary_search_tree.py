from . import bst_node as bn
from DataStructures.List import single_linked_list as sll
from DataStructures.List import array_list as al

def new_map():
    map = {'root': None,
           'type': 'BST'}
    return map
    
def put(my_bst, key, value):
    if my_bst['root'] == None:
        my_bst['root'] = bn.new_node(key, value)
        return my_bst
    
    insert_node(my_bst['root'], key, value)
    
    return my_bst

def insert_node(root, key, value):
    
    if default_compare(key, root['key']) == -1:
        if root['left'] == None:
            root['left'] = bn.new_node(key, value)
            root['size'] += 1
        else:
            old_size = root['left']['size']
            insert = insert_node(root['left'], key, value)
            if insert['size'] > old_size:
                root['size'] += 1
    
    elif default_compare(key, root['key']) == 1:
        if root['right'] == None:
            root['right'] = bn.new_node(key, value)
            root['size'] += 1
        else:
            old_size = root['right']['size']
            insert = insert_node(root['right'], key, value)
            if insert['size'] > old_size:
                root['size'] += 1
    
    else:
        root['value'] = value
    
    return root 

def get(my_bst, key):
    return get_node(my_bst['root'], key)
    
def get_node(root, key):

    comparison = default_compare(key, bn.get_key(root))
    if comparison == 0:
        return root['value']
    elif comparison == -1:
        return get_node(root['left'], key)
    elif comparison == 1:
        return get_node(root['right'], key)
    else: 
        return None

def remove(my_bst, key):
    remove_node(my_bst['root'], key)
    return my_bst

def remove_node(root, key):
    if root == None:
        return root
    
    comparison = default_compare(key, bn.get_key(root))
    if comparison == 0:
        if root['left'] != None:
            return root['left']
        else:
            return root['right']
    
    elif comparison == -1:
        if root['left'] != None:
            old_size = root['left']['size']
            removal = removal_node_check(root, key, 'left')
            
            if old_size > removal['size']:
                root['size'] -= 1
        
        return root
        
    elif comparison == 1:
        if root['right'] != None:
            old_size = root['right']['size']
            removal = removal_node_check(root, key, 'right')
            
            if old_size > removal['size']:
                root['size'] -= 1
        
        return root
            
def removal_node_check(root, key, direction):
    comparison = default_compare(key, bn.get_key(root[direction]))
    
    if comparison == 0:
        if root[direction]['size'] == 1:
            root[direction] = None
        elif (root[direction]['left'] != None) ^ (root[direction]['right'] != None):
            root[direction] = remove_node(root[direction], key)
        else:
            current_root = root[direction]['right']
            if current_root['size'] == 1:
                current_root['left'] = root[direction]['left']
                current_root['size'] += 1
                root[direction] = current_root
            else:
                pass
                
        root['size'] -= 1
        return root
    else:
        return remove_node(root[direction], key)

def contains(my_bst, key):
    result = get(my_bst, key)
    return False if result == None else True

def size(my_bst):
    if is_empty(my_bst): return 0
    size = 1
    
    if my_bst['root']['left'] != None:
        size += size_tree(my_bst['root']['left'])
    if my_bst['root']['right'] != None:
        size += size_tree(my_bst['root']['right'])
    
    return size
    
def size_tree(root):
    size = 1
    if root['left'] != None:
        size += size_tree(root['left'])
    if root['right'] != None:
        size += size_tree(root['right'])
    return size


def is_empty(my_bst):
    return True if my_bst['root']==None else False

def key_set(my_bst):
    key_list = al.new_list()
    if is_empty(my_bst): return key_list
    
    key_set_tree(my_bst['root']['left'], key_list)
    al.add_last(key_list, my_bst['root']['key'])
    key_set_tree(my_bst['root']['right'], key_list)
    
    return key_list

def key_set_tree(root, key_list):
    if root == None: return
    
    key_set_tree(root['left'], key_list)
    al.add_last(key_list, root['key'])
    key_set_tree(root['right'], key_list)
    
    return key_list

def value_set(my_bst):
    value_list = al.new_list()
    if is_empty(my_bst): return value_list
    
    value_set_tree(my_bst['root']['left'], value_list)
    al.add_last(value_list, my_bst['root']['value'])
    value_set_tree(my_bst['root']['right'], value_list)
    
    return value_list

def value_set_tree(root, value_list):
    if root == None: return
    
    value_set_tree(root['left'], value_list)
    al.add_last(value_list, root['value'])
    value_set_tree(root['right'], value_list)
    
    return value_list


def left_key(my_bst):
    if is_empty(my_bst): return None
    
    return left_key_node(my_bst['root'])

def left_key_node(root):
    if root['left'] == None:
        return root['key']
    else:
        return left_key_node(root['left'])

def right_key(my_bst):
    if is_empty(my_bst): return None
    
    return right_key_node(my_bst['root'])

def right_key_node(root):
    if root['right'] == None:
        return root['key']
    else:
        return right_key_node(root['right'])


def delete_left(my_bst):
    if size(my_bst) <= 1: return my_bst
    
    delete_left_tree(my_bst['root'])
    return my_bst
    
def delete_left_tree(root):
    if root['left'] == None:
        root = None
        return root
    else:
        root['left'] = delete_left_tree(root['left'])
        root['size'] -= 1
        return root

def delete_right(my_bst):
    if size(my_bst) <= 1: return my_bst
    
    delete_right_tree(my_bst['root'])
    return my_bst

def delete_right_tree(root):
    if root['right'] == None:
        root = None
        return root
    else:
        root['right'] = delete_right_tree(root['right'])
        root['size'] -= 1
        return root

def floor(my_bst, key):
    if is_empty(my_bst): return None
    
    return floor_key(my_bst['root'], key)

def floor_key(root, key):
    comparison = default_compare(key, root['key'])
    print ('\n',root['key'], key, comparison)
    
    if comparison == 0:
        return key
    elif comparison == 1:
        if root['right'] != None:
            return floor_key(root['right'], key)
        else:
            return root['key']
    elif comparison == -1:
        if root['left'] != None:
            return floor_key(root['left'], key)
        else:
            return None
    

def ceiling(my_bst, key):
    if is_empty(my_bst): return None
    
    result = ceiling_key(my_bst['root'], key)
    print (result)
    return result

def ceiling_key(root, key):
    comparison = default_compare(key, root['key'])
    print ('\n',root['key'], key, comparison)
    
    if comparison == 0:
        return key
    
    elif comparison == 1:
        if root['right'] != None:
            return ceiling_key(root['right'], key)
        else:
            return None
    
    elif comparison == -1:
        if root['left'] != None:
            result = ceiling_key(root['left'], key)
            if result == None:
                return root['key']
            
            return result
        else:
            return root['key']


def select(my_bst, pos):
    if is_empty(my_bst): return None
    #if my_bst['root']['size'] < pos: return None
    
    return select_key(my_bst['root'], pos)
    

def select_key(root, key):
    print (root, key)
    if root == None: return root
    
    left_size = size(root['left'])
    
    if left_size > key:
        return select_key(root['left'], key)
    elif left_size < key:
        return select_key(root['right'], key - left_size - 1)
    else:
        return root
            

def rank(my_bst, key):
    pass

def height(my_bst):
    pass

def keys(my_bst, key_lo, key_hi):
    pass

def values(my_bst, key_lo, key_hi):
    pass

def rank_keys(root, key):
    pass

def height_tree(root):
    pass

def keys_range(root, key_lo, key_hi, list_key):
    pass

def values_range(root, key_lo, key_hi, list_values):
    pass

def default_compare(key, element):
    if element == None:
        return None
    if key > element:
        return 1
    elif key == element:
        return 0
    else:
        return -1
from . import bst_node as bn

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
    pass

def value_set(my_bst):
    pass

def min_key(my_bst):
    pass

def max_key(my_bst):
    pass

def delete_min(my_bst):
    pass

def delete_max(my_bst):
    pass

def floor(my_bst, key):
    pass

def ceiling(my_bst, key):
    pass

def select(my_bst, pos):
    pass

def rank(my_bst, key):
    pass

def height(my_bst):
    pass

def keys(my_bst, key_lo, key_hi):
    pass

def values(my_bst, key_lo, key_hi):
    pass


def value_set_tree(root, value_list):
    pass

def key_set_tree(root, key_list):
    pass

def min_key_node(root):
    pass

def max_key_node(root):
    pass

def delete_min_tree(root):
    pass

def delete_max_tree(root):
    pass

def floor_key(root, key):
    pass

def ceiling_key(root, key):
    pass

def select_key(root, key):
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
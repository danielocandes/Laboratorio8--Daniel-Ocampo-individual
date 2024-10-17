from DataStructures.Tree import bst_node as bn

def new_map():
    map = {'root': None,
           'type': 'BST'}
    

def put(my_bst, key, value):
    pair = bn.new_node(key, value)
    insert_node(my_bst['root'], key, value)

def insert_node(root, key, value):
    if default_compare(key, root['key']) == -1:
        if root['left'] == None:
            root['left'] = bn.new_node(key, value)
        else:
            insert_node(root['left'], key, value)
    
    elif default_compare(key, root['key']) == 1:
        if root['right'] == None:
            root['right'] = bn.new_node(key, value)
        else:
            insert_node(root['right'], key, value)
            
    else:
        new_node = bn.new_node(key, value)
        new_node['right'], new_node['left'] = root['right'], root['left']
        
        root = new_node

def get(my_bst, key):
    pass

def remove(my_bst, key):
    pass

def contains(my_bst, key):
    pass

def size(my_bst):
    pass

def is_empty(my_bst):
    pass

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

def get_node(root, key):
    pass

def remove_node(root, key):
    pass

def size_tree(root):
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
    if key > element:
        return 1
    elif key == element:
        return 0
    else:
        return -1
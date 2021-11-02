import sys
sys.path.append('src')
from graph import Graph

g = Graph([(0,2), (0,3), (0,8), (2,3), (3,1), (3,2), (3,5), (3,9), (4,0), (4,6), (4,8), (5,7), (6,3)])
if g.get_children(3) != [1,2,5,9]:
    print('get_children failed on input 3')
if g.get_parents(3) != [0,2,6]:
    print('get_parents failed on input 3')
if g.get_children(4) != [0,6,8]:
    print('get_children failed on input 4')
if g.get_parents(4) != []:
    print('get_parents failed on input 4')
if g.get_children(7) != []:
    print('get_children failed on input 7')
if g.get_parents(7) != [5]:
    print('get_parents failed on input 7')
if g.breadth_first(4) != [4, 0, 6, 8, 2, 3, 1, 5, 9, 7]:
    print('breadth_first failed on input 4')
if g.depth_first(4) != [4, 8, 6, 3, 9, 5, 7, 2, 1, 0]:
    print('depth_first failed on input 4')

r = Graph([(1,2), (1,4), (2,3), (4,3), (5,6), (5,8), (6,7), (8,7)])
if r.get_children(3) != []:
    print('get_children failed on input 3')
if r.get_parents(3) != [2,4]:
    print('get_parents failed on input 3')
if r.get_children(4) != [3]:
    print('get_children failed on input 4')
if r.get_parents(4) != [1]:
    print('get_parents failed on input 4')
if r.get_children(7) != []:
    print('get_children failed on input 7')
if r.get_parents(7) != [6,8]:
    print('get_parents failed on input 7')

a = Graph([(1,2), (2,3), (2,4), (3,5), (3,6)])
if a.breadth_first(1) != [1,2,3,4,5,6]:
    print('breadth_first failed on input 1')
if a.depth_first(1) != [1,2,4,3,6,5]:
    print('depth_first failed on input 1')
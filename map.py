import settings
from itertools import product
import pygame as pg
import random 

def create_maze(m, n):
    def vecinos(i, j):                  
        if 0 < i: yield i - 1, j
        if i < m - 1: yield i + 1, j
        if 0 < j: yield i, j - 1
        if j < n - 1: yield i, j + 1

    def visitar(i, j):                  
        X.add((i, j))                   
        N = list(vecinos(i, j)); random.shuffle(N)  
        for h, k in N:                  
            if (h, k) in X: continue    
            A[i + h + 1][j + k + 1] = '0'  
            visitar(h, k)               

    A = [['1']*(2*n + 1) for i in range(2*m + 1)] 
    for i, j in product(range(1, 2*m + 1, 2), range(1, 2*n + 1, 2)):
        if (2*m)!=i and (2*m)!=j:
            A[i][j] = '0'            
        else:
            A[i][j] = '2'

    X = set()                           
    visitar(random.randint(0, m - 1), random.randint(0, n - 1))  

    T=[]
    for count,fila in enumerate(A):
        T.append([])
        for i in fila: 
            T[count].append(int(i))


    return T






class Map:
    def __init__(self, game, mini_map):
        self.game = game
        self.mini_map = mini_map
        self.world_map = {}
        self.rows = len(self.mini_map)
        self.cols = len(self.mini_map[0])
        self.get_map()

    def get_map(self):
        for j, row in enumerate(self.mini_map):
            for i, value in enumerate(row):
                if value==1:
                    self.world_map[(i, j)] = 1

    def draw(self):
        [pg.draw.rect(self.game.screen, 'darkgray', ((pos[0] * 10), pos[1] * 10, 10, 10), 2)
         for pos in self.world_map]

        SL=self.game.object_handler.sprite_list
        [pg.draw.rect(self.game.screen, (0,250,0), ((pos.x * 10)-2.5, (pos.y * 10)-2.5, 5, 5), 0)
         for pos in SL]
        SL=self.game.object_handler.goals_list
        [pg.draw.rect(self.game.screen, (255,0,0), ((pos.x * 10)-2.5, (pos.y * 10)-2.5, 5, 5), 0)
         for pos in SL]

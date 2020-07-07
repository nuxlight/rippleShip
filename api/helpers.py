import numpy as np
import random 
import logging
import uuid

from .models import Ship, Grid, Position, Party, ShipType

logger = logging.getLogger('django')

'''
This class defined all methods for the game
'''
class GameEngine():

    GRID_SIZE = 10
    CROISEUR_NUMBER = 1
    ESCORTEUR_NUMBER = 2
    TORPILLEUR_NUMBER = 3
    SOUSMARIN_NUMBER = 4
    MARGIN_VALUE = 8
    LIST_OF_SHIP = [CROISEUR_NUMBER,ESCORTEUR_NUMBER,TORPILLEUR_NUMBER,SOUSMARIN_NUMBER]
    
    def __init__(self, grid_size, croiseur_number, 
            escorteur_number, torpilleur_number, sousmarin__number):
        self.GRID_SIZE = grid_size
        self.CROISEUR_NUMBER = croiseur_number
        self.ESCORTEUR_NUMBER = escorteur_number
        self.TORPILLEUR_NUMBER = torpilleur_number
        self.SOUSMARIN_NUMBER = sousmarin__number
        super().__init__()

    def create_game_board(self):
        grid = np.full((self.GRID_SIZE,self.GRID_SIZE), 0)
        party = Party(uuid=str(uuid.uuid4()), grid=Grid(width=self.GRID_SIZE,height=self.GRID_SIZE))
        # Create dict type for each ship
        croiseur = {"name": "C","type": 1,"size": 4}
        escorteurs = {"name": "E","type": 2,"size": 3}
        torpilleurs = {"name": "T","type": 3,"size": 2}
        sousmarin = {"name": "S","type": 4,"size": 1}
        # generate ship positions
        for i in range(0, self.CROISEUR_NUMBER):
            path = self.create_ship(croiseur, grid)
            ship = Ship(party=party, ship_type=1)
            ship.save()
            Position(ship=ship, abs=path["abs"], ord=path["ord"]).save()
        for i in range(0, self.ESCORTEUR_NUMBER):
            self.create_ship(escorteurs, grid)
        for i in range(0, self.TORPILLEUR_NUMBER):
            self.create_ship(torpilleurs, grid)
        for i in range(0, self.SOUSMARIN_NUMBER):
            self.create_ship(sousmarin, grid)
        self.clean_grid(grid)
        logger.info("New board generated")
        logger.info(grid)

    def clean_grid(self, grid):
        np.place(grid, grid==8, 0)

    def create_ship(self, ship, grid):
        position = self.generate_position()
        while self.check_position(position["ord"],position["abs"],grid) == False:
            position = self.generate_position()
        path = self.generate_path(ship, position, grid)
        while self.check_path(path) == False:
            position = self.generate_position()
            path = self.generate_path(ship, position, grid)
        self.generate_marge(path, grid, ship)
        self.draw_ship(path, ship, position, grid)
        return path


    def draw_ship(self, path, ship, position, grid):
        for empl in path:
            grid[empl["ord"]][empl["abs"]] = ship["type"]

    def generate_marge(self, path, grid, ship):
        for empl in path:
            try:
                if grid[empl["ord"]][empl["abs"]+1] not in self.LIST_OF_SHIP:
                    grid[empl["ord"]][empl["abs"]+1] = self.MARGIN_VALUE
            except:
                pass
            try:
                if grid[empl["ord"]][empl["abs"]-1] not in self.LIST_OF_SHIP:
                    grid[empl["ord"]][empl["abs"]-1] = self.MARGIN_VALUE
            except:
                pass
            try:
                if grid[empl["ord"]+1][empl["abs"]] not in self.LIST_OF_SHIP:
                    grid[empl["ord"]+1][empl["abs"]] = self.MARGIN_VALUE
            except:
                pass
            try:    
                if grid[empl["ord"]-1][empl["abs"]] not in self.LIST_OF_SHIP:
                    grid[empl["ord"]-1][empl["abs"]] = self.MARGIN_VALUE
            except:
                pass
            try:
                if grid[empl["ord"]+1][empl["abs"]+1] not in self.LIST_OF_SHIP:
                    grid[empl["ord"]+1][empl["abs"]+1] = self.MARGIN_VALUE
            except:
                pass
            try:
                if grid[empl["ord"]-1][empl["abs"]+1] not in self.LIST_OF_SHIP:
                    grid[empl["ord"]-1][empl["abs"]+1] = self.MARGIN_VALUE
            except:
                pass
            try:
                if grid[empl["ord"]+1][empl["abs"]-1] not in self.LIST_OF_SHIP:
                    grid[empl["ord"]+1][empl["abs"]-1] = self.MARGIN_VALUE
            except:
                pass
            try:
                if grid[empl["ord"]-1][empl["abs"]-1] not in self.LIST_OF_SHIP:
                    grid[empl["ord"]-1][empl["abs"]-1] = self.MARGIN_VALUE
            except:
                pass

    def generate_path(self, ship, position, grid):
        direction = {}
        left_dir = []
        for l in range(0, position["abs"]):
            index = grid[position["ord"]][l]
            if index == 0 and len(left_dir) < ship["size"] and index != self.MARGIN_VALUE:
                left_dir.append({
                    "ord": position["ord"],
                    "abs": l
                })
        right_dir = []
        for r in range(position["abs"], self.GRID_SIZE):
            index = grid[position["ord"]][r]
            if index == 0 and len(right_dir) < ship["size"] and index != self.MARGIN_VALUE:
                right_dir.append({
                    "ord": position["ord"],
                    "abs": r
                })
        up_dir = []
        for u in range(0, position["ord"]):
            index = grid[u][position["abs"]]
            if index == 0 and len(up_dir) < ship["size"] and index != self.MARGIN_VALUE:
                up_dir.append({
                    "ord": u,
                    "abs": position["abs"]
                })
        down_dir = []
        for d in range(position["ord"], self.GRID_SIZE):
            index = grid[d][position["abs"]]
            if index == 0 and len(down_dir) < ship["size"] and index != self.MARGIN_VALUE:
                down_dir.append({
                    "ord": d,
                    "abs": position["abs"]
                })
        if len(left_dir) == ship["size"]:
            direction["left"] = left_dir
        if len(right_dir) == ship["size"]:
            direction["right"] = right_dir
        if len(up_dir) == ship["size"]:
            direction["up"] = up_dir
        if len(down_dir) == ship["size"]:
            direction["down"] = down_dir
        path = random.choice(list(direction.keys()))
        return direction[path]

    def check_path(self, path):
        if len(path) == 1:
            return True
        ordList = []
        absList = []
        for elm in path:
            ordList.append(elm["ord"])
            absList.append(elm["abs"])
        if ordList[0] == ordList[1] and self.isAList(absList):
            return True
        elif absList[0] == absList[1] and self.isAList(ordList):
            return True
        else:
            return False

    def isAList(self, list):
        size = len(list)
        for a in range(1, size):
            if list[a-1] - list[a] == -1:
                continue
            else:
                return False
        return True

    def check_position(self, rand_position_abs, rand_position_ord, grid):
        if grid[rand_position_abs][rand_position_ord] == 0:
            return True
        else:
            return False

    def generate_position(self):
        rand_position_abs = random.randrange(0, self.GRID_SIZE)
        rand_position_ord = random.randrange(0, self.GRID_SIZE)
        return {
            "abs" : rand_position_abs,
            "ord" : rand_position_ord
        }
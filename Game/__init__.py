from . import DungeonFloor 
from curses import color_pair as c
from curses import start_color 
from curses import echo 
from curses import noecho 
from curses import init_pair 
from curses import COLOR_BLUE 
from curses import COLOR_BLACK 
from curses import COLOR_RED 
from curses import COLOR_WHITE 
from curses import COLOR_MAGENTA 
from curses import A_BOLD 
from curses import use_default_colors 
from curses import KEY_RESIZE 
from curses import KEY_LEFT 
from curses import KEY_RIGHT 
from curses import KEY_UP 
from curses import KEY_DOWN 
from curses import resizeterm 
from curses import is_term_resized
from .Tiletype import Tiletype
from .NPC import NPC
from .Camera import Camera

from random import randint

class Game:
    def __init__(self, title='my game', renderer=None):
        self.title = title
        self.logs = []
        self.currentTurnCount = 0
        assert(renderer != None)
        self.renderer = renderer
        rows = randint(5,15)
        cols = randint(5,15)
        self.dungeonFloor = DungeonFloor.DungeonFloor(self, rows, cols)
        self.camera_mode = False
        self.logger_mode = False
        self.logger_offset = 0
        self.camera = Camera()


    def __str__(self):
        return self.title

    def addLog(self,log):
        if log==None or log=="":
            raise Exception("Log is empty or none")
        self.logs.append(f"{log}")
        #self.logs.append(f"{self.currentTurnCount}: {log}")

    def incrTurns(self):
        self.currentTurnCount += 1
    
    def handle_input(self, pc, k):
        rows, cols = self.renderer.s.getmaxyx()
        # Help Menu
        help_key = '?'
        quit_key_0 = 'q'
        quit_key_1 = 'Q'
        camera_key = 'c'
        input_keys = [ 'a', 's', 'd', 'f', 'j', 'k', 'l', ';', 'KEY_DOWN', 'KEY_UP', 'KEY_RIGHT', 'KEY_LEFT', 'KEY_RESIZE', quit_key_0, quit_key_1, help_key, camera_key ]
        #movement_keys = ['a','s','d','f','j','k','l',';','KEY_DOWN', 'KEY_UP', 'KEY_RIGHT', 'KEY_LEFT']
        movement_keys = ['a','s','d','f','KEY_DOWN', 'KEY_UP', 'KEY_RIGHT', 'KEY_LEFT']

        selection_keys = ['1','2','3','4','5','6','7','8','9','0']

        left_keys = ['a','j','KEY_LEFT']
        up_keys =   ['s','k','KEY_UP']
        down_keys = ['d','l','KEY_DOWN']
        right_keys = ['f',';','KEY_RIGHT']
        logger_mode_switch_keys = ['l']
        display_inventory_key = ['i']
        retval = False
        
        if k == help_key:
            self.help_menu()
            return False
        elif k == camera_key:
            if self.camera_mode == False:
                self.camera_mode = True
                return False
            else:
                self.camera_mode = False
                return False
        elif k in movement_keys:
            if not self.camera_mode and not self.logger_mode:
                result = self.handle_movement(pc, k)
            elif self.logger_mode and not self.camera_mode:
                self.handle_logger_movement(k)
                return False
            elif self.camera_mode and not self.logger_mode:
                self.handle_camera_movement(k)
                return False

        elif k in logger_mode_switch_keys:
            if self.logger_mode == True:
                self.logger_mode = False
                self.logger_offset = 0
            else:
                self.logger_mode = True
            return False
        
        elif k == "KEY_RESIZE":
            self.addLog("handle_resize")
            resize = is_term_resized(rows, cols)
            if resize:
                self.handle_resize()
            return False

        elif k in display_inventory_key:
            self.display_inventory(pc)
            return False
        
        # exit game
        elif k == quit_key_0 or k == quit_key_1:
            #self.renderer.draw_quit_screen()
            exit(0)
        
        # pickup item
        elif k == ",":
            self.handle_item_pickup(pc)
            return True

        elif k in selection_keys:
            # depends on the selection 'mode'
            # for instance, if we are picking up an item, like one of many on a tile
            # we'll be given a selection we can make such as 1 or 2
            #self.addLog(f"Unimplemented selection key pressed: {k}")
            self.handle_item_pickup_main(pc, k)
            return True
        else:
            self.addLog(f"Unimplemented key pressed: {k}")
            return False
        return True


    def handle_item_pickup_main(self, pc, k):

        # this is bad code lol needs fixing already see bugs ahead

        x = pc.x
        y = pc.y
        i = int(k)
        items = [item for item in self.dungeonFloor.items if item.x==x and item.y==y]
        
        item = items[i]
        
        pc.items.append( item )

        # find the real item in the dungeonFloor items list and remove it
        for x in range(len(self.dungeonFloor.items)):
            item_ = self.dungeonFloor.items[x]
            if item == item_:
                self.dungeonFloor.items.pop(x)
                break

        self.addLog('----------')
        self.addLog(f"{self.currentTurnCount}. Picked up a {item.name}")




    def handle_item_pickup(self, pc):
        x = pc.x
        y = pc.y
        i = 0
        items = [item for item in self.dungeonFloor.items if item.x==x and item.y==y]
        # single-item case
        if len(items)==1:
            pc.items.append( items[0] )
            self.addLog(f"{self.currentTurnCount}: Picked up {items[0].name}")
            self.dungeonFloor.items.pop(0)
        # multiple-items case
        else:
            self.addLog(f"There are multiple items here.")
            self.addLog(f"Which would you like to pick up?")
            self.item_selection_mode = True
            for i in range(len(items)):
                item = items[i]
                self.addLog(f"{i}. {item.name}")



    def display_inventory(self, pc):
        self.addLog(f"Displaying inventory:")
        for item in pc.items:
            self.addLog(f"{item}")





    def handle_resize(self):
        rows, cols = self.renderer.s.getmaxyx()
        self.renderer.s.clear()
        resizeterm(rows, cols)
        self.renderer.s.refresh()

    def handle_movement(self, pc, k):
        y = 0
        x = 0
        if k == 'a' or k == 'j' or k == 'KEY_LEFT': # left
            x = -1
        elif k == 's' or k == 'k' or k == 'KEY_UP': # up
            y = -1
        elif k == 'd' or k == 'l' or k == 'KEY_DOWN': # down
            y = 1
        elif k == 'f' or k == ';' or k == 'KEY_RIGHT': # right
            x = 1
        return self.check_movement(pc, y, x)

    def handle_logger_movement(self, k):
        if k == 'KEY_UP':
            # decrement logger index
            if self.logger_offset + len(self.logs) - 5 >= 0:
                self.logger_offset -= 1
        elif k == 'KEY_DOWN':
            if self.logger_offset < 0:
                self.logger_offset += 1


    def handle_camera_movement(self, k):
        self.addLog(f"handle_camera_movement({k})")
        if k == 'a' or k == 'j' or k == 'KEY_LEFT': # left
            self.camera.x -= 1
        elif k == 's' or k == 'k' or k == 'KEY_UP': # up
            self.camera.y -= 1
        elif k == 'd' or k == 'l' or k == 'KEY_DOWN': # down
            self.camera.y += 1
        elif k == 'f' or k == ';' or k == 'KEY_RIGHT': # right
            self.camera.x += 1



    def check_movement(self, pc, y, x):
        assert(pc != None)
        assert(y in [-1, 0, 1])
        assert(x in [-1, 0, 1])
        retval = True
        dir_ = ""
        if y==0 and x==1:
            dir_ = "east"
        elif y==1 and x==0:
            dir_ = "south"
        elif y==-1 and x==0:
            dir_ = "north"
        elif y==0 and x==-1:
            dir_ = "west"
        result = self.check_pc_next_tile(pc, y, x)
        if not result:
            self.addLog(f"Cannot move {dir_}")
            retval = False
        else:
            result = self.check_pc_npc_collision(pc, y, x ) 
            if not result:
                pc.y += y
                pc.x += x
                self.addLog(f"{self.currentTurnCount}: Walked {dir_}")
                item_collision = self.check_pc_item_collision(pc)
                if item_collision:
                    for item in self.dungeonFloor.items:
                        if item.x == item_collision.x and item.y == item_collision.y:
                            self.addLog(f"There is a {item.name} here")
            else:
                self.handle_pc_npc_collision(pc, result)
        return retval


    def check_pc_next_tile(self, pc, y, x):
        assert(pc != None)
        assert(y in [-1, 0, 1])
        assert(x in [-1, 0, 1])
        retval = False
        rows = self.dungeonFloor.rows
        cols = self.dungeonFloor.cols

        walkable_tiles = [ Tiletype.STONE_FLOOR, 
            Tiletype.GRASS
        ]

        if self.check_pc_dungeon_bounds(pc, y, x ):
            nx = pc.x + x
            ny = pc.y + y
            if nx >= 0 and nx < cols and ny >= 0 and ny < rows:
                next_tile = self.dungeonFloor.map_[ pc.y+y ][ pc.x+x ] 
                if next_tile.tiletype in walkable_tiles:
                    retval = True
        return retval

    def handle_pc_npc_collision(self, pc, npc):
        if type(npc) == NPC:
            pc.attack(npc)
            if npc.hp <= 0:
                self.addLog(f"{self.currentTurnCount}: You killed {npc.name}!")
                self.dungeonFloor.npcs.remove(npc)
                # just add 1 xp for now lol
                pc.xp += 1


    def check_pc_item_collision(self, pc):
        for item in self.dungeonFloor.items:
            if pc.x == item.x and pc.y == item.y:
                # in other words, pc WOULD move into the item
                # so we'd return true
                # game.addLog("bumped into npc")
                # considering returning the NPC that caused the collision
                #return True
                return item
        return None





    def check_pc_npc_collision(self, pc, y, x):
        for npc in self.dungeonFloor.npcs:
            if pc.x + x == npc.x and pc.y + y == npc.y:
                # in other words, pc WOULD move into the npc
                # so we'd return true
                # game.addLog("bumped into npc")
                # considering returning the NPC that caused the collision
                #return True
                return npc
        return None

    def check_pc_dungeon_bounds(self, pc, y, x):
        retval = True 
        rows = self.dungeonFloor.rows
        cols = self.dungeonFloor.cols
        if pc.x+x < 0 or pc.y+y < 0 or pc.y+y > rows or pc.x+x > cols:
            retval = False
        return retval

    def help_menu(self):
        self.renderer.s.clear()
        a = None
        rows, cols = self.renderer.s.getmaxyx()
        with open("txt/helpmenu.txt", "r") as infile:
            a = infile.readlines()
        y = 0
        for line in a:
            if y < rows:
                try:
                    self.renderer.s.addstr(y, 0, line, c(1))
                    y += 1
                except Exception as e:
                    print("Caught Exception")
                    print("----------")
                    print("WTF")
            else:
                break
        self.renderer.s.refresh()
        self.renderer.s.getkey()


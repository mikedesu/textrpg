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
                self.handle_movement(pc, k)
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
            return False
        else:
            self.addLog(f"Unimplemented key pressed: {k}")
            return False
        return True

    def handle_item_pickup(self, pc):
        x = pc.x
        y = pc.y
        i = 0
        pickedUp = False
        while i < len(self.dungeonFloor.items):
            item = self.dungeonFloor.items[i]
            if item.x == x and item.y == y:
                pc.items.append( item )
                self.addLog(f"{self.currentTurnCount}: Picked up {item.name}")
                pickedUp = True
                break # only pickup one item at a time
            i += 1
        if pickedUp:
            # remove that item from the dungeon itemlist
            self.dungeonFloor.items.pop(i)
            # it shouldn't render after this


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
        self.check_movement(pc, y, x)

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
        result = self.check_pc_next_tile(pc, y, x)
        if result:
            result = self.check_pc_npc_collision(pc, y, x ) 
            if not result:

                pc.y += y
                pc.x += x
                if y==0 and x==1:
                    self.addLog(f"{self.currentTurnCount}: Walked east")
                elif y==1 and x==0:
                    self.addLog(f"{self.currentTurnCount}: Walked south")
                elif y==-1 and x==0:
                    self.addLog(f"{self.currentTurnCount}: Walked north")
                elif y==0 and x==-1:
                    self.addLog(f"{self.currentTurnCount}: Walked west")

                item_collision = self.check_pc_item_collision(pc)
                if item_collision:
                    self.addLog(f"There is a {item_collision.name} here")


            else:
                self.handle_pc_npc_collision(pc, result)
        else:
            if y==0 and x==1:
                self.addLog("cannot move east")
            elif y==1 and x==0:
                self.addLog("cannot move south")
            elif y==-1 and x==0:
                self.addLog("cannot move north")
            elif y==0 and x==-1:
                self.addLog("cannot move west")


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


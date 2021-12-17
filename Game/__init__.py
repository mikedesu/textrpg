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

from .DungeonFloor import DungeonFloor 
from .Tiletype import Tiletype
from .NPC import NPC
from .Camera import Camera
from .Menu import Menu
from .ItemPickupMenu import ItemPickupMenu

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
        self.dungeonFloor = DungeonFloor(self, rows, cols)
        self.currentMode = "Player"
        #self.itemSelectionMode = False
        self.logger_offset = 0
        self.camera = Camera()
        self.debug_mode = False

        self.testMenu = None

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
        movement_keys = ['a','s','d','f','KEY_DOWN', 'KEY_UP', 'KEY_RIGHT', 'KEY_LEFT', '1','2','3','4','5','6','7','8','9']
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
            if self.currentMode == "Player":
                self.currentMode = "Camera"
            elif self.currentMode == "Camera":
                self.currentMode = "Player"
            return False

           # if self.camera_mode == False:
           #     self.camera_mode = True
           #     return False
           # else:
           #     self.camera_mode = False
           #     return False
        #elif k in movement_keys and not self.itemSelectionMode:
        elif k in movement_keys: #and not self.itemSelectionMode:

            if self.currentMode == "Player":
                result = self.handle_movement(pc, k, True)
            elif self.currentMode == "Camera":
                self.handle_camera_movement(k)
                return False
            elif self.currentMode == "Logger":
                self.handle_logger_movement(k)
                return False


        elif k in logger_mode_switch_keys:

            if self.currentMode != "Logger":
                self.currentMode = "Logger"
                self.logger_offset = 0
            else:
                self.currentMode = "Player"


        
        elif k == "KEY_RESIZE":
            if self.debug_mode:
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
            self.renderer.draw_quit_screen()
            exit(0)
        
        # pickup item
        elif k == ",":
 
            
            self.handle_item_pickup(pc)
            return True

        # wait in one spot / inspect / search ground / area around you
        elif k == ".":
            # more to implement later...
            return True

        #elif self.itemSelectionMode and k in selection_keys:
            # depends on the selection 'mode'
            # for instance, if we are picking up an item, like one of many on a tile
            # we'll be given a selection we can make such as 1 or 2
            #self.addLog(f"Unimplemented selection key pressed: {k}")
            #self.handle_item_pickup_main(pc, k)
            #return True
        else:
            self.addLog(f"Unimplemented key pressed: {k}")
            return False
        return True


    def handle_item_pickup_main(self, pc, k):
        # this is bad code lol needs fixing already see bugs ahead
        i = int(k)
        # get all items on current tile
        items = [item for item in self.dungeonFloor.items if item.x==pc.x and item.y==pc.y]
        
        item = items[i]
        # add the item to the pc's items
        pc.items.append( item )

        # find the real item in the dungeonFloor items list and remove it
        for x in range(len(self.dungeonFloor.items)):
            item_ = self.dungeonFloor.items[x]
            if item == item_:
                self.dungeonFloor.items.pop(x)
                break
        


        self.addLog('----------')
        self.addLog(f"{self.currentTurnCount}. Picked up a {item.name}")
        
        self.itemSelectionMode = False


    def decrOneHungerUnitPC(self):
        self.pc.hunger -= 1
        if self.pc.hunger <= 0:
            self.addLog(f"{self.pc.name} died of hunger! Game over!")
            self.renderer.draw_quit_screen()
            exit(0)
    
    def incrOneHungerUnitPC(self):
        self.pc.hunger += 1 
        if self.pc.hunger >= self.pc.maxhunger:
            self.pc.hunger = self.pc.maxhunger 





    def process_npc_turn(self):
        # for right now, lets make them move randomly
        movement_keys = ['KEY_DOWN', 'KEY_UP', 'KEY_RIGHT', 'KEY_LEFT']
        for i in range( len( self.dungeonFloor.npcs ) ):
            try:
                npc = self.dungeonFloor.npcs[i]
                # select a random keypress
                random_index = randint(0, len(movement_keys)-1)
                random_key = movement_keys[ random_index ] 
                self.handle_movement( npc , random_key, False ) 
                #self.handle_movement( npc , random_key, True ) 
            except Exception as e:
                pass
                #self.addLog(f"{e}")

    def handleItemPickupHelper(self, i):
        x = self.pc.x
        y = self.pc.y
        items = [item for item in self.dungeonFloor.items if item.x==x and item.y==y]
        item = items[i]
        # add the item to the pc's items
        self.pc.items.append( item )
        self.addLog(f"{self.currentTurnCount}: {self.pc.name} picked up a {item.name}")
        # find the real item in the dungeonFloor items list and remove it
        for x in range(len(self.dungeonFloor.items)):
            item_ = self.dungeonFloor.items[x]
            if item == item_:
                self.dungeonFloor.items.pop(x)
                break


    def handle_item_pickup(self, pc):
        x = pc.x
        y = pc.y
        items = [item for item in self.dungeonFloor.items if item.x==x and item.y==y]

        # single-item case
        if len(items)==1:
            pc.items.append( items[0] )
            self.addLog(f"{self.currentTurnCount}: Picked up {items[0].name}")
            self.dungeonFloor.items.pop(0)
        # multiple-items case
        elif len(items) > 1:
            menuItems=[(items[i].name, self.handleItemPickupHelper, i ) for i in range(len(items))]
            self.testMenu = ItemPickupMenu( "Which item would you like to pick up?", menuItems, self.renderer.s )
            self.testMenu.display()
        else:
            # do nothing
            self.addLog(f"There is nothing here!")
            pass




    def display_inventory(self, pc):
        self.addLog(f"Displaying inventory:")
        for item in pc.items:
            self.addLog(f"{item}")





    def handle_resize(self):
        rows, cols = self.renderer.s.getmaxyx()
        self.renderer.s.clear()
        resizeterm(rows, cols)
        self.renderer.s.refresh()

    def handle_movement(self, entity, k, doLog):
        y = 0
        x = 0
        lefts  = ['a','j','KEY_LEFT','4']
        rights = ['f',';','KEY_RIGHT','6']
        ups    = ['s','k','KEY_UP','8']
        downs  = ['d','l','KEY_DOWN','2']
        ul     = ['7']
        ur     = ['9']
        dl     = ['1']
        dr     = ['3']
        if k in lefts:
            x = -1
        elif k in ups:
            y = -1
        elif k in downs:
            y = 1
        elif k in rights:
            x = 1
        elif k in ul:
            x = -1
            y = -1
        elif k in ur:
            x = 1
            y = -1
        elif k in dl:
            x = -1
            y = 1
        elif k in dr:
            x = 1
            y = 1
        return self.check_movement(entity, y, x, doLog)

    def handle_logger_movement(self, k):
        if k == 'KEY_UP':
            # decrement logger index
            if self.logger_offset + len(self.logs) - 5 >= 0:
                self.logger_offset -= 1
        elif k == 'KEY_DOWN':
            if self.logger_offset < 0:
                self.logger_offset += 1


    def handle_camera_movement(self, k):
        
        if self.debug_mode:
            self.addLog(f"handle_camera_movement({k})")
        
        if k == 'a' or k == 'j' or k == 'KEY_LEFT': # left
            self.camera.x -= 1
        elif k == 's' or k == 'k' or k == 'KEY_UP': # up
            self.camera.y -= 1
        elif k == 'd' or k == 'l' or k == 'KEY_DOWN': # down
            self.camera.y += 1
        elif k == 'f' or k == ';' or k == 'KEY_RIGHT': # right
            self.camera.x += 1



    def check_movement(self, entity, y, x, doLog):
        assert(entity != None)
        assert(y in [-1, 0, 1])
        assert(x in [-1, 0, 1])
        assert(isinstance(doLog, bool))
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
        elif y==-1 and x==-1:
            dir_ = "northwest"
        elif y==-1 and x==1:
            dir_ = "northeast"
        elif y==1 and x==-1:
            dir_ = "southwest"
        elif y==1 and x==1:
            dir_ = "southeast"
        result = self.check_pc_next_tile(entity, y, x)
        if not result:
            if doLog and entity.is_player:
                self.addLog(f"{entity.name} cannot move {dir_}")
            retval = False
        else:
            result = self.check_pc_npc_collision(entity, y, x ) 
            if not result:
                entity.y += y
                entity.x += x
                #if doLog:
                if doLog and entity.is_player:
                    self.addLog(f"{self.currentTurnCount}: {entity.name} walked {dir_}")
                item_collision = self.check_pc_item_collision(entity)
                if item_collision:
                    for item in self.dungeonFloor.items:
                        if item.x == item_collision.x and item.y == item_collision.y:
                            if doLog and entity.is_player:
                                self.addLog(f"There is a {item.name} here")
            else:
                self.handle_pc_npc_collision(entity, result, doLog)
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

    def handle_pc_npc_collision(self, pc, npc, doLog):
        if type(npc) == NPC:
            pc.attack(npc, doLog)
            if npc.hp <= 0:
                if doLog:
                    self.addLog(f"{self.currentTurnCount}: {pc.name} killed {npc.name}!")
                if not npc.is_player:
                    self.dungeonFloor.npcs.remove(npc)
                    # just add 1 xp for now lol
                    pc.xp += 1
                else:
                    # game over!
                    self.addLog(f"{npc.name} died! Game over!")
                    self.renderer.draw_quit_screen()
                    exit(0)


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





    def check_pc_npc_collision(self, entity, y, x):
        # check NPC against player
        if not entity.is_player:
            if entity.x + x == self.pc.x and entity.y + y == self.pc.y:
                return self.pc
        # for all entities, check against NPCs
        for npc in self.dungeonFloor.npcs:
            if entity != npc:
                if entity.x + x == npc.x and entity.y + y == npc.y:
                    # in other words, entity WOULD move into the npc
                    return npc
        # otherwise, return nothing
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


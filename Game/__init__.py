# import curses
from curses import color_pair as c
# from curses import start_color
# from curses import echo
# from curses import noecho
# from curses import init_pair
# from curses import COLOR_BLUE
# from curses import COLOR_BLACK
# from curses import COLOR_RED
# from curses import COLOR_WHITE
# from curses import COLOR_MAGENTA
# from curses import A_BOLD
# from curses import use_default_colors
# from curses import KEY_RESIZE
# from curses import KEY_LEFT
# from curses import KEY_RIGHT
# from curses import KEY_UP
# from curses import KEY_DOWN
from curses import resizeterm
from curses import is_term_resized
from random import randint
from .DungeonFloor import DungeonFloor
from .Tiletype import Tiletype
from .Entity import Entity
from .Camera import Camera
# from .Menu import Menu
from .ItemPickupMenu import ItemPickupMenu
from .InventoryMenu import InventoryMenu
from .EquipMenu import EquipMenu
from .Subequipmenu import Subequipmenu
from .Bodypart import Bodypart
# from .MessageWindow import MessageWindow
from .ModTable import ModTable
from .ItemClass import ItemClass


class Game:
    def __init__(self, title='darkhack', renderer=None):
        self.title = title
        self.logs = [f"Welcome to {title}!"]
        self.currentTurnCount = 0
        assert(renderer is not None)
        self.renderer = renderer
        # rows = randint(15,25)
        # cols = randint(15,25)
        self.hasShownStarvingMessage = False
        self.hasShownHungerMessage = False
        self.leftHandVim = True
        self.rightHandVim = True
        self.loadConfigFile()
        rows = 21
        cols = 50
        self.dungeonFloor = DungeonFloor(self, rows, cols)
        self.currentMode = "Player"
        self.logger_offset = 0
        # self.camera = Camera(0, 51)
        self.camera = Camera(0, 42)
        self.debug_mode = False
        self.testMenu = None
        self.equipMenu = None
        self.subequipMenu = None
        self.debugPanel = False
        self.modTable = ModTable()

    def __str__(self):
        return self.title

    def loadConfigFile(self):
        with open("config.txt", 'r') as infile:
            lines = infile.readlines()
            for line in lines:
                splitLine = line.split('=')
                varName = splitLine[0]
                value = splitLine[1]
                if varName == 'leftHandVim':
                    if value[:-1] == 'True':
                        self.leftHandVim = True
                    else:
                        self.leftHandVim = False
                if varName == 'rightHandVim':
                    if value[:-1] == 'True':
                        self.rightHandVim = True
                    else:
                        self.rightHandVim = False

    def addLog(self, log):
        if log is None or log == "":
            raise Exception("Log is empty or none")
        self.logs.append(f"{log}")

    def incrTurns(self):
        self.currentTurnCount += 1

    @property
    def debugPanel(self):
        return self._debugPanel

    @debugPanel.setter
    def debugPanel(self, v):
        assert(isinstance(v, bool))
        self._debugPanel = v

    def handleInput(self, pc, k):
        rows, cols = self.renderer.s.getmaxyx()
        # Help Menu
        help_key = '?'
        quit_key_0 = 'q'
        quit_key_1 = 'Q'
        # camera_key = 'c'
        # input_keys = [ 'a', 's', 'd', 'f', 'j', 'k', 'l', ';', 'KEY_DOWN',
        #     'KEY_UP', 'KEY_RIGHT', 'KEY_LEFT', 'KEY_RESIZE', quit_key_0,
        #     quit_key_1, help_key, camera_key ,
        #     'KEY_HOME', 'KEY_PPAGE', 'KEY_NPAGE', 'KEY_END', 'KEY_B2'
        # ]
        movement_keys = ['KEY_DOWN', 'KEY_UP', 'KEY_RIGHT', 'KEY_LEFT', '1',
                         '2', '3', '4', '5', '6', '7', '8', '9',
                         'KEY_HOME', 'KEY_PPAGE', 'KEY_NPAGE', 'KEY_END',
                         'KEY_B2'
                         ]
        if self.leftHandVim:
            for k in ['a', 's', 'd', 'f', 'r', 't', 'c', 'v']:
                movement_keys.append(k)
        if self.rightHandVim:
            for k in ['j', 'k', 'l', ';', 'y', 'u', 'b', 'n']:
                movement_keys.append(k)
        # selection_keys = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']
        # left_keys = ['a', 'j', 'KEY_LEFT']
        # up_keys = ['s', 'k', 'KEY_UP']
        # down_keys = ['d', 'l', 'KEY_DOWN']
        # right_keys = ['f', ';', 'KEY_RIGHT']
        # up_left_keys = ['7', 'KEY_HOME']
        # up_right_keys = ['9', 'KEY_PPAGE']
        # down_right_keys = ['3', 'KEY_NPAGE']
        # down_left_keys = ['1', 'KEY_END']
        # logger_mode_switch_keys = ['l']
        display_inventory_key = ['i']
        display_equip_menu_key = ['e']
        # debugPanelKey=['d']
        openKey = ['o']
        # retval = False
        if k == help_key:
            self.help_menu()
            return False
        elif k in openKey:
            self.addLog("Open in which direction?")
            self.renderer.drawMainscreen(self)
            return self.handleOpen()
        # elif k in debugPanelKey:
        #    self.debugPanel = not self.debugPanel
        #    return False
        # elif k == camera_key:
        #    if self.currentMode == "Player":
        #        self.currentMode = "Camera"
        #    elif self.currentMode == "Camera":
        #        self.currentMode = "Player"
        #    return False

        elif k in movement_keys:  # and not self.itemSelectionMode:
            if self.currentMode == "Player":
                # result = self.handle_movement(pc, k, True)
                self.handle_movement(pc, k, True)
            elif self.currentMode == "Camera":
                self.handle_camera_movement(k)
                return False
            elif self.currentMode == "Logger":
                self.handle_logger_movement(k)
                return False
        # elif k in logger_mode_switch_keys:
        #    if self.currentMode != "Logger":
        #        self.currentMode = "Logger"
        #        self.logger_offset = 0
        #    else:
        #        self.currentMode = "Player"
        #    return False
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
        elif k in display_equip_menu_key:
            return self.display_equip_menu()
            # return False
        # exit game
        elif k == quit_key_0 or k == quit_key_1:
            # self.renderer.draw_quit_screen()
            exit(0)
        # pickup item
        elif k == ",":
            return self.handle_item_pickup(pc)
        # wait in one spot / inspect / search ground / area around you
        elif k == ".":
            return True  # more to implement later...
        elif k == 'm':
            # experimenting with drawing windows on top of the dungeon
            return False
        else:
            self.addLog(f"Unimplemented key pressed: {k}")
            return False
        return True

    def handleOpenDirection(self, key):
        assert(key is not None)
        # assert(key in ['1','2','3','4','5','6','7','8','9'])
        # self.addLog(f"{key}")
        y = 0
        x = 0
        dirs = {
            'KEY_LEFT': (0, -1),
            'KEY_RIGHT': (0, 1),
            'KEY_UP': (-1, 0),
            'KEY_DOWN': (1, 0),
            '1': (1, -1),
            'KEY_END': (1, -1),
            '2': (1, 0),
            '3': (1, 1),
            'KEY_NPAGE': (1, 1),
            '4': (0, -1),
            '5': (0, 0),
            '6': (0, 1),
            '7': (-1, -1),
            'KEY_HOME': (-1, -1),
            '8': (-1, 0),
            '9': (-1, 1),
            'KEY_PPAGE': (-1, 1),
        }
        try:
            y = dirs[key][0]
            x = dirs[key][1]
            newX = self.pc.x + x
            newY = self.pc.y + y
            for i in range(len(self.dungeonFloor.doors)):
                door = self.dungeonFloor.doors[i]
                if door.x == newX and door.y == newY:
                    prevState = door.isClosed
                    log = ''
                    if prevState:
                        log = 'Opened door'
                    else:
                        log = 'Closed door'
                    self.addLog(log)
                    door.isClosed = not door.isClosed
                    return True
            self.addLog("No door to open")
            return True
        except Exception:
            return False

    def handleOpen(self):
        # self.addLog("Open in which direction?")
        key = self.renderer.s.getkey()
        return self.handleOpenDirection(key)

    def removeItemFromDungeonFloor(self, item):
        # find the real item in the dungeonFloor items list and remove it
        for x in range(len(self.dungeonFloor.items)):
            item_ = self.dungeonFloor.items[x]
            if item == item_:
                self.dungeonFloor.items.pop(x)
                break

    def handle_item_pickup_main(self, pc, k):
        # get all items on current tile
        items = [item for item in self.dungeonFloor.items if item.x == pc.x and
                 item.y == pc.y]
        item = items[int(k)]
        # pc.items.append( item )# add the item to the pc's items
        pc.addItemToInventory(item)
        self.removeItemFromDungeonFloor(item)
        self.addLog(f"{self.currentTurnCount}: {pc.name} picked up a \
                    {item.name}")
        self.itemSelectionMode = False

    def decrOneHungerUnitPC(self):
        self.pc.hunger -= 1
        if self.pc.hunger <= 0:
            self.addLog(f"{self.pc.name} died of hunger! Game over!")
            self.renderer.draw_quit_screen()
            exit(0)
        elif self.pc.hunger < (self.pc.maxhunger / 4):
            if not self.hasShownStarvingMessage:
                self.addLog(f"{self.pc.name} is fkn dyin of hunger!")
                self.hasShownStarvingMessage = True
                self.hasShownHungerMessage = True
        elif self.pc.hunger < (self.pc.maxhunger / 2):
            if not self.hasShownHungerMessage:
                self.addLog(f"{self.pc.name} starts to get hongreh")
                self.hasShownHungerMessage = True

    def incrOneHungerUnitPC(self):
        self.pc.hunger += 1
        if self.pc.hunger >= self.pc.maxhunger:
            self.pc.hunger = self.pc.maxhunger

    def process_npc_turn(self):
        # for right now, lets make them move randomly
        movement_keys = ['KEY_DOWN', 'KEY_UP', 'KEY_RIGHT', 'KEY_LEFT']
        for i in range(len(self.dungeonFloor.npcs)):
            try:
                npc = self.dungeonFloor.npcs[i]
                # select a random keypress
                random_index = randint(0, len(movement_keys)-1)
                random_key = movement_keys[random_index]
                self.handle_movement(npc, random_key, False)
                # self.handle_movement( npc , random_key, True )
            except Exception:
                pass

    def handleItemPickupHelper(self, i):
        x = self.pc.x
        y = self.pc.y
        items = [item for item in self.dungeonFloor.items if item.x == x and
                 item.y == y]
        assert(i >= 0)
        assert(i <= len(items))
        if i == len(items):
            return False
        item = items[i]
        # add the item to the pc's items
        self.pc.items.append(item)
        self.addLog(f"{self.currentTurnCount}: {self.pc.name} picked up a \
                    {item.name}")

        # find the real item in the dungeonFloor items list and remove it
        for k in range(len(self.dungeonFloor.items)):
            item_ = self.dungeonFloor.items[k]
            # self.addLog(f"Looping...{item_.name}")
            if item_.x == item.x and item_.y == item.y:
                # self.addLog(f"Removing item from dungeon: {item_.name}")
                # self.dungeonFloor.items.pop(x)
                del self.dungeonFloor.items[k]
                return True
        # should never get here...

    def handle_item_pickup(self, pc):
        x = pc.x
        y = pc.y
        items = [item for item in self.dungeonFloor.items if item.x == x and
                 item.y == y]
        # single-item case
        # if len(items)==1:
        #    pc.items.append( items[0] )
        #    self.addLog(f"{self.currentTurnCount}: Picked up {items[0].name}")
        #    self.dungeonFloor.items.pop(0)
        #    return True
        # multiple-items case
        if len(items) >= 1:
            menuItems = [(items[i].name, self.handleItemPickupHelper, i)
                         for i in range(len(items))]
            testMenuTitle = "Which item would you like to pick up?"
            self.testMenu = ItemPickupMenu(testMenuTitle, menuItems,
                                           self.renderer.s, self)
            return self.testMenu.display()
        # do nothing
        self.addLog(f"{self.currentTurnCount}: There is nothing here!")
        pass

    def eatFood(self, item):
        # get hunger points on item
        self.pc.hunger += item.hungerpoints
        if self.pc.hunger > self.pc.maxhunger:
            self.pc.hunger = self.pc.maxhunger
        self.addLog(f"{self.pc.name} ate a {item.name}")

    def displayInventoryHelper(self, i):
        item = self.pc.items[i]
        if item.itemclass == ItemClass.FOOD:
            # eat food
            self.eatFood(item)
            # remove item
            del self.pc.items[i]
        else:
            self.addLog(f"Cannot use item {item} yet")
        pass

    # bp: bodypart
    def displaySubequipmenuHelper(self, bp, item):
        # actually perform the equipping
        success = False
        mylog = None
        if bp == Bodypart.Righthand or bp == Bodypart.Lefthand:
            if self.pc.lefthand != item and self.pc.righthand != item:
                if bp == Bodypart.Righthand:
                    self.pc.righthand = item
                elif bp == Bodypart.Lefthand:
                    self.pc.lefthand = item
                success = True
            elif self.pc.lefthand == item:
                mylog = f"{item.name} is already equipped on \
                    {Bodypart.Lefthand}"
            elif self.pc.righthand == item:
                mylog = f"{item.name} is already equipped on \
                    {Bodypart.Righthand}"
        else:
            mylog = f"Equipping on {bp} is unimplemented right now..."
        if success:
            mylog = f"{self.pc.name} equipped a {item.name} on their {bp}"
        if mylog is not None:
            self.addLog(mylog)
        return success

    def displayEquipMenuHelper(self, bodypart):
        items = self.pc.items
        menuItems = [(bodypart, items[i], self.displaySubequipmenuHelper)
                     for i in range(len(items))]
        title = "Which item are you equipping?"
        if len(menuItems) == 0:
            title = "You have nothing to equip!"
        else:
            menuItems.append(("Exit", None))
        self.subequipMenu = Subequipmenu(title, menuItems, self.renderer.s,
                                         self)
        return self.subequipMenu.display()

    def display_inventory(self, pc):
        items = pc.items
        menuItems = [(items[i].name, self.displayInventoryHelper, i)
                     for i in range(len(items))]
        self.testMenu = InventoryMenu("Inventory", menuItems, self.renderer.s,
                                      self)
        self.testMenu.display()

    def display_equip_menu(self):
        myfun = self.displayEquipMenuHelper
        menuItems = [
            (Bodypart.Righthand, myfun),
            (Bodypart.Lefthand,  myfun),
            ("Exit",             None)
        ]
        mystr = 'Which body part are you equipping on?'
        self.equipMenu = EquipMenu(mystr, menuItems, self.renderer.s, self)
        return self.equipMenu.display()

    def handle_resize(self):
        rows, cols = self.renderer.s.getmaxyx()
        self.renderer.s.clear()
        resizeterm(rows, cols)
        self.renderer.s.refresh()

    def handle_movement(self, entity, k, doLog):
        y = 0
        x = 0
        lefts = ['KEY_LEFT', '4']
        downs = ['KEY_DOWN', '2']
        ups = ['KEY_UP', '8']
        rights = ['KEY_RIGHT', '6']
        ul = ['7', 'KEY_HOME']
        ur = ['9', 'KEY_PPAGE']
        dl = ['1', 'KEY_END']
        dr = ['3', 'KEY_NPAGE']
        noMove = ['5', 'KEY_B2']
        if self.leftHandVim:
            lefts.append('a')
            downs.append('s')
            ups.append('d')
            rights.append('f')
            ul.append('r')
            ur.append('t')
            dl.append('c')
            dr.append('v')
        if self.rightHandVim:
            lefts.append('j')
            downs.append('k')
            ups.append('l')
            rights.append(';')
            ul.append('y')
            ur.append('u')
            dl.append('b')
            dr.append('n')

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
        elif k in noMove:
            x = 0
            y = 0
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
        if k == 'a' or k == 'j' or k == 'KEY_LEFT':  # left
            self.camera.x -= 1
        elif k == 's' or k == 'k' or k == 'KEY_UP':  # up
            self.camera.y -= 1
        elif k == 'd' or k == 'l' or k == 'KEY_DOWN':  # down
            self.camera.y += 1
        elif k == 'f' or k == ';' or k == 'KEY_RIGHT':  # right
            self.camera.x += 1

    def check_movement(self, entity, y, x, doLog):
        assert(entity is not None)
        assert(y in [-1, 0, 1])
        assert(x in [-1, 0, 1])
        assert(isinstance(doLog, bool))
        retval = True
        dir_ = ""
        if y == 0 and x == 1:
            dir_ = "east"
        elif y == 1 and x == 0:
            dir_ = "south"
        elif y == -1 and x == 0:
            dir_ = "north"
        elif y == 0 and x == -1:
            dir_ = "west"
        elif y == -1 and x == -1:
            dir_ = "northwest"
        elif y == -1 and x == 1:
            dir_ = "northeast"
        elif y == 1 and x == -1:
            dir_ = "southwest"
        elif y == 1 and x == 1:
            dir_ = "southeast"
        elif y == 0 and x == 0:
            dir_ = "no direction"
            retval = True
        if dir_ != "no direction":
            result = self.check_pc_next_tile(entity, y, x)
            if not result:
                if doLog and entity.is_player:
                    mylog = f"{self.currentTurnCount}: {entity.name} tried to \
                        walk {dir_} but cannot!"
                    self.addLog(mylog)
                retval = False
            else:
                result = self.check_pc_npc_collision(entity, y, x)
                if not result:
                    dc = self.checkEntityDoorCollision(entity, y, x)
                    if dc:
                        for d in self.dungeonFloor.doors:
                            if d.x == dc.x and d.y == dc.y:
                                if doLog and entity.is_player:
                                    mylog = f"There is a {d.doortype} door\
                                        here"
                                    self.addLog(mylog)
                                return False
                    entity.y += y
                    entity.x += x
                    ic = self.check_pc_item_collision(entity)
                    if ic:
                        for item in self.dungeonFloor.items:
                            if item.x == ic.x and item.y == ic.y:
                                if doLog and entity.is_player:
                                    self.addLog(f"There is a {item.name} here")
                else:
                    self.handle_pc_npc_collision(entity, result, doLog)
        return retval

    def check_pc_next_tile(self, pc, y, x):
        assert(pc is not None)
        assert(y in [-1, 0, 1])
        assert(x in [-1, 0, 1])
        retval = False
        rows = self.dungeonFloor.rows
        cols = self.dungeonFloor.cols
        walkable_tiles = [
            Tiletype.STONE_FLOOR,
            Tiletype.GRASS
        ]
        if self.check_pc_dungeon_bounds(pc, y, x):
            nx = pc.x + x
            ny = pc.y + y
            if nx >= 0 and nx < cols and ny >= 0 and ny < rows:
                next_tile = self.dungeonFloor.map_[pc.y+y][pc.x+x]
                if next_tile.tiletype in walkable_tiles:
                    retval = True
        return retval

    def handle_pc_npc_collision(self, pc, npc, doLog):
        if isinstance(npc, Entity):
            pc.attack(npc, doLog)
            if npc.hp <= 0:
                if doLog:
                    mylog = f"{self.currentTurnCount}: {pc.name} killed \
                        {npc.name}!"
                    self.addLog(mylog)
                if not npc.is_player:
                    self.dungeonFloor.npcs.remove(npc)
                    # just add 1 xp for now lol
                    pc.xp += 1
                    pc.killcount += 1
                # test
                    # pc.lightradius += 1
                else:
                    # game over!
                    self.addLog(f"{npc.name} died! Game over!")
                    self.renderer.draw_quit_screen()
                    exit(0)

    def check_pc_item_collision(self, pc):
        for item in self.dungeonFloor.items:
            if pc.x == item.x and pc.y == item.y:
                return item
        return None

    def checkEntityDoorCollision(self, e, y, x):
        for d in self.dungeonFloor.doors:
            if e.x+x == d.x and e.y+y == d.y:
                if d.isClosed:
                    return d
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
                except Exception:
                    print("Caught Exception")
                    print("----------")
                    print("WTF")
            else:
                break
        self.renderer.s.refresh()
        self.renderer.s.getkey()

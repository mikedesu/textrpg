from random import randint
from Game import Game
from Game.NPC import NPC
from Game.Race import Race
from Game.Job import Job
from Game.Gender import Gender
from Game.Alignment import Alignment
from curses import color_pair as c, start_color, echo, noecho, init_pair, \
    COLOR_BLUE, COLOR_BLACK, COLOR_RED, COLOR_WHITE, COLOR_MAGENTA, A_BOLD, use_default_colors, \
    KEY_RESIZE, KEY_LEFT, KEY_RIGHT, KEY_UP, KEY_DOWN 

def get_user_input_ch(s, input_set):
    cc = s.getkey()
    while cc not in input_set:
        cc = s.getkey()
    return cc

def get_player_name(s):
    echo()
    s.clear()
    input_str = 'What is your name:'
    s.addstr(0,0,input_str,c(1))
    s.refresh()
    name = s.getstr(0, len(input_str)+1, 16).decode('utf-8')
    input_str = f'You entered: {name}'
    s.addstr(1,0,input_str,c(1))
    input_str = 'Press any key to continue'
    s.addstr(2,0,input_str,c(1))
    s.refresh()
    cc = s.getch()
    return name

def get_player_job(s):
    s.clear()
    noecho()
    input_str = 'What is your job? Select from the following:'
    s.addstr(0,0,input_str,c(1))
    input_str = 'q - Fighter'
    s.addstr(1,0,input_str,c(1))
    input_str = 'w - Cleric'
    s.addstr(2,0,input_str,c(1))
    input_str = 'e - Mage'
    s.addstr(3,0,input_str,c(1))
    input_str = 'r - Thief'
    s.addstr(4,0,input_str,c(1))
    s.refresh()
    cc = ''
    current_line = 5
    cc = get_user_input_ch(s, ['q', 'w', 'e', 'r'])
    out_str = f'You entered: '
    a = ''
    if cc=='q':
        a='Fighter'
    elif cc=='w':
        a='Cleric'
    elif cc=='e':
        a='Mage'
    elif cc=='r':
        a='Thief'
    out_str += a
    s.addstr(current_line,0,out_str,c(1))
    current_line += 1
    out_str = 'Press any key to continue'
    s.addstr(current_line,0,out_str,c(1))
    s.refresh()
    cc = s.getch()
    return a 

def get_player_alignment(s):
    s.clear()
    noecho()
    a = [
        "What is your alignment?",
        "",
        "1 - Lawful Good",
        "2 - Lawful Neutral",
        "3 - Lawful Evil",
        "4 - Neutral Good",
        "5 - True Neutral",
        "6 - Neutral Evil",
        "7 - Chaotic Good",
        "8 - Chaotic Neutral",
        "9 - Chaotic Evil"
    ]
    y=0
    for line in a:
        s.addstr(y,0,line,c(1))
        y+=1
    s.refresh()
    cc = get_user_input_ch(s, ['1','2','3','4','5','6','7','8','9'])
    
    b = None # this is causing a bug atm
    #b = Alignment.LAWFUL_GOOD 

    if cc=='1':
        b=Alignment.LAWFUL_GOOD
    elif cc=='2':
        b=Alignment.LAWFUL_NEUTRAL
    elif cc=='3':
        b=Alignment.LAWFUL_EVIL
    elif cc=='4':
        b=Alignment.NEUTRAL_GOOD
    elif cc=='5':
        b=Alignment.TRUE_NEUTRAL
    elif cc=='6':
        b=Alignment.NEUTRAL_EVIL
    elif cc=='7':
        b=Alignment.CHAOTIC_GOOD
    elif cc=='8':
        b=Alignment.CHAOTIC_NEUTRAL
    elif cc=='9':
        b=Alignment.CHAOTIC_EVIL

    s.addstr(y, 0, f"You entered: {b}", c(1))
    s.addstr(y+1, 0, f"Press any key to continue", c(1))
    s.getkey()
    return b




def get_player_gender(s):
    s.clear()
    noecho()
    input_str = 'What is your gender? Select from the following:'
    s.addstr(0,0,input_str,c(1))
    input_str = 'q - Male'
    s.addstr(1,0,input_str,c(1))
    input_str = 'w - Female'
    s.addstr(2,0,input_str,c(1))
    s.refresh()
    cc = get_user_input_ch(s, ['q', 'w'])
    out_str = f'You entered: '
    a = ''
    if cc=='q':
        a='Male'
    elif cc=='w':
        a='Female'
    out_str += a
    current_line = 3
    s.addstr(current_line,0,out_str,c(1))
    current_line += 1
    out_str = 'Press any key to continue'
    s.addstr(current_line,0,out_str,c(1))
    s.refresh()
    cc = s.getch()
    return a 

def get_player_race(s):
    s.clear()
    noecho()
    input_str = 'What is your race? Select from the following:'
    s.addstr(0,0,input_str,c(1))
    input_str = 'q - Human'
    s.addstr(1,0,input_str,c(1))
    input_str = 'w - Elf'
    s.addstr(2,0,input_str,c(1))
    input_str = 'e - Dwarf'
    s.addstr(3,0,input_str,c(1))
    input_str = 'r - Gnome'
    s.addstr(4,0,input_str,c(1))
    s.refresh()
    cc = ''
    current_line = 5
    cc = get_user_input_ch(s, ['q', 'w', 'e', 'r'])
    out_str = f'You entered: '
    a = ''
    if cc=='q':
        a='Human'
    elif cc=='w':
        a='Elf'
    elif cc=='e':
        a='Dwarf'
    elif cc=='r':
        a='Gnome'
    out_str += a
    s.addstr(current_line,0,out_str,c(1))
    current_line += 1
    out_str = 'Press any key to continue'
    s.addstr(current_line,0,out_str,c(1))
    s.refresh()
    cc = s.getch()
    return a 

def translate_race_str_to_enum(race):
    r = None
    if race == 'Human':
        r = Race.HUMAN
    elif race == 'Elf':
        r = Race.ELF 
    elif race == 'Dwarf':
        r = Race.DWARF 
    elif race == 'Gnome':
        r = Race.GNOME 
    return r

def translate_job_str_to_enum(job):
    r = None
    if job == 'Fighter':
        r = Job.FIGHTER 
    elif job == 'Mage':
        r = Job.MAGE 
    elif job == 'Thief':
        r = Job.THIEF 
    elif job == 'Cleric':
        r = Job.CLERIC 
    return r

def translate_gender_str_to_enum(gender):
    r = None
    if gender == 'Male':
        r = Gender.MALE
    elif gender == 'Female':
        r = Gender.FEMALE
    return r
def translate_alignment_str_to_enum(alignment):
    r = None
    if alignment == 'Lawful Good':
        r = Alignment.LAWFUL_GOOD
    elif alignment == 'Lawful Neutral':
        r = Alignment.LAWFUL_NEUTRAL
    elif alignment == 'Lawful Evil':
        r = Alignment.LAWFUL_EVIL
    elif alignment == 'Chaotic Good':
        r = Alignment.CHAOTIC_GOOD
    elif alignment == 'Chaotic Neutral':
        r = Alignment.CHAOTIC_NEUTRAL
    elif alignment == 'Chaotic Evil':
        r = Alignment.CHAOTIC_EVIL
    elif alignment == 'Neutral Good':
        r = Alignment.NEUTRAL_GOOD
    elif alignment == 'True Neutral':
        r = Alignment.TRUE_NEUTRAL
    elif alignment == 'Neutral Evil':
        r = Alignment.NEUTRAL_EVIL
    return r



def generate_random_stats():
    a = [ randint(3,18), randint(3,18), randint(3,18), randint(3,18), randint(3,18), randint(3,18) ]
    return a

def handle_new_game_stats(s, rerolls = 0, total_rerolls = 3):
    noecho()
    s.clear()
    y = 0
    s.addstr(y,0,"Rolling your character's stats...",c(1))
    # traditional d&d 3.0-style
    # 3d6, so lowest stat can be rolled is 3 and highest is 18
    a = generate_random_stats()
    s.addstr(y+1, 0, f"Strength: {a[0]}", c(1))
    s.addstr(y+2, 0, f"Dexterity: {a[1]}", c(1))
    s.addstr(y+3, 0, f"Constitution: {a[2]}", c(1))
    s.addstr(y+4, 0, f"Intelligence: {a[3]}", c(1))
    s.addstr(y+5, 0, f"Wisdom: {a[4]}", c(1))
    s.addstr(y+6, 0, f"Charisma: {a[5]}", c(1))
    s.addstr(y+8, 0, "If this is acceptable, press c", c(1))
    s.addstr(y+9, 0, f"If you wish to re-roll, press r (Re-rolls \
remaining: {total_rerolls - rerolls})", c(1))
    s.refresh()
    y += 10
    cc = get_user_input_ch(s, ['r', 'c'])
    if cc == 'c':
        return a
    elif cc == 'r' and rerolls < total_rerolls:
        return handle_new_game_stats(s, rerolls+1, total_rerolls)
    elif cc == 'r':
        s.addstr(y, 0, "Too many re-rolls!", c(1))
        s.addstr(y+1, 0, "Using most recent roll...", c(1))
        s.refresh()
        cc = s.getch()
        return a
    # should never get here
    return None



def new_character_display(s, pc):
    s.clear()
    stats = pc.attribs
    y = 0
    x = 0
    s.addstr(y,   x, f"Your name: {pc.name}",  c(1))
    s.addstr(y+1, x, f"Your race: {pc.race}" , c(1))
    s.addstr(y+2, x, f"Gender: {pc.gender}",   c(1))
    s.addstr(y+3, x, f"Alignment: {pc.alignment}",   c(1))
    s.addstr(y+4, x, f"Your job: {pc.job}" ,   c(1))
    y += 5
    stat_names = ["Strength: ", "Dexterity: ", "Constitution: ", 
                  "Intelligence: ", "Wisdom: ", "Charisma: " ]
    for i in range(len(stats)):
        stat_name_str = stat_names[i]
        s.addstr(y+i, x, f"{stat_name_str} {stats[i]}", c(1))
    y += len(stats)
    s.addstr(y+1, x, f"Press any key to continue", c(1))
    s.refresh()
    cc = s.getch()





def new_character(s):
    name = get_player_name(s)
    stats = handle_new_game_stats( s , 0, 3 )
    race = translate_race_str_to_enum( get_player_race(s) )
    job  = translate_job_str_to_enum( get_player_job(s) )
    gender = translate_gender_str_to_enum( get_player_gender(s) )
    alignment =  get_player_alignment(s) 
    pc = NPC(name=name, level=1, race=race, job=job, attribs=stats, 
        gender=gender, alignment=alignment, is_player=True)

    new_character_display(s, pc)
    return pc 


def quick_new_character(s):
    name = "dm"
    stats = generate_random_stats()
    race = Race.HUMAN 
    job  = Job.MAGE
    gender = Gender.MALE
    alignment = Alignment.LAWFUL_EVIL
    pc = NPC(name=name, level=1, race=race, job=job, attribs=stats, gender=gender, alignment=alignment, is_player=True)
    return pc 



def help_menu(renderer):
    renderer.s.clear()
    a = None
    with open("txt/helpmenu.txt", "r") as infile:
        a = infile.readlines()
    y = 0
    for line in a:
        renderer.s.addstr(y, 0, line, c(1))
        y += 1
    renderer.s.refresh()
    renderer.s.getkey()


def check_pc_dungeon_bounds(game, pc, y, x):
    retval = True 
    if pc.x+x < 0 or pc.y+y < 0 or pc.y+y > len(game.dungeonFloor.map_)-4 or pc.x+x > len(game.dungeonFloor.map_[0])-1:
        game.addLog("cannot go outside dungeon walls")
        retval = False
    return retval

def check_pc_npc_collision(game, pc, y, x):
    for npc in game.dungeonFloor.npcs:
        if pc.x + x == npc.x and pc.y + y == npc.y:
            # in other words, pc WOULD move into the npc
            # so we'd return true
            game.addLog("bumped into npc")
            return True
    return False
            



def handle_input(game, renderer, pc, k):
    rows, cols = renderer.s.getmaxyx()
    # Help Menu
    help_key = '?'
    quit_key_0 = 'q'
    quit_key_1 = 'Q'
    input_keys = [ 'a', 's', 'd', 'f', 'j', 'k', 'l', ';', 'KEY_DOWN', 'KEY_UP', 'KEY_RIGHT', 'KEY_LEFT', 'KEY_RESIZE', quit_key_0, quit_key_1, help_key ]
    movement_keys = ['a','s','d','f','j','k','l',';','KEY_DOWN', 'KEY_UP', 'KEY_RIGHT', 'KEY_LEFT']
    left_keys = ['a','j','KEY_LEFT']
    up_keys =   ['s','k','KEY_UP']
    down_keys = ['d','l','KEY_DOWN']
    right_keys = ['f',';','KEY_RIGHT']
    if k == '?':
        help_menu(renderer)
        return False
    elif k in movement_keys:
        

        if k == 'a' or k == 'j' or k == 'KEY_LEFT': # left
            if not check_pc_npc_collision( game, pc, 0, -1 ):
                if check_pc_dungeon_bounds(game, pc, 0, -1):
                    pc.x -= 1
        elif k == 's' or k == 'k' or k == 'KEY_UP': # up
            if not check_pc_npc_collision( game, pc, -1, 0 ):
                if check_pc_dungeon_bounds(game, pc, -1, 0):
                    pc.y -= 1
        elif k == 'd' or k == 'l' or k == 'KEY_DOWN': # down
            if not check_pc_npc_collision( game, pc, 1, 0 ):
                if check_pc_dungeon_bounds(game, pc, 1, 0):
                    pc.y += 1
        elif k == 'f' or k == ';' or k == 'KEY_RIGHT': # right
            if not check_pc_npc_collision( game, pc, 0, 1 ):
                if check_pc_dungeon_bounds(game, pc, 0, 1 ):
                    pc.x += 1



        #check_pc_dungeon_bounds(game, pc)
    elif k == KEY_RESIZE:
        handle_resize(renderer)
        return False
    # exit game
    elif k == quit_key_0 or k == quit_key_1:
        exit(0)
    else:
        game.addLog(f"Unimplemented key pressed: {k}")
        return False
    return True

def handle_resize(renderer):
    rows, cols = renderer.s.getmaxyx()
    renderer.s.clear()
    renderer.s.resizeterm(rows, cols)
    renderer.s.refresh()


from Game import Game
from Game.NPC import NPC
from Game.Race import Race
from Game.Job import Job
from curses import start_color
from curses import echo
from curses import noecho
from curses import init_pair
from curses import color_pair as c
from curses import COLOR_BLACK
from curses import COLOR_RED
from curses import COLOR_WHITE
from curses import A_BOLD
from curses import use_default_colors

from random import randint


#def startup(s):
#    use_default_colors()
#    start_color()
#    s.clear()
#    init_pair(1, COLOR_WHITE, -1)
#    init_pair(2, COLOR_RED,   COLOR_WHITE)
#    init_pair(3, COLOR_BLACK, COLOR_WHITE)

def get_user_input_ch(s, input_set):
    cc = s.getkey()
    while cc not in input_set:
        cc = s.getkey()
    return cc

def draw_titlescreen(s):
    s.addstr(0, 0, 'Welcome to the RPG', c(1))
    s.addstr(1, 0, 'By darkmage', c(1))
    s.addstr(2, 0, 'This is error text', c(2) | A_BOLD)
    s.addstr(3, 0, 'Press q to quit', c(3))
    s.addstr(4, 0, 'Press n for new game', c(3))
    s.refresh()

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

def generate_random_stats():
    a = [ randint(3,18), randint(3,18), randint(3,18), randint(3,18), 
          randint(3,18), randint(3,18) ]
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


def new_character(s):
    name = get_player_name(s)
    stats = handle_new_game_stats( s , 0, 3 )
    race = translate_race_str_to_enum( get_player_race(s) )
    job  = translate_job_str_to_enum( get_player_job(s) )
    pc = NPC(name, 1, race, job, stats)
    s.clear()
    y = 0
    x = 0
    your_name_str = "Your name: "
    s.addstr(y, x, f"{your_name_str}", c(1))
    x += len(your_name_str)
    s.addstr(y, x, f"{pc.name}", c(1)) # no formatting
    x = 0
    y += 1
    your_race_str = "Your race: "
    s.addstr(y, x, f"{your_race_str}", c(1))
    x += len(your_race_str)
    s.addstr(y, x, f"{pc.race}" , c(1))
    x = 0
    y += 1
    your_job_str = "Your job: "
    s.addstr(y, x, f"{your_job_str}", c(1))
    x += len(your_job_str)
    s.addstr(y, x, f"{pc.job}" , c(1))
    x = 0
    y += 1
    stat_names = ["Strength: ", "Dexterity: ", "Constitution: ", 
                  "Intelligence: ", "Wisdom: ", "Charisma: " ]
    for i in range(len(stats)):
        stat_name_str = stat_names[i]
        s.addstr(y+i, x, f"{stat_name_str}", c(1))
        x += len(stat_name_str)
        s.addstr(y+i, x, f"{stats[i]}" , c(1))
        x = 0
    y += len(stats)
    s.addstr(y+1, x, f"Press any key to continue", c(1))
    s.refresh()
    cc = s.getch()
    return pc 



def draw_main_screen(s, pc):
    # experimental main-game drawing
    s.clear()
    rows, cols = s.getmaxyx()
    x, y = 0, 0
    line = "-" * cols
    s.addstr(y, x, line)
    y += 1
    line = "|" + (" "*(cols-2)) + "|"
    while y < rows-4:
        s.addstr(y, x, line)
        y += 1
    line = "-" * cols
    s.addstr(y, x, line)
    y += 1
    s.addstr(y, x, str(pc))
    s.refresh()
 

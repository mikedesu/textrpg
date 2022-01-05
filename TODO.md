# TODO

## Bugfixes Needed

- Create food/rations
- Enemies need to sometimes drop corpses, rations, and other items 
- Options-menu on Title Screen
    - Controls
        - Left-hand VIM-like mode  ON/OFF
        - Right-hand VIM-like mode ON/OFF
- VIM-like movement for menus and door-opening
- Non-numpad movement in menus 
- Light radius issue(s):
    - The distance formula seems to be off-by-one vertically
    - We should not be able to see what is behind a closed door
- Escape should be able to close menus (can't do right now)
    - Python curses handles escape key differently
- Numpad movement in menus

--------------------------------------------------------------------------------

## Easy 

- Maybe get rid of the whole left/right-hand concept entirely? 
    - Make it like: Free hands?
        - Free hand 1
        - Free hand 2
- Actually make equipped-shields matter during attacks
- Weapon-classes (Blunt, Cutting, Poking)
- Kicking ('k')

--------------------------------------------------------------------------------

## Medium

- Actually-Good Name Generator
- Be able to immediately equip items that might be on the floor
- Notes that you can pick-up and read
- Kicking doors down / breaking doors down
    - How would I implement this?
        - Similar to open door
- Chests / storage containers
- Shields
- Equipping Shields
- Basic NPC Movement
    - intelligent movement
    - movement "strategies"
- Basic dungeon crafting
    - Define a room
- Basics of a shell/terminal for longer commands and debugging
- Add the properties for handling turn priority
    - based off of Dexterity

--------------------------------------------------------------------------------

## Hard / Long

- Deciding on the experience-level progression
- proper HELP menu(s)
- item class definition
    - weapon sub-class 
    - armor sub-class
        - deeper-system definition:
            arms, legs, feet, torso, head, shoulders, back, 
    - usable items
        - potions
        - candles
        - torches
        - etc
    - weight
        - actually manage the weight in a game-balancing way so that you can't just pick up infinite items


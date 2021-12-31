# TODO

## Bugfixes Needed

- Opening doors diagonally does not work for some reason
- Light radius issue(s):
    - The distance formula seems to be off-by-one vertically
    - We should not be able to see what is behind a closed door
- Escape should be able to close menus
- Numpad movement in menus

--------------------------------------------------------------------------------

## Easy 

- Basic Name Generator
- Actually make equipped-shields matter during attacks
- Weapon-classes (Blunt, Cutting, Poking)
- Kicking ('k')

--------------------------------------------------------------------------------

## Medium

- Be able to immediately equip items that might be on the floor
- Tile-discovery so tiles stay "lit-up" after you "discover" them
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


# TODO

## Bugfixes Needed

- Create food/rations
- Enemies need to sometimes drop corpses, rations, and other items 
- Light radius issue(s):
    - The distance formula seems to be off-by-one vertically
    - We should not be able to see what is behind a closed door
- New logging system needs to push old messages off-screen
    - calc # of log-lines on-screen
- Turn off all the addLog windows for now

--------------------------------------------------------------------------------

## Easy 

- Actually make equipped-shields matter during attacks
- Weapon-classes (Blunt, Cutting, Poking)
- Kicking ('k')

--------------------------------------------------------------------------------

## Medium

- Fatalities (thx b-rex for the suggestion!)
    - limb-targeting (ala Vagrant Story-style)
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
- Actually-Good Name Generator


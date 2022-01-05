
# CHANGELOG

-----

## 05-01-2021
    - MessageWindow (using the Menu class)
    - NameGenerator generating totally random names lol

## 04-01-2021
    - OptionMenu beginning
    - Re-factored how TitleMenu and OptionMenu are constructed
        - Menu-contents can largely be defined internally now
    - Left and Right-hand VIM-like movement are temporarily enabled
             r t  y u
        a s d f    j k l ;
             c v  b n
        Left-hand VIM-mode has a key-conflict with the debugPanel
    - Started a Pipfile for the project anticipating library-dependencies, but we have none :D

## 31-12-2021
    - Re-did title screen as a Menu
    - Re-named renderer methods to stand in defiance of PEP 8 :D 
    - Created an "EndgameScreen" to display credits, thanks, etc.
    - Opening doors diagonally does NOW work because i fixed it :D 
    - Tile-discovery so tiles stay "lit-up" after you "discover" them

## 28-12-2021
    - Opening doors with 'o' and then a direction no longer crashes (arrowkeys still wont work for this)
    - Hitting enter on an empty inventory screen no longer crashes the game
    - Can now open doors using arrow keys in addition to numpad movement keys

## 26-12-2021
    - Debug panel by pressing 'd'
    - Basic hallway drawing
    - Basic wooden doors, closed, functionally blocking you from walking down a halfway
    - Light radius basics!
    - Demo: killing enemies increases your lightradius

## 21-12-2021
    - Equipping weapon on right hand now impacts attack and damage calc
    - Equipping weapons costs 1 turn, no cost to exit the menu
    - Equipping weapons on either left or right hand is now possible! 
    - updated how item symbols are set. it is now based on the item's itemclass.
    - When an enemy makes attack contact with you, need to log that event *DONE* 
    - There appears to be a glitch with item placement. Items I've only single-placed in the dungeon are able to be picked up twice sometimes *MAYBE FIXED*

## 17-12-2021
    - item pickup menu!
        - looks good, functions as intended
    - bugfixes
        - logger no longer uses turns
        - camera no longer uses turns or hunger
        - *FIXED* that damn rendering bug!!!!
        - Hitting 'Exit' on the ItemPickupMenu no longer consumes a turn!

## 15-12-2021
    - several changes since last update, including:
        - diagonal movement
        - bugfixes
    - Personality Traits
        - Speciesm 

## 10-12-2021
    - added: multiple items on a single tile, also handling selecting from among multiple items when picking up an item

## 05-12-2021
    - fixed: camera-rendering bug, where dungeon was being rendered above/below the dungeon UI
    - fixed: same with NPCs
    - fixed: camera off-screen rendering bug, where game would crash on too-far X left/right movement
    - added: quit screen
    - added: basic item rendering
    - added: basic item logic - can walk on top of item and have it recognized
    - added: basic item logic - can pick up an item now and it no longer renders in the dungeon

## 02-12-2021
    - fixed: Problem displaying help menu lol
    - fixed: after swapping to tiles, the renderer is once again overlaying the dungeon on top of the bottom HUD

## 28-11-2021
    - created CHANGELOG
    - extend the top log window area by a couple lines
    - handling resize events
        - dungeon and npcs drawn within viewport
    - not hard-coding bounds detection
    - checking next tile before moving
    - smaller starting sandbox room

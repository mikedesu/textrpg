
# CHANGELOG

-----

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

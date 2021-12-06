
# CHANGELOG

-----

## 05-12-2021
    - fixed: camera-rendering bug, where dungeon was being rendered above/below the dungeon UI
    - fixed: same with NPCs
    - fixed: camera off-screen rendering bug, where game would crash on too-far X left/right movement

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
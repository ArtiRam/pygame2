import pygame

GRASS = 1
WATER = 2
STONE = 3

textures = {
    GRASS: "gfx\grass.png",
    WATER: "gfx\water.png",
    STONE: "gfx\stone.png"

    }

tile_map = [
       [GRASS, GRASS, WATER, WATER, WATER, GRASS],
       [WATER, GRASS, WATER, WATER, WATER, GRASS],
       [WATER, GRASS, WATER, WATER, WATER, GRASS],
       [WATER, GRASS, WATER, WATER, WATER, GRASS],
    ]

tilesize = 32
# encoding: utf-8
"""

                   GNU GENERAL PUBLIC LICENSE

                       Version 3, 29 June 2007


 Copyright (C) 2007 Free Software Foundation, Inc. <http://fsf.org/>

 Everyone is permitted to copy and distribute verbatim copies

 of this license document, but changing it is not allowed.
 """
__author__ = "Yoann Berenguer"
__copyright__ = "Copyright 2007, Cobra Project"
__credits__ = ["Yoann Berenguer"]
__license__ = "GPL"
__version__ = "1.0.0"
__maintainer__ = "Yoann Berenguer"
__email__ = "yoyoberenguer@hotmail.com"
__status__ = "Alpha Demo"


import pygame
from Sprites import EPIMET_ASTEROID_SPRITE, HYPERION_ASTEROID_SPRITE, PROMETHEUS_ASTEROID_SPRITE, \
    PROMETHEUS1_ASTEROID_SPRITE, STATIC_ASTEROID_SPRITE, DEIMOS_ASTEROID_SPRITE, BURST_DOWN_RED, EXPLOSIONS
from random import randint
from Constants import MAX_PLAYER_HITPOINTS
from Sounds import IMPACT1, EXPLOSION_COLLECTION_SOUND

# Various asteroid sizes
sizes = ['16x16', '32x32', '48x48', '64x64', '80x80', '96x96', '112x112', '128x128', '256x256']
# Gained scores
score = [100, 120, 140, 200, 320, 350, 400, 500, 700]
mass = [10, 20, 30, 40, 60, 70, 80, 90, 180]


class Asteroids:

    def __init__(self, animation_, name_, explosion_, impact_animation_, size_, explosion_sound_, impact_sound_):
        # -------------- ANIMATION ---------------------
        self.animation = animation_.copy()
        self.explosion = explosion_.copy()
        self.impact_animation = impact_animation_.copy()
        # -----------------------------------------------
        self.name = name_
        self.size = sizes[size_ % len(sizes) - 1]
        self.asteroid_class = size_

        self.hp = [randint(10, 50), randint(51, 150), randint(151, 300), randint(301, 450),
                   randint(451, 550), randint(551, 700), randint(701, 1000), randint(1001, 1500),
                   randint(1501, 2000)][size_ % len(sizes) - 1]
        self.max_hp = self.hp

        self.score = score[size_ % len(score) - 1]
        self.mass = mass[size_ % len(mass) - 1]

        if isinstance(animation_, list):
            _i = 0

            for surface_ in animation_:
                self.animation[_i] = pygame.transform.smoothscale(surface_, [int(self.size.split('x')[0]),
                                                                             int(self.size.split('x')[1])])
                _i += 1
        else:
            self.animation = pygame.transform.smoothscale(animation_, [int(self.size.split('x')[0]),
                                                                       int(self.size.split('x')[1])])

        if isinstance(explosion_, list):
            _i = 0
            for surface_ in self.explosion:
                self.explosion[_i] = pygame.transform.smoothscale(surface_, (round(surface_.get_width() * size_ / 3),
                                                                             round(surface_.get_height() * size_ / 3)))
                _i += 1
        else:
            self.explosion = pygame.transform.smoothscale(animation_, (round(surface_.get_width() * size_ / 3),
                                                                       round(surface_.get_height() * size_ // 3)))

        self.damage = [randint(5, 100), randint(101, 200), randint(201, 300),
                       randint(301, 400), randint(401, 500), randint(501, 600),
                       MAX_PLAYER_HITPOINTS, MAX_PLAYER_HITPOINTS, MAX_PLAYER_HITPOINTS][size_]

        self.explosion_sound = explosion_sound_
        self.impact_sound = impact_sound_


asteroids_list = [Asteroids(EPIMET_ASTEROID_SPRITE, 'EPIMET_CLASS_1', EXPLOSIONS[randint(0, len(EXPLOSIONS) - 1)],
                            BURST_DOWN_RED, 1,
                            EXPLOSION_COLLECTION_SOUND[randint(0, len(EXPLOSION_COLLECTION_SOUND) - 1)], IMPACT1),
                  Asteroids(EPIMET_ASTEROID_SPRITE, 'EPIMET_CLASS_2', EXPLOSIONS[randint(0, len(EXPLOSIONS) - 1)],
                            BURST_DOWN_RED, 2,
                            EXPLOSION_COLLECTION_SOUND[randint(0, len(EXPLOSION_COLLECTION_SOUND) - 1)], IMPACT1),
                  Asteroids(EPIMET_ASTEROID_SPRITE, 'EPIMET_CLASS_3', EXPLOSIONS[randint(0, len(EXPLOSIONS) - 1)],
                            BURST_DOWN_RED, 3,
                            EXPLOSION_COLLECTION_SOUND[randint(0, len(EXPLOSION_COLLECTION_SOUND) - 1)], IMPACT1),
                  Asteroids(EPIMET_ASTEROID_SPRITE, 'EPIMET_CLASS_4', EXPLOSIONS[randint(0, len(EXPLOSIONS) - 1)],
                            BURST_DOWN_RED, 4,
                            EXPLOSION_COLLECTION_SOUND[randint(0, len(EXPLOSION_COLLECTION_SOUND) - 1)], IMPACT1),
                  Asteroids(HYPERION_ASTEROID_SPRITE, 'HYPERION_CLASS_1', EXPLOSIONS[randint(0, len(EXPLOSIONS) - 1)],
                            BURST_DOWN_RED, 1,
                            EXPLOSION_COLLECTION_SOUND[randint(0, len(EXPLOSION_COLLECTION_SOUND) - 1)], IMPACT1),
                  Asteroids(HYPERION_ASTEROID_SPRITE, 'HYPERION_CLASS_2', EXPLOSIONS[randint(0, len(EXPLOSIONS) - 1)],
                            BURST_DOWN_RED, 2,
                            EXPLOSION_COLLECTION_SOUND[randint(0, len(EXPLOSION_COLLECTION_SOUND) - 1)], IMPACT1),
                  Asteroids(HYPERION_ASTEROID_SPRITE, 'HYPERION_CLASS_3', EXPLOSIONS[randint(0, len(EXPLOSIONS) - 1)],
                            BURST_DOWN_RED, 3,
                            EXPLOSION_COLLECTION_SOUND[randint(0, len(EXPLOSION_COLLECTION_SOUND) - 1)], IMPACT1),
                  Asteroids(HYPERION_ASTEROID_SPRITE, 'HYPERION_CLASS_4', EXPLOSIONS[randint(0, len(EXPLOSIONS) - 1)],
                            BURST_DOWN_RED, 4,
                            EXPLOSION_COLLECTION_SOUND[randint(0, len(EXPLOSION_COLLECTION_SOUND) - 1)], IMPACT1),
                  Asteroids(PROMETHEUS_ASTEROID_SPRITE, 'PROMETHEUS_CLASS_1',
                            EXPLOSIONS[randint(0, len(EXPLOSIONS) - 1)],
                            BURST_DOWN_RED, 1,
                            EXPLOSION_COLLECTION_SOUND[randint(0, len(EXPLOSION_COLLECTION_SOUND) - 1)], IMPACT1),
                  Asteroids(PROMETHEUS_ASTEROID_SPRITE, 'PROMETHEUS_CLASS_2',
                            EXPLOSIONS[randint(0, len(EXPLOSIONS) - 1)],
                            BURST_DOWN_RED, 2,
                            EXPLOSION_COLLECTION_SOUND[randint(0, len(EXPLOSION_COLLECTION_SOUND) - 1)], IMPACT1),
                  Asteroids(PROMETHEUS_ASTEROID_SPRITE, 'PROMETHEUS_CLASS_3',
                            EXPLOSIONS[randint(0, len(EXPLOSIONS) - 1)],
                            BURST_DOWN_RED, 3,
                            EXPLOSION_COLLECTION_SOUND[randint(0, len(EXPLOSION_COLLECTION_SOUND) - 1)], IMPACT1),
                  Asteroids(PROMETHEUS_ASTEROID_SPRITE, 'PROMETHEUS_CLASS_4',
                            EXPLOSIONS[randint(0, len(EXPLOSIONS) - 1)],
                            BURST_DOWN_RED, 4,
                            EXPLOSION_COLLECTION_SOUND[randint(0, len(EXPLOSION_COLLECTION_SOUND) - 1)], IMPACT1),
                  Asteroids(PROMETHEUS1_ASTEROID_SPRITE, 'PROMETHEUS1_CLASS_1',
                            EXPLOSIONS[randint(0, len(EXPLOSIONS) - 1)], BURST_DOWN_RED, 1,
                            EXPLOSION_COLLECTION_SOUND[randint(0, len(EXPLOSION_COLLECTION_SOUND) - 1)], IMPACT1),
                  Asteroids(PROMETHEUS1_ASTEROID_SPRITE, 'PROMETHEUS1_CLASS_2',
                            EXPLOSIONS[randint(0, len(EXPLOSIONS) - 1)], BURST_DOWN_RED, 2,
                            EXPLOSION_COLLECTION_SOUND[randint(0, len(EXPLOSION_COLLECTION_SOUND) - 1)], IMPACT1),
                  Asteroids(PROMETHEUS1_ASTEROID_SPRITE, 'PROMETHEUS1_CLASS_3',
                            EXPLOSIONS[randint(0, len(EXPLOSIONS) - 1)], BURST_DOWN_RED, 3,
                            EXPLOSION_COLLECTION_SOUND[randint(0, len(EXPLOSION_COLLECTION_SOUND) - 1)], IMPACT1),
                  Asteroids(PROMETHEUS1_ASTEROID_SPRITE, 'PROMETHEUS1_CLASS_4',
                            EXPLOSIONS[randint(0, len(EXPLOSIONS) - 1)], BURST_DOWN_RED, 4,
                            EXPLOSION_COLLECTION_SOUND[randint(0, len(EXPLOSION_COLLECTION_SOUND) - 1)], IMPACT1),
                  Asteroids(STATIC_ASTEROID_SPRITE[0], 'DEIMOS_STATIC_CLASS_1',
                            EXPLOSIONS[randint(0, len(EXPLOSIONS) - 1)], BURST_DOWN_RED, 1,
                            EXPLOSION_COLLECTION_SOUND[randint(0, len(EXPLOSION_COLLECTION_SOUND) - 1)], IMPACT1),
                  Asteroids(STATIC_ASTEROID_SPRITE[0], 'DEIMOS_STATIC_CLASS_2',
                            EXPLOSIONS[randint(0, len(EXPLOSIONS) - 1)], BURST_DOWN_RED, 2,
                            EXPLOSION_COLLECTION_SOUND[randint(0, len(EXPLOSION_COLLECTION_SOUND) - 1)], IMPACT1),
                  Asteroids(STATIC_ASTEROID_SPRITE[0], 'DEIMOS_STATIC_CLASS_3',
                            EXPLOSIONS[randint(0, len(EXPLOSIONS) - 1)], BURST_DOWN_RED, 3,
                            EXPLOSION_COLLECTION_SOUND[randint(0, len(EXPLOSION_COLLECTION_SOUND) - 1)], IMPACT1),
                  Asteroids(STATIC_ASTEROID_SPRITE[0], 'DEIMOS_STATIC_CLASS_4',
                            EXPLOSIONS[randint(0, len(EXPLOSIONS) - 1)], BURST_DOWN_RED, 4,
                            EXPLOSION_COLLECTION_SOUND[randint(0, len(EXPLOSION_COLLECTION_SOUND) - 1)], IMPACT1),
                  Asteroids(STATIC_ASTEROID_SPRITE[1], 'ENCELA_STATIC_CLASS_1',
                            EXPLOSIONS[randint(0, len(EXPLOSIONS) - 1)], BURST_DOWN_RED, 1,
                            EXPLOSION_COLLECTION_SOUND[randint(0, len(EXPLOSION_COLLECTION_SOUND) - 1)], IMPACT1),

                  Asteroids(STATIC_ASTEROID_SPRITE[1], 'ENCELA_STATIC_CLASS_2',
                            EXPLOSIONS[randint(0, len(EXPLOSIONS) - 1)],
                            BURST_DOWN_RED, 1,
                            EXPLOSION_COLLECTION_SOUND[randint(0, len(EXPLOSION_COLLECTION_SOUND) - 1)], IMPACT1),

                  Asteroids(STATIC_ASTEROID_SPRITE[1], 'ENCELA_STATIC_CLASS_3',
                            EXPLOSIONS[randint(0, len(EXPLOSIONS) - 1)],
                            BURST_DOWN_RED, 3,
                            EXPLOSION_COLLECTION_SOUND[randint(0, len(EXPLOSION_COLLECTION_SOUND) - 1)], IMPACT1),
                  Asteroids(STATIC_ASTEROID_SPRITE[1], 'ENCELA_STATIC_CLASS_4',
                            EXPLOSIONS[randint(0, len(EXPLOSIONS) - 1)],
                            BURST_DOWN_RED, 4,
                            EXPLOSION_COLLECTION_SOUND[randint(0, len(EXPLOSION_COLLECTION_SOUND) - 1)], IMPACT1),
                  Asteroids(STATIC_ASTEROID_SPRITE[2], 'EPIMET_STATIC_CLASS_1',
                            EXPLOSIONS[randint(0, len(EXPLOSIONS) - 1)],
                            BURST_DOWN_RED, 1,
                            EXPLOSION_COLLECTION_SOUND[randint(0, len(EXPLOSION_COLLECTION_SOUND) - 1)], IMPACT1),
                  Asteroids(STATIC_ASTEROID_SPRITE[2], 'EPIMET_STATIC_CLASS_2',
                            EXPLOSIONS[randint(0, len(EXPLOSIONS) - 1)],
                            BURST_DOWN_RED, 2,
                            EXPLOSION_COLLECTION_SOUND[randint(0, len(EXPLOSION_COLLECTION_SOUND) - 1)], IMPACT1),
                  Asteroids(STATIC_ASTEROID_SPRITE[2], 'EPIMET_STATIC_CLASS_3',
                            EXPLOSIONS[randint(0, len(EXPLOSIONS) - 1)],
                            BURST_DOWN_RED, 3,
                            EXPLOSION_COLLECTION_SOUND[randint(0, len(EXPLOSION_COLLECTION_SOUND) - 1)], IMPACT1),
                  Asteroids(STATIC_ASTEROID_SPRITE[2], 'EPIMET_STATIC_CLASS_4',
                            EXPLOSIONS[randint(0, len(EXPLOSIONS) - 1)],
                            BURST_DOWN_RED, 4,
                            EXPLOSION_COLLECTION_SOUND[randint(0, len(EXPLOSION_COLLECTION_SOUND) - 1)], IMPACT1),
                  Asteroids(STATIC_ASTEROID_SPRITE[3], 'HYPERION_STATIC_CLASS_1',
                            EXPLOSIONS[randint(0, len(EXPLOSIONS) - 1)],
                            BURST_DOWN_RED, 1,
                            EXPLOSION_COLLECTION_SOUND[randint(0, len(EXPLOSION_COLLECTION_SOUND) - 1)], IMPACT1),
                  Asteroids(STATIC_ASTEROID_SPRITE[3], 'HYPERION_STATIC_CLASS_2',
                            EXPLOSIONS[randint(0, len(EXPLOSIONS) - 1)],
                            BURST_DOWN_RED, 2,
                            EXPLOSION_COLLECTION_SOUND[randint(0, len(EXPLOSION_COLLECTION_SOUND) - 1)], IMPACT1),
                  Asteroids(STATIC_ASTEROID_SPRITE[3], 'HYPERION_STATIC_CLASS_3',
                            EXPLOSIONS[randint(0, len(EXPLOSIONS) - 1)],
                            BURST_DOWN_RED, 3,
                            EXPLOSION_COLLECTION_SOUND[randint(0, len(EXPLOSION_COLLECTION_SOUND) - 1)], IMPACT1),
                  Asteroids(STATIC_ASTEROID_SPRITE[3], 'HYPERION_STATIC_CLASS_3',
                            EXPLOSIONS[randint(0, len(EXPLOSIONS) - 1)],
                            BURST_DOWN_RED, 4,
                            EXPLOSION_COLLECTION_SOUND[randint(0, len(EXPLOSION_COLLECTION_SOUND) - 1)], IMPACT1),
                  Asteroids(STATIC_ASTEROID_SPRITE[4], 'HYPERION1_STATIC_CLASS_1',
                            EXPLOSIONS[randint(0, len(EXPLOSIONS) - 1)],
                            BURST_DOWN_RED, 1,
                            EXPLOSION_COLLECTION_SOUND[randint(0, len(EXPLOSION_COLLECTION_SOUND) - 1)], IMPACT1),
                  Asteroids(STATIC_ASTEROID_SPRITE[4], 'HYPERION1_STATIC_CLASS_2',
                            EXPLOSIONS[randint(0, len(EXPLOSIONS) - 1)],
                            BURST_DOWN_RED, 2,
                            EXPLOSION_COLLECTION_SOUND[randint(0, len(EXPLOSION_COLLECTION_SOUND) - 1)], IMPACT1),
                  Asteroids(STATIC_ASTEROID_SPRITE[4], 'HYPERION1_STATIC_CLASS_3',
                            EXPLOSIONS[randint(0, len(EXPLOSIONS) - 1)],
                            BURST_DOWN_RED, 3,
                            EXPLOSION_COLLECTION_SOUND[randint(0, len(EXPLOSION_COLLECTION_SOUND) - 1)], IMPACT1),
                  Asteroids(STATIC_ASTEROID_SPRITE[4], 'HYPERION1_STATIC_CLASS_4',
                            EXPLOSIONS[randint(0, len(EXPLOSIONS) - 1)],
                            BURST_DOWN_RED, 4,
                            EXPLOSION_COLLECTION_SOUND[randint(0, len(EXPLOSION_COLLECTION_SOUND) - 1)], IMPACT1),
                  Asteroids(STATIC_ASTEROID_SPRITE[5], 'JANUS_STATIC_CLASS_1',
                            EXPLOSIONS[randint(0, len(EXPLOSIONS) - 1)],
                            BURST_DOWN_RED, 1,
                            EXPLOSION_COLLECTION_SOUND[randint(0, len(EXPLOSION_COLLECTION_SOUND) - 1)], IMPACT1),
                  Asteroids(STATIC_ASTEROID_SPRITE[5], 'JANUS_STATIC_CLASS_2',
                            EXPLOSIONS[randint(0, len(EXPLOSIONS) - 1)],
                            BURST_DOWN_RED, 2,
                            EXPLOSION_COLLECTION_SOUND[randint(0, len(EXPLOSION_COLLECTION_SOUND) - 1)], IMPACT1),
                  Asteroids(STATIC_ASTEROID_SPRITE[5], 'JANUS_STATIC_CLASS_3',
                            EXPLOSIONS[randint(0, len(EXPLOSIONS) - 1)],
                            BURST_DOWN_RED, 3,
                            EXPLOSION_COLLECTION_SOUND[randint(0, len(EXPLOSION_COLLECTION_SOUND) - 1)], IMPACT1),
                  Asteroids(STATIC_ASTEROID_SPRITE[5], 'JANUS_STATIC_CLASS_4',
                            EXPLOSIONS[randint(0, len(EXPLOSIONS) - 1)],
                            BURST_DOWN_RED, 4,
                            EXPLOSION_COLLECTION_SOUND[randint(0, len(EXPLOSION_COLLECTION_SOUND) - 1)], IMPACT1),
                  Asteroids(STATIC_ASTEROID_SPRITE[6], 'PROMETHEUS_STATIC_CLASS_1',
                            EXPLOSIONS[randint(0, len(EXPLOSIONS) - 1)],
                            BURST_DOWN_RED, 1,
                            EXPLOSION_COLLECTION_SOUND[randint(0, len(EXPLOSION_COLLECTION_SOUND) - 1)], IMPACT1),
                  Asteroids(STATIC_ASTEROID_SPRITE[6], 'PROMETHEUS_STATIC_CLASS_2',
                            EXPLOSIONS[randint(0, len(EXPLOSIONS) - 1)],
                            BURST_DOWN_RED, 2,
                            EXPLOSION_COLLECTION_SOUND[randint(0, len(EXPLOSION_COLLECTION_SOUND) - 1)], IMPACT1),
                  Asteroids(STATIC_ASTEROID_SPRITE[6], 'PROMETHEUS_STATIC_CLASS_3',
                            EXPLOSIONS[randint(0, len(EXPLOSIONS) - 1)],
                            BURST_DOWN_RED, 3,
                            EXPLOSION_COLLECTION_SOUND[randint(0, len(EXPLOSION_COLLECTION_SOUND) - 1)], IMPACT1),
                  Asteroids(STATIC_ASTEROID_SPRITE[6], 'PROMETHEUS_STATIC_CLASS_4',
                            EXPLOSIONS[randint(0, len(EXPLOSIONS) - 1)],
                            BURST_DOWN_RED, 4,
                            EXPLOSION_COLLECTION_SOUND[randint(0, len(EXPLOSION_COLLECTION_SOUND) - 1)], IMPACT1, ),
                  Asteroids(STATIC_ASTEROID_SPRITE[7], 'DEIMOS_STATIC_CLASS_3_LAVA1',
                            EXPLOSIONS[randint(0, len(EXPLOSIONS) - 1)],
                            BURST_DOWN_RED, 3,
                            EXPLOSION_COLLECTION_SOUND[randint(0, len(EXPLOSION_COLLECTION_SOUND) - 1)], IMPACT1),
                  Asteroids(STATIC_ASTEROID_SPRITE[8], 'DEIMOS_STATIC_CLASS_3_LAVA2',
                            EXPLOSIONS[randint(0, len(EXPLOSIONS) - 1)],
                            BURST_DOWN_RED, 3,
                            EXPLOSION_COLLECTION_SOUND[randint(0, len(EXPLOSION_COLLECTION_SOUND) - 1)], IMPACT1),
                  Asteroids(STATIC_ASTEROID_SPRITE[9], 'DEIMOS_STATIC_CLASS_3_LAVA3',
                            EXPLOSIONS[randint(0, len(EXPLOSIONS) - 1)],
                            BURST_DOWN_RED, 3,
                            EXPLOSION_COLLECTION_SOUND[randint(0, len(EXPLOSION_COLLECTION_SOUND) - 1)], IMPACT1),
                  Asteroids(STATIC_ASTEROID_SPRITE[9], 'DEIMOS_STATIC_CLASS_3_LAVA3',
                            EXPLOSIONS[randint(0, len(EXPLOSIONS) - 1)],
                            BURST_DOWN_RED, 3,
                            EXPLOSION_COLLECTION_SOUND[randint(0, len(EXPLOSION_COLLECTION_SOUND) - 1)], IMPACT1),
                  Asteroids(STATIC_ASTEROID_SPRITE[10], 'DEIMOS_STATIC_CLASS_3_LAVA4',
                            EXPLOSIONS[randint(0, len(EXPLOSIONS) - 1)],
                            BURST_DOWN_RED, 3,
                            EXPLOSION_COLLECTION_SOUND[randint(0, len(EXPLOSION_COLLECTION_SOUND) - 1)], IMPACT1),
                  Asteroids(STATIC_ASTEROID_SPRITE[11], 'DEIMOS_STATIC_CLASS_3_LAVA5',
                            EXPLOSIONS[randint(0, len(EXPLOSIONS) - 1)],
                            BURST_DOWN_RED, 3,
                            EXPLOSION_COLLECTION_SOUND[randint(0, len(EXPLOSION_COLLECTION_SOUND) - 1)], IMPACT1),
                  Asteroids(STATIC_ASTEROID_SPRITE[12], 'DEIMOS_STATIC_CLASS_3_LAVA6',
                            EXPLOSIONS[randint(0, len(EXPLOSIONS) - 1)],
                            BURST_DOWN_RED, 3,
                            EXPLOSION_COLLECTION_SOUND[randint(0, len(EXPLOSION_COLLECTION_SOUND) - 1)], IMPACT1),
                  # Asteroids(STATIC_ASTEROID_SPRITE[13], 'ENCELA_STATIC_CLASS_3_LAVA1',
                  #          EXPLOSIONS[randint(0, len(EXPLOSIONS) - 1)],
                  #          BURST_DOWN_RED, 3,
                  #          EXPLOSION_COLLECTION_SOUND[randint(0, len(EXPLOSION_COLLECTION_SOUND) - 1)], IMPACT1),
                  Asteroids(STATIC_ASTEROID_SPRITE[14], 'ENCELA_STATIC_CLASS_3_LAVA2',
                            EXPLOSIONS[randint(0, len(EXPLOSIONS) - 1)],
                            BURST_DOWN_RED, 3,
                            EXPLOSION_COLLECTION_SOUND[randint(0, len(EXPLOSION_COLLECTION_SOUND) - 1)], IMPACT1),
                  Asteroids(STATIC_ASTEROID_SPRITE[15], 'ENCELA_STATIC_CLASS_3_LAVA3',
                            EXPLOSIONS[randint(0, len(EXPLOSIONS) - 1)],
                            BURST_DOWN_RED, 3,
                            EXPLOSION_COLLECTION_SOUND[randint(0, len(EXPLOSION_COLLECTION_SOUND) - 1)], IMPACT1),

                  Asteroids(STATIC_ASTEROID_SPRITE[16], 'EPIMET_STATIC_CLASS_3_LAVA1',
                            EXPLOSIONS[randint(0, len(EXPLOSIONS) - 1)],
                            BURST_DOWN_RED, 3,
                            EXPLOSION_COLLECTION_SOUND[randint(0, len(EXPLOSION_COLLECTION_SOUND) - 1)], IMPACT1),
                  Asteroids(STATIC_ASTEROID_SPRITE[17], 'EPIMET_STATIC_CLASS_3_LAVA2',
                            EXPLOSIONS[randint(0, len(EXPLOSIONS) - 1)],
                            BURST_DOWN_RED, 3,
                            EXPLOSION_COLLECTION_SOUND[randint(0, len(EXPLOSION_COLLECTION_SOUND) - 1)], IMPACT1),
                  Asteroids(STATIC_ASTEROID_SPRITE[18], 'EPIMET_STATIC_CLASS_3_LAVA3',
                            EXPLOSIONS[randint(0, len(EXPLOSIONS) - 1)],
                            BURST_DOWN_RED, 3,
                            EXPLOSION_COLLECTION_SOUND[randint(0, len(EXPLOSION_COLLECTION_SOUND) - 1)], IMPACT1),

                  Asteroids(STATIC_ASTEROID_SPRITE[19], 'HYPERION_STATIC_CLASS_3_LAVA1',
                            EXPLOSIONS[randint(0, len(EXPLOSIONS) - 1)],
                            BURST_DOWN_RED, 3,
                            EXPLOSION_COLLECTION_SOUND[randint(0, len(EXPLOSION_COLLECTION_SOUND) - 1)], IMPACT1),
                  Asteroids(STATIC_ASTEROID_SPRITE[20], 'HYPERION_STATIC_CLASS_3_LAVA2',
                            EXPLOSIONS[randint(0, len(EXPLOSIONS) - 1)],
                            BURST_DOWN_RED, 3,
                            EXPLOSION_COLLECTION_SOUND[randint(0, len(EXPLOSION_COLLECTION_SOUND) - 1)], IMPACT1),
                  Asteroids(STATIC_ASTEROID_SPRITE[21], 'HYPERION_STATIC_CLASS_3_LAVA3',
                            EXPLOSIONS[randint(0, len(EXPLOSIONS) - 1)],
                            BURST_DOWN_RED, 3,
                            EXPLOSION_COLLECTION_SOUND[randint(0, len(EXPLOSION_COLLECTION_SOUND) - 1)], IMPACT1),

                  Asteroids(STATIC_ASTEROID_SPRITE[22], 'HYPERION1_STATIC_CLASS_3_LAVA1',
                            EXPLOSIONS[randint(0, len(EXPLOSIONS) - 1)],
                            BURST_DOWN_RED, 3,
                            EXPLOSION_COLLECTION_SOUND[randint(0, len(EXPLOSION_COLLECTION_SOUND) - 1)], IMPACT1),
                  Asteroids(STATIC_ASTEROID_SPRITE[23], 'HYPERION1_STATIC_CLASS_3_LAVA2',
                            EXPLOSIONS[randint(0, len(EXPLOSIONS) - 1)],
                            BURST_DOWN_RED, 3,
                            EXPLOSION_COLLECTION_SOUND[randint(0, len(EXPLOSION_COLLECTION_SOUND) - 1)], IMPACT1),
                  Asteroids(STATIC_ASTEROID_SPRITE[24], 'HYPERION1_STATIC_CLASS_3_LAVA3',
                            EXPLOSIONS[randint(0, len(EXPLOSIONS) - 1)],
                            BURST_DOWN_RED, 3,
                            EXPLOSION_COLLECTION_SOUND[randint(0, len(EXPLOSION_COLLECTION_SOUND) - 1)], IMPACT1),

                  Asteroids(STATIC_ASTEROID_SPRITE[25], 'JANUS_STATIC_CLASS_3_LAVA1',
                            EXPLOSIONS[randint(0, len(EXPLOSIONS) - 1)],
                            BURST_DOWN_RED, 3,
                            EXPLOSION_COLLECTION_SOUND[randint(0, len(EXPLOSION_COLLECTION_SOUND) - 1)], IMPACT1),
                  Asteroids(STATIC_ASTEROID_SPRITE[26], 'JANUS_STATIC_CLASS_3_LAVA2',
                            EXPLOSIONS[randint(0, len(EXPLOSIONS) - 1)],
                            BURST_DOWN_RED, 3,
                            EXPLOSION_COLLECTION_SOUND[randint(0, len(EXPLOSION_COLLECTION_SOUND) - 1)], IMPACT1),
                  Asteroids(STATIC_ASTEROID_SPRITE[27], 'JANUS_STATIC_CLASS_3_LAVA3',
                            EXPLOSIONS[randint(0, len(EXPLOSIONS) - 1)],
                            BURST_DOWN_RED, 3,
                            EXPLOSION_COLLECTION_SOUND[randint(0, len(EXPLOSION_COLLECTION_SOUND) - 1)], IMPACT1),

                  Asteroids(STATIC_ASTEROID_SPRITE[28], 'PROMETHE_STATIC_CLASS_3_LAVA1',
                            EXPLOSIONS[randint(0, len(EXPLOSIONS) - 1)],
                            BURST_DOWN_RED, 3,
                            EXPLOSION_COLLECTION_SOUND[randint(0, len(EXPLOSION_COLLECTION_SOUND) - 1)], IMPACT1),
                  Asteroids(STATIC_ASTEROID_SPRITE[29], 'PROMETHE_STATIC_CLASS_3_LAVA2',
                            EXPLOSIONS[randint(0, len(EXPLOSIONS) - 1)],
                            BURST_DOWN_RED, 3,
                            EXPLOSION_COLLECTION_SOUND[randint(0, len(EXPLOSION_COLLECTION_SOUND) - 1)], IMPACT1),
                  Asteroids(STATIC_ASTEROID_SPRITE[30], 'PROMETHE_STATIC_CLASS_3_LAVA3',
                            EXPLOSIONS[randint(0, len(EXPLOSIONS) - 1)],
                            BURST_DOWN_RED, 3,
                            EXPLOSION_COLLECTION_SOUND[randint(0, len(EXPLOSION_COLLECTION_SOUND) - 1)], IMPACT1),


                  Asteroids(DEIMOS_ASTEROID_SPRITE, 'DEIMOS_CLASS_1', EXPLOSIONS[randint(0, len(EXPLOSIONS) - 1)],
                            BURST_DOWN_RED, 1,
                            EXPLOSION_COLLECTION_SOUND[randint(0, len(EXPLOSION_COLLECTION_SOUND) - 1)], IMPACT1),
                  Asteroids(DEIMOS_ASTEROID_SPRITE, 'DEIMOS_CLASS_2', EXPLOSIONS[randint(0, len(EXPLOSIONS) - 1)],
                            BURST_DOWN_RED, 2,
                            EXPLOSION_COLLECTION_SOUND[randint(0, len(EXPLOSION_COLLECTION_SOUND) - 1)], IMPACT1),
                  Asteroids(DEIMOS_ASTEROID_SPRITE, 'DEIMOS_CLASS_3', EXPLOSIONS[randint(0, len(EXPLOSIONS) - 1)],
                            BURST_DOWN_RED, 3,
                            EXPLOSION_COLLECTION_SOUND[randint(0, len(EXPLOSION_COLLECTION_SOUND) - 1)], IMPACT1),
                  Asteroids(DEIMOS_ASTEROID_SPRITE, 'DEIMOS_CLASS_4', EXPLOSIONS[randint(0, len(EXPLOSIONS) - 1)],
                            BURST_DOWN_RED, 4,
                            EXPLOSION_COLLECTION_SOUND[randint(0, len(EXPLOSION_COLLECTION_SOUND) - 1)], IMPACT1)]

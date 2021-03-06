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

from Constants import SCREENRECT
from Sprites import ANOMALY_1, ANOMALY_2, ANOMALY_3, ANOMALY_4, ANOMALY_5


class Anomaly:
    active = False

    def __init__(self, name_: str, animation_: list):
        assert isinstance(name_, str), 'Expecting string for argument name_ got %s ' % type(name_)
        assert isinstance(animation_, list), 'Expecting list for argument animation_ got %s ' % type(animation_)
        self.images = animation_
        self.image = animation_[0]
        self.name = name_
        # Position will be set before instantiation
        self.Rect = self.image.get_rect(center=SCREENRECT.center)

    def location(self):
        return self.Rect

    def set_centre(self, x, y):
        assert isinstance(x, int), 'Expecting int for argument x got %s ' % type(x)
        assert isinstance(y, int), 'Expecting int for argument y got %s ' % type(y)
        self.Rect.center = (x, y)


anomalies_list = [Anomaly(name_='ANOMALY_1', animation_=ANOMALY_1),
                  Anomaly(name_='ANOMALY_2', animation_=ANOMALY_2),
                  Anomaly(name_='ANOMALY_3', animation_=ANOMALY_3),
                  Anomaly(name_='ANOMALY_4', animation_=ANOMALY_4),
                  Anomaly(name_='ANOMALY_5', animation_=ANOMALY_5),
                  ]

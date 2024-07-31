from game.components.power_ups.power_up import PowerUp
from game.utils.constants import HEART, HEART_TYPE


class Live(PowerUp):
    def __init__(self):
        super().__init__(HEART, HEART_TYPE)

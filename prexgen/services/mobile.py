from enum import Enum
from random import choice, uniform

class MobileTypes(Enum):
    MOTOR = 'motorizado'
    PERSON = 'pessoa'
    OBJECT = 'objeto'



class Mobile:
    def __init__(self, t: 'MobileTypes', is_male: bool, n: str,
            pr: dict):
        for k, v in pr.items():
            assert (isinstance(v, tuple) and len(v) == 2)

        self.type = t
        self.name = n
        self.is_male = is_male
        self.property_ranges = pr
        

    def __str__(self):
        return f"{self.name}"


    def set_random_length(self) -> float:
        return uniform(self.property_ranges['length'][0], self.property_ranges['length'][1])


    def set_random_speed(self) -> float:
        return uniform(self.property_ranges['speed'][0], self.property_ranges['speed'][1])


    def set_random_distance(self) -> float:
        return uniform(self.property_ranges['distance'][0], self.property_ranges['distance'][1])


    def set_random_mass(self) -> float:
        return uniform(self.property_ranges['mass'][0], self.property_ranges['mass'][1])
    


class MobileOptions(Enum):
    MOTOCYCLE = Mobile(MobileTypes.MOTOR, False, 'moto',
        {'length': (1.5, 2.5), 'distance': (500, 300_000), 'speed': (10, 35), 'mass': (110, 500)})
    CAR = Mobile(MobileTypes.MOTOR, True, 'carro', 
        {'length': (1.6, 5), 'distance': (500, 300_000), 'speed': (10, 35), 'mass': (6e2, 2e3)})
    TRUCK = Mobile(MobileTypes.MOTOR, True, 'caminhão',
        {'length': (3, 14), 'distance': (500, 300_000), 'speed': (10, 35), 'mass': (1e3, 3.6e5)})
    TRAIN = Mobile(MobileTypes.MOTOR, True, 'trem',
        {'length': (50, 500), 'distance': (2000, 500_000), 'speed': (10, 150), 'mass': (6e4, 1e8)})
    
    PERSON = Mobile(MobileTypes.PERSON, False, 'pessoa',
        {'length': (0, 0), 'distance': (100, 5_000), 'speed': (.5, 2), 'mass': (50, 100)})
    ATHELETE = Mobile(MobileTypes.PERSON, True, 'atleta',
        {'length': (0, 0), 'distance': (5_000, 30_000), 'speed': (2, 5), 'mass': (60, 120)})

    BILLIARD_BALL = Mobile(MobileTypes.OBJECT, False, 'bola de bilhar',
        {'length': (.05, .07), 'distance': (.01, 2), 'speed': (1, 14), 'mass': (.15, .17)})
    BRICK = Mobile(MobileTypes.OBJECT, True, 'tijolo',
        {'length': (.1, .3), 'distance': (.5, 30), 'speed': (.5, 2), 'mass': (.5, 5)})

    def __str__(self):
        return self.value.__str__()

    @staticmethod
    def randomMobile(mobile_can_be_person: bool):
        return choice(list(MobileOptions)).value if mobile_can_be_person else choice([m.value for m in MobileOptions if m.value.type == MobileTypes.MOTOR])


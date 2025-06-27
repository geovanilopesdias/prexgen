from enum import Enum
from random import choice, uniform

class MobileTypes(Enum):
    MOTOR = 'motorizado'
    SPECIAL = 'especial'
    PERSON = 'pessoa'
    OBJECT = 'objeto'



class Mobile:
    def __init__(self, t: 'MobileTypes', is_male: bool, n: str, pr: dict):
        self.type = t
        self.name = n
        self.is_male = is_male

        self.check_range_registration_standard(pr)
        self.property_ranges = pr
        

    def __str__(self):
        return f"{self.name}"


    def check_range_registration_standard(self, ranges_to_set: dict):
        for k, v in ranges_to_set.items():
            if not isinstance(v, tuple):
                raise ValueError("All Mobile instance ranges must be tuples.")
            if len(v) != 2:
                raise ValueError("Only the minimum and maximum value of Mobile ranges must be prescribed.")
            if v[0] > v[1]:
                raise ValueError("The minimum value of Mobile range must be listed first.")


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

    BRICK = Mobile(MobileTypes.OBJECT, True, 'tijolo',
        {'length': (.1, .3), 'distance': (.5, 30), 'speed': (.5, 2), 'mass': (.5, 5)})
    BALL = Mobile(MobileTypes.OBJECT, False, 'bola',
        {'length': (.15, .3), 'distance': (1, 200), 'speed': (5, 20), 'mass': (.35, .45)})
    BOX = Mobile(MobileTypes.OBJECT, False, 'caixa',
        {'length': (0, 0), 'distance': (0, 0), 'speed': (1, 5), 'mass': (.5, 20)})
    VASE = Mobile(MobileTypes.OBJECT, True, 'vaso',
        {'length': (0, 0), 'distance': (0, 0), 'speed': (1, 5), 'mass': (.1, 3)})
    
    BILLIARD_BALL = Mobile(MobileTypes.SPECIAL, False, 'bola de bilhar',
        {'length': (.05, .07), 'distance': (.01, 2), 'speed': (1, 14), 'mass': (.15, .17)})
    ROLLER_COASTER_TRAIN = Mobile(MobileTypes.SPECIAL, True, 'vagão de montanha-russa',
        {'length': (10, 20), 'distance': (15, 1_000), 'speed': (1, 65), 'mass': (4_000, 10_000)})

    def __str__(self):
        return self.value.__str__()


    @staticmethod
    def random_mobile(mobile_can_be_person: bool) -> 'Mobile':
        return (
            choice([m.value for m in MobileOptions if m.value.type in (MobileTypes.PERSON, MobileTypes.MOTOR)]) if mobile_can_be_person
            else choice([m.value for m in MobileOptions if m.value.type == MobileTypes.MOTOR])
        )
    
    @staticmethod
    def random_object() -> 'Mobile':
        """
        Returns a random instance of Mobile as an raw object (box, ball etc.).
        """
        return choice([m.value for m in MobileOptions if m.value.type == MobileTypes.OBJECT])
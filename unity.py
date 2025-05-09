from random import choice
from enum import Enum

class UnitType(Enum):
    LENGTH = 'comprimento'
    TIME = 'tempo'
    SPEED = 'velocidade'
    ACCELERATION = 'aceleração'
    MASS = 'massa'
    VOLUME = 'volume'
    ENERGY = 'energia'



class Unity:
    def __init__(self, n: str, s: str, t: 'UnitType', e: float):
        self.name = n
        self.symbol = s
        self.type = t
        self.si_eq = e  # Factor to multiply for in order to obtain the SI measure


    def __str__(self, symbol_should_be_shown: bool = False):
        return f"{self.name} ({self.symbol})" if symbol_should_be_shown else f"{self.name}"
        
    

class UnitiesTable(Enum):
    METER = Unity('metro', 'm', UnitType.LENGTH, 1.0)
    MILE = Unity('milhas', 'mi', UnitType.LENGTH, 1_609.34)
    CENTIMETER = Unity('centímetro', 'cm', UnitType.LENGTH, 1e-2)
    KILOMETER = Unity('quilômetro', 'km', UnitType.LENGTH, 1e3)
    INCH = Unity('polegada', 'in', UnitType.LENGTH, .0254)

    SECOND = Unity('segundo', 's', UnitType.TIME, 1)
    MINUTE = Unity('minuto', 'min', UnitType.TIME, 60)
    HOUR = Unity('hora', 'h', UnitType.TIME, 3_600)

    METER_PER_SECOND = Unity('metro por segundo', 'm/s', UnitType.SPEED, 1.0)
    KILOMETER_PER_HOUR = Unity('quilômetro por hora', 'km/h', UnitType.SPEED, 1/3.6)
    MILE_PER_HOUR = Unity('milha por hora', 'mi/h', UnitType.SPEED, .44704)

    METER_PER_SECOND_SQUARE = Unity('metro por segundo ao quadrado', 'm/s²', UnitType.ACCELERATION, 1.0)
    KILOMETER_PER_HOUR_PER_SECOND = Unity('quilômetro por hora por segundo', 'km/h∙s', UnitType.ACCELERATION, 1/3.6)

    KILOGRAM = Unity('quilograma', 'kg', UnitType.MASS, 1.0)
    GRAM = Unity('quilograma', 'kg', UnitType.MASS, 1e-3)
    MILIGRAM = Unity('quilograma', 'kg', UnitType.MASS, 1e-6)
    METRIC_TONNE = Unity('tonelada', 'ton', UnitType.MASS, 1e3)

    JOULE = Unity('joule', 'J', UnitType.ENERGY, 1.0)
    

    def __str__(self):
        return self.value.__str__()
           
    
    @staticmethod
    def randomUnity(variable: str):
        match variable:
            case ('distance' | 'length' | 'height' | 'mobile_length' | 'section_length'):
                return UnitiesTable.randomLengthUnity()
            case ('speed' | 'velocity' | 'higher_speed' | 'lower_speed'):
                return UnitiesTable.randomSpeedUnity()
            case ('time' | 'interval' | 'instant' | 'time_difference'):
                return UnitiesTable.randomTimeUnity()
            case _:
                raise ValueError(f'Variable {variable} not implemented.')

    
    @staticmethod
    def randomLengthUnity():
        unities = (UnitiesTable.METER, UnitiesTable.MILES, UnitiesTable.KILOMETER)
        return choice(unities)

    @staticmethod
    def randomTimeUnity():
        unities = (UnitiesTable.SECOND, UnitiesTable.MINUTE, UnitiesTable.HOUR)
        return choice(unities)

    @staticmethod
    def randomSpeedUnity():
        unities = (UnitiesTable.METER_PER_SECOND, UnitiesTable.KILOMETER_PER_HOUR, UnitiesTable.MILES_PER_HOUR)
        return choice(unities)

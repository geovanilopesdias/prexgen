from unity import *
from lexical import Lexical
from random import choice
from math import hypot, sin, cos, atan2, degrees, radians

class EscalarQuantity:
    def __init__(self, v: float, u: 'UnitiesTable', n: str, is_male: bool):
        self.value = v
        self.unity = u
        self.name = n
        self.is_male = is_male

    
    def convert_to(self, desired_unity: 'UnitiesTable'):
        """
        It changes the value and unity of the instance according to the desired_unity.
        """
        if self.unity.value.type != desired_unity.value.type:
            raise TypeError('Instance and desired unities type don\'t match.')
        
        if self.unity.value == desired_unity.value:
            return
        self.value = self.value * self.unity.value.si_eq / desired_unity.value.si_eq
        self.unity = desired_unity


    def __str__(self):
        return f"{Lexical.format_with_comma(self.value)} {self.unity.value.symbol}"

    # IS IT REALLY NECESSARY?
##    def sum_escalars(self, other_q, nem_name: str, new_name_is_male: bool): 
##        if not isinstance(other_q, EscalarQuantity):
##            raise TypeError('Other isn\'t an instance of EscalarQuantity.')
##        if self.unity != other_q.unity:
##            raise TypeError('Instance and other do not match their unities.')
##        
##        return EscalarQuantity(self.value + other_q, self.unity, new_name, new_name_is_male)

        
    def adapt_unity_randomly(self):
        """
        According to the instance value, it changes its value and unity
        to a more proper quantity expression, avoiding really small ou big
        odd/ugly values, but randomly between the enumerator.
        """
        match self.unity.value.type:
            case UnitType.LENGTH:
                self.convert_to(UnitiesTable.METER)
                if self.value >= 1_600:
                    self.convert_to(choice((UnitiesTable.KILOMETER, UnitiesTable.MILE)))
                elif self.value < .1:
                    self.convert_to(choice((UnitiesTable.CENTIMETER, UnitiesTable.INCH)))
                else:
                    return

            case UnitType.TIME:
                self.convert_to(UnitiesTable.SECOND)
                if self.value >= 200 and self.value <= 12_000:  # Between 200 s and 200 min
                    self.convert_to(UnitiesTable.MINUTE)
                elif self.value > 12_000:  # Above 200 min
                    self.convert_to(UnitiesTable.HOUR)
                else:
                    return

            case UnitType.SPEED:
                self.convert_to(choice((
                    UnitiesTable.METER_PER_SECOND, UnitiesTable.KILOMETER_PER_HOUR, UnitiesTable.MILE_PER_HOUR)))
                return

            case _:
                return


    # >>> Need to be tested!
    @staticmethod
    def adapt_all_unities_in(variables: dict):
        """
        Applies the method adapt_unity_randomly to all EscalarQuantity
        instances within the given dictionary.
        """
        for k, v in variables.items():            
            if isinstance(v, EscalarQuantity):
                v.adapt_unity_randomly() 



class BidimensionalVectorialQuantity:
    STRING_MODES = ('escalar', 'rectangular', 'polar')

    def __init__(self, u: 'UnitiesTable', n: str, is_male: bool,
        pol_n: tuple = (), rec_n: tuple = ()):
        self.value = 0
        self.unity = u
        self.name = n
        self.is_male = is_male
        self.rectangular_notation = rec_n
        self.polar_notation = pol_n


    def set_value(self):
        if not self.polar_notation:
            pass
        else:
            self.value = self.polar_notation[0]
  

    def set_rectangular_notation(self, x_coord: float = 0, y_coord: float = 0):
        """
        Sets the rectangular notation of the instance.
        As polar notation is bonded to it, it also sets it.
        """
        if not self.polar_notation:
            self.rectangular_notation = (x_coord, y_coord)
            self.set_polar_notation()
        else:
            x = self.polar_notation[0] * cos(radians(self.polar_notation[1]))
            y = self.polar_notation[0] * sin(radians(self.polar_notation[1]))
            self.rectangular_notation = (x, y)


    def set_polar_notation(self, r_coord: float = 0, theta_coord: float = 0):
        """
        Sets the polar notation of the instance.
        As rectangular notation is bonded to it, it also sets it.
        """
        if not self.rectangular_notation:
            self.polar_notation = (r_coord, theta_coord)
            self.set_rectangular_notation()
        else:
            r = hypot(self.rectangular_notation[0], self.rectangular_notation[1])
            t = degrees(atan2(self.rectangular_notation[1], self.rectangular_notation[0]))
            t += 360 if t < 0 else 0
            self.polar_notation = (r, t)
        self.set_value()


    def __str__(self):
        return f"{Lexical.format_with_comma(self.value)} {self.unity.value.symbol}"


    def to_string_as(self, mode: str = 'escalar'):
        if mode not in self.STRING_MODES:
            raise ValueError(f"Mode must be one of {self.STRING_MODES}.")
        match mode:
            case 'escalar':
                return self.__str__()

            case 'rectangular':
                if not self.rectangular_notation:
                    raise IndexError('Rectangular notation tuple attribute is not set.')

                x_coord = f"{self.rectangular_notation[0]}î" if self.rectangular_notation[0] != 0 else ''
                y_coord = f"{self.rectangular_notation[1]}ĵ" if self.rectangular_notation[1] != 0 else ''
                middle_signal = '+' if self.rectangular_notation[1] >= 0 else ''
                return f"({x_coord}{middle_signal}{y_coord}) {self.unity.value.symbol}"

            case 'polar':
                if not self.polar_notation:
                    raise IndexError('Polar notation tuple attribute is not set.')
                
                r_coord = self.polar_notation[0]
                theta_coord = self.polar_notation[1]
                return f"{Lexical.format_with_comma(r_coord)} {self.unity.value.symbol} ∡ {theta_coord}°"



# Tests:
v = BidimensionalVectorialQuantity(UnitiesTable.DIMENSIONLESS, 'vetor', True)
v.set_polar_notation(5, 225)
print(v.to_string_as('rectangular'))
print(v.to_string_as('polar'))
print(v)

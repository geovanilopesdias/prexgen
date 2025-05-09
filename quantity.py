from unity import *
from lexical import Lexical
from random import choice

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
        
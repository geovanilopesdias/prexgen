from unity import *
from lexical import Lexical

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


    def sum_escalars(self, other_q, nem_name: str, new_name_is_male: bool): 
        if not isinstance(other_q, EscalarQuantity):
            raise TypeError('Other isn\'t an instance of EscalarQuantity.')
        if self.unity != other_q.unity:
            raise TypeError('Instance and other do not match their unities.')
        
        return EscalarQuantity(self.value + other_q, self.unity, new_name, new_name_is_male)

        
##    def adapt_unity(self):
##        #Length
##        if self.unity.symbol == 'm':
##            if self.value >= 1_000:
##                self.value = Unity.convertFromSI(self.value, UnitiesTable.KILOMETER)
##                self.unity = UnitiesTable.KILOMETER
##            elif self.value < 1:
##                self.value = Unity.convertFromSI(self.value, UnitiesTable.CENTIMETER)
##                self.unity = UnitiesTable.CENTIMETER
##            else:
##                pass
##        elif self.unity.symbol == 'km' or self.unity.symbol == 'mi' and self.value < 1:
##            self.value = Unity.convertToSI(self.value, UnitiesTable.METER)
##            self.unity = UnitiesTable.METER
##
##        # Time
##        elif self.unity.symbol == 's':
##            if self.value > 60 and self.value < 3600:
##                self.value = Unity.convertFromSI(self.value, UnitiesTable.METER)
##                self.unity = UnitiesTable.METER
##            elif self.value > 3600:
##                return convertFromSI(value, UnitiesTable.HOUR)
##            else:
##                pass
##        elif self.unity.symbol == 's':



# q = EscalarQuantity(2, UnitiesTable.METER, 'altura', False)


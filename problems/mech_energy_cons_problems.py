from .problem import Problem
from services.quantity import EscalarQuantity
from services.lexical import Lexical
from services.unity import *
from services.mobile import *

class MechanicalEnergyConservation(Problem):   
    """
    Abstracts situational problems solvable by the concept of
    conservation of mechanical energy,

    Factory descriptions and proto-text body in Portuguese:
    - name: Korean Seesaw
        "Exemplo". 
    """
    FACTORIES = ('korean_seesaw', 'billiard_balls_collision')

    def __init__(self, ctx: str = '', todo: str = '', uvk = '', ans: str = '', var: dict = dict()):
        super().__init__(ctx, todo, uvk, ans, var)


    @classmethod
    def ProblemFactory(cls, factory_name: str) -> 'MechanicalEnergyConservation':
        if factory_name not in cls.FACTORIES:
            raise ValueError(f"No method found for the factory '{factory_name}'")
        p = MechanicalEnergyConservation()
        p.build_problem_for(factory_name)
        return p

    
    def raffle_unknown_variable_key(self, factory_name: str):
        super().raffle_unknown_variable_key()
        
    
    # ----- Korean Seesaw:
    def set_variables_for_korean_seesaw(self):
        subject = MobileOptions.PERSON
        mass_a = EscalarQuantity(subject.random_mass(), UnitiesTable.KILOGRAM, 'massa da pessoa a', False)
        mass_b = EscalarQuantity(subject.random_mass(), UnitiesTable.KILOGRAM, 'massa da pessoa b', False)
        height_range = uniform(.5, 2)
        height_a = EscalarQuantity(height_range, UnitiesTable.METER, 'altura de que cai a pessoa a', False)
        height_b = EscalarQuantity(height_a * mass_a / mass_b, UnitiesTable.METER, 'altura que a pessoa b sobe', False)

        self.variables = {'subject': subject, 'mass_a': mass_a, 'mass_b': mass_b, 'height_a': height_a, 'height_b': height_b}


    def set_context_phrase_for_korean_seesaw(self):
        pass
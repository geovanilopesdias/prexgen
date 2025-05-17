from random import choice, uniform
from .problem import Problem
from services import *

class Uvrm(Problem):   
    """
    Abstracts situational problems solvable by equations or the UVRM:
    
    Factory descriptions and proto-text body in Portuguese:
    """
    FACTORIES = ('average_speed', 'average_speed')

    def __init__(self, ctx: str = '', todo: str = '', uvk = '', ans: str = '', var: dict = dict()):
        super().__init__(ctx, todo, uvk, ans, var)


    @classmethod
    def ProblemFactory(cls, factory_name: str) -> 'Uvrm':
        if factory_name not in cls.FACTORIES:
            raise ValueError(f"No method found for the factory '{factory_name}'")
        p = Uvrm()
        p.build_problem_for(factory_name)
        return p


    def raffle_unknown_variable_key(self, factory_name: str):
        super().raffle_unknown_variable_key()


    def set_variables_for_average_speed(self):
        subject = MobileOptions.randomMobile(mobile_can_be_person = True)
        speed_f = EscalarQuantity(round(subject.set_random_speed(), 1),
                                UnitiesTable.METER_PER_SECOND, 'velocidade final', False)
        speed_i_factor = uniform(.1, .9)
        speed_i = EscalarQuantity(round(speed_f.value * speed_i_factor, 1),
                                   UnitiesTable.METER_PER_SECOND, 'velocidade inicial', False)
        average_speed = EscalarQuantity(round((speed_f.value + speed_i.value)/2, 1),
                               UnitiesTable.METER_PER_SECOND, 'velocidade média', True)
        
        EscalarQuantity.adapt_unity_randomly(speed_f)
        speed_i.convert_to(speed_f.unity)
        average_speed.convert_to(speed_f.unity)
        
        self.variables = {'subject': subject, 'speed_f': speed_f, 'speed_i': speed_i, 'average_speed': average_speed}
                  

    def set_context_phrase_for_average_speed(self):
        subject = self.variables['subject']
        context_phrase_head = (
            f"{Lexical.undefined_article(subject.is_male)} {subject.name}"
            if self.does_context_come_first
            else f"{Lexical.random_condition_articulator()} {Lexical.pronoun(subject.is_male)}"
        )
        
        match self.unknown_variable_key:
            case 'average_speed':
                self.context_phrase = (
                    f"{context_phrase_head} {Lexical.random_verb_to_present('speed', subject.type)} {Lexical.random_distance_adverb()} "
                    f"uma estrada e {Lexical.random_verb_for_changing(Lexical.ChangingMode.GENERIC)} a sua velocidade "
                    f"de {self.variables['speed_i']} para {self.variables['speed_f']} "
                )

            case 'speed_f':
                self.context_phrase = (
                    f"{context_phrase_head} {Lexical.random_verb_to_present('speed', subject.type)} {Lexical.random_distance_adverb()} "
                    f"uma estrada desenvolvendo uma {self.variables['average_speed'].name} de {self.variables['average_speed']}. "
                    f"{Lexical.random_condition_articulator()} {Lexical.random_verb_for_changing(Lexical.ChangingMode.INCREASE)}-a sua velocidade "
                    f"a partir de {self.variables['speed_i']}, "
                )
                
            case 'speed_i':
                self.context_phrase = (
                    f"{context_phrase_head} {Lexical.random_verb_to_present('speed', subject.type)} {Lexical.random_distance_adverb()} "
                    f"uma estrada desenvolvendo uma {self.variables['average_speed'].name} de {self.variables['average_speed']}. "
                    f"{Lexical.random_condition_articulator()} {Lexical.random_verb_for_changing(Lexical.ChangingMode.INCREASE)}-a sua velocidade "
                    f"até {self.variables['speed_f']}, "
                )

            


    


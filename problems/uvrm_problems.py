from random import choice, uniform
from services.unity import *
from services.quantity import *
from services.mobile import *
from .problem import Problem

# To-do list:
### DifferenceInTravelTimes appears to not drawing variables coherently (the calculations are wrong).
### Test wether TwiceStretchRoad is randomizing variables coherently.

class Uvrm(Problem):   
    """
    Abstracts situational problems solvable by equations or the UVRM:
    v = (vf + vi)/2 | a = (vf - vi)/t | vf² = vi² + 2a*d
    d = vi*t + (vf-vi)t²/2 | sf = si + vi*t + (vf-vi)t²/2.
    It currrently can draw up to ___ (...) different
    problems, regardless of the variable values and unities randomization.
    """
    FACTORIES = ('average_speed')

    def __init__(self, ctx: str = '', todo: str = '', uvk = '', ans: str = '', var: dict = dict()):
        super().__init__(ctx, todo, uvk, ans, var)

    
    def set_variables_for_average_speed(self):
        subject = MobileOptions.randomMobile(mobile_can_be_person = True)
        speed_f = EscalarQuantity(round(subject.set_random_speed(), 1),
                                UnitiesTable.METER_PER_SECOND, 'velocidade final', False)
        speed_i = EscalarQuantity(round(subject.set_random_distance(), 1),
                                   UnitiesTable.METER_PER_SECOND, 'velocidade inicial', False)
        average_speed = EscalarQuantity(round((speed_f.value + speed_i.value)/2, 1),
                               UnitiesTable.METER_PER_SECOND, 'intervalo de tempo', True)
        
        EscalarQuantity.adapt_unity_randomly(speed_f)
        speed_i.convert_to(speed_f.unity)
        average_speed.convert_to(speed_f.unity)
        
        self.variables = {'subject': subject, 'speed_f': speed_f, 'speed_i': speed_i, 'average_speed': average_speed}
               

    # Dunno if it'd be needed:
    #def raffle_unknown_variable_key(self, factory_name: str):
    #    super().raffle_unknown_variable_key()
    

    def set_context_phrase_for_average_speed(self):
        subject = self.variables['subject']
        context_phrase_head = (
            f"{Lexical.undefined_article(subject.is_male)} {subject.name}"
            if self.does_context_come_first
            else f"{Lexical.random_condition_articulator()} {Lexical.pronoun(subject.is_male)}"
        )
        
        match self.unknown_variable_key:
            case 'speed':
                self.context_phrase = (
                    f"{context_phrase_head} {Lexical.random_motion_verb(subject.type)} {Lexical.random_distance_adverb()} "
                    f"{self.variables['distance']} {Lexical.random_interval_adverb()} {self.variables['time']}"
                )
                
            case 'distance':
                self.context_phrase = (
                    f"{context_phrase_head} {Lexical.random_verb_to_present('speed', subject.type)} "
                    f"{self.variables['speed']} {Lexical.random_interval_adverb()} {self.variables['time']}"
                )

            case 'time':
                self.context_phrase = (
                    f"{context_phrase_head} {Lexical.random_verb_to_present('speed', subject.type)} "
                    f"{self.variables['speed']} {Lexical.random_distance_adverb()} {self.variables['distance']}"
                )


    @classmethod
    def ProblemFactory(cls, factory_name: str) -> 'Uvrm':
        if factory_name not in cls.FACTORIES:
            raise ValueError(f"No method found for the factory '{factory_name}'")
        p = Uvrm()
        p.build_problem_for(factory_name)
        return p


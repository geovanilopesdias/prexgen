from random import choice, uniform
from .problem import Problem
from services.quantity import EscalarQuantity
from services.lexical import Lexical
from services.unity import *
from services.mobile import *


# To-do list:
### DifferenceInTravelTimes appears to not drawing variables coherently (the calculations are wrong).

class AverageSpeed(Problem):   
    """
    Abstracts situational problems solveble by the definition of average speed,
    i.e., the equation v = d/t. It currrently can draw up to 240 (3*4*4*5) different
    problems, regardless of the variable values and unities randomization.
    """
    FACTORIES = ('simple_voyage', 'section_crossing', 'difference_in_travel_times', 'two_stretch_road')

    def __init__(self, ctx: str = '', todo: str = '', uvk = '', ans: str = '', var: dict = dict()):
        super().__init__(ctx, todo, uvk, ans, var)


    # ----- Variables setters:
    def set_variables_for_simple_voyage(self):
        subject = MobileOptions.randomMobile(mobile_can_be_person = True)
        speed = EscalarQuantity(round(subject.set_random_speed(), 1),
                                UnitiesTable.METER_PER_SECOND, 'velocidade média', False)
        distance = EscalarQuantity(round(subject.set_random_distance(), 1),
                                   UnitiesTable.METER, 'distância', False)
        time = EscalarQuantity(round(distance.value / speed.value, 1),
                               UnitiesTable.SECOND, 'intervalo de tempo', True)
        
        self.variables = {'subject': subject, 'speed': speed, 'distance': distance, 'time': time}
        EscalarQuantity.adapt_all_unities_in(self.variables)


    def set_variables_for_section_crossing(self):
        subject = MobileOptions.randomMobile(mobile_can_be_person = False)        
        subject_length = EscalarQuantity(
            round(subject.set_random_length(), 1),
            UnitiesTable.METER, 'comprimento', True)

        section = choice((  # There should be options feasible to both trains and cars/trucks!
            {'name': 'ponte', 'is_male': False},
            {'name': 'túnel', 'is_male': True}
        ))
        section_length = EscalarQuantity(
            round(uniform(subject_length.value * 10, subject_length.value * 50), 1),
            UnitiesTable.METER, 'comprimento', True)      

        speed = EscalarQuantity(
            round(subject.set_random_speed(), 1),
            UnitiesTable.METER_PER_SECOND, 'velocidade média', False)
        
        time = EscalarQuantity(
            round((section_length.value + subject_length.value) / speed.value, 1),
            UnitiesTable.SECOND, 'intervalo de tempo', True)
        
        speed.adapt_unity_randomly()
        self.variables = {'subject': subject, 'section_length': section_length, 'subject_length':subject_length, 'section': section, 'speed': speed, 'time': time}


    def set_variables_for_difference_in_travel_times(self):
        subject = MobileOptions.randomMobile(mobile_can_be_person = False)        
        
        higher_speed = EscalarQuantity(
            round(subject.set_random_speed(), 1),
            UnitiesTable.METER_PER_SECOND, 'velocidade maior', False)

        lower_speed = EscalarQuantity(
            round(higher_speed.value * uniform(.6, .9), 1),
            UnitiesTable.METER_PER_SECOND, 'velocidade menor', False)

        distance = EscalarQuantity(round(subject.set_random_distance(), 1),
                                   UnitiesTable.METER, 'distância', False)
        
        time_difference = EscalarQuantity(
            round(distance.value * (1/lower_speed.value - 1/higher_speed.value), 1),
            UnitiesTable.SECOND, 'diferença dos tempos de viagem', True)
                
        self.variables = {
            'subject': subject, 'higher_speed': higher_speed, 'lower_speed': lower_speed,
            'distance': distance, 'time_difference': time_difference
            }
        EscalarQuantity.adapt_all_unities_in(self.variables)
        self.variables['lower_speed'].convert_to(higher_speed.unity)  # Set both speeds in the same unity avoids unessesary complexity.


    def set_variables_for_two_stretch_road(self):
        subject = MobileOptions.randomMobile(mobile_can_be_person = False)

        speed_a = EscalarQuantity(
            round(subject.set_random_speed(), 1),
            UnitiesTable.METER_PER_SECOND, 'velocidade do trecho A', False)

        speed_b = EscalarQuantity(
            round(subject.set_random_speed(), 1),
            UnitiesTable.METER_PER_SECOND, 'velocidade do trecho B', False)

        distance_a = EscalarQuantity(
            round(subject.set_random_distance(), 1),
            UnitiesTable.METER, 'distância do trecho A', False)

        distance_b = EscalarQuantity(
            round(subject.set_random_distance(), 1),
            UnitiesTable.METER, 'distância do trecho B', False)

        time_a = EscalarQuantity(
            round(distance_a.value / speed_a.value, 1),
            UnitiesTable.SECOND, 'intervalo de tempo do trecho A', True)

        time_b = EscalarQuantity(
            round(distance_b.value / speed_b.value, 1),
            UnitiesTable.SECOND, 'intervalo de tempo do trecho B', True)
        
        average_speed = EscalarQuantity(
            round((distance_a.value + distance_b.value) / (time_a.value + time_b.value), 1),
            UnitiesTable.METER_PER_SECOND, 'velocidade média', False)
        
        distance_a.adapt_unity_randomly()
        time_b.adapt_unity_randomly()
        
        # Variables of the same type should have the same unity to avoid unnecessary complexity:
        speed_a.adapt_unity_randomly()
        speed_b.convert_to(speed_a.unity)
        average_speed.convert_to(speed_a.unity)
        
        self.variables = {
            'subject': subject, 'average_speed': average_speed, 'speed_a': speed_a, 'speed_b': speed_b,
            'distance_a': distance_a, 'distance_b': distance_b, 'time_a': time_a, 'time_b': time_b
            }
        

    def raffle_unknown_variable_key(self, factory_name: str):
        match factory_name:
            case 'TwiceStretchRoad':
                key_options = ('average_speed', 'speed_a', 'speed_b', 'distance_a', 'time_b')
                self.unknown_variable_key = choice(key_options)
            case _:
                super().raffle_unknown_variable_key()
        
    
    # ----- Context phrase setters:
    def set_context_phrase_for_simple_voyage(self):
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


    def set_context_phrase_for_section_crossing(self):
        subject = self.variables['subject']  # instance of Mobile
        sub_len = self.variables['subject_length']  # instance of EscalarQuantity
        section = self.variables['section']  # dict
        sec_len = self.variables['section_length']
        context_phrase_head = (
            f"{Lexical.undefined_article(subject.is_male)} {subject.name}"
            if self.does_context_come_first
            else f"{Lexical.random_condition_articulator()} {Lexical.pronoun(subject.is_male)}"
        )

        match self.unknown_variable_key:
            case 'speed':
                self.context_phrase = (
                    f"{context_phrase_head} {Lexical.random_attribute_indicator_verb()} {Lexical.undefined_article(subject.is_male)} "
                    f"{sub_len.name.split()[0]} de {sub_len} e {Lexical.random_crossing_verb()} {Lexical.undefined_article(section['is_male'])} "
                    f"{section['name']} de {sec_len} {Lexical.random_interval_adverb()} {self.variables['time']}"
                )

            case 'section_length':
                self.context_phrase = (
                    f"{context_phrase_head} {Lexical.random_attribute_indicator_verb()} {Lexical.undefined_article(subject.is_male)} "
                    f"{sub_len.name.split()[0]} de {sub_len} e {Lexical.random_crossing_verb()} {Lexical.undefined_article(section['is_male'])} "
                    f"{section['name']} a {self.variables['speed']} {Lexical.random_interval_adverb()} {self.variables['time']}"
                )

            case 'subject_length':
                self.context_phrase = (
                    f"{context_phrase_head} {Lexical.random_crossing_verb()} {Lexical.undefined_article(section['is_male'])} "
                    f"{section['name']} de {sec_len} a {self.variables['speed']} {Lexical.random_interval_adverb()} {self.variables['time']}"
                )

            case 'time':
                self.context_phrase = (
                    f"{context_phrase_head} {Lexical.random_attribute_indicator_verb()} {Lexical.undefined_article(subject.is_male)} "
                    f"{sub_len.name.split()[0]} de {sub_len} e {Lexical.random_crossing_verb()} {Lexical.undefined_article(section['is_male'])} "
                    f"{section['name']} de {sec_len} a {self.variables['speed']}"
                )

    
    def set_context_phrase_for_difference_in_travel_times(self):
        self.does_context_come_first = True  # So problem texts shall be simpler/clearer.
        subject = self.variables['subject']
        context_phrase_head = f"{Lexical.undefined_article(subject.is_male)} {subject.name} {Lexical.random_motion_verb(subject.type)}"

        match self.unknown_variable_key:
            case 'higher_speed':
                self.context_phrase = (
                    f"{context_phrase_head} {Lexical.random_distance_adverb()} "
                    f"{self.variables['distance']} a duas velocidades diferentes, sendo a menor {self.variables['lower_speed']}. "
                    f"{Lexical.random_condition_articulator()} a {self.variables['time_difference'].name} foi de {self.variables['time_difference']}"
                )

            case 'lower_speed':
                self.context_phrase = (
                    f"{context_phrase_head} {Lexical.random_distance_adverb()} "
                    f"{self.variables['distance']} a duas velocidades diferentes, sendo a maior {self.variables['higher_speed']}. "
                    f"{Lexical.random_condition_articulator()} a {self.variables['time_difference'].name} foi de {self.variables['time_difference']}"
                )

            case 'distance':
                self.context_phrase = (
                    f"{context_phrase_head} sob duas velocidades diferentes: "
                    f"{self.variables['lower_speed']} e {self.variables['higher_speed']}. "
                    f"{Lexical.random_condition_articulator()} a {self.variables['time_difference'].name} foi de {self.variables['time_difference']}"
                )

            case 'time_difference':
                self.context_phrase = (
                    f"{context_phrase_head} {Lexical.random_distance_adverb()} "
                    f"{self.variables['distance']} a duas velocidades diferentes: {self.variables['lower_speed']} e {self.variables['higher_speed']}"
                )


    def set_context_phrase_for_two_stretch_road(self):
        self.does_context_come_first = True  # So problem texts shall be simpler/clearer.
        subject = self.variables['subject']
        context_first_sentence = (
            f"{Lexical.undefined_article(subject.is_male)} {subject.name} {Lexical.random_motion_verb(subject.type)} "
            f"{Lexical.random_distance_adverb()} dois trechos A e B. "
        )

        match self.unknown_variable_key:
            case 'average_speed':
                self.context_phrase = (
                    f"{context_first_sentence} No trecho A, {Lexical.pronoun(subject.is_male)} {Lexical.random_motion_verb(subject)} a {self.variables['speed_a']} "
                    f"{Lexical.random_distance_adverb()} {self.variables['distance_a']}; {Lexical.random_contrast_marker()} "
                    f"no trecho B {Lexical.pronoun(subject.is_male)} {Lexical.random_motion_verb(subject)} a {self.variables['speed_b']} "
                    f"{Lexical.random_interval_adverb()} {self.variables['time_b']}. "
                )
            
            case 'speed_a':
                self.context_phrase = (
                    f"{context_first_sentence} No trecho A, {Lexical.pronoun(subject.is_male)} {Lexical.random_motion_verb(subject)} "
                    f"{Lexical.random_distance_adverb()} {self.variables['distance_a']}; {Lexical.random_contrast_marker()} "
                    f"no trecho B {Lexical.pronoun(subject.is_male)} {Lexical.random_motion_verb(subject)} a {self.variables['speed_b']} "
                    f"{Lexical.random_interval_adverb()} {self.variables['time_b']}. "
                    f"{Lexical.random_condition_articulator()} a sua {self.variables['average_speed'].name} é de {self.variables['average_speed']}, "
                )
            
            case 'speed_b':
                self.context_phrase = (
                    f"{context_first_sentence}  No trecho A, {Lexical.pronoun(subject.is_male)} {Lexical.random_motion_verb(subject)} a {self.variables['speed_a']} "
                    f"{Lexical.random_distance_adverb()} {self.variables['distance_a']}; {Lexical.random_contrast_marker()} "
                    f"no trecho B {Lexical.pronoun(subject.is_male)} {Lexical.random_motion_verb(subject)} "
                    f"{Lexical.random_interval_adverb()} {self.variables['time_b']}. "
                    f"{Lexical.random_condition_articulator()} a sua {self.variables['average_speed'].name} é de {self.variables['average_speed']}, "
                )
            
            case 'distance_a':
                self.context_phrase = (
                    f"{context_first_sentence} No trecho A, {Lexical.pronoun(subject.is_male)} {Lexical.random_motion_verb(subject)} a {self.variables['speed_a']}; "
                    f"{Lexical.random_contrast_marker()} "
                    f"no trecho B {Lexical.pronoun(subject.is_male)} {Lexical.random_motion_verb(subject)} a {self.variables['speed_b']} "
                    f"{Lexical.random_interval_adverb()} {self.variables['time_b']}. "
                    f"{Lexical.random_condition_articulator()} a sua {self.variables['average_speed'].name} é de {self.variables['average_speed']}, "
                )
            
            case 'time_b':
                self.context_phrase = (
                    f"{context_first_sentence} No trecho A, {Lexical.pronoun(subject.is_male)} {Lexical.random_motion_verb(subject)} a {self.variables['speed_a']} "
                    f"{Lexical.random_distance_adverb()} {self.variables['distance_a']}; {Lexical.random_contrast_marker()} "
                    f"no trecho B {Lexical.pronoun(subject.is_male)} {Lexical.random_motion_verb(subject)} a {self.variables['speed_b']}. "
                    f"{Lexical.random_condition_articulator()} a sua {self.variables['average_speed'].name} é de {self.variables['average_speed']}, "
                )


    @classmethod
    def ProblemFactory(cls, factory_name: str) -> 'AverageSpeed':
        if factory_name not in cls.FACTORIES:
            raise ValueError(f"No method found for the factory '{factory_name}'")
        p = AverageSpeed()
        p.build_problem_for(factory_name)
        return p

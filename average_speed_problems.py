from random import choice, uniform
from lexical import Lexical
from unity import *
from quantity import *
from mobile import *
from activity import Problem


class AverageSpeed(Problem):   
    def __init__(self, ctx: str = '', todo: str = '', uvk = '', ans: str = '', var: dict = dict(), uni: dict = dict()):
        super().__init__(ctx, todo, uvk, ans, var, uni)


    # ----- Variables setting:
    def set_random_unities_and_variables(self, factory_name: str):
        """
        Sets the base instance and random values for problems about average speed
        according to the static factory name passed.
        """
        match factory_name:
            case 'SimpleVoyage':
                self.set_random_unities(('speed', 'distance', 'time'))
                self.set_variables_for_simple_voyage()
            case 'SectionCrossing':
                self.set_random_unities(('speed', 'speed'))
                self.set_variables_for_section_crossing()
            case _:
                raise ValueError(f"No method found for the factory '{factory_name}'")

    
    def set_variables_for_simple_voyage(self):
        subject = MobileOptions.randomMobile(mobile_can_be_person = True)
        speed = EscalarQuantity(round(subject.set_random_speed(), 1),
                                UnitiesTable.METER_PER_SECOND, 'velocidade média', False)
        distance = EscalarQuantity(round(subject.set_random_distance(), 1),
                                   UnitiesTable.METER, 'distância', False)
        time = EscalarQuantity(round(distance.value / speed.value, 1),
                               UnitiesTable.SECOND, 'intervalo de tempo', True)
        
        speed.convert_to(self.unities['speed'])
        distance.convert_to(self.unities['distance'])
        time.convert_to(self.unities['time'])

        self.variables = {'subject': subject, 'speed': speed, 'distance': distance, 'time': time}


    def set_variables_for_section_crossing(self):
        subject = MobileOptions.randomMobile(mobile_can_be_person = False)        
        subject_length = EscalarQuantity(
            round(subject.set_random_length(), 1),
            UnitiesTable.METER, 'comprimento', True)

        section = choice((
            {'name': 'ponte', 'is_male': False},
            {'name': 'túnel', 'is_male': True},
            {'name': 'trecho de faixa única', 'is_male': True},
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
        
        speed.convert_to(self.unities['speed'])
        self.variables = {'subject': subject, 'section_length': section_length, 'subject_length':subject_length, 'section': section, 'speed': speed, 'time': time}



    # ----- Problem text body setting:
    def set_todo_statement_and_answer(self):
        """
        Builds the to-do statement and answer. So, it can only be used after
        set_random_unities_and_variables method.
        """
        if not self.unities or not self.variables:
            raise ValueError('A problem text should be used only after problem variables AND unities are set.')            

        self.unknown_variable_key = choice([k for k, v in self.variables.items() if isinstance(v, EscalarQuantity)])
        self.answer = f"{self.variables[self.unknown_variable_key]}"
        
        todo_statement_head = Lexical.random_inquisitive_pronoun() if self.is_inquisitive else Lexical.random_imperative_verb()
        subject_reference = (
            Lexical.pronoun(self.variables['subject'].is_male)
            if self.does_context_come_first
            else f"{Lexical.undefined_article(self.variables['subject'].is_male)} {self.variables['subject'].name}"
        )

        unk_var = self.variables[self.unknown_variable_key]

        #  FUNCIONA APENAS PARA SIMPLE VOYAGE; SECTION CROSSING PODE TER NO FINAL ALGO COMO "QUE COMPRIMENTO POSSUI"
        self.todo_statement = (
                f"{todo_statement_head} {Lexical.defined_article(unk_var.is_male)} "
                f"{unk_var.name} (em {unk_var.unity.value.symbol}) "
                f"que {subject_reference} {Lexical.random_motion_verb(self.variables['subject'].type)}")


    def set_context_phrase_for(self, factory_name: str):
        """
        Sets the instance's context phrase for problems about average speed
        according to the static factory name passed.
        """
        if not self.unities or not self.variables:
            raise ValueError('A problem text should be used only after problem variables AND unities are set.')
        
        match factory_name:
            case 'SimpleVoyage':
                self.set_context_phrase_for_simple_voyage()
            case 'SectionCrossing':
                self.set_context_phrase_for_section_crossing()
            case _:
                raise ValueError(f"No method found for the factory '{factory_name}'")


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
            case 'speed':  # The flexy nature of two variable names make match/case block unfeasible...
                self.context_phrase = (
                    f"{context_phrase_head} {Lexical.random_attribute_indicator_verb()} {Lexical.undefined_article(subject.is_male)} "
                    f"{sub_len.name.split()[0]} de {sub_len} e {Lexical.random_crossing_verb()} {Lexical.undefined_article(section['is_male'])}"
                    f"{section['name']} de {sec_len} {Lexical.random_interval_adverb()} {self.variables['time']}"
                )

            case 'section_length':
                self.context_phrase = (
                    f"{context_phrase_head} {Lexical.random_attribute_indicator_verb()} {Lexical.undefined_article(subject.is_male)} "
                    f"{sub_len.name.split()[0]} de {sub_len} e {Lexical.random_crossing_verb()} {Lexical.undefined_article(section['is_male'])}"
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


    # ----- Factory methods:
    def SimpleVoyageProblem() -> 'AverageSpeed':
        p = AverageSpeed()
        p.set_random_unities_and_variables(factory_name = 'SimpleVoyage')
        p.set_todo_statement_and_answer()
        p.set_context_phrase_for('SimpleVoyage')
        return p


    #Funciona, mas precisa adaptar o todo statement para comportar o comprimento apropriadamente.
    def SectionCrossingProblem() -> 'AverageSpeed':
        p = AverageSpeed()
        p.set_random_unities_and_variables(factory_name = 'SectionCrossing')
        p.set_todo_statement_and_answer()
        p.set_context_phrase_for('SectionCrossing')
        return p



for c in range(1, 101):
    p = AverageSpeed.SectionCrossingProblem()
    print(f'{c}) {p}')

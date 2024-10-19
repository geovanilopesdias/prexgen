import locale
from random import choice, uniform
from lexical import Lexical
from unity import *
from mobile import *
from activity import Problem

locale.setlocale(locale.LC_NUMERIC, 'pt_BR.UTF-8')

class AverageSpeedProblem(Problem):
    def __init__(self, ctx: str = '', todo: str = '', ans: str = '', var: dict = dict(), uni: dict = dict()):
        super().__init__(ctx, todo, ans, var, uni)


    def set_random_variables(self, mobile_can_be_person: bool = True):
        """
        Sets the base instance and random values for problems about average speed.
        """
        mobile = MobileOptions.randomMobile() if mobile_can_be_person else MobileOptions.randomMotorMobile()
        speed = mobile.randomSpeedFor()
        distance = mobile.randomDistanceFor()
        self.variables = {'mobile': mobile, 'speed': speed, 'distance': distance, 'time': distance / speed}


    def set_random_unities(self) -> dict:
        """
        Sets random unities base instance and random values for problems about average speed. Should be call after set_random_variables method.
        """
        unities = dict()
        unities['distance'] = UnitiesTable.randomLengthUnity()
        self.variables['distance'] = Unity.convertFromSI(self.variables['distance'], unities['distance'])
        
        unities['time'] = UnitiesTable.randomTimeUnity()
        self.variables['time'] = Unity.convertFromSI(self.variables['time'], unities['time'])

        unities['speed'] = UnitiesTable.randomSpeedUnity()
        self.variables['speed'] = Unity.convertFromSI(self.variables['speed'], unities['speed'])
        self.unities = unities

    
    def SimpleVoyageProblem(precision = 2) -> 'AverageSpeedProblem':
        # Problem variables setting:
        p = AverageSpeedProblem()
        p.set_random_variables()
        p.set_random_unities()
        m = p.variables['mobile']

        # Problem variable values formating (r_f stands for "round and formatted with comma"):
        r_f_distance = locale.format_string("%.2f", round(p.variables['distance'], precision), grouping=True)
        r_f_time = locale.format_string("%.2f", round(p.variables['time'], precision), grouping=True)
        r_f_speed = locale.format_string("%.2f", round(p.variables['speed'], precision), grouping=True)

        # Problem structure definition:
        unknown_var = choice(('distance', 'time', 'speed'))   
        match unknown_var:
            case 'distance':
                if p.does_context_come_first:
                    phrase = f"{Lexical.undefined_article(m.is_male)} {m.name} {Lexical.random_verb_to_present('speed', m.type)} {r_f_speed} {p.unities['speed'].symbol}. {Lexical.random_condition_articulator()} {Lexical.pronoun(m.is_male)} {Lexical.random_motion_verb(m.type)} {Lexical.random_interval_adverb()} {r_f_time} {p.unities['time'].symbol},"
                    if p.is_inquisitive:                    
                        statement = f"{Lexical.random_inquisitive_pronoun(False)} distância (em {p.unities[unknown_var].symbol}) que {Lexical.pronoun(m.is_male)} {Lexical.random_motion_verb(m.type)}"
                    else:
                        statement = f"{Lexical.random_imperative_verb(False)} distância (em {p.unities[unknown_var].symbol}) que {Lexical.pronoun(m.is_male)} {Lexical.random_motion_verb(m.type)}"

                else:
                    phrase = f"{Lexical.random_condition_articulator()} {Lexical.pronoun(m.is_male)} {Lexical.random_verb_to_present('speed', m.type)} {r_f_speed} {p.unities['speed'].symbol} {Lexical.random_interval_adverb()} {r_f_time} {p.unities['time'].symbol}"
                    if p.is_inquisitive:                    
                        statement = f"{Lexical.random_inquisitive_pronoun(False)} distância (em {p.unities[unknown_var].symbol}) que {Lexical.undefined_article(m.is_male)} {m.name} {Lexical.random_motion_verb(m.type)},"
                    else:
                        statement = f"{Lexical.random_imperative_verb(False)} distância (em {p.unities[unknown_var].symbol}) que {Lexical.undefined_article(m.is_male)} {m.name} {Lexical.random_motion_verb(m.type)},"

                answer = f"Resposta: {r_f_distance} {p.unities[unknown_var].symbol}."

            case 'time':
                if p.does_context_come_first:
                    phrase = f"{Lexical.undefined_article(m.is_male)} {m.name} {Lexical.random_verb_to_present('speed', m.type)} {r_f_speed} {p.unities['speed'].symbol}. {Lexical.random_condition_articulator()} {Lexical.pronoun(m.is_male)} {Lexical.random_motion_verb(m.type)} {Lexical.random_distance_adverb()} {r_f_distance} {p.unities['distance'].symbol},"
                    if p.is_inquisitive:                    
                        statement = f"{Lexical.random_inquisitive_pronoun(True)} tempo (em {p.unities[unknown_var].symbol}) durante o qual {Lexical.pronoun(m.is_male)} {Lexical.random_motion_verb(m.type)}"
                    else:
                        statement = f"{Lexical.random_imperative_verb(True)} tempo (em {p.unities[unknown_var].symbol}) durante o qual {Lexical.pronoun(m.is_male)} {Lexical.random_motion_verb(m.type)}"

                else:
                    phrase = f"{Lexical.random_condition_articulator()} {Lexical.pronoun(m.is_male)} {Lexical.random_verb_to_present('speed', m.type)} {r_f_speed} {p.unities['speed'].symbol} {Lexical.random_distance_adverb()} {r_f_distance} {p.unities['distance'].symbol}"
                    if p.is_inquisitive:                    
                        statement = f"{Lexical.random_inquisitive_pronoun(True)} tempo (em {p.unities[unknown_var].symbol}) durante o qual {Lexical.undefined_article(m.is_male)} {m.name} {Lexical.random_motion_verb(m.type)},"
                    else:
                        statement = f"{Lexical.random_imperative_verb(True)} tempo (em {p.unities[unknown_var].symbol}) durante o qual {Lexical.undefined_article(m.is_male)} {m.name} {Lexical.random_motion_verb(m.type)},"
                answer = f"Resposta: {r_f_time} {p.unities[unknown_var].symbol}."

            case 'speed':
                if p.does_context_come_first:
                    phrase = f"{Lexical.undefined_article(m.is_male)} {m.name} {Lexical.random_motion_verb(m.type)} {Lexical.random_distance_adverb()} {r_f_distance} {p.unities['distance'].symbol} {Lexical.random_interval_adverb()} {r_f_time} {p.unities['time'].symbol}."
                    if p.is_inquisitive:                    
                        statement = f"{Lexical.random_inquisitive_pronoun(False)} velocidade média (em {p.unities[unknown_var].symbol}) com a qual {Lexical.pronoun(m.is_male)} {Lexical.random_motion_verb(m.type)}"
                    else:
                        statement = f"{Lexical.random_imperative_verb(False)} velocidade média (em {p.unities[unknown_var].symbol}) com a qual {Lexical.pronoun(m.is_male)} {Lexical.random_motion_verb(m.type)}"

                else:
                    phrase = f"{Lexical.random_condition_articulator()} {Lexical.pronoun(m.is_male)} {Lexical.random_verb_to_present('distance', m.type)} {r_f_distance} {p.unities['distance'].symbol} {Lexical.random_interval_adverb()} {r_f_time} {p.unities['time'].symbol}"
                    if p.is_inquisitive:                    
                        statement = f"{Lexical.random_inquisitive_pronoun(False)} velocidade média (em {p.unities[unknown_var].symbol}) com que {Lexical.undefined_article(m.is_male)} {m.name} {Lexical.random_motion_verb(m.type)},"
                    else:
                        statement = f"{Lexical.random_imperative_verb(False)} velocidade média (em {p.unities[unknown_var].symbol}) com que {Lexical.undefined_article(m.is_male)} {m.name} {Lexical.random_motion_verb(m.type)},"
                answer = f"Resposta: {r_f_speed} {p.unities[unknown_var].symbol}."

        p.context_phrase = phrase
        p.todo_statement = statement
        p.answer = answer
        return p

    # ADAPTAR STATEMENT E PHRASE!
    def SectionCrossingProblem(precision = 2) -> 'AverageSpeedProblem':
        """
        Draws a problem of bridge (or else) crossing.
        """
        # Problem variables setting:
        p = AverageSpeedProblem()
        p.set_random_variables(mobile_can_be_person = False)
        p.set_random_unities()
        m = p.variables['mobile']
        mobile_length = m.randomLengthFor()  # Meter
        section = choice(({'name': 'ponte', 'is_male': False}, {'name': 'túnel', 'is_male': True}))
        section['length'] = uniform(10, 100)  # Meter
        

        # Problem variable values formating (r_f stands for "round and formatted with comma"):
        r_f_distance = locale.format_string("%.2f", round(p.variables['distance'], precision), grouping=True)
        r_f_time = locale.format_string("%.2f", round(p.variables['time'], precision), grouping=True)
        r_f_speed = locale.format_string("%.2f", round(p.variables['speed'], precision), grouping=True)

        # Problem structure definition:
        unknown_var = choice(('distance', 'time', 'speed'))            
        match unknown_var:
            case 'distance':
                if p.does_context_come_first:
                    phrase = f"{Lexical.undefined_article(m.is_male)} {m.name} {Lexical.random_verb_to_present('speed', m.type)} {r_f_speed} {p.unities['speed'].symbol}. {Lexical.random_condition_articulator()} {Lexical.pronoun(m.is_male)} {Lexical.random_motion_verb(m.type)} {Lexical.random_interval_adverb()} {r_f_time} {p.unities['time'].symbol},"
                    if p.is_inquisitive:                    
                        statement = f"{Lexical.random_inquisitive_pronoun(False)} distância (em {p.unities[unknown_var].symbol}) que {Lexical.pronoun(m.is_male)} {Lexical.random_motion_verb(m.type)}"
                    else:
                        statement = f"{Lexical.random_imperative_verb(False)} distância (em {p.unities[unknown_var].symbol}) que {Lexical.pronoun(m.is_male)} {Lexical.random_motion_verb(m.type)}"

                else:
                    phrase = f"{Lexical.random_condition_articulator()} {Lexical.pronoun(m.is_male)} {Lexical.random_verb_to_present('speed', m.type)} {r_f_speed} {p.unities['speed'].symbol} {Lexical.random_interval_adverb()} {r_f_time} {p.unities['time'].symbol}"
                    if p.is_inquisitive:                    
                        statement = f"{Lexical.random_inquisitive_pronoun(False)} distância (em {p.unities[unknown_var].symbol}) que {Lexical.undefined_article(m.is_male)} {m.name} {Lexical.random_motion_verb(m.type)},"
                    else:
                        statement = f"{Lexical.random_imperative_verb(False)} distância (em {p.unities[unknown_var].symbol}) que {Lexical.undefined_article(m.is_male)} {m.name} {Lexical.random_motion_verb(m.type)},"

                answer = f"Resposta: {r_f_distance} {p.unities[unknown_var].symbol}."

            case 'time':
                if p.does_context_come_first:
                    phrase = f"{Lexical.undefined_article(m.is_male)} {m.name} {Lexical.random_verb_to_present('speed', m.type)} {r_f_speed} {p.unities['speed'].symbol}. {Lexical.random_condition_articulator()} {Lexical.pronoun(m.is_male)} {Lexical.random_motion_verb(m.type)} {Lexical.random_distance_adverb()} {r_f_distance} {p.unities['distance'].symbol},"
                    if p.is_inquisitive:                    
                        statement = f"{Lexical.random_inquisitive_pronoun(True)} tempo (em {p.unities[unknown_var].symbol}) durante o qual {Lexical.pronoun(m.is_male)} {Lexical.random_motion_verb(m.type)}"
                    else:
                        statement = f"{Lexical.random_imperative_verb(True)} tempo (em {p.unities[unknown_var].symbol}) durante o qual {Lexical.pronoun(m.is_male)} {Lexical.random_motion_verb(m.type)}"

                else:
                    phrase = f"{Lexical.random_condition_articulator()} {Lexical.pronoun(m.is_male)} {Lexical.random_verb_to_present('speed', m.type)} {r_f_speed} {p.unities['speed'].symbol} {Lexical.random_distance_adverb()} {r_f_distance} {p.unities['distance'].symbol}"
                    if p.is_inquisitive:                    
                        statement = f"{Lexical.random_inquisitive_pronoun(True)} tempo (em {p.unities[unknown_var].symbol}) durante o qual {Lexical.undefined_article(m.is_male)} {m.name} {Lexical.random_motion_verb(m.type)},"
                    else:
                        statement = f"{Lexical.random_imperative_verb(True)} tempo (em {p.unities[unknown_var].symbol}) durante o qual {Lexical.undefined_article(m.is_male)} {m.name} {Lexical.random_motion_verb(m.type)},"
                answer = f"Resposta: {r_f_time} {p.unities[unknown_var].symbol}."

            case 'speed':
                if p.does_context_come_first:
                    phrase = f"{Lexical.undefined_article(m.is_male)} {m.name} {Lexical.random_motion_verb(m.type)} {Lexical.random_distance_adverb()} {r_f_distance} {p.unities['distance'].symbol} {Lexical.random_interval_adverb()} {r_f_time} {p.unities['time'].symbol}."
                    if p.is_inquisitive:                    
                        statement = f"{Lexical.random_inquisitive_pronoun(False)} velocidade média (em {p.unities[unknown_var].symbol}) com a qual {Lexical.pronoun(m.is_male)} {Lexical.random_motion_verb(m.type)}"
                    else:
                        statement = f"{Lexical.random_imperative_verb(False)} velocidade média (em {p.unities[unknown_var].symbol}) com a qual {Lexical.pronoun(m.is_male)} {Lexical.random_motion_verb(m.type)}"

                else:
                    phrase = f"{Lexical.random_condition_articulator()} {Lexical.pronoun(m.is_male)} {Lexical.random_verb_to_present('distance', m.type)} {r_f_distance} {p.unities['distance'].symbol} {Lexical.random_interval_adverb()} {r_f_time} {p.unities['time'].symbol}"
                    if p.is_inquisitive:                    
                        statement = f"{Lexical.random_inquisitive_pronoun(False)} velocidade média (em {p.unities[unknown_var].symbol}) com que {Lexical.undefined_article(m.is_male)} {m.name} {Lexical.random_motion_verb(m.type)},"
                    else:
                        statement = f"{Lexical.random_imperative_verb(False)} velocidade média (em {p.unities[unknown_var].symbol}) com que {Lexical.undefined_article(m.is_male)} {m.name} {Lexical.random_motion_verb(m.type)},"
                answer = f"Resposta: {r_f_speed} {p.unities[unknown_var].symbol}."

        p.context_phrase = phrase
        p.todo_statement = statement
        p.answer = answer
        return p


for c in range(0, 20):
    print(f'{c+1}) {AverageSpeedProblem.RandomProblem().for_exhibition()} \n')
        

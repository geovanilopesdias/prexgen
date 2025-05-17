from random import choice, uniform
from .problem import Problem
from services import *

class MechanicalEnergyConservation(Problem):   
    """
    Abstracts situational problems solvable by the concept of
    conservation of mechanical energy, envolving equations such as
    work (W = F*d), kinetic (K = .5*m*v²) and gravitational potencial 
    (U = m*g*h) energies.

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
        subject = MobileOptions.ATHELETE.value  # Instance of Mobile
        mass_1 = EscalarQuantity(round(subject.set_random_mass(), 1), UnitiesTable.KILOGRAM, 'massa da pessoa que cai', False)
        mass_2 = EscalarQuantity(round(subject.set_random_mass(), 1), UnitiesTable.KILOGRAM, 'massa da pessoa que sobe', False)
        height_range = uniform(.5, 2)
        height_past = EscalarQuantity(round(height_range, 1), UnitiesTable.METER, 'altura da pessoa que cai', False)
        height_future = EscalarQuantity(round((height_past.value * mass_1.value / mass_2.value), 1), UnitiesTable.METER, 'altura da pessoa que sobe', False)

        self.variables = {'subject': subject, 'mass_1': mass_1, 'mass_2': mass_2, 'height_past': height_past, 'height_future': height_future}


    def set_context_phrase_for_korean_seesaw(self):
        self.does_context_come_first = True  # So problem texts shall be simpler/clearer.
        subject = self.variables['subject']
        phrase_head_options = (
            "Dois artistas circenceses estão treinando em uma gangorra coreana. ",
            "Numa gangorra coreana, dois artistas estão a treinar. "
        )
        context_phrase_head = choice(phrase_head_options)
        
        match self.unknown_variable_key:
            case 'mass_1':
                self.context_phrase = (
                    f"{context_phrase_head} "
                    f"Um deles cai do repouso a partir de {self.variables['height_past']} de altura "
                    f"enquanto o outro, de {self.variables['mass_2']}, sobe até {self.variables['height_future']}. "
                )

            case 'mass_2':
                self.context_phrase = (
                    f"{context_phrase_head} "
                    f"Um deles, de {self.variables['mass_1']}, cai do repouso a partir de {self.variables['height_past']} de altura "
                    f"enquanto o outro sobe até {self.variables['height_future']}. "
                )
            
            case 'height_past':
                self.context_phrase = (
                    f"{context_phrase_head} "
                    f"Um deles, de {self.variables['mass_1']}, cai do repouso de certa altura "
                    f"enquanto o outro, de {self.variables['mass_2']}, sobe até {self.variables['height_future']}. "
                )
            
            case 'height_future':
                self.context_phrase = (
                    f"{context_phrase_head} "
                    f"Um deles, de {self.variables['mass_1']}, cai do repouso a partir de {self.variables['height_past']}"
                    f"enquanto o outro, de {self.variables['mass_2']}, sobe até certa altura. "
                )


    # ----- Billiard Balls Collision:
    def set_variables_for_billiard_balls_collision(self):
        subject = MobileOptions.BILLIARD_BALL.value
        
        # White ball definitions:
        mass_white = EscalarQuantity(subject.property_ranges['mass'][1], UnitiesTable.KILOGRAM, 'massa da bola branca', False)
        speed_white_initial = EscalarQuantity(subject.random_speed(), UnitiesTable.METER_PER_SECOND, 'velocidade inicial da bola branca', False)
        white_ball_stops_after_collision = choice(True, False)
        white_ball_speed_reduction = uniform(.05, .1)
        speed_white_final = (
            EscalarQuantity(0, UnitiesTable.METER_PER_SECOND, 'velocidade final da bola branca', False)
            if white_ball_stops_after_collision
            else EscalarQuantity(subject.random_speed() * white_ball_speed_reduction, UnitiesTable.METER_PER_SECOND, 'velocidade final da bola branca', False)
        )

        # Blue ball definitions:
        mass_blue = EscalarQuantity(subject.property_ranges['mass'][0], UnitiesTable.KILOGRAM, 'massa da bola azul', False)
        blue_ball_starts_at_rest = choice(True, False)
        blue_ball_slower_factor = uniform(.1, .9)  # The blue ball, if at motion, need to be slower than the wihte one so it can be smashed.
        speed_blue_initial = (
            EscalarQuantity(0, UnitiesTable.METER_PER_SECOND, 'velocidade inicial da bola azul', False)
            if blue_ball_starts_at_rest
            else EscalarQuantity(speed_white_initial.value * blue_ball_slower_factor, UnitiesTable.METER_PER_SECOND, 'velocidade inicial da bola azul', False)
        )

        speed_blue_final = EscalarQuantity(
            sqrt(
                mass_white * (speed_white_initial.value ^2 - speed_white_final.value ^ 2) /
                mass_blue.value - speed_blue_initial.value ^ 2),
            UnitiesTable.METER_PER_SECOND, 'velocidade final da bola azul', False)

        self.variables = {'subject': subject, 'mass_white': mass_white, 'mass_blue': mass_blue, 
            'speed_white_initial': speed_white_initial, 'speed_white_final': speed_white_final, 
            'speed_blue_initial': speed_blue_initial, 'speed_blue_final': speed_blue_final
        }

        def set_context_phrase_for_billiard_balls_collision(self):
            pass
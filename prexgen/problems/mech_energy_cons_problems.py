from math import sqrt, pow
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
    FACTORIES = (
        'korean_seesaw',
        #'billiard_balls_collision',
        'free_fall',
        #'roller_coaster',
        )
        
    GRAV = PhysicalConstants.EARTH_GRAVITY_ACCELERATION.value.value

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
        phrase_head_options = (
            "Dois artistas circenceses estão treinando em uma gangorra coreana.",
            "Numa gangorra coreana, dois artistas estão a treinar."
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
                    f"Um deles, de {self.variables['mass_1']}, cai do repouso a partir de "
                    f"{self.variables['height_past']} de altura "
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
                    f"Um deles, de {self.variables['mass_1']}, cai do repouso a partir de {self.variables['height_past']} "
                    f"enquanto o outro, de {self.variables['mass_2']}, sobe até certa altura. "
                )
        self.todo_statement = self.todo_statement.capitalize()


    # ----- Billiard Balls Collision:
    def set_variables_for_billiard_balls_collision(self):
        subject = MobileOptions.BILLIARD_BALL.value
        
        # White ball definitions:
        mass_white = EscalarQuantity(subject.property_ranges['mass'][1], UnitiesTable.KILOGRAM, 'massa da bola branca', False)
        speed_white_initial = EscalarQuantity(subject.set_random_speed(), UnitiesTable.METER_PER_SECOND, 'velocidade inicial da bola branca', False)
        white_ball_stops_after_collision = choice((True, False))
        white_ball_speed_reduction = uniform(.05, .1)
        speed_white_final = (
            EscalarQuantity(0, UnitiesTable.METER_PER_SECOND, 'velocidade final da bola branca', False)
            if white_ball_stops_after_collision
            else EscalarQuantity(subject.set_random_speed() * white_ball_speed_reduction, UnitiesTable.METER_PER_SECOND, 'velocidade final da bola branca', False)
        )

        # Blue ball definitions:
        mass_blue = EscalarQuantity(subject.property_ranges['mass'][0], UnitiesTable.KILOGRAM, 'massa da bola azul', False)
        blue_ball_starts_at_rest = choice((True, False))
        
        # The blue ball, if initially at motion, need to be slower than the white one, so it can be bumped.
        blue_ball_slower_factor = uniform(.1, .9)  
        speed_blue_initial = (
            EscalarQuantity(0, UnitiesTable.METER_PER_SECOND, 'velocidade inicial da bola azul', False)
            if blue_ball_starts_at_rest
            else EscalarQuantity(speed_white_initial.value * blue_ball_slower_factor, UnitiesTable.METER_PER_SECOND, 'velocidade inicial da bola azul', False)
        )

        speed_blue_final = EscalarQuantity(
            sqrt(
                mass_white.value * (pow(speed_white_initial.value, 2) - pow(speed_white_final.value, 2)) /
                mass_blue.value + pow(speed_blue_initial.value, 2)),
            UnitiesTable.METER_PER_SECOND, 'velocidade final da bola azul', False)

        mass_white.convert_to(UnitiesTable.GRAM)
        mass_blue.convert_to(UnitiesTable.GRAM)

        self.variables = {'subject': subject, 'mass_white': mass_white, 'mass_blue': mass_blue, 
            'speed_white_initial': speed_white_initial, 'speed_white_final': speed_white_final, 
            'speed_blue_initial': speed_blue_initial, 'speed_blue_final': speed_blue_final
        }


    def set_context_phrase_for_billiard_balls_collision(self):
        self.does_context_come_first = True  # So problem texts shall be simpler/clearer.
        does_white_ball_stop = bool(self.variables['speed_white_final'].value == 0.0)
        does_blue_ball_start_at_rest = bool(self.variables['speed_blue_initial'].value == 0.0)

        context_phrase_head = "Uma bola de bilhar branca"
        blue_initial_speed_disclaimer = (
            f"{Lexical.random_condition_articulator()} a bola azul estava em repouso" if does_blue_ball_start_at_rest
            else f"{Lexical.random_condition_articulator()} a bola azul já se movia a {self.variables['speed_blue_initial']} na mesma direção e sentido"
        )

        blue_final_speed_disclaimer = f"a bola azul é acelerada a {self.variables['speed_blue_final']}"

        white_final_speed_disclaimer = (
            f"a bola branca para com o impacto," if does_white_ball_stop
            else f"a bola branca ainda se move a {self.variables['speed_white_final']} após o impacto"
        )
       
        match self.unknown_variable_key:
            case 'mass_white':
                self.context_phrase = (
                    f"{context_phrase_head} colide a {self.variables['speed_white_initial']} "
                    f"numa bola azul de {self.variables['mass_blue']}. "
                    f"{blue_initial_speed_disclaimer.capitalize()}, que {white_final_speed_disclaimer} e que {blue_final_speed_disclaimer}, "
                )

            case 'mass_blue':
                self.context_phrase = (
                    f"{context_phrase_head} de {self.variables['mass_white']} "
                    f"colide a {self.variables['speed_white_initial']} numa bola azul. "
                    f"{blue_initial_speed_disclaimer.capitalize()}, que {white_final_speed_disclaimer} e que {blue_final_speed_disclaimer}, "
                )
            
            case 'speed_white_initial':
                self.context_phrase = (
                    f"{context_phrase_head} de {self.variables['mass_white']} "
                    f"colide numa bola azul de {self.variables['mass_blue']}. "
                    f"{blue_initial_speed_disclaimer.capitalize()}, que {white_final_speed_disclaimer} e que {blue_final_speed_disclaimer}, "
                )
            
            # Due to rounding, when vwf is zero, pencil-and-paper calculations may bump into imaginary numbers.
            # case 'speed_white_final':
            #     self.context_phrase = (
            #         f"{context_phrase_head} de {self.variables['mass_white']} "
            #         f"colide a {self.variables['speed_white_initial']} "
            #         f"numa bola azul de {self.variables['mass_blue']}. "
            #         f"{blue_initial_speed_disclaimer.capitalize()} e que {blue_final_speed_disclaimer}, "
            #     )
            
            case 'speed_blue_initial':
                self.context_phrase = (
                    f"{context_phrase_head} de {self.variables['mass_white']} "
                    f"colide a {self.variables['speed_white_initial']} "
                    f"numa bola azul de {self.variables['mass_blue']}. "
                    f"{Lexical.random_condition_articulator().capitalize()} {white_final_speed_disclaimer} "
                    f"e que {blue_final_speed_disclaimer}, "
                )

            case 'speed_blue_final':
                self.context_phrase = (
                    f"{context_phrase_head} de {self.variables['mass_white']} "
                    f"colide a {self.variables['speed_white_initial']} "
                    f"numa bola azul de {self.variables['mass_blue']}. "
                    f"{blue_initial_speed_disclaimer.capitalize()} e que {white_final_speed_disclaimer}, "
                )


    # ----- Free fall:
    def set_variables_for_free_fall(self):
        subject = MobileOptions.random_object()  # Instance of Mobile
        speed_initial_value = choice((0.0, round(subject.set_random_speed(), 1)))
        speed_initial = EscalarQuantity(speed_initial_value, UnitiesTable.METER_PER_SECOND, 'velocidade com que partira', False)
        
        height_range = uniform(2, 20)
        height_initial = EscalarQuantity(round(height_range, 1), UnitiesTable.METER, 'altura de que caíra', False)
        
        speed_final = EscalarQuantity(
            round(sqrt(pow(speed_initial.value, 2) + 2 * self.GRAV * height_initial.value), 1),
            UnitiesTable.METER_PER_SECOND, 'velocidade com que atinge o solo', False)
        
        speed_initial.adapt_unity_randomly()
        speed_final.convert_to(speed_initial.unity)

        self.variables = {'subject': subject, 'speed_initial': speed_initial, 'height_initial': height_initial, 'speed_final': speed_final}


    def set_context_phrase_for_free_fall(self):
        self.does_context_come_first = True  # So problem texts shall be simpler/clearer.
        sjt = self.variables['subject']
        context_phrase_head = f"{Lexical.undefined_article(sjt.is_male).capitalize()} {sjt.name} "
        initial_speed_disclaimer = (
            "despenca" if self.variables['speed_initial'].value == 0.0
            else f"é arremessad{Lexical.defined_article(sjt.is_male)} para baixo a {self.variables['speed_initial']}"
        )

        match self.unknown_variable_key:
            case 'speed_final':
                self.context_phrase = (
                    f"{context_phrase_head} {initial_speed_disclaimer} verticalmente "
                    f"a partir duma altura de {self.variables['height_initial']}. "
                )
                self.todo_statement = self.todo_statement.capitalize()

            case 'height_initial':
                self.context_phrase = (
                    f"{context_phrase_head} {initial_speed_disclaimer} verticalmente a partir de certa altura. "
                    f"{Lexical.random_condition_articulator().capitalize()} {Lexical.pronoun(sjt.is_male)} "
                    f"atinge o solo a {self.variables['speed_final']}, "
                )
            
            case 'speed_initial':
                self.context_phrase = (
                    f"{context_phrase_head} cai verticalmente a partir de {self.variables['height_initial']}. "
                    f"{Lexical.random_condition_articulator().capitalize()} {Lexical.pronoun(sjt.is_male)} "
                    f"atinge o solo a {self.variables['speed_final']}, "
                )   


    # ----- Interrupted rising
    def set_variables_for_interrupted_rising(self):
        subject = MobileOptions.random_object()  # Instance of Mobile
        speed_initial = EscalarQuantity(round(subject.set_random_speed(), 1), UnitiesTable.METER_PER_SECOND, 'velocidade com que fora arremessado', False)
        
        height_top_value = .5 * pow(speed_initial.value, 2) / self.GRAV
        interruption = uniform(.5, .9)
        height_final = EscalarQuantity(round(height_top_value * interruption, 1), UnitiesTable.METER, 'altura com que atinge o bloqueio', False)
                
        speed_final = EscalarQuantity(
            round(sqrt(pow(speed_initial.value, 2) - 2 * self.GRAV * height_final.value), 1),
            UnitiesTable.METER_PER_SECOND, 'velocidade com que atinge o bloqueio', False)
        
        speed_initial.adapt_unity_randomly()
        speed_final.convert_to(speed_initial.unity)

        self.variables = {'subject': subject, 'speed_initial': speed_initial, 'height_final': height_final, 'speed_final': speed_final}


    def set_context_phrase_for_interrupted_rising(self):
        self.does_context_come_first = True  # So problem texts shall be simpler/clearer.
        sjt = self.variables['subject']
        context_phrase_head = f"{Lexical.undefined_article(sjt.is_male).capitalize()} {sjt.name} "

        match self.unknown_variable_key:
            case 'speed_final':
                self.context_phrase = (
                    f"{context_phrase_head} é arremessado, a partir do solo e verticalmente, a {self.variables['speed_initial']}. "
                    f"{Lexical.random_condition_articulator().capitalize()} {Lexical.pronoun(sjt.is_male)} "
                    f"atinge um bloqueio a {self.variables['height_final']}, "
                )

            case 'height_final':
                self.context_phrase = (
                    f"{context_phrase_head} é arremessado, a partir do solo e verticalmente, a {self.variables['speed_initial']}, "
                    f"subindo até atingir um bloqueio a certa altura. "
                    f"{Lexical.random_condition_articulator().capitalize()} {Lexical.pronoun(sjt.is_male)} "
                    f"bate no bloqueio a {self.variables['speed_final']}, "
                )
            
            case 'speed_initial':
                self.context_phrase = (
                    f"{context_phrase_head} é arremessado, a partir do solo e verticalmente, "
                    f"subindo até atingir um bloqueio a {self.variables['height_final']}. "
                    f"{Lexical.random_condition_articulator().capitalize()} {Lexical.pronoun(sjt.is_male)} "
                    f"bate no bloqueio a {self.variables['speed_final']}, "
                )
            

    # ----- Roller coaster:
    def set_variables_for_roller_coaster(self):
        subject = MobileOptions.ROLLER_COASTER_TRAIN.value  # Instance of Mobile
        speed_initial = EscalarQuantity(round(subject.set_random_speed(), 1), UnitiesTable.METER_PER_SECOND, 'velocidade com que partira', False)
        
        height_top_value = .5 * pow(speed_initial.value, 2) / self.GRAV
        height_initial_range = uniform(5, 100)
        height_initial = EscalarQuantity(round(height_initial_range, 1), UnitiesTable.METER, 'altura inicial', False)
        interruption = uniform(.5, .9)
        height_final = EscalarQuantity(round(height_top_value * interruption, 1), UnitiesTable.METER, 'altura final', False)

        speed_final = EscalarQuantity(
            round(sqrt(pow(speed_initial.value, 2) + 2 * self.GRAV * (height_initial.value - height_final.value)), 1),
            UnitiesTable.METER_PER_SECOND, 'velocidade que atingiu no segundo ponto', False)

        self.variables = {'subject': subject, 'height_initial': height_initial, 'height_final': height_final,
            'speed_initial': speed_initial, 'speed_final': speed_final}


    def set_context_phrase_for_roller_coaster(self):
        self.does_context_come_first = True  # So problem texts shall be simpler/clearer.
        context_phrase_head = "Um carrinho de montanha russa parte dum ponto"
        
        match self.unknown_variable_key:
            case 'height_initial':
                self.context_phrase = (
                    f"{context_phrase_head} "
                    f"a certa altura a {self.variables['speed_initial']}. Sem ser tracionado, "
                    f"segue do ponto onde está a outro ponto a {self.variables['height_final']} do solo, "
                    f"onde atinge {self.variables['speed_final']}. "
                )

            case 'height_final':
                self.context_phrase = (
                    f"{context_phrase_head} "
                    f"a {self.variables['height_initial']} de altura e a {self.variables['speed_initial']}. Sem ser tracionado, "
                    f"segue até outro ponto, onde atinge {self.variables['speed_final']}. "
                )
            
            case 'speed_initial':
                self.context_phrase = (
                    f"{context_phrase_head} "
                    f"a {self.variables['height_initial']} de altura e a certa velocidade. Sem ser tracionado, "
                    f"segue do ponto onde está até outro ponto a {self.variables['height_final']} de altura, "
                    f"onde atinge {self.variables['speed_final']}. "
                )
            
            case 'speed_final':
                self.context_phrase = (
                    f"{context_phrase_head} "
                    f"a {self.variables['height_initial']} de altura e a {self.variables['speed_initial']}. Sem ser tracionado, "
                    f"segue do ponto onde está até outro ponto a {self.variables['height_final']} de altura. "
                )
        self.todo_statement = self.todo_statement.capitalize()


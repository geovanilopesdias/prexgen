from random import choice, uniform
from .problem import Problem
from services import Lexical, EscalarQuantity, UnitiesTable, MaterialOptions, MaterialTypes

class Concentration(Problem):   
    """
    Abstracts situational problems solvable by the the idea of chemical concentration.
    
    Factory descriptions and proto-text body in Portuguese:
    - concentration-definition: a simple situation that uses de definition of concentration, such as:
        "Calcula a concentração de um soluto na solução, sabendo que a porção de X g tem Y g de soluto". 
    - food_nutrient_comparison: a test of comparison between two foods about which portion of each has more nutrient or else, as in:
        "Qual porção de alimento tem mais ferro: W g de couve (ferro a X%) ou a Y g de feijão (ferro a Z%)?".
    - pollutant_removal: 
    """
    FACTORIES = ('concentration_definition', 'food_nutrient_comparison')
    #, 'pollutant_removal', 'alloy_modification'

    def __init__(self, ctx: str = '', todo: str = '', uvk = '', ans: str = '', var: dict = dict()):
        super().__init__(ctx, todo, uvk, ans, var)


    @classmethod
    def ProblemFactory(cls, factory_name: str) -> 'Concentration':
        if factory_name not in cls.FACTORIES:
            raise ValueError(f"No method found for the factory '{factory_name}'")
        p = Concentration()
        p.build_problem_for(factory_name)
        return p

    
    def raffle_unknown_variable_key(self, factory_name: str):
        super().raffle_unknown_variable_key()
        
    
    # ----- Concentration definition:
    def set_variables_for_concentration_definition(self):
        subject = MaterialOptions.random_material()
        solute = subject.get_random_solute()
        solute_percentage = EscalarQuantity(solute[1], UnitiesTable.MASS_PERCENTAGE, f'concentração de {solute[0]}', False)
        material_mass = EscalarQuantity(uniform(10, 1000), UnitiesTable.GRAM, f'massa dessa porção', False)
        solute_mass = EscalarQuantity(material_mass.value * solute[1]/100, UnitiesTable.GRAM, f'massa de {solute[0]} nela contida', False)
        self.variables = {
            'subject': subject, 'solute_name': solute[0],
            'material_mass': material_mass, 'solute_mass': solute_mass, 'solute_percentage': solute_percentage
            }
        EscalarQuantity.adapt_all_unities_in(self.variables)


    def set_context_phrase_for_concentration_definition(self):
        subject = self.variables['subject']
        self.does_context_come_first = True
        rock_disclaimer = "um mineral composto" if subject.type == MaterialTypes.ROCK else f"compost{Lexical.defined_article(subject.is_male)}"
        context_phrase_head = (
                f"{Lexical.defined_article(subject.is_male).capitalize()} {subject.name} é "
                f"{rock_disclaimer} de {self.variables['solute_name']}"
            )
        match self.unknown_variable_key:
            case 'material_mass':
                self.context_phrase = (
                    f"{context_phrase_head} na concentração de {self.variables['solute_percentage']}. "
                    f"{Lexical.random_condition_articulator().capitalize()} há {self.variables['solute_mass']} de "
                    f"{self.variables['solute_name']} numa porção de {subject.name}, "
                )
                
            case 'solute_mass':
                self.context_phrase = (
                    f"{context_phrase_head} na concentração de {self.variables['solute_percentage']}. "
                    f"{Lexical.random_condition_articulator().capitalize()} uma porção de "
                    f"{subject.name} tenha {self.variables['material_mass']}, "
                )

            case 'solute_percentage':
                self.context_phrase = (
                    f"{context_phrase_head} em certa concentração. "
                    f"{Lexical.random_condition_articulator().capitalize()} uma porção desse material possua {self.variables['material_mass']} "
                    f"e que ela contém {self.variables['solute_mass']} de {self.variables['solute_name']}, "
                )


# ----- Food nutrient comparison:
    def set_variables_for_food_nutrient_comparison(self):
        subject = MaterialOptions.random_material()
        solute = subject.get_random_solute()
        solute_percentage = EscalarQuantity(solute[1], UnitiesTable.MASS_PERCENTAGE, f'concentração de {solute[0]}', False)
        material_mass = EscalarQuantity(uniform(10, 1000), UnitiesTable.GRAM, f'massa dessa porção', False)
        solute_mass = EscalarQuantity(material_mass.value * solute[1]/100, UnitiesTable.GRAM, f'massa de {solute[0]} nela contida', False)
        self.variables = {
            'subject': subject, 'solute_name': solute[0],
            'material_mass': material_mass, 'solute_mass': solute_mass, 'solute_percentage': solute_percentage
            }
        EscalarQuantity.adapt_all_unities_in(self.variables)


    def set_context_phrase_for_food_nutrient_comparison(self):
        subject = self.variables['subject']
        self.does_context_come_first = True
        rock_disclaimer = "um mineral composto" if subject.type == MaterialTypes.ROCK else f"compost{Lexical.defined_article(subject.is_male)}"
        context_phrase_head = (
                f"{Lexical.defined_article(subject.is_male).capitalize()} {subject.name} é "
                f"{rock_disclaimer} de {self.variables['solute_name']}"
            )
        match self.unknown_variable_key:
            case 'material_mass':
                self.context_phrase = (
                    f"{context_phrase_head} na concentração de {self.variables['solute_percentage']}. "
                    f"{Lexical.random_condition_articulator().capitalize()} há {self.variables['solute_mass']} de "
                    f"{self.variables['solute_name']} numa porção de {subject.name}, "
                )
                
            case 'solute_mass':
                self.context_phrase = (
                    f"{context_phrase_head} na concentração de {self.variables['solute_percentage']}. "
                    f"{Lexical.random_condition_articulator().capitalize()} uma porção de "
                    f"{subject.name} tenha {self.variables['material_mass']}, "
                )

            case 'solute_percentage':
                self.context_phrase = (
                    f"{context_phrase_head} em certa concentração. "
                    f"{Lexical.random_condition_articulator().capitalize()} uma porção desse material possua {self.variables['material_mass']} "
                    f"e que ela contém {self.variables['solute_mass']} de {self.variables['solute_name']}, "
                )
# Dados alimentícios coletados de:
# Tabela Brasileira de Composição de Alimentos (TBCA). Universidade de São Paulo (USP). Food Research Center (FoRC). Versão 7.2. São Paulo, 2023. [Acesso em: xxxx]. Disponível em: http://www.fcf.usp.br/tbca.

from enum import Enum
from random import choice, uniform

class MaterialTypes(Enum):
    ROCK = 'rocha'
    METAL_ALLOY = 'liga metálica'
    MEDICINE = 'medicamento'
    POLLUTANT = 'poluente'
    FOOD = 'alimento'



class Material:
    def __init__(self, t: 'MaterialTypes', is_male: bool, n: str, cp: dict):
        self.type = t
        self.name = n
        self.is_male = is_male
        self.check_range_registration_standard(cp)
        self.composition = cp
        

    def __str__(self):
        return f"{self.name}"


    def check_range_registration_standard(self, composition: dict):
        for k, v in composition.items():
            if not isinstance(v, float):
                raise ValueError("All values must be float.")
            if v >= 100:
                raise ValueError("All concentrations should be presented as percentages (i.e., less than 100).")
        if sum(list(composition.values())) > 100:
            raise ValueError("Total concentration must not exceed 100%.")


    def get_random_solute(self) -> list:
        return choice(self.composition.items())



class MaterialOptions(Enum):
    # Rocks:
    BAUXITE = Material(
        MaterialTypes.ROCK, False, 'bauxita',
        {'óxido de alumínio': 50, 'água': 19, 'sílica': 8, 'óxido de ferro': 15, 'dióxido de titânio': 3})
    HEMATITE = Material(
        MaterialTypes.ROCK, False, 'hematita',
        {'ferro': 70, 'oxigênio': 30})
    GALENA = Material(
        MaterialTypes.ROCK, False, 'galena',
        {'chumbo': 86.6, 'enxofre': 13.4})
    CHALCOPYRITE = Material(
        MaterialTypes.ROCK, False, 'calcopirita',
        {'cobre': 34.6, 'ferro': 30.4, 'enxofre': 35})

    # Alloys:
    GOLD_18K = Material(
        MaterialTypes.METAL_ALLOY, True, 'ouro 18K',
        {'ouro': 75, 'prata': 25})
    GOLD_10K = Material(
        MaterialTypes.METAL_ALLOY, True, 'ouro 10K',
        {'ouro': 42, 'prata': 58})
    ROSE_GOLD = Material(
        MaterialTypes.METAL_ALLOY, True, 'ouro rosé',
        {'ouro': 37, 'prata': 20, 'cobre': 43})
    ALUZINC = Material(
        MaterialTypes.METAL_ALLOY, True, 'aluzinco',
        {'alumínio': 55, 'zinco': 43.5, 'silício': 1.5})
    BRONZE = Material(
        MaterialTypes.METAL_ALLOY, True, 'bronze',
        {'cobre': 67, 'estanho': 33})
    ALPHA_BRASS = Material(
        MaterialTypes.METAL_ALLOY, True, 'latão alfa',
        {'cobre': 70, 'zinco': 30})
    BETHA_BRASS = Material(
        MaterialTypes.METAL_ALLOY, True, 'latão beta',
        {'cobre': 50, 'zinco': 50})
    STEEL = Material(
        MaterialTypes.METAL_ALLOY, True, 'aço',
        {'ferro': 96.5, 'carbono': 2, 'manganês': 1, 'níquel': .5})
    STAINLESS_STEEL = Material(
        MaterialTypes.METAL_ALLOY, True, 'inox',
        {'ferro': 73, 'cromo': 15, 'carbono': 1, 'níquel': 10, 'manganês': 1})

    # Foods:
    RICE = Material(
        MaterialTypes.FOOD, True, 'arroz cozido',
        {'cálcio': 5.17e-3, 'fibra': 1.2, 'ferro': .33e-3, 'proteína': 2.38, 'sódio': 1.58e-3, 'carboidrato disponível': 28.4})
    QUINOA = Material(
        MaterialTypes.FOOD, False, 'quinoa cozida',
        {'cálcio': 17e-3, 'fibra': 2.8, 'ferro': 1.49E-3, 'proteína': 2.38, 'sódio': 7e-3, 'carboidrato disponível': 18.5})
    HOMINY = Material(
        MaterialTypes.FOOD, False, 'canjica cozida',
        {'cálcio': .64e-3, 'fibra': 1.27, 'proteína': 2.38, 'ferro': .11e-3, 'sódio': .21e-3, 'carboidrato disponível': 24.3})
    LAMEN = Material(
        MaterialTypes.FOOD, True, 'macarrão cozido',
        {'cálcio': 8.48e-3, 'fibra': 3.51, 'proteína': 4.9, 'ferro': .44e-3, 'sódio': 1.85e-3, 'carboidrato disponível': 22.9})
    CORN = Material(
        MaterialTypes.FOOD, True, 'milho cozido',
        {'cálcio': 1.74e-3, 'fibra': 3.66, 'proteína': 6.16, 'ferro': .8e-3,  'sódio': .78e-3, 'carboidrato disponível': 23.0})
    POPCORN = Material(
        MaterialTypes.FOOD, False, 'pipoca',
        {'cálcio': 2.93e-3, 'fibra': 14.3, 'proteína': 9.93, 'ferro': 1.16e-3,  'sódio': 4.32e-3, 'carboidrato disponível': 56.0})

    PEA = Material(
        MaterialTypes.FOOD, False, 'ervilha cozida',
        {'cálcio': 23.8e-3, 'fibra': 7.26, 'proteína': 7.45, 'ferro': 3.05e-3,  'sódio': 3.59e-3, 'carboidrato disponível': 10.3})
    BLACK_BEAN = Material(
        MaterialTypes.FOOD, True, 'feijão preto cozido',
        {'cálcio': 122e-3, 'fibra': 21.5, 'proteína': 22.4, 'ferro': 9.83e-3, 'carboidrato disponível': 37.6})
    LENTIL = Material(
        MaterialTypes.FOOD, False, 'lentilha cozida',
        {'cálcio': 19e-3, 'fibra': 6.44, 'proteína': 7.3, 'ferro': 1.75e-3,  'sódio': 1.39e-3, 'carboidrato disponível': 13.2})

    CHICKEN = Material(
        MaterialTypes.FOOD, True, 'peito de frango frito',
        {'cálcio': 5.08e-3, 'colesterol': 84.7e-3, 'proteína': 30.4, 'ferro': .32e-3,  'sódio': 47.7e-3})
    CALF = Material(
        MaterialTypes.FOOD, True, 'bife de gado frito',
        {'cálcio': 3.73e-3, 'colesterol': 84.2e-3, 'proteína': 32.2, 'ferro': 2.56e-3,  'sódio': 43.5e-3})
    PORK = Material(
        MaterialTypes.FOOD, False, 'bisteca de porco frita',
        {'cálcio': 69.1e-3, 'colesterol': 126e-3, 'proteína': 33.4, 'ferro': .82e-3,  'sódio': 63e-3})

    LETTUCE = Material(
        MaterialTypes.FOOD, False, 'alface',
        {'cálcio': 37.5e-3, 'ferro': .4e-3, 'fibra': 1.83, 'potássio': 267e-3, 'vitamina C': 15.6e-3})
    CABBAGE = Material(
        MaterialTypes.FOOD, False, 'couve',
        {'cálcio': 208e-3, 'ferro': .67e-3, 'fibra': 3.12, 'potássio': 557e-3, 'vitamina C': 102e-3})
    TOMATO = Material(
        MaterialTypes.FOOD, True, 'tomate',
        {'cálcio': 6.94e-3, 'ferro': .3e-3, 'fibra': 1.6, 'potássio': 191e-3, 'vitamina C': 15.5e-3})
    ARUGULA = Material(
        MaterialTypes.FOOD, False, 'rúcula',
        {'cálcio': 107e-3, 'ferro': 1.02e-3, 'fibra': 2.44, 'potássio': 298e-3, 'vitamina C': 57.8e-3})
    RADISH = Material(
        MaterialTypes.FOOD, True, 'rabanete',
        {'cálcio': 20.6e-3, 'ferro': .35e-3, 'fibra': 1.81, 'potássio': 326e-3, 'vitamina C': 9.59e-3})
    SPINACH = Material(
        MaterialTypes.FOOD, True, 'espinafre',
        {'cálcio': 91.2e-3, 'ferro': .48e-3, 'fibra': 2.83, 'potássio': 452e-3, 'vitamina C': 3.26e-3})
    BEET = Material(
        MaterialTypes.FOOD, False, 'beterraba',
        {'cálcio': 14.4e-3, 'ferro': .32e-3, 'fibra': 3.37, 'potássio': 375e-3, 'vitamina C': 3.12e-3})


    def __str__(self):
        return self.value.__str__()


    @staticmethod
    def random_material() -> 'Material':
        return choice([m.value for m in MaterialOptions])
    
    
    @staticmethod
    def random_food() -> 'Material':
        return choice([m.value for m in MaterialOptions if m.value.type == MaterialTypes.FOOD])
    
    @staticmethod
    def random_rock() -> 'Material':
        return choice([m.value for m in MaterialOptions if m.value.type == MaterialTypes.ROCK])

    @staticmethod
    def random_alloy() -> 'Material':
        return choice([m.value for m in MaterialOptions if m.value.type == MaterialTypes.METAL_ALLOY])
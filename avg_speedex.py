from random import choice, uniform, randint
from enum import Enum
import locale
locale.setlocale(locale.LC_NUMERIC, 'pt_BR.UTF-8')


class Unity:
    def __init__(self, n: str, s: str, t: 'UnitType', e: float):
        self.name = n
        self.symbol = s
        self.type = t
        self.si_eq = e  # Factor to multiply for in order to obtain the SI measure

    @staticmethod
    def convertToSI(value, unity: 'Unity'):
        return value * unity.si_eq

    @staticmethod
    def convertFromSI(value, unity: 'Unity'):
        return value / unity.si_eq

    def __str__(self, symbol_should_be_shown: bool = False):
        return f"{self.name} ({self.symbol})" if symbol_should_be_shown else f"{self.name}"
        
    

class UnitType(Enum):
    LENGTH = 'comprimento'
    TIME = 'time'
    SPEED = 'velocidade'



class UnitiesTable(Enum):
    METER = Unity('metro', 'm', UnitType.LENGTH, 1.0)
    MILES = Unity('milhas', 'mi', UnitType.LENGTH, 1_609.34)
    CENTIMETER = Unity('centímetro', 'cm', UnitType.LENGTH, 1e-2)
    KILOMETER = Unity('quilômetro', 'km', UnitType.LENGTH, 1e3)

    SECOND = Unity('segundo', 's', UnitType.TIME, 1)
    MINUTE = Unity('minuto', 'min', UnitType.TIME, 60)
    HOUR = Unity('hora', 'h', UnitType.TIME, 3_600)

    METER_PER_SECOND = Unity('metro por segundo', 'm/s', UnitType.SPEED, 1.0)
    KILOMETER_PER_HOUR = Unity('quilômetro por hora', 'km/h', UnitType.SPEED, 1/3.6)
    MILES_PER_HOUR = Unity('milha por hora', 'mi/h', UnitType.SPEED, .44704)

    def __str__(self):
        return self.value.__str__()
    
    @staticmethod
    def randomLengthUnity():
        unities = (UnitiesTable.METER, UnitiesTable.MILES, UnitiesTable.KILOMETER)
        return choice(unities).value

    @staticmethod
    def randomTimeUnity():
        unities = (UnitiesTable.SECOND, UnitiesTable.MINUTE, UnitiesTable.HOUR)
        return choice(unities).value

    @staticmethod
    def randomSpeedUnity():
        unities = (UnitiesTable.METER_PER_SECOND, UnitiesTable.KILOMETER_PER_HOUR, UnitiesTable.MILES_PER_HOUR)
        return choice(unities).value



class MobileTypes(Enum):
    MOTOR = 'motor'
    PERSON = 'person'



class Mobile:
    def __init__(self, t: 'MobileTypes', is_male: bool, n: str, verb: str, dr: tuple, sr: tuple):
        assert (len(dr) == 2 and len(sr) == 2)
        self.mobile_type = t
        self.name = n
        self.is_male = is_male
        self.verb = verb
        self.distance_range = dr
        self.speed_range = sr
        
    def __str__(self):
        return f"{self.name} {self.verb}"

    def randomSpeedFor(self) -> float:
        return uniform(self.speed_range[0], self.speed_range[1])

    def randomDistanceFor(self) -> float:
        return uniform(self.distance_range[0], self.distance_range[1])

    def article(self, is_definite: bool = False):
        if self.is_male:
            return 'o' if is_definite else 'um'
        else:
            return 'a' if is_definite else 'uma'

    def pronoun(self):
        if self.is_male:
            return 'ele'
        else:
            return 'ela'

    def set_random_motion_verb(self, does_indicate_speed: bool = True):
        if not does_indicate_speed:
            verbs = ('percorre', 'atravessa')
        else:
            if self.mobile_type == MobileTypes.MOTOR:
                verbs = ('viaja a', 'é digirido a')
            else:
                verbs = ('anda a', 'se move a')
        self.verb = choice(verbs)

     



class MobileOptions(Enum):
    CAR = Mobile(MobileTypes.MOTOR, True, 'carro', '', (500, 300_000), (10, 35))
    PERSON = Mobile(MobileTypes.PERSON, False, 'pessoa', '', (100, 5_000), (1, 2))

    def __str__(self):
        return self.value.__str__()
    
    def randomSpeedFor(self) -> float:
        return self.value.randomSpeedFor()

    def randomDistanceFor(self) -> float:
        return self.value.randomDistanceFor()

    @staticmethod
    def randomMobile():
        return choice(list(MobileOptions)).value



class Problem():  # Definir como geral noutro local...
    def __init__(self, sta: str = '', ans: str = '', var: dict = dict()):
        self.statement = sta
        self.answer = ans
        self.variables = var

    def __str__(self):
        return self.sta + '\n' + self.ans

    def set_random_variables() -> dict:
        mobile = MobileOptions.randomMobile()
        speed = mobile.randomSpeedFor()
        distance = mobile.randomDistanceFor()
        return {'mobile': mobile, 'speed': speed, 'distance': distance, 'time': distance / speed}

    def set_random_unities(self) -> dict:
        """
        Sorteia unidades para variáveis da instância de problema, convertendo-as;
        Retorna um dicionário com instâncias de Unity sortedas para manipulação.
        """
        unities = dict()
        unities['distance'] = UnitiesTable.randomLengthUnity()
        self.variables['distance'] = Unity.convertFromSI(self.variables['distance'], unities['distance'])
        
        unities['time'] = UnitiesTable.randomTimeUnity()
        self.variables['time'] = Unity.convertFromSI(self.variables['time'], unities['time'])

        unities['speed'] = UnitiesTable.randomSpeedUnity()
        self.variables['speed'] = Unity.convertFromSI(self.variables['speed'], unities['speed'])
        return unities

    def SimpleVoyage(precision = 2):
        # Configurações iniciais:
        v = Problem.set_random_variables()  # Sorteia as variáveis
        m = v['mobile']  # Simplifica expressão do móvel estabelecido
        m.set_random_motion_verb()  # Sorteia verbo de movimento
        p = Problem(var = v)  # Constrói o problema com as variáveis sorteadas
        u = p.set_random_unities()  # Sorteia e armazenas as unidades, convertendo os valores das variáveis da instância de problema.
        r_f_distance = locale.format_string("%.2f", round(v['distance'], precision), grouping=True)
        r_f_time = locale.format_string("%.2f", round(v['time'], precision), grouping=True)
        r_f_speed = locale.format_string("%.2f", round(v['speed'], precision), grouping=True)

        # Genérico: Um [carro anda] a 20 km/h.
        unknown_var = choice(('distance', 'time', 'speed'))
        match unknown_var:
            case 'distance':
                p.sta = f"{m.article().capitalize()} {str(m)} {r_f_speed} {u['speed'].symbol}. Se {m.pronoun()} anda durante {r_f_time} {u['time'].symbol}, que distância (em {str(u['distance'])}) {m.pronoun()} percorre?"
                p.ans = f"Resposta: {r_f_distance} {u['distance'].symbol}."
            case 'time':
                p.sta = f"{m.article().capitalize()} {str(m)} {r_f_speed} {u['speed'].symbol}. Se {m.pronoun()} percorre {r_f_distance} {u['distance'].symbol}, em quanto tempo (em {str(u['time'])}) {m.pronoun()} o faz?"
                p.ans = f"Resposta: {r_f_time} {u['time'].symbol}."
            case 'speed':
                p.sta = f"{m.article().capitalize()} {str(m)} certa velocidade. Se {m.pronoun()} percorre {r_f_distance} {u['distance'].symbol} em {r_f_time} {u['time'].symbol}, qual é sua velocidade média (em {str(u['speed'])})?"
                p.ans = f"Resposta: {r_f_speed} {u['speed'].symbol}."
        

        return p

for c in range(0, 20):
    print(f'{c+1}) {Problem.SimpleVoyage()}')
        

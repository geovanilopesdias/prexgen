from typing import List
from .unity import UnityTable
from .quantity import EscalarQuantity
from problems.problem import Problem


class Hint:
    """
    Abstracts the idea of a hint to help students to
    solve problems or attend to exercise training
    without giving them out the answers.
    """
    # Probably should turned into child classes...
    HINT_TYPES = ('conversion', 'equation', 'strategy')

    def __init__(self, lbl: str = '', txt: str = '', ht: str = ''):
        if ht not in self.HINT_TYPES:
            raise ValueError(f"Invalid hint type: {ht}")

        self.label = lbl
        self.text = txt
        self.hint_type = ht


    def build_detailed_hint_for_conversion(self, unknown_unity: 'UnityTable', known_symbols: List['UnityTable']) -> str:
        """
        Returns a string with the detailed hint for conversion based on the problem unities.
        """
        match unknown_unity.value.type:
            case UnitType.LENGTH:
                pass
            case _:
                pass


    def ForConversionInProblems(self,
                                p: 'Problem',
                                details_should_be_shown: bool = False) -> 'Hint':
        """
        Factory method to create a basic or detailed hint for conversion in problems.
        """
        unknown_unity = p.variables[p.unknown_variable_key].unity
        known_unities = [v.unity for k, v in items(p.variables) if isinstance(v, EscalarQuantity) and k != p.unknown_variable_key]
        variables = [v for v in p.variables if isinstance(v, EscalarQuantity)]
        v_names = ', '.join(v.name for v in variables)
        v_symbols = [v.unity.value.symbol for v in variables]
        base_hint = (
            f"Evita conversões desnecessárias! Confere as unidades de medida de cada grandeza "
            f"({v_names}), especialmente a da incógnita ({unknown_unity.value.symbol}) "
            f"para decidir qual medida precisa ser convertida - e se, de fato, há "
            f"alguma para ser feita."
        )
        details = str()
        if details_should_be_shown:
            details = self.build_detailed_hint_for_conversion(unknown_unity, known_unities)
        return Hint('conversão', f"{base_hint}\n{details}", 'conversion')

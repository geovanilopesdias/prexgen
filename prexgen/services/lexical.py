from enum import Enum
import re
import locale
from random import choice
from .mobile import MobileTypes

locale.setlocale(locale.LC_NUMERIC, 'pt_BR.UTF-8')

class Lexical:
    """
    Service class to encapsulate grammar and syntactic functions and rafflers for different
    syntactic expressions.
    """
    class ChangingMode(Enum):
        GENERIC = 'GENERIC'
        INCREASE = 'INCREASE'
        DECREASE = 'DECREASE'
    
    class VerbTense(Enum):
        PRESENT = 'PRESENT'
        PAST = 'PAST'
        FUTURE = 'FUTURE'
    
    
    def capitalize_after_punctuation(phrase: str):
        punc_filter = re.compile('([.!?]\s*)')
        splitted_phrase = punc_filter.split(phrase)
        return ''.join([word.capitalize() for word in splitted_phrase])


    def format_with_comma(value: float) -> str:
        return locale.format_string("%.1f", value)


    def undefined_article(is_male: bool):
        return 'um' if is_male else 'uma'

    
    def defined_article(is_male: bool):
        return 'o' if is_male else 'a'


    def pronoun(is_male: bool):
        """
        Returns 'ele' or 'ela' according to the gender passed.
        """
        return 'ele' if is_male else 'ela'


    def possessive_pronoun(is_male: bool):
        """
        Returns 'seu' or 'sua' according to the gender passed.
        """
        return 'seu' if is_male else 'sua'


    def random_inquisitive_pronoun():  # Avoid the use of gender!
        return choice(('qual', 'quanto vale'))


    # ----- Rando verbs
    def random_imperative_verb():
        return choice(('calcula', 'determina'))


    @classmethod
    def random_attribute_indicator_verb(cls, vt: 'VerbTense' = VerbTense.PRESENT):
        match vt:
            case cls.VerbTense.PRESENT:
                return choice(('tem', 'possui'))
            case cls.VerbTense.PAST:
                return choice(('tinha', 'possuía'))
            case cls.VerbTense.FUTURE:
                return choice(('terá', 'possuirá'))


    def random_crossing_verb():
        return choice(('atravessa', 'perpassa', 'passa por'))


    def random_motion_verb(mob_type: 'MobileTypes'):
        if mob_type == MobileTypes.MOTOR:
            verbs = ('viaja', 'translada', 'transita', 'trafega')
        else:
            verbs = ('anda', 'se move')
        return choice(verbs)


    @classmethod
    def random_verb_for_changing(cls, mode: 'ChangingMode'):
        match mode:
            case cls.ChangingMode.GENERIC:
                verbs = ('altera', 'modifica', 'muda')
            case cls.ChangingMode.INCREASE:
                verbs = ('aumenta', 'cresce', 'sobe')
            case cls.ChangingMode.DECREASE:
                verbs = ('diminui', 'reduz')          
        return choice(verbs)


    # ----- Random adverbs
    def random_completeness_adverb():
        return choice(('completamente', 'inteiramente', 'integralmente', 'inteiramente'))
    

    def random_interval_adverb():
        return choice(('em', 'durante', 'sob o intervalo de', 'ao longo de'))


    def random_distance_adverb():
        return choice(('ao longo de', 'por', 'percorrendo'))


    def random_condition_articulator():
        return choice(('se', 'supondo que', 'pressupondo que', 'sabendo que', 'considerando que', 'admitindo que'))


    def random_contrast_marker() -> str:
        """
        It raffles a adverb or a adverbial locution that serves as a contrast marker
        that can be used in a sentence both right before or after the subject.
        """
        return choice(('por sua vez', 'porém', 'entretanto', 'contudo', 'todavia', 'no entanto'))
    

    def random_verb_to_present(variable: str, mob_type: 'MobileTypes'):
        if variable != 'speed':
            verbs = ('percorre', 'atravessa', 'se move por', 'se locomove por')
        else:
            if mob_type == MobileTypes.MOTOR:
                verbs = ('viaja a', 'se move a', 'se locomove a', 'transita a')
            else:
                verbs = ('anda a', 'se move a', 'se locomove a')
        return choice(verbs)


    @classmethod
    def random_crossing_verb_with_pronun(cls, is_male: bool, is_gerundio: bool = False):
        modifier = 'ndo' if is_gerundio else ''
        return choice((f'atravessa{modifier}-{cls.defined_article(is_male)}',
                       f'cruza{modifier}-{cls.defined_article(is_male)}',
                       f'percorre{modifier}-{cls.defined_article(is_male)}',
                       f'passa{modifier} por {cls.pronoun(is_male)}'))
    
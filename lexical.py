from random import choice
from mobile import MobileTypes
import re
import locale

locale.setlocale(locale.LC_NUMERIC, 'pt_BR.UTF-8')

class Lexical:
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
        return 'ele' if is_male else 'ela'


    def random_inquisitive_pronoun():  # Avoid the use of gender!
        return choice(('qual', 'quanto vale'))


    # ----- Rando verbs
    def random_imperative_verb():
        return choice(('calcula', 'determina'))


    def random_attribute_indicator_verb():
        return choice(('tem', 'possui', 'apresenta', 'exibe'))


    def random_crossing_verb():
        return choice(('atravessa', 'perpassa', 'passa por'))


    def random_motion_verb(mob_type: 'MobileTypes'):
        if mob_type == MobileTypes.MOTOR:
            verbs = ('viaja', 'anda')
        else:
            verbs = ('anda', 'se move')
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
    

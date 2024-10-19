from random import choice
from mobile import MobileTypes
import re

class Lexical:
    def capitalize_after_punctuation(phrase: str):
        punc_filter = re.compile('([.!?]\s*)')
        splitted_phrase = punc_filter.split(phrase)
        return ''.join([word.capitalize() for word in splitted_phrase])


    def undefined_article(is_male: bool):
        return 'um' if is_male else 'uma'

    
    def defined_article(is_male: bool):
        return 'o' if is_male else 'a'


    def pronoun(is_male: bool):
        return 'ele' if is_male else 'ela'


    def random_inquisitive_pronoun(is_male):
        return choice(('que', f'qual {Lexical.defined_article(is_male)}', f'qual o valor d{Lexical.defined_article(is_male)}'))


    def random_imperative_verb(is_male):
        return choice((f'calcula {Lexical.defined_article(is_male)}', f'determina {Lexical.defined_article(is_male)}'))


    def random_condition_articulator():
        return choice(('se', 'supondo que', 'pressupondo que', 'sabendo que', 'considerando que', 'admitindo que'))


    def random_interval_adverb():
        return choice(('durante', 'sob o intervalo de', 'ao longo de'))


    def random_distance_adverb():
        return choice(('ao longo de', 'por', 'percorrendo'))


    def random_motion_verb(mob_type: 'MobileTypes'):
        if mob_type == MobileTypes.MOTOR:
            verbs = ('viaja', 'anda')
        else:
            verbs = ('anda', 'se move')
        return choice(verbs)


    def random_verb_to_present(variable: str, mob_type: 'MobileTypes'):
        if variable != 'speed':
            verbs = ('percorre', 'atravessa', 'se move por')
        else:
            if mob_type == MobileTypes.MOTOR:
                verbs = ('viaja a', 'é digirido a')
            else:
                verbs = ('anda a', 'se move a')
        return choice(verbs)

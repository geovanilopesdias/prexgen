from lexical import Lexical
from random import choice

class Problem():
    def __init__(self, ctx: str = '', todo: str = '', uvk: str = '', ans: str = '', var: dict = dict()):
        self.context_phrase = ctx
        self.todo_statement = todo
        self.unknown_variable_key = uvk
        self.answer = ans
        self.variables = var
        self.does_context_come_first = choice((True, False))
        self.is_inquisitive = choice((True, False))


    def __str__(self):
        punctuation = '?' if self.is_inquisitive else '.'
        if self.does_context_come_first:
            return Lexical.capitalize_after_punctuation(f"{self.context_phrase}; {self.todo_statement}{punctuation}" + '\n' + self.answer)
        else:
            return Lexical.capitalize_after_punctuation(f"{self.todo_statement}, {self.context_phrase}{punctuation}" + '\n' + self.answer)

    
    # Ainda não testado
    @classmethod
    def RandomProblem(cls) -> 'Problem':
        """
        Draws a random factory method within the child class.
        """
        return choice([getattr(cls, method) for method in dir(cls) if callable(getattr(cls, method)) and method.endswith('Problem')])()


    def set_random_variables():
        raise NotImplementedError
    

    def set_formated_quantities(self):
        self.variables['form_vars'] = {key: Lexical.format_with_comma(value) for key, value in self.variables.items() if isinstance(value, float)}


    def build_problem_text():
        raise NotImplementedError
        
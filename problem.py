from lexical import Lexical
from random import choice


class Problem():
    """
    Abstracts the idea of a problem (mathematical, physical, chemical etc.), i.e.,
    a question or order underlined by some context that imposes
    some sort of reasoning (commonly encompassing calculation)
    in order to solve it (i.e., answer or attend to it).
    """
    FACTORIES: tuple[str, ...] = ()

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
            return Lexical.capitalize_after_punctuation(f"{self.context_phrase}. {self.todo_statement}{punctuation}" + '\n' + self.answer)
        else:
            return Lexical.capitalize_after_punctuation(f"{self.todo_statement}, {self.context_phrase}{punctuation}" + '\n' + self.answer)


    def set_random_variables():
        raise NotImplementedError

    
    def build_problem_text():
        raise NotImplementedError

    
    def ProblemFactory(cls, factory_name: str):
        raise NotImplementedError
    

    @classmethod
    def raffle_a_problem(cls):
        return cls.ProblemFactory(choice(cls.FACTORIES))


    @classmethod
    def raffle_problem_set_of_each_type(cls, n: int = 1):
        return [cls.ProblemFactory(name) for name in cls.FACTORIES for _ in range(n)]
       

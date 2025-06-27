from random import choice
from services import Lexical, EscalarQuantity, UnitiesTable

class Problem():
    """
    Abstracts the idea of a problem (mathematical, physical, chemical etc.), i.e.,
    a question or order underlined by some context that imposes
    some sort of reasoning (commonly encompassing calculation)
    in order to solve it (i.e., answer it or attend to it).
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
        p = '?' if self.is_inquisitive else '.'
        return (
            f"{self.context_phrase}{self.todo_statement}{p}"
            if self.does_context_come_first
            else f"{self.todo_statement}{self.context_phrase}{p}"
        )
        

    def validate_factory_name(self, factory_name: str):
        """
        It raises NotImplementedError if the factory_name passed is not
        previwed in the child class' FACTORY tuple.
        """
        if factory_name not in self.FACTORIES:
            raise NotImplementedError(f"No method found for the factory '{factory_name}'")


    def set_random_variables(self, factory_name: str):
        """
        Sets the variables of the instance according to the factory name passed.
        See the class documentation for the factory names and descriptions.
        """
        getattr(self, f"set_variables_for_{factory_name}")()


    def set_context_phrase(self, factory_name: str):
        """Sets the context phrase of the instance according to the factory name passed.
        See the class documentation for the factory names and descriptions."""
        getattr(self, f"set_context_phrase_for_{factory_name}")()


    def raffle_unknown_variable_key(self):
        """
        Randomizes the key of the unknown variable from the EscalarQuantity instances,
        so, it can only be used after set_random_variables method.

        If some factory need specific implementation, it should be overwritten in
        match/case block having the super method as the default case.
        """
        key_options = [k for k, v in self.variables.items() if isinstance(v, EscalarQuantity)]
        self.unknown_variable_key = choice(key_options)


    def set_todo_statement_and_answer(self):
        """
        Builds the to-do statement and answer, so it can only be used after
        set_random_variables and raffle_unknown_variable_key methods.
        """       
        self.answer = f"{self.variables[self.unknown_variable_key]}"
        
        todo_statement_head = Lexical.random_inquisitive_pronoun() if self.is_inquisitive else Lexical.random_imperative_verb()
        subject_reference = (
            Lexical.pronoun(self.variables['subject'].is_male)
            if self.does_context_come_first
            else f"{Lexical.undefined_article(self.variables['subject'].is_male)} {self.variables['subject'].name}"
        )
        match self.unknown_variable_key:
            # subject_tail should begin with a space in order to avoid one unecessary if the tail is empty.
            case 'length' | 'speed':
                subject_tail = (
                    f" que {subject_reference} {Lexical.random_attribute_indicator_verb()}"
                )
            case 'distance' | 'time':
                subject_tail = (
                    f" que {subject_reference} {Lexical.random_motion_verb(self.variables['subject'].type)}"
                )
            case 'higher_speed' | 'lower_speed':
                subject_tail = (
                    f" que {subject_reference} {Lexical.random_attribute_indicator_verb(Lexical.VerbTense.PAST)}"
                )
            case _:
                subject_tail = str()

        unk_var = self.variables[self.unknown_variable_key]
        self.todo_statement = (
                f"{todo_statement_head} {Lexical.defined_article(unk_var.is_male)} "
                f"{unk_var.name} (em {unk_var.unity.value.symbol}){subject_tail}"
        )


    def build_problem_for(self, factory_name: str):
        """
        Sets an instance of Problem with randomized attributes according to the
        static factory name passed.
        """
        self.validate_factory_name(factory_name)
        self.set_random_variables(factory_name)
        self.raffle_unknown_variable_key(factory_name)
        self.set_todo_statement_and_answer()
        self.set_context_phrase(factory_name)


    def ProblemFactory(cls, factory_name: str):
        raise NotImplementedError
    

    @classmethod
    def raffle_a_problem(cls):
        return cls.ProblemFactory(choice(cls.FACTORIES))


    @classmethod
    def raffle_problem_set_of_each_type(cls, n: int = 1):
        return [cls.ProblemFactory(name) for name in cls.FACTORIES for _ in range(n)]
       

from .system_factories import SystemFactories
from problems import *

class Assessment:      
    
    # Alterar local de constantes abaixo!
    SCHOOL = 'EEEM Erni Oscar Fauth'
    SUBJECT = 'Física'
    TEACHER = 'Me. Geovani L. Dias'
    QUARTER = 2


    @classmethod
    def header(cls, student_name: str, classroom: str):
        return (
            f"{cls.SCHOOL} | Prof.: {cls.TEACHER} \nRecuperação de {cls.SUBJECT}, {cls.QUARTER}º trimestre \nNome: {student_name} | Turma: {classroom}\n"
            "Atenção: devido aos arredondamentos computados pelo programa, especialmente quando envolvem raízes quadradas, podem ocorrer pequenas diferenças nos resultados (entre 1 e 2)."
            )


    @classmethod
    def footer(cls):
        return '\n---\n'

    @classmethod
    def get_subject(cls, subject: 'SystemFactories', qnt_of_each: int = 1) -> list:
        match subject:
            case SystemFactories.AVERAGE_SPEED:
                return AverageSpeed.raffle_problem_set_of_each_type(qnt_of_each)
            case SystemFactories.UVRM:
                return Uvrm.raffle_problem_set_of_each_type(qnt_of_each)
            case SystemFactories.MECH_ENERGY_CONS:
                return MechanicalEnergyConservation.raffle_problem_set_of_each_type(qnt_of_each)
            case SystemFactories.CONCENTRATION:
                return Concentration.raffle_problem_set_of_each_type(qnt_of_each)


    @classmethod
    def attribute_problems_to_school(cls, school: list, subject: 'SystemFactories', qnt_of_each: int = 1) -> dict:
        """
        Generate a dictionary with all problems and answers for each student.
        The keys of the inner dictionaries use the pattern 'f"{c['name']}-{s}"'
        where c and s are the respective names of classroom and students.
        """
        school_stack = {'problems': dict(), 'answers': dict()}
        for c in school:
            for s in c['students_names']:
                problems = cls.get_subject(subject, qnt_of_each)
                school_stack['problems'][f"{c['name']}-{s}"] = list()
                school_stack['answers'][f"{c['name']}-{s}"] = list()
                for index, p in enumerate(problems):
                    school_stack['problems'][f"{c['name']}-{s}"].append(f'{index+1}) {p}')
                    school_stack['answers'][f"{c['name']}-{s}"].append(f'{index+1}) {p.answer}')
        
        return school_stack


    @classmethod
    def print_test(cls, school: list, subject: 'SystemFactories', qnt_of_each: int = 1):
        """
        Print out problems hiding the answers (but from the teacher) so students may be tested.
        """
        school_stack = cls.attribute_problems_to_school(school, subject, qnt_of_each)
        for c in school:
            for s in c['students_names']:
                print(cls.header(s, c['name']))
                for p in school_stack['problems'][f"{c['name']}-{s}"]:
                    print(p)
                print(cls.footer())
        
        for c in school:
            print(f"Respostas da turma {c['name']}:")
            for s in c['students_names']:
                print(f'\n{s}:')
                for a in school_stack['answers'][f"{c['name']}-{s}"]:
                    print(f'{a}')


    @classmethod
    def generate_training(cls, school: list, subject: 'SystemFactories', qnt_of_each: int = 1):
        """
        Print out problems with the answers, so students may be trained.
        """
        school_stack = cls.attribute_problems_to_school(school, subject, qnt_of_each)
        for c in school:
            for s in c['students_names']:
                print(cls.header(s, c['name']))
                for p in school_stack['problems'][f"{c['name']}-{s}"]:
                    print(p)
                print('Respostas: ' + ' | '.join(school_stack['answers'][f"{c['name']}-{s}"]))
                print(cls.footer())
           
    
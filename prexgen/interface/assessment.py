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
        return f'{cls.SCHOOL} | Prof.: {cls.TEACHER} \nAvaliação de {cls.SUBJECT}, {cls.QUARTER}º trimestre \nNome: {student_name} | Turma: {classroom}'


    @classmethod
    def footer(cls):
        return '\n---\n'


    @classmethod
    def generate(cls, school: list, subject: 'SystemFactories', qnt_of_each: int = 1):
        school_answers = dict()
        for c in school:
            for s in c['students_names']:
                school_answers[f"{c['name']}-{s}"] = list()
                print(cls.header(s, c['name']))

                match subject:
                    case SystemFactories.AVERAGE_SPEED:
                        problems = AverageSpeed.raffle_problem_set_of_each_type(qnt_of_each)
                    case SystemFactories.UVRM:
                        problems = Uvrm.raffle_problem_set_of_each_type(qnt_of_each)
                    case SystemFactories.MECH_ENERGY_CONS:
                        problems = MechanicalEnergyConservation.raffle_problem_set_of_each_type(qnt_of_each)
                    
                for index, p in enumerate(problems):
                    print(f'{index+1}) {p}')
                    school_answers[f"{c['name']}-{s}"].append(f'{index+1}) {p.answer}')
                print(cls.footer())

        for student, student_answer in school_answers.items():
            print(f'\n{student}:')
            for answer in student_answer:
                print(answer)
    
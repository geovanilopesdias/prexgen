from problems import *

class Assessment:
    SCHOOL = 'Aula Particular'
    SUBJECT = 'Física e Química'
    TEACHER = 'Me. Geovani L. Dias'
    QUARTER = 3

    CLASSROOMS = [
        {'name': 'Remoto',
        'students_names': [
            'Guilherme Leitte']}
##        {'name': 112,
##        'students_names': [
##            'Alan Mateus Musskopf',
##            'Cleiton de Mattos Santos',
##            'Emily Gabriela da Rosa',
##            'Erick Alves Schmitzhaus',
##            'Ezequiel Lopes da Motta',
##            'Gabriel Henrique Herzer',
##            'Gabriel RIcardo Stahlhofer',
##            'Hellen Talia Rodrigues da Borba',
##            'Lara Tabata Souza',
##            'Laura Stephanie Ritter',
##            'Leandro Santos de Oliveira',
##            'Liana Eduarda de Oliveira',
##            'Manuela de Souza Dill',
##            'Manuela Dorneles Gonçalves',
##            'Marina Kerber Buttenbender',
##            'Matheus Kaspar Pedroso',
##            'Natália Etzberger Klein',
##            'Pedro Henrique Schroeder',
##            'Roni José Cimadon',
##            'Talita Vitoria Silveira']}
    ]


    @classmethod
    def header(cls, student_name: str, classroom: str):
        return f'{cls.SCHOOL} | Prof.: {cls.TEACHER} \nAvaliação de {cls.SUBJECT}, {cls.QUARTER}º trimestre \nNome: {student_name} | Turma: {classroom}'


    @classmethod
    def footer(cls):
        return '\n---\n'


    @classmethod
    def generate(cls, quantity: int = 12):
        school_answers = dict()
        for c in cls.CLASSROOMS:
            for s in c['students_names']:
                school_answers[f"{c['name']}-{s}"] = list()
                print(cls.header(s, c['name']))
                for index in range(0, quantity):
                    problems = AverageSpeed.raffle_problem_set_of_each_type(12)
                    print(f'{index+1}) {problems[index]}')
                    school_answers[f"{c['name']}-{s}"].append(f'{index+1}) {problems[index].answer}')
                print(cls.footer())

        for student, student_answer in school_answers.items():
            print(f'\n{student}:')
            for answer in student_answer:
                print(answer)
                    
Assessment.generate()

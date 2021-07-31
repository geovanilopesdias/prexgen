class ConjDados():
    def __init__(self, dado1, unid1, dado2, unid2, incog, unidincog, respo):
        self._d1 = dado1
        self._u1 = unid1
        self._d2 = dado2
        self._u2 = unid2
        self._i = incog
        self._ui = unidincog
        self._r = respo

    @property
    def d1(self):
        return self._d1

    @d1.setter
    def d1(self, d1):
        self._d1 = d1

    @property
    def d2(self):
        return self._d2

    @d2.setter
    def d2(self, d2):
        self._d2 = d2

    @property
    def i(self):
        return self._i

    @i.setter
    def i(self, i):
        self._i = i

    @property
    def u1(self):
        return self._u1

    @u1.setter
    def u1(self, u1):
        self._u1 = u1

    @property
    def u2(self):
        return self._u2

    @u2.setter
    def u2(self, u2):
        self._u2 = u2

    @property
    def ui(self):
        return self._ui

    @ui.setter
    def ui(self, ui):
        self._ui = ui

    @property
    def r(self):
        return self._r

    @d1.setter
    def r(self, r):
        self._r = r


def sorteia_sujeito():
    from random import randint
    return randint(1, 2)  # 1 para Pessoa e 2 para Veiculo


def construtor():
    """
    Constroi randomicamente os dados do exercício cinemático.
    :return: Lista com incógnita sorteada (1: rapidez; 2: deslocamento; 3: tempo), e os demais dados necessários a seu
    cálculo com as respectivas unidades de medida.
    """
    from random import randint as st
    s = sorteia_sujeito()
    dados = gera_dados(s)
    s1 = ['pessoa ',
          'indivíduo ',
          'rapaz ',
          'moça ']
    v1 = ['caminha ',
          'corre ',
          'anda ',
          'passeia ']
    s2 = ['ciclista ',
          'moto ',
          'carro ',
          'caminhão ',
          'ônibus ',
          'trem ',
          'avião ']
    v2 = ['viaja ',
          'se move ',
          'circula ',
          'transita ']

    # condições da primeira oração
    # RAPIDEZ
    ca_r = ['com uma rapidez de ',
            'a uma rapidez de ',
            'com rapidez de ']
    # DESLOCAMENTO
    ca_d = ['ao longo de um trajeto de ',
            'por um percurso de ']

    # condições da segunda oração
    # DESLOCAMENTO
    cb_d = ['. Sabendo que o trajeto é de ',
          '. Levando em conta que o percurso é de ',
          '. Se considerarmos a distância percorrida como sendo de ',
          '. Supondo que o movimento se deu ao longo de ',
          '. Considerando um deslocamento de ']
    cb_t = ['. Sabendo que o movimento durou ',
          '. Levando em conta que passaram-se ',
          '. Se considerarmos o intervalo de tempo de ',
          '. Supondo que o movimento se deu em ',
          '. Considerando uma duração do movimento de ']

    ordem = [', calcula a/o ',
             ', determina a/o ',
             ', verifica a/o ']
    movel = st(0, len(s1) - 1)
    if s == 1 and dados[0] == 'rapidez':
        return ['Um/a '+str(s1[movel]) + ' ' + str(v1[st(0, len(v1) - 1)]) +
              str(ca_d[st(0, len(ca_d) - 1)]) + str(dados[2]) + ' ' + str(dados[3]) +
              str(cb_t[st(0, len(ca_d) - 1)]) + str(dados[4]) + ' ' + str(dados[5]) +
              str(ordem[st(0, len(ca_d) - 1)]) + str(dados[0]) + ' do/a ' +
              str(s1[movel]) + ' em ' + str(dados[1]) + '.\n', dados[6], dados[1]]
    elif s == 2 and dados[0] == 'rapidez':
        return ['Um/a ' + str(s2[movel]) + ' ' + str(v2[st(0, len(v2) - 1)]) +
               str(ca_d[st(0, len(ca_d) - 1)]) + str(dados[2]) + ' ' + str(dados[3]) +
               str(cb_t[st(0, len(ca_d) - 1)]) + str(dados[4]) + ' ' + str(dados[5]) +
               str(ordem[st(0, len(ca_d) - 1)]) + str(dados[0]) + ' do/a ' +
               str(s2[movel]) + ' em ' + str(dados[1]) + '.\n', dados[6], dados[1]]

    elif s == 1 and dados[0] == 'deslocamento':
        return ['Um/a ' + str(s1[movel]) + ' ' + str(v1[st(0, len(v1) - 1)]) +
               str(ca_r[st(0, len(ca_d) - 1)]) + str(dados[2]) + ' ' + str(dados[3]) +
               str(cb_t[st(0, len(ca_d) - 1)]) + str(dados[4]) + ' ' + str(dados[5]) +
               str(ordem[st(0, len(ca_d) - 1)]) + str(dados[0]) + ' do/a ' +
               str(s1[movel]) + ' em ' + str(dados[1]) + '.\n', dados[6], dados[1]]
    elif s == 2 and dados[0] == 'deslocamento':
        return ['Um/a ' + str(s2[movel]) + ' ' + str(v2[st(0, len(v2) - 1)]) +
               str(ca_r[st(0, len(ca_d) - 1)]) + str(dados[2]) + ' ' + str(dados[3]) +
               str(cb_t[st(0, len(ca_d) - 1)]) + str(dados[4]) + ' ' + str(dados[5]) +
               str(ordem[st(0, len(ca_d) - 1)]) + str(dados[0]) + ' do/a ' +
               str(s2[movel]) + ' em ' + str(dados[1]) + '.\n', dados[6], dados[1]]

    elif s == 1 and dados[0] == 'tempo':
        return ['Um/a ' + str(s1[movel]) + ' ' + str(v1[st(0, len(v1) - 1)]) +
               str(ca_r[st(0, len(ca_d) - 1)]) + str(dados[2]) + ' ' + str(dados[3]) +
               str(cb_d[st(0, len(ca_d) - 1)]) + str(dados[4]) + ' ' + str(dados[5]) +
               str(ordem[st(0, len(ca_d) - 1)]) + str(dados[0]) + ' do/a ' +
               str(s1[movel]) + ' em ' + str(dados[1]) + '.\n', dados[6], dados[1]]
    elif s == 2 and dados[0] == 'tempo':
        return ['Um/a ' + str(s2[movel]) + ' ' + str(v2[st(0, len(v2) - 1)]) +
               str(ca_r[st(0, len(ca_d) - 1)]) + str(dados[2]) + ' ' + str(dados[3]) +
               str(cb_d[st(0, len(ca_d) - 1)]) + str(dados[4]) + ' ' + str(dados[5]) +
               str(ordem[st(0, len(ca_d) - 1)]) + str(dados[0]) + ' do/a ' +
               str(s2[movel]) + ' em ' + str(dados[1]) + '.\n', dados[6], dados[1]]


def gera_dados(sujeito):
    """
    Constroi randomicamente os dados do exercício cinemático.
    :param sujeito: tipo de sujeito definido pelo método "sujeito". Define a faixa de rapidez aceitável para o sorteio
    dos dados.
    :return: Lista com incógnita sorteada (1: rapidez; 2: deslocamento; 3: tempo), e os demais dados necessários a seu
    cálculo com as respectivas unidades de medida.
    """
    from random import randint as sti, uniform as stf
    if sujeito == 1:
        ir = (3, 30)  # intervalo de rapidez em km/h para pessoa
        idm = (10, 200)  # intervalo de deslocamento em m para pessoa
        idk = (1, 10)  # intervalo em km
    elif sujeito == 2:
        ir = (40, 120)   # intervalo de rapidez em km/h para veiculo
        idm = (10, 900)  # intervalo de deslocamento em m
        idk = (1, 400)  # intervalo em km
    dados = ConjDados
    incogs = ('rapidez', 'deslocamento', 'tempo')
    rapidunid = ('km/h', 'm/s')
    deslounid = ('km', 'm')
    tempounid = ('h', 'min', 's')

    # Definição da incógnita e sua unidade de medida (mas não valor!)
    dados.i = incogs[sti(0, 2)]
    if dados.i == incogs[0]:  # rapidez
        dados.ui = rapidunid[sti(0, 1)]
    elif dados.i == incogs[1]:  # deslocamento
        dados.ui = deslounid[sti(0, 1)]
    elif dados.i == incogs[2]:  # tempo
        dados.ui = tempounid[sti(0, 2)]

    # rapidez incógnita: d1=deslocamento | d2=tempo
    if dados.i == incogs[0]:
        dados.u1 = deslounid[sti(0, 1)]
        dados.u2 = tempounid[sti(0, 2)]
        if dados.u1 == deslounid[0] and dados.u2 == tempounid[0]:  # km e h
            dados.d1 = sti(idk[0], idk[1])
            dados.r = sti(ir[0], ir[1])
            dados.d2 = dados.d1 / dados.r
        elif dados.u1 == deslounid[0] and dados.u2 == tempounid[1]:  # km e min
            dados.d1 = sti(idk[0], idk[1])
            dados.r = sti(ir[0], ir[1])
            dados.d2 = dados.d1 / (dados.r/60)
        elif dados.u1 == deslounid[0] and dados.u2 == tempounid[2]:  # km e s
            dados.d1 = sti(idk[0], idk[1])
            dados.r = sti(ir[0], ir[1])
            dados.d2 = dados.d1 / (dados.r/3600)
        elif dados.u1 == deslounid[1] and dados.u2 == tempounid[0]:  # m e h
            dados.d1 = sti(idm[0], idm[1])
            dados.r = sti(ir[0], ir[1])
            dados.d2 = dados.d1 / (dados.r / 0.001)
        elif dados.u1 == deslounid[1] and dados.u2 == tempounid[1]:  # m e min
            dados.d1 = sti(idm[0], idm[1])
            dados.r = sti(ir[0], ir[1])
            dados.d2 = dados.d1 / (dados.r / (3/50))
        elif dados.u1 == deslounid[1] and dados.u2 == tempounid[2]:  # m e s
            dados.d1 = sti(idm[0], idm[1])
            dados.r = sti(ir[0], ir[1])
            dados.d2 = dados.d1 / (dados.r /3.6)
        if dados.ui == rapidunid[1]:
            dados.r = dados.r / 3.6

    # deslocamento incógnito: d1=rapidez | d2=tempo
    if dados.i == incogs[1]:  #PARAMOS AQUI!
        dados.u1 = rapidunid[sti(0, 1)]
        dados.u2 = tempounid[sti(0, 2)]
        if dados.ui == deslounid[0]:  # km
            dados.r = sti(idk[0], idk[1])
        elif dados.ui == deslounid[1]:  # m:
            dados.r = sti(idm[0], idm[1])

        if dados.u1 == rapidunid[0] and dados.u2 == tempounid[0]:  # km/h e h
            dados.d1 = sti(ir[0], ir[1])
            if dados.ui == deslounid[0]:  # km
                dados.r = sti(idk[0], idk[1])
                dados.d2 = dados.r / dados.d1
            elif dados.ui == deslounid[1]:  # m
                dados.r = sti(idm[0], idm[1])
                dados.d2 = dados.r / (dados.d1/0.001)
        elif dados.u1 == rapidunid[0] and dados.u2 == tempounid[1]:  # km/h e min
            dados.d1 = sti(ir[0], ir[1])
            if dados.ui == deslounid[0]:  # km
                dados.r = sti(idk[0], idk[1])  # km
                dados.d2 = dados.r / (dados.d1 / 60)
            elif dados.ui == deslounid[1]:  # m
                dados.r = sti(idm[0], idm[1])
                dados.d2 = dados.r / (dados.d1/(3/50))
        elif dados.u1 == rapidunid[0] and dados.u2 == tempounid[2]:  # km/h e s
            dados.d1 = sti(ir[0], ir[1])
            if dados.ui == deslounid[0]:  # km
                dados.r = sti(idk[0], idk[1])  # km
                dados.d2 = dados.r / (dados.d1 / 3600)
            elif dados.ui == deslounid[1]:  # m
                dados.r = sti(idm[0], idm[1])
                dados.d2 = dados.r / (dados.d1/3.6)
        elif dados.u1 == rapidunid[1] and dados.u2 == tempounid[0]:  # m/s e h
            dados.d1 = round((sti(ir[0], ir[1]))/3.6, 2)  # valor inteiro da conversão do sorteio para m/s
            if dados.ui == deslounid[0]:  # km
                dados.r = sti(idk[0], idk[1])  # km
                dados.d2 = dados.r / (dados.d1*3.6)
            elif dados.ui == deslounid[1]:  # m
                dados.r = sti(idm[0], idm[1])
                dados.d2 = dados.r / dados.d1
        elif dados.u1 == rapidunid[1] and dados.u2 == tempounid[1]:  # m/s e min
            dados.d1 = round((sti(ir[0], ir[1]))/3.6, 2)  # m/s
            if dados.ui == deslounid[0]:  # km
                dados.r = sti(idk[0], idk[1])  # km
                dados.d2 = dados.r / (dados.d1*0.06)  # m/s para km/min
            elif dados.ui == deslounid[1]:  # m
                dados.r = sti(idm[0], idm[1])
                dados.d2 = dados.r / (dados.d1*60)  # m/s para m/min
        elif dados.u1 == rapidunid[1] and dados.u2 == tempounid[2]:  # m/s e s
            dados.d1 = round((sti(ir[0], ir[1]))/3.6, 2)  # m/s
            if dados.ui == deslounid[0]:  # km
                dados.r = sti(idk[0], idk[1])  # km
                dados.d2 = dados.r / (dados.d1*0.001)  # m/s para km/s
            elif dados.ui == deslounid[1]:  # m
                dados.r = sti(idm[0], idm[1])
                dados.d2 = dados.r / (dados.d1)

    # tempo incógnito: d1=rapidez | d2=deslocamento
    if dados.i == incogs[2]:
        dados.u1 = rapidunid[sti(0, 1)]
        dados.u2 = deslounid[sti(0, 1)]
        if dados.u1 == rapidunid[0] and dados.u2 == deslounid[0]:  # km/h e km
            dados.d1 = sti(ir[0], ir[1])
            dados.d2 = sti(idk[0], idk[1])
            dados.r = dados.d2 / dados.d1  # padrão em h
            if dados.ui == tempounid[0]:  # h
                pass
            elif dados.ui == tempounid[1]:  # min
                dados.r = dados.r*60
            elif dados.ui == tempounid[2]:  # s
                dados.r = dados.r*3600
        elif dados.u1 == rapidunid[0] and dados.u2 == deslounid[1]:  # km/h e m
            dados.d1 = sti(ir[0], ir[1])
            dados.d2 = sti(idm[0], idm[1])
            dados.r = (dados.d2/1000) / dados.d1  # padrão em h
            if dados.ui == tempounid[0]:  # h
                pass
            elif dados.ui == tempounid[1]:  # min
                dados.r = dados.r*60
            elif dados.ui == tempounid[2]:  # s
                dados.r = dados.r*3600
        elif dados.u1 == rapidunid[1] and dados.u2 == deslounid[0]:  # m/s e km
            dados.d1 = sti(ir[0], ir[1])/3.6
            dados.d2 = sti(idk[0], idk[1])
            dados.r = dados.d2 / (dados.d1*3.6)  # padrão em h
            if dados.ui == tempounid[0]:  # h
                pass
            elif dados.ui == tempounid[1]:  # min
                dados.r = dados.r*60
            elif dados.ui == tempounid[2]:  # s
                dados.r = dados.r*3600
        elif dados.u1 == rapidunid[1] and dados.u2 == deslounid[1]:  # m/s e m
            dados.d1 = sti(ir[0], ir[1])/3.6
            dados.d2 = sti(idm[0], idm[1])
            dados.r = dados.d2 / dados.d1  # padrão em s
            if dados.ui == tempounid[0]:  # h
                dados.r = dados.r/3600
            elif dados.ui == tempounid[1]:  # min
                dados.r = dados.r/60
            elif dados.ui == tempounid[2]:  # s
                pass
    dados.d1 = round(dados.d1)
    if dados.d2 < 1:
        dados.d2 = round(dados.d2, 4)
    else:
        dados.d2 = round(dados.d2, 1)
    if dados.r < 1:
        dados.r = round(dados.r, 4)
    else:
        dados.r = round(dados.r, 1)
    return [dados.i, dados.ui, dados.d1, dados.u1, dados.d2, dados.u2, dados.r]


def cria_lista():
    while True:
        quantidade = int(input('Insira o número de exercícios desejados: '))
        if isinstance(quantidade, int) is True and quantidade > 0:
            break
        else:
            print(f'\033[31mInsira um valor numérico, inteiro e não nulo!\033[m')
            continue
    contador = 0
    with open('exerc_mru.txt', 'w') as arquivo:
        pass
    gabarito = [[], []]  # Índice 0 valor da resposta; índice 1, sua unidade.
    while True:
        contador += 1
        with open('exerc_mru.txt', 'a') as arquivo:
            exercicio = construtor()
            arquivo.write(str(contador) + ') ' + exercicio[0])
            gabarito[0].append(exercicio[1])  # Valor da resposta
            gabarito[1].append(exercicio[2])  # Unidade de medida da resposta.
        if contador == quantidade:
            break
    with open('exerc_mru.txt', 'a') as arquivo:
        for indice in range(0, len(gabarito[0])):
            arquivo.write(str(indice+1)+') ' + str(gabarito[0][indice]) + ' ' + str(gabarito[1][indice]) +
                          ('.' if indice == (len(gabarito[0]) - 1) else '; '))


cria_lista()
# a = construtor()
# print(a[2])

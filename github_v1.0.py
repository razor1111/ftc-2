import re


def validar_id(campo):
    try:
        teste = re.match(r'^[a-zA-Z][a-zA-Z\d]*$', campo)
        return teste
    except:
        return False


def validar_senha(campo):
    try:
        teste = re.match(r'^[a-fA-F\d]{2}\.[a-fA-F\d]{2}\.[a-fA-F\d]{2}\.[a-fA-F\d]{2}$', campo)
        return teste
    except:
        return False


def validar_ip(campo):
    try:
        teste = re.match(r'^\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}$', campo)
        return teste
    except:
        return False


def validar_email(campo):
    try:
        teste = re.match(r'^[a-zA-z][\w\.\-_]*@\w+\.([\w.]+)*$', campo)
        return teste
    except:
        return False


def validar_transacao(campo):
    try:
        teste = re.match(r'^[a-zA-Z]+$', campo)
        return teste
    except:
        return False


def validar_repositorio(campo):
    try:
        teste = re.match(r'^[a-z][a-z_]+$', campo)
        return teste
    except:
        return False


def validar_hash(campo):
    try:
        teste = re.match(r'^[a-f\d]{32}$', campo)
        return teste
    except:
        return False


def verificar_ip(campo):
    list_ip = []
    for simb in campo:
        if simb == '.':
            campo = campo.replace(simb, ' ')
    campo = campo.split()
    for simb in campo:
        num = int(simb)
        list_ip.append(num)

    for numero in list_ip:
        if numero < 0 or numero > 255:
            return False
    return True


def verificar_senha(campo):
    for simb in campo:
        if simb == '.':
            campo = campo.replace('.', '')

    verify = char_adjacente(campo)

    return verify


def char_adjacente(campo):
    point1_1 = re.search(r'^[A-Fa-f]$', campo[0])
    point1_2 = re.search(r'^[A-Fa-f]$', campo[1])

    point2_1 = re.search(r'^[A-Fa-f]$', campo[2])
    point2_2 = re.search(r'^[A-Fa-f]$', campo[3])

    point3_1 = re.search(r'^[A-Fa-f]$', campo[4])
    point3_2 = re.search(r'^[A-Fa-f]$', campo[5])

    point4_1 = re.search(r'^[A-Fa-f]$', campo[6])
    point4_2 = re.search(r'^[A-Fa-f]$', campo[7])

    if point1_1 and point1_2:
        return False
    elif point2_1 and point2_2:
        return False
    elif point3_1 and point3_2:
        return False
    elif point4_1 and point4_2:
        return False
    return True


def verificar_id(campo):
    lista = []
    cont_str = 0
    cont_int = 0
    for simb in campo:
        lista.append(simb)

    for simb in lista:
        string = re.search(r'^[a-zA-Z]', simb)
        inteiro = re.search(r'^[\d]', simb)
        if string:
            cont_str += 1
        if inteiro:
            cont_int += 1

    if cont_str >= cont_int:
        return True
    return False


def verificar_transacao(campo):
    permitidos = ['pull', 'push', 'stash', 'fork', 'pop']
    for transacao in permitidos:
        if campo == transacao:
            return True

    return False


try:
    entrada = str(input())

    campos = entrada.split()
    id_user = validar_id(campos[0])
    senha = validar_senha(campos[1])
    ip = validar_ip(campos[2])
    email = validar_email(campos[3])
    transacao = validar_transacao(campos[4])
    repositorio = validar_repositorio(campos[5])
    valor_hash = validar_hash(campos[6])

    ip_correto = verificar_ip(campos[2])
    senha_correta = verificar_senha(campos[1])
    id_correto = verificar_id(campos[0])
    transacao_correta = verificar_transacao(campos[4])

    if id_user and senha and ip and email and transacao and repositorio and valor_hash and ip_correto \
            and senha_correta and id_correto and transacao_correta:
        print(True)
    else:
        print(False)

except:
    print(False)


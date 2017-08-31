import re


def validar_id(campo):
    teste = re.match(r'^[a-zA-Z][a-zA-Z\d]*$', campo)
    return teste


def validar_senha(campo):
    teste = re.match(r'^[A-F\d]{2}\.[A-F\d]{2}\.[A-F\d]{2}\.[A-F\d]{2}$', campo)
    return teste


def validar_ip(campo):
    teste = re.match(r'^\d{3}\.\d{1,3}\.\d{1,3}\.\d{1,3}$', campo)
    return teste


def validar_email(campo):
    teste = re.match(r'^[a-zA-z.-_][\w.-_]+@\w+\.[\w.]+$', campo)
    return teste


def validar_transacao(campo):
    teste = re.match(r'^[pu[l]{2}|push|stash|fork|pop]+$', campo)
    return teste


def validar_repositorio(campo):
    teste = re.match(r'^[a-z_]+$', campo)
    return teste


def validar_hash(campo):
    teste = re.match(r'^[a-f\d]{32}$', campo)
    return teste


def verificar_ip(campo):
    list_ip = []
    for simb in campo:
        if simb == '.':
            campo = campo.replace(simb,' ')
    campo = campo.split()
    for simb in campo:
        num = int(simb)
        list_ip.append(num)
        if num < 0 or num > 255:
            return False

    return True

try:
    idUser = False
    senha = False
    ip = False
    email = False
    transacao = False
    repositorio = False
    valor_hash = False

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


    if id_user and senha and ip and email and transacao and repositorio and valor_hash and ip_correto:
        print(True)
    else:
        print(False)

except:
    print(False)

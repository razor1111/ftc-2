import re

def validar_senha(campo):
    teste = False
    teste = re.search(r'^[A-F\d]{2}\.[A-F\d]{2}\.[A-F\d]{2}\.[A-F\d]{2}',campo)
    return teste
def validar_email(campo):
    teste = False
    teste = re.search(r'^[a-zA-z\.-_][\w\.-_]+@\w+\.[\w\.]+',campo)
    return teste
def validar_transacao(campo):
    teste = False
    teste = re.search(r'[pull|push|stash|fork|pop]+',campo)
    return teste
def validar_ip(campo):
    teste = False
    teste = re.search(r'\d{3}\.\d{1,3}\.\d{1,3}\.\d{1,3}',campo)
    return teste
def validar_id(campo):
    teste = False
    teste = re.search(r'[a-zA-Z][a-zA-Z\d]*',campo)
    return teste
def validar_repositorio(campo):
    teste = False
    teste = re.search(r'[a-z\_]+',campo)
    return teste

try:
    idUser = False
    senha = False
    ip = False
    email = False
    transacao = False
    repositorio = False

    entrada = str(input())

    campos = entrada.split()
    idUser = validar_id(campos[0])
    senha = validar_senha(campos[1])
    ip = validar_ip(campos[2])
    email = validar_email(campos[3])
    transacao = validar_transacao(campos[4])
    repositorio = validar_repositorio(campos[5])

    print(idUser)
    print(senha)
    print(ip)
    print(email)
    print(transacao)
    print(repositorio)

    if idUser and senha and ip and email and transacao and repositorio:
        print(True)
    else:
        print(False)

except:
    print(False)


    #Elloa 03.A5.2B.F8 192.168.11.0 ebgcosta@uea.edu.br push projeto_ftc
    #03.A5.2B.F8 266.168.11.0 ebgcosta@uea.edu.br push
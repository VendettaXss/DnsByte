#!/usr/bin/python3
import os
import socket

print('\033[35m'" ____  _  _  ___  ____  _  _  ____  ___")
print("(  _ \( \( )/ __)(  _ \( \/ )(_  _)( ___)")
print(" )(_) ))  ( \__ \ ) _ < \  /   )(   )__) ")
print("(____/(_)\_)(___/(____/ (__)  (__) (____)")
print(" By:Vendetta.xs")
      
print('\033[33m'"0.1v")

def verificar_dns(site):
    try:
        ip = socket.gethostbyname(site)
        return ip
    except socket.gaierror:
        return '\033[31m'"DNS nao encontrado"

def main():

    while True:
        site = input('\033[34m'"Digite o site (ou 'sair' para sair)
        if site.lower() == 'sair':
            break
        resultado = verificar_dns(site)
        print('\033[32m'f'O DNS de {site} {resultado}')

if __name__ == "__main__":
    main()

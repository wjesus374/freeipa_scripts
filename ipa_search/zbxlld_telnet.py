#!/usr/bin/python 

import telnetlib
import re
import json
import argparse

#Informacoes adicionais para enviar via telnet
adicional_info = {'port': 6666, 'send': 'PING\n', 'reply': '(PONG)'}
#Realizar o telnet somente com os hosts que tenham no nome a palavra pad.
#Possivel colocar mais de um nome utilizando o pipe. Ex. 'pad|radius|teste'
re_match = 'pad'

def telnet_def(hostlist):
    #Dict para retorno de dados
    result = {}
    result['data'] = []

    for info in hostlist:
        #print(info['host'])
        try:
            tn = telnetlib.Telnet(info['host'],int(info['port']),1)
            tn.write(info['send'])
            reply = tn.read_all()

            if re.search(info['reply'],reply):
                #print('OK')
                result['data'].append({'host': info['host'], 'status' : 'OK'})
            else:
                #print('No data')
                result['data'].append({'host': info['host'], 'status' : 'KO'})
        except Exception as e:
            #print("Erro: %s" %e)
            result['data'].append({'host': info['host'], 'status' : str(e)})

    return result

def discovery_def():
    #Lista para fazer o telnet
    data = []
    hosts = readconf('hostlist.json')
    
    for host in hosts:
        stat = {}
        if re.search(re_match,host):
            #print(host)
            stat = adicional_info.copy()
            stat['host'] = host
            data.append(stat)
            
            
    #print(data)
    result = telnet_def(data)
    print(json.dumps(result))

def read_def():
    print('Read')

def readconf(configfile):
    with open(configfile, "r") as jsonfile:
        data = json.load(jsonfile)

    return data

#Mapa de valores:
fmap = { 'discovery': discovery_def, 'read': read_def }

if __name__ == "__main__":
    parser = argparse.ArgumentParser(prog='Host Monitor')
    parser.add_argument('commands', choices=fmap.keys())
    #, help='Gerar JSON LLD para Zabbix')
    #parser.add_argument('read', choices=fmap.keys(), help='Ler os dados gravados e retornar status do host')
    args = parser.parse_args()
    func = fmap[args.commands]
    func()


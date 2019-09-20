#!/usr/bin/python3

import ipahttp
import json
import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

#Lista com todos os hosts
hostlist = []

ipaserver='ipa-server'
user='usuario'
password='123456'
jsonfile='hostlist.json'

def writeconf(configfile,data):
    with open(configfile,"w") as outfile:
        json.dump(data, outfile, ensure_ascii=False)

if __name__ == "__main__":
    ipa = ipahttp.ipa(ipaserver)
    ipa.login(user,password)
    reply = ipa.host_find()
    for host in reply['result']['result']:
        #print(host)
        #print('Found host %s' % host['fqdn'][0])
        hostlist.append(host['fqdn'][0])

    #print(hostlist)
    writeconf(jsonfile,hostlist)

# Script's para FreeIPA

Na pasta *ipa_export*, tem script's em BASH para exportar e importar valores do FreeIPA localmente:

* ipa_export.sh - Exporta todas (ou quase todas) as configurações do IPA
* hosts_import.sh - Importa todos os hosts exportados do script *ipa_export.sh*
* users_import.sh - Importa todos os usuários exportados do script *ipa_export.sh*

Na pasta *ipa_search*, tem script's em Python para:

* ipa_host_search.py - Gerar uma lista com todos os host's do seu FreeIPA
* zbxlld_telnet.py - Realizar o teste de telnet e aguardar uma resposta
  * Por padrão ele envia um PING e aguarda um PONG do host
* ipahttp.py - O mesmo que está no GIT << https://github.com/nordnet/python-freeipa-json >>

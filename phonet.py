# -*- coding: utf-8 -*-
import sys
import time
import os
import requests
import phonenumbers
from phonenumbers import carrier, geocoder
from colorama import init, Fore, Style

init(autoreset=True)

C_YELLOW = Fore.YELLOW
C_GRAY = Fore.LIGHTBLACK_EX
C_WHITE = Fore.WHITE
C_RESET = Style.RESET_ALL

# ⚠️ COLOQUE SEU TOKEN DA API ENTRE AS ASPAS ABAIXO:
API_KEY = "COLE_SEU_TOKEN_AQUI"

BANNER_ART = f"""{C_YELLOW}
8888888b.  888    888  .d88888b.  888b    888 8888888888    88888888888 8888888b.         d8888 8888888b.
888   Y88b 888    888 d88P" "Y88b 8888b   888 888               888     888   Y88b       d88888 888   Y88b
888    888 888    888 888     888 88888b  888 888               888     888    888      d88P888 888    888
888   d88P 8888888888 888     888 888Y88b 888 8888888           888     888   d88P     d88P 888 888   d88P
8888888P"  888    888 888     888 888 Y88b888 888               888     8888888P"     d88P  888 8888888P"
888        888    888 888     888 888  Y88888 888      888888   888     888 T88b     d88P   888 888
888        888    888 Y88b. .d88P 888   Y8888 888               888     888  T88b   d8888888888 888
888        888    888  "Y88888P"  888    Y888 8888888888        888     888   T88b d88P     888 888

V.1.0 © copyright mrmaestrox.
                                                         ..::::..
                                              :+#%%%%%#*+======+*#%%%%%#+:
                                        .=#%%#*:                       -+*#%%#=.
                                    -+%#*=-::===.      ........       -==-:===*#%%+-
                                .+##*=-----:::-==-=++++++++++++++++=-===:.:===++++*#%#+.
                              +%%+-----------::-===+++++++++++++++++===...:===++++++++*%%+
                           :#%*==-------------::-==++++++++++++++++===:....::-=++++++++++#%#:
                         =#*:  :===-----------::-==++++++++++++++++==-....:-====+++++++++++*%%
                       =%+.      -==---------::===-++++++++++++++++--=-....:-====++++++++++++*#%=
                     -%*           -===------==-:-=++++++++++++++++=::-=-:...-=====++++++++++=. *%-
                   .*#.              :======-:::-+++++++++++++++++++=::::-==========+++++++=.    .#*.
                  -#=                .::::::::-=+++++++++++++++++++++=-:::::::::--==-:-==:         =#-
                 +#:                 .::::::-========++++++++++++=======-::::::::..::-:.            :#+
                ##.                  :::--===============================-:::::::.                   .##
              .%#                   .-====================================-:::::::                     #%.
             .#*                    .-=====================================-::::::                      *#.
            .**                     :=========-:..:-==============-:...:-===--::::                       **.
            +#.                     :======-:.       :==========-.       .-====--:                       .#+
           -%-                      :======:.         :========-          .-=====-.                       -%-
          .*+.                      .-====-:.         .========-         ..-=====-                        .+*.
          -%-                       .-=====-:.       .-=========:       ..:-=======+==-.                   -%-
          +*.                        :-=====-:......:-===--=+++==-:.....:-=======+++++++=                  .*+
         .#=                          :============++++-=+++=-+++++==================+++=                   =#.
         :%-                          .-=========+++++=:==++++-=+++++=========--========.                   -%:
         -#:              .::::::.     ::-======++++=:..-==++++-.=++=========-:-=======-...:-.              :#-
         =#:           --=======+====: .:::-======+++-..-==+++++:=========-::::-=======-....-=-             :#=
         =#:        :-======+++++=======-::..:=========:-===++++-=======-:..::-========:....:-=+.           :#=
         -#:      .-======++++++==========-:...-=======:====+++--=====-:...:::--======-.....:-=++-          :#
         :%-     -======++++++++===========-:....:--===:::----:-===--:....:::.-======-:.....-=++++=.        -%:
         .#=    -====-===++++++=============-:.........:====+++:.........:::..-=====-.....:-=++++++=.       =#.
          +*.  :-:::::::::::::-=============-:::.......:====+++:.......:::...:-===-.....:-==++++++++=.     .*+
          -%-   :::...........::::--=========:::::.....:====+++:....::::....:-====-::-==-=+++++++++++=     -%-
          .*+.    ................:::---=====:...:::::.:====+++:::::::......:--====---::::=+++++++++++=-. .+*.
           -%-    ......-==+++++++==--:::--=-:.......::.-==+++=.:::........::::-===-:::::::-=+++++++++::=.-%-
            +#.   ..:=+++++++++++++=====--::::::.......--::::--=++++=:::::::::::-===-::::::::-+++++++-...:#+
            .**   -==+++++++++++++++======--::::::...::-==-:-=+++++++=-=+++=:::::-==-::::::::::-+++=:....#*.
             .#*.-===++++++++++++++++=======-::::::.:-:---=--=+++++++++-++++-:::::-=-  .:::::::::-:.....*#.
              .%#====++++++++++++++++========-::::..:-:=+++=-==++++++==-:+++=::::::--.  ::.............#%.
                #%===++++++++++++++++========-:::...--:-=--::----------:.-==-::::::-=:  :::::........:##
                 +%+=+++++++++++++++++========-::...-=-:::::::-++++++++++=-:::::::::-:  ::::::::::-=+%+
                  -%*+++++++++++++++++=========:....-=-::-+++=:++++++++++=::::::::::--  .::::::::-+#%
                   .*%*++++++++++++++++========-....=+-:=+++=-:-=========-:--:::::::--. .::::::::=%*.
                     -%%+++++++++++++++========-...:=+-::::::::-----------.--::::::::-. .::::::-#%-
                       =%#*++++++++++++=========:..:=+=::::::::=++++++++++=-:::::::::-:  ::::-*%=
                         =%#*++++++++++=========:..:=++-::-=++-:++++++++++=::::::::::-:  ::=##=
                           :#%#++++++++=========-..:=++=::-==--:-=========-::::::::::--  =%#:
                              +%%*+++++=========-..:=+++=-::::::-=======-----::::::::-+#%+
                                .+#%#+===========..:=+++++=-::::::::::-------:::::-+##+.
                                    -+%#*=--=====..:=+++++++-:----:::-====+=::=*#%+-
                                        .=#%%#*+=..:=+++++++=-:-:::::::-+*%%%#=.
                                              :+#%%%%%%####*****##%%%%%#+:
                                                        ..::::..

{C_RESET}"""

# Dicionário de contingência para garantir localização por DDD se a API falhar
DDD_MAP = {
    '11': 'Sao Paulo (Capital/Metropolitana), Brasil', '12': 'Sao Jose dos Campos/Vale do Paraiba, Brasil',
    '13': 'Santos/Baixada Santista, Brasil', '14': 'Bauru/Marilia, Brasil', '15': 'Sorocaba/Itapetininga, Brasil',
    '16': 'Ribeirao Preto/Franca, Brasil', '17': 'Sao Jose do Rio Preto, Brasil', '18': 'Presidente Prudente/Aracatuba, Brasil',
    '19': 'Campinas/Piracicaba, Brasil', '21': 'Rio de Janeiro (Capital/Metropolitana), Brasil', '22': 'Campos dos Goytacazes/Maceio, Brasil',
    '24': 'Petropolis/Volta Redonda, Brasil', '27': 'Vitoria/Vila Velha (Espirito Santo), Brasil', '28': 'Cachoeiro de Itapemirim, Brasil',
    '31': 'Belo Horizonte (Metropolitana), Brasil', '32': 'Juiz de Fora/Barbacena, Brasil', '33': 'Governador Valadares/Teofilo Otoni, Brasil',
    '34': 'Uberlandia/Uberaba (Triangulo Mineiro), Brasil', '35': 'Pouso Alegre/Poços de Caldas, Brasil', '37': 'Divinopolis/Bom Despacho, Brasil',
    '38': 'Montes Claros/Diamantina, Brasil', '41': 'Curitiba (Metropolitana), Brasil', '42': 'Ponta Grossa/Guarapuava, Brasil',
    '43': 'Londrina/Apucarana, Brasil', '44': 'Maringa/Campo Mourao, Brasil', '45': 'Cascavel/Foz do Iguacu, Brasil',
    '46': 'Francisco Beltrao/Pato Branco, Brasil', '47': 'Joinville/Blumenau/Balneario Camboriu, Brasil', '48': 'Florianopolis (Metropolitana), Brasil',
    '49': 'Chapeco/Lages, Brasil', '51': 'Porto Alegre (Metropolitana), Brasil', '53': 'Pelotas/Rio Grande, Brasil',
    '54': 'Caxias do Sul/Passo Fundo, Brasil', '55': 'Santa Maria/Uruguaiana, Brasil', '61': 'Brasilia/Distrito Federal, Brasil',
    '62': 'Goiania (Metropolitana), Brasil', '63': 'Tocantins (Estado Completo), Brasil', '64': 'Rio Verde/Itumbiara, Brasil',
    '65': 'Cuiaba (Metropolitana), Brasil', '66': 'Rondonopolis/Sinop, Brasil', '67': 'Mato Grosso do Sul (Estado Completo), Brasil',
    '68': 'Acre (Estado Completo), Brasil', '69': 'Rondonia (Estado Completo), Brasil', '71': 'Salvador (Metropolitana), Brasil',
    '73': 'Ilheus/Itabuna/Porto Seguro, Brasil', '74': 'Juazeiro/Jacobina, Brasil', '75': 'Feira de Santana/Alagoinhas, Brasil',
    '77': 'Vitoria da Conquista/Barreiras, Brasil', '79': 'Sergipe (Estado Completo), Brasil', '81': 'Recife (Metropolitana), Brasil',
    '82': 'Alagoas (Estado Completo), Brasil', '83': 'Paraiba (Estado Completo), Brasil', '84': 'Rio Grande do Norte (Estado Completo), Brasil',
    '85': 'Fortaleza (Metropolitana), Brasil', '86': 'Teresina/Parnaiba, Brasil', '87': 'Petrolina/Garanhuns, Brasil',
    '88': 'Juazeiro do Norte/Sobral, Brasil', '89': 'Picos/Floriano, Brasil', '91': 'Belem (Metropolitana), Brasil',
    '92': 'Manaus (Metropolitana), Brasil', '93': 'Santarem/Altamira, Brasil', '94': 'Maraba/Parauapebas, Brasil',
    '95': 'Roraima (Estado Completo), Brasil', '96': 'Amapa (Estado Completo), Brasil', '97': 'Amazonas (Interior), Brasil',
    '98': 'Sao Luis (Metropolitana), Brasil', '99': 'Imperatriz/Caxias (Maranhao), Brasil'
}

def clear_terminal():
    os.system('clear' if os.name == 'posix' else 'cls')

def loading_bar():
    print(f"\n{C_GRAY}Initializing system modules...{C_RESET}")
    slots = ["█" * i + "░" * (20 - i) for i in range(1, 21)]
    for slot in slots:
        sys.stdout.write(f"\r{C_YELLOW}[{slot}] Loading PHONE-TRAP...")
        sys.stdout.flush()
        time.sleep(0.05)
    print(f"\n\n{Fore.GREEN}▶ Setup Complete.{C_RESET}\n")
    time.sleep(0.5)

def print_menu():
    print(f"{C_GRAY}┌────────────────────────────────────────────────────────┐")
    print(f" │  SELECT AN OPTION                      │")
    print(f" └────────────────────────────────────────────────────────┘")
    print(f"  [1] ── NUMBER")
    print(f"  [2] ── EXIT")
    print(f" ──────────────────────────────────────────────────────────")
    print(f" ❯ Enter your option: {C_RESET}", end='')

def get_phone_info(raw_number):
    try:
        raw_number = raw_number.replace(" ", "").replace("-", "").replace("(", "").replace(")", "")
        if raw_number.startswith('0') and not raw_number.startswith('+'):
            raw_number = raw_number[1:]
        if not raw_number.startswith('+'):
            if len(raw_number) in [10, 11]:
                raw_number = '+55' + raw_number
            else:
                return {"error": "Formato invalido. Use o padrao com DDD (Ex: 11999999999)"}

        # Extração local de segurança
        parsed = phonenumbers.parse(raw_number, None)
        cc = str(parsed.country_code)
        national = phonenumbers.format_number(parsed, phonenumbers.PhoneNumberFormat.NATIONAL)
        
        nsn = str(parsed.national_number)
        ddd = nsn[:2] if cc == "55" else nsn[:3] 

        # Atribui localização estática padrão baseada no DDD para nunca vir vazio
        location_name = DDD_MAP.get(ddd, "Brasil (Regiao nao mapeada)") if cc == "55" else "International Registry"
        orig_operator = carrier.name_for_number(parsed, 'en')
        current_operator = orig_operator if orig_operator else "Carrier Database Restricted"
        valid_status = "Local Database Resolution (No API Key)"

        # Consulta externa via API HTTP Requests (Se houver chave ativa)
        if API_KEY and "COLE_SEU" not in API_KEY:
            try:
                url = f"https://api.numlookupapi.com/v1/validate/{raw_number}?apikey={API_KEY}"
                response = requests.get(url, timeout=5)
                if response.status_code == 200:
                    data = response.json()
                    if data.get('valid') == False:
                        return {"error": "A API informou que este numero nao existe na rede."}
                    
                    if data.get('carrier'): 
                        current_operator = data.get('carrier')
                    if data.get('location'): 
                        location_name = data.get('location')
                    valid_status = "Active / Global Carrier Verified"
                else:
                    valid_status = f"API Error ({response.status_code}) - Fallback Active"
            except Exception:
                valid_status = "API Timeout - Local Fallback Active"

        maps_query = f"{location_name}".replace(" ", "+")
        maps_link = f"https://www.google.com/maps/search/?api=1&query={maps_query}"

        return {
            "original_operator": orig_operator if orig_operator else "Base Telecom Network",
            "current_operator": current_operator,
            "country_code": f"+{cc}",
            "area_code": ddd,
            "national_format": national,
            "status": valid_status,
            "location": location_name,
            "maps_link": maps_link
        }
    except Exception as e:
        return {"error": f"Erro na analise: {str(e)}"}

def display_results(info):
    if "error" in info:
        print(f"\n{Fore.RED}[!] {info['error']}\n")
        return
    print(f"\n{C_GRAY}┌── [ RESULTS  ] ────────────────────────────────────────")
    print(f" │   Network Status    : {C_YELLOW}{info['status']}")
    print(f" │   Original Operator : {C_WHITE}{info['original_operator']}")
    print(f" │   Current Carrier   : {C_WHITE}{info['current_operator']}")
    print(f" │   Country Code (CC) : {C_WHITE}{info['country_code']}")
    print(f" │   Area Code (DDD)   : {C_WHITE}{info['area_code']}")
    print(f" │   National Format   : {C_WHITE}{info['national_format']}")
    print(f" │   Location Region   : {C_WHITE}{info['location']}")
    print(f" │   Google Maps link  : {C_YELLOW}{info['maps_link']}")
    print(f"{C_GRAY} └───────────────────────────────────────────────────────────\n")

def main():
    clear_terminal()
    print(f"{C_WHITE}┌────────────────────────────────────────────────────────┐")
    print(f" │ WELCOME TO PHONE-TRAP                                  │")
    print(f" ├────────────────────────────────────────────────────────┤")
    print(f"   The tool is intended for educational and neutral use;\n   its use is the user's responsibility.")
    print(f"   Are you responsible for the use of the tool?\n")
    print(f"       [ Y ]      [ N ]")
    print(f" └────────────────────────────────────────────────────────┘")
    
    while True:
        choice = input(f"{C_GRAY}❯ {C_WHITE}").strip().upper()
        if choice == 'Y':
            loading_bar()
            break
        elif choice == 'N':
            print(f"{Fore.RED}[!] Execution aborted.")
            sys.exit(0)
        else:
            print(f"{Fore.RED}Type Y or N.{C_RESET}")

    while True:
        clear_terminal()
        print(BANNER_ART)
        print_menu()
        option = input().strip()
        if option == '2':
            sys.exit(0)
        elif option == '1':
            print(f"\n{C_GRAY}── TARGET ACQUISITION ─────────────────────────────────────{C_RESET}")
            phone_target = input(f" ❯ Enter Target Phone Number: {C_WHITE}").strip()
            print(f"{C_GRAY} Querying global telecom databases...{C_RESET}")
            results = get_phone_info(phone_target)
            display_results(results)
            input(f"{C_GRAY}Press Enter to return to menu...{C_RESET}")
        else:
            time.sleep(1)

if __name__ == "__main__":
    main()

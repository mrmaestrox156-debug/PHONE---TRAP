PHONE-TRAP
Minimalist telecom intelligence and dynamic OSINT routing tool for terminal environments.

![PHONE-TRAP Interface](https://i.postimg.cc/cHyXnPMy/Novo-projeto-0AFD310.png)

FEATURES
- Preliminary automated string sanitation for space, hyphen, and country-code variations.
- External telecom network database integration via global HTTP API checking.
- Automated local fallback logic mapping local area codes (DDD) to prevent missing data vectors.

REQUIREMENTS
The tool requires Python 3 and basic system compilation packages to handle SSL and network structures correctly.

TERMUX CONFIGURATION
Execute the commands sequentially in the Termux prompt:

pkg update -y
pkg upgrade -y
pkg install python -y
pkg install git -y
pip install requests colorama phonenumbers
git clone https://github.com/mrmaestrox156-debug/PHONE---TRAP.git
cd PHONE---TRAP
python phonet.py

KALI LINUX CONFIGURATION
Execute the commands sequentially in the Kali Linux terminal:

sudo apt update -y
sudo apt install python3 python3-pip git -y
pip3 install requests colorama phonenumbers --break-system-packages
git clone https://github.com/mrmaestrox156-debug/PHONE---TRAP.git
cd PHONE---TRAP
python3 phonet.py

CREDENTIALS ASSIGNMENT
To initiate deep network checking, open phonet.py in your system text editor and append your API credential string directly inside the API_KEY parameter variable on line 19.

INTERFACE PROFILE
The framework displays processed telemetry inside low-contrast ANSI bordered frames designed to preserve diagnostic data clarity.

DEVELOPED BY MRMAESTROX — NEUTRAL USE OSINT FRAMEWORK

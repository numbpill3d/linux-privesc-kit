#!/usr/bin/env python3
"""linpeas-parser.py — surface HIGH-signal lines. Usage: python3 linpeas-parser.py linpeas.txt"""
import sys, re
HIGH=[r'\[91m',r'CVE-',r'SUID',r'sudo.*NOPASSWD',r'cap_',r'writable',r'/docker\.sock',r'password']
MED=[r'cron',r'sudo',r'docker',r'nfs']
with open(sys.argv[1], errors='ignore') as f:
    lines=f.readlines()
print(f"total: {len(lines)}")
for l in lines:
    import re
    if any(re.search(p,l,re.I) for p in HIGH):
        print(l.rstrip())
print("Full guide: https://numbpilled.gumroad.com/")

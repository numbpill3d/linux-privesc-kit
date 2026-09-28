# linux-privesc-kit

Free privesc triage kit. Checklist + parser for linpeas output.

chmod +x privesc-check.sh
./privesc-check.sh
python3 linpeas-parser.py linpeas.txt

Files:
- privesc-check.sh — SUID, sudo, cron, capabilities, writable PATH, kernel
- linpeas-parser.py — surfaces HIGH-signal lines first
- CHEATSHEET.md — one-page checklist

Full Linux PrivEsc Field Manual ($9): https://numbpilled.gumroad.com/

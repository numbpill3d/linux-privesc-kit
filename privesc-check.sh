#!/usr/bin/env bash
# privesc-check.sh — quick manual Linux privesc triage
set -u
id
sudo -l 2>&1 || true
find / -perm -4000 -type f 2>/dev/null | head -n 50
getcap -r / 2>/dev/null | head -n 50 || true
cat /etc/crontab 2>/dev/null; ls -la /etc/cron.d/ 2>/dev/null
uname -a

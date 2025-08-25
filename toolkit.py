#!/usr/bin/env python3
# Termux Ethical Hacking Toolkit Pro++ (Full Edition)
# Educational & Authorized use only.

import os, shutil, sys, time
from datetime import datetime

# ---------- Colors ----------
RESET   = "\033[0m"
BOLD    = "\033[1m"
GREEN   = "\033[92m"
CYAN    = "\033[96m"
YELLOW  = "\033[93m"
RED     = "\033[91m"
MAGENTA = "\033[95m"

# ---------- UI helpers ----------
def clear():
    os.system("clear" if os.name != "nt" else "cls")

def banner():
    clear()
    print(f"""{BOLD}{MAGENTA}
 ████████╗███████╗██████╗ ███╗   ███╗██╗   ██╗██╗  ██╗
 ╚══██╔══╝██╔════╝██╔══██╗████╗ ████║██║   ██║██║ ██╔╝
    ██║   █████╗  ██████╔╝██╔████╔██║██║   ██║█████╔╝
    ██║   ██╔══╝  ██╔══██╗██║╚██╔╝██║██║   ██║██╔═██╗
    ██║   ███████╗██║  ██║██║ ╚═╝ ██║╚██████╔╝██║  ██╗
    ╚═╝   ╚══════╝╚═╝  ╚═╝╚═╝     ╚═╝ ╚═════╝ ╚═╝  ╚═╝
{RESET}{CYAN}Termux Ethical Security Toolkit Pro++{RESET}
{YELLOW}Use only on systems you own or have permission to test.{RESET}
""")

def loading_screen():
    clear()
    msg = f"{CYAN}{BOLD}Welcome, seeker... You have entered my domain...{RESET}\n"
    for c in msg:
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(0.03)
    print(f"{MAGENTA}Powered by: T3RROR REBORN ⚡{RESET}\n")
    time.sleep(0.5)
    for i in range(0, 101, 10):
        sys.stdout.write(f"\r{YELLOW}Loading Categories: {i}%{RESET}")
        sys.stdout.flush()
        time.sleep(0.15)
    print("\n")

def pause(msg="Press ENTER to continue..."):
    input(f"\n{BOLD}{msg}{RESET}")

def info(msg): print(f"{CYAN}[i]{RESET} {msg}")
def ok(msg): print(f"{GREEN}[✓]{RESET} {msg}")
def warn(msg): print(f"{RED}[!]{RESET} {msg}")

def run(cmd, save_report=False, tool_name=""):
    if save_report:
        os.makedirs("reports", exist_ok=True)
        ts = datetime.now().strftime("%Y%m%d-%H%M%S")
        fname = f"reports/{tool_name}_{ts}.txt"
        os.system(f"{cmd} | tee {fname}")
        ok(f"Output saved in {fname}")
    else:
        os.system(cmd)

def is_installed(bin_name):
    return shutil.which(bin_name) is not None

# ---------- Categories & Tools ----------
CATEGORIES = {
    "1": { "name": "Recon & Scanning", "tools": {
        "1": {"bin":"nmap","name":"Nmap","desc":"Network scanner.","install":["pkg install -y nmap"],"launch":"nmap scanme.nmap.org","tutorial":"Use Nmap to scan hosts and ports."},
        "2": {"bin":"whois","name":"Whois","desc":"Domain lookup.","install":["pkg install -y whois"],"launch":"whois example.com","tutorial":"Shows domain registration info."},
        "3": {"bin":"dig","name":"DNS utils","desc":"DNS queries.","install":["pkg install -y dnsutils"],"launch":"dig example.com","tutorial":"DNS lookups with dig/nslookup."},
        "4": {"bin":"theHarvester","name":"theHarvester","desc":"Email & subdomain gathering.","install":["pip install theHarvester"],"launch":"theHarvester -d example.com -b google","tutorial":"Collect emails, subdomains, usernames."},
        "5": {"bin":"whatweb","name":"WhatWeb","desc":"Website fingerprinting.","install":["pkg install -y whatweb"],"launch":"whatweb example.com","tutorial":"Identifies web technologies."},
    }},
    "2": { "name": "Web Vulnerability Scanners", "tools": {
        "1": {"bin":"nikto","name":"Nikto","desc":"Web server scanner.","install":["pkg install -y nikto"],"launch":"nikto -h http://example.com","tutorial":"Scans for misconfigurations & vulnerabilities."},
        "2": {"bin":"wapiti","name":"Wapiti","desc":"Web app vuln scanner.","install":["pkg install -y wapiti"],"launch":"wapiti http://example.com","tutorial":"Checks for SQLi, XSS, etc."},
        "3": {"bin":"sqlmap.py","name":"SQLmap","desc":"Automated SQL injection testing.","install":["pip install git+https://github.com/sqlmapproject/sqlmap.git"],"launch":"sqlmap -u 'http://site.com/index.php?id=1' --dbs","tutorial":"Automates SQLi detection."},
    }},
    "3": { "name": "Password Attacks", "tools": {
        "1": {"bin":"hydra","name":"Hydra","desc":"Brute force logins.","install":["pkg install -y hydra"],"launch":"hydra -l admin -P rockyou.txt ftp://127.0.0.1","tutorial":"Password guessing tool."},
        "2": {"bin":"john","name":"John the Ripper","desc":"Hash cracker.","install":["pkg install -y john"],"launch":"john --wordlist=rockyou.txt hashes.txt","tutorial":"Cracks password hashes."},
        "3": {"bin":"crunch","name":"Crunch","desc":"Wordlist generator.","install":["pkg install -y crunch"],"launch":"crunch 8 8 abc123 -o wordlist.txt","tutorial":"Generates wordlists."},
    }},
    "4": { "name": "Wireless Cracking", "tools": {
        "1": {"bin":"aircrack-ng","name":"Aircrack-ng","desc":"WiFi cracking suite.","install":["pkg install -y aircrack-ng"],"launch":"aircrack-ng capture.cap","tutorial":"Cracks WEP/WPA keys."},
        "2": {"bin":"bettercap","name":"Bettercap","desc":"Network MITM framework.","install":["pkg install -y bettercap"],"launch":"bettercap -iface wlan0","tutorial":"Sniffing & MITM attacks."},
        "3": {"bin":"mdk4","name":"MDK4","desc":"WiFi DoS attacks.","install":["pkg install -y mdk4"],"launch":"mdk4 wlan0 d","tutorial":"Performs stress tests on WiFi."},
    }},
    "5": { "name": "Social Engineering & Phishing", "tools": {
        "1": {"bin":"zphisher.sh","name":"Zphisher","desc":"Automated phishing.","install":["git clone https://github.com/htr-tech/zphisher.git"],"launch":"cd zphisher && bash zphisher.sh","tutorial":"Creates fake login pages."},
        "2": {"bin":"sherlock","name":"Sherlock","desc":"Find usernames.","install":["git clone https://github.com/sherlock-project/sherlock.git","cd sherlock && pip install -r requirements.txt"],"launch":"python3 sherlock/sherlock.py username","tutorial":"Checks username availability."},
    }},
    "6": { "name": "Learning Resources", "tools": {
        "1": {"name":"Linux Basics","bin": None,"install": None,"desc":"Learn Linux essentials","launch": None,"tutorial":"Free resources: https://linuxjourney.com, https://overthewire.org (Bandit)"},
        "2": {"name":"Networking 101","bin": None,"install": None,"desc":"TCP/IP, ports, protocols","launch": None,"tutorial":"Free resources: https://www.geeksforgeeks.org/computer-network-tutorials/, https://hackthebox.com"},
        "3": {"name":"Python for Hackers","bin": None,"install": None,"desc":"Python scripting","launch": None,"tutorial":"Free resources: https://automatetheboringstuff.com, https://www.learnpython.org/"},
        "4": {"name":"Ethical Hacking Mindset","bin": None,"install": None,"desc":"Legal & ethical hacking","launch": None,"tutorial":"Free resources: https://www.hacker101.com, https://portswigger.net/web-security"},
    }},
}

# ---------- Tool Handling ----------
def install_tool(tool):
    if tool["bin"] and not is_installed(tool["bin"]):
        info(f"Installing {tool['name']}…")
        for cmd in tool["install"]:
            os.system(cmd)
        if is_installed(tool["bin"]):
            ok(f"{tool['name']} installed.")
            return True
        else:
            warn(f"{tool['name']} installation failed.")
            return False
    else:
        ok(f"{tool['name']} already installed or not required.")
        return True

def tool_menu(cat_key):
    cat = CATEGORIES[cat_key]
    while True:
        banner()
        print(f"{BOLD}{MAGENTA}{cat['name']}{RESET}\n")
        for k, t in cat["tools"].items():
            print(f"[{k}] {GREEN}{t['name']}{RESET} — {t['desc']}")
        if cat_key != "6":
            print(f"[A] {YELLOW}Install All Tools in this Category{RESET}")
        print("[0] Back")

        choice = input("\nSelect a tool: ").strip().lower()
        if choice == "0": return
        elif choice == "a" and cat_key != "6":
            for t in cat["tools"].values(): install_tool(t)
            pause()
            continue
        elif choice in cat["tools"]:
            t = cat["tools"][choice]
            banner()
            print(f"{BOLD}{t['name']}{RESET}\n{t['desc']}\n")
            print(f"{CYAN}Resources / Tutorial:{RESET} {t['tutorial']}\n")
            if t["bin"] and cat_key != "6":
                if install_tool(t):
                    action = input("\n(L)aunch, (S)ave report, (B)ack: ").strip().lower()
                    if action == "l": run(t["launch"])
                    elif action == "s": run(t["launch"], save_report=True, tool_name=t["name"])
            else:
                pause("Press ENTER to continue...")
        else:
            warn("Invalid choice."); time.sleep(1)

# ---------- Main Menu ----------
def main():
    loading_screen()
    while True:
        banner()
        print("Select a category:\n")
        for k, v in CATEGORIES.items():
            print(f"[{k}] {CYAN}{v['name']}{RESET}")
        print("[0] Exit")

        choice = input("\nYour choice: ").strip()
        if choice == "0":
            print("Goodbye — stay ethical!"); sys.exit()
        elif choice in CATEGORIES:
            tool_menu(choice)
        else:
            warn("Invalid category."); time.sleep(1)

if __name__ == "__main__":
    main()

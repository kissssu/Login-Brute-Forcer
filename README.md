# Flask Login Brute Forcer
A Python project that demonstrates brute forcing a Flask-based login system using custom wordlists for usernames and passwords. This repository includes a simple Flask application to simulate a vulnerable login system and the brute forcer script.

## Project Structure
```bash
.
├── Main.py           # The brute force script
├── flask.py          # Flask application with login functionality
├── templates/
│   ├── login.html    # Login page template
```

## Features
1. A basic Flask application to simulate a login system:
- Login Form: Accepts username and password.
- Success Page: Displays on successful login.
2. A brute force script (Main.py) to crack the login credentials using wordlists.

## Requirements
- **Python 3.6+**
- **Flask**: For running the web application.
- **Requests Library**: For making HTTP requests in the brute force script.

Install the required libraries:
```bash
pip install flask requests
```

## Setup & Usage
1. Run the Flask Application
- Navigate to the project directory.
- Start the Flask application:
```bash
python3 flask.py
```
- Access the app in your browser at http://127.0.0.1:5000.

2. Prepare Wordlists
- Create a usernames.txt file with possible usernames (one per line).
- Create a passwords.txt file with possible passwords (one per line).

Example:
- usernames.txt:
```
admin
user
test
```
- passwords.txt:
```
password
admin123
guest123
```

3. Run the Brute Forcer
- Run the Main.py script to perform the brute force attack:
```bash
python3 Main.py
```

- Output example:
```
Copy code
[*] Starting brute force attack...
[*] Trying: Username: admin | Password: password
[*] Trying: Username: admin | Password: admin123
[+] Found! Username: admin | Password: admin123
```
## Flask Application
**Endpoints**
- ```/```: Home page, redirects to /login.
- ```/login```: Login page where users can submit credentials.
- ```/success```: Page displayed on successful login.

## Templates
- ```login.html```: Contains the login form.
- ```success.html```: Displays a success message.

## Disclaimer
This project is for educational purposes only. Do not use it for unauthorized access or malicious purposes.

## License
This project is under the MIT License. See LICENSE for details.
# PassGuard – Password Security Evaluation Tool

College project for **CyberRotPasswordSecurity**  
GitHub: https://github.com/theashokjagarwal/CyberRotPasswordSecurity

## Purpose

PassGuard is an educational password security awareness tool.

You type a password. The page checks it in your browser and shows:

- Strength: Very Weak / Weak / Medium / Strong
- Risk: Low / Medium / High
- Score out of 100
- Problems found
- Suggestions to improve

This is a simple BCA / college project. It is not a professional security product.

## Privacy

**Your password is checked locally in your browser and is never sent anywhere.**

Flask only opens the webpage. The password is not sent to Python, not saved in a file, and not sent to any API.

## Features

- Live check while you type
- Show / Hide password button
- Length check (minimum 8, better 12+)
- Checks lowercase, UPPERCASE, numbers, special characters
- Finds repeated characters like `aaaa` or `1111`
- Finds sequences like `1234`, `abcd`, `qwer`
- Small common password list (`password`, `qwerty`, `admin`, ...)
- Catches trick spelling like `p@ssw0rd`
- Finds easy patterns like letters + year (`hello2024`)

## Technologies

- Python
- Flask (only to show the page)
- HTML
- CSS
- JavaScript (all password checks)

No database. No extra libraries except Flask.

## Project files

PassGuard/

├── app.py

├── templates/index.html

├── static/style.css

├── rules/common_passwords.txt

├── requirements.txt

└── README.md



- `app.py` — tiny Flask server. It only shows the page.
- `templates/index.html` — the page and all JavaScript checks
- `static/style.css` — look of the page
- `rules/common_passwords.txt` — small list of common passwords

## How it works

1. Flask opens `index.html`.
2. Flask also counts how many lines are in `common_passwords.txt` and shows: `Checked against 10 common passwords`.
3. When you type, JavaScript checks the password inside the browser.
4. Score starts at 0.
5. Points are added for length and character types.
6. Points are taken away for problems.
7. If it is a common password, score is capped at 10.
8. Score is mapped to Very Weak / Weak / Medium / Strong.

This score is an educational estimate, not a scientifically exact measurement.

## How to run on Windows

1. Install Python from https://www.python.org/downloads/  
   Tick **Add Python to PATH** during install.

2. Put all project files in one folder, for example `Desktop\PassGuard`.

3. Open Command Prompt and go to that folder:

cd Desktop\PassGuard



4. Install Flask:

python -m pip install flask



If `python` does not work, try:

py -m pip install flask



5. Start the app:

python app.py



If `python` does not work, try:

py app.py



6. Open a browser and go to:

http://127.0.0.1:5000



7. Type a password. Results should change while you type.

To stop the server, click the Command Prompt window and press `Ctrl + C`.

## Test passwords

Try these:

| Password | What you should see |
|---|---|
| `qwerty` | Very Weak, common password, score about 10 or less |
| `p@ssw0rd` | Very Weak, still caught as common |
| `123456` | Very Weak, common password |
| `hello2024` | Weak / Medium, letters + year |
| `Strong#Pass2025` | Stronger score, mixed types, longer |

## Limitations

- Small common password list only (10 words)
- Simple scoring, not a real security audit
- Does not check if a password was leaked on the internet
- For learning only


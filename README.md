
---

## ⚡ Quick Start

```bash
# 1. Clone the repo
git clone https://github.com/theashokjagarwal/CyberRotPasswordSecurity.git
cd CyberRotPasswordSecurity

# 2. Install Flask
python -m pip install flask
# (use `py` instead of `python` on some Windows setups)

# 3. Run the app
python app.py

# 4. Open your browser
http://127.0.0.1:5000
```

Stop the server anytime with `Ctrl + C`.

<details>
<summary><strong>🪟 Full Windows walkthrough</strong></summary>

1. Install Python from [python.org](https://www.python.org/downloads/) — tick **Add Python to PATH**.
2. Put all project files in one folder and open Command Prompt there.
3. `python -m pip install flask` (or `py -m pip install flask`)
4. `python app.py` (or `py app.py`)
5. Open **http://127.0.0.1:5000**
6. Type a password — results update live.

</details>

---

## 🧮 How Scoring Works

Score starts at **0** and is capped between **0–100**.

<table>
<tr><td>

**➕ Points added**
| Rule | Points |
|---|---|
| 8+ characters | +20 |
| 12+ characters | +15 |
| 16+ characters | +10 |
| Lowercase | +10 |
| UPPERCASE | +10 |
| Number | +10 |
| Special character | +15 |

</td><td>

**➖ Points deducted**
| Rule | Points |
|---|---|
| Repeated characters | −15 |
| Sequence | −15 |
| Predictable pattern | −15 |
| Shorter than 8 | −20 |

</td></tr>
</table>

🚨 **Hard rule:** if the password matches the common-password list, the score is capped at **10**, no matter what else scores.

| Score Range | Strength | Risk |
|:---:|:---:|:---:|
| 0 – 24 | 🔴 Very Weak | High |
| 25 – 49 | 🟠 Weak | High |
| 50 – 74 | 🟡 Medium | Medium |
| 75 – 100 | 🟢 Strong | Low |

*This is an educational estimate, not a scientific measurement.*

---

## 🧪 Example Results

| Password | Result |
|---|---|
| `qwerty` | 🔴 Very Weak — common password |
| `p@ssw0rd` | 🔴 Very Weak — still caught as common |
| `123456` | 🔴 Very Weak — common password |
| `hello2024` | 🟠 Weak/Medium — letters + year |
| `Strong#Pass2025` | 🟢 Strong — long & mixed |

---

## ⚙️ Function Reference

<details>
<summary><strong>Click to expand the JavaScript function list</strong></summary>

| Function | Purpose |
|---|---|
| `toggleShow()` | Show / hide password |
| `checkLength(p)` | Flags passwords under 8 chars |
| `hasLower(p)` / `hasUpper(p)` | Checks letter case |
| `hasNumber(p)` / `hasSpecial(p)` | Checks digits / symbols |
| `checkRepeat(p)` | Finds `aaaa`, `1111`, etc. |
| `checkSequence(p)` | Finds `1234`, `abcd`, `qwer`... |
| `stripTricks(p)` | Normalizes leetspeak (`@`→a, `0`→o...) |
| `checkCommon(p)` | Matches the common-password list |
| `checkPredictable(p)` | Flags letters+year or digits-only |
| `getScore(p)` | Computes the final score |
| `strengthName(score)` / `riskName(score)` | Maps score → label |
| `checkPassword()` | Orchestrates everything & updates the UI |

</details>

---

## 🚧 Limitations

- 📋 Only 10 common passwords in the list
- 🧮 Simple heuristic scoring, not a security audit
- 🌐 Doesn't check real-world leaked-password databases
- 🎓 Built for learning, not production use

## 🔮 Roadmap

- [ ] Random strong-password generator (client-side)
- [ ] Expand `common_passwords.txt`
- [ ] Dark / light theme toggle

---

<div align="center">

Made with 💚 by **Team CyberRot** · Team No. 16

</div>

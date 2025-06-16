<div align="right">
<b>English</b> | <a href="README.id.md">Bahasa Indonesia</a>
</div>
## Python Payload Generator

A command-line interface (CLI) tool written in Python to automatically generate obfuscated code injection payloads. This tool is designed to help security researchers and CTF players learn and bypass simple security filters.

---

### ⚠️ Usage Warning & Disclaimer

**This tool is created purely for educational and security research purposes within a legal and controlled environment (such as CTF platforms or personal labs).**

The author is not responsible for any form of misuse or damage caused by this tool. Using this tool to attack targets for which you do not have explicit permission is illegal. **Use at your own risk.**

---

### ✨ Features

* **Dual Mode:** Supports two payload generation modes:
    1.  **Simple Mode:** For basic commands like `open('file.txt').read()`.
    2.  **Advanced Mode:** For more complex, chained commands like `__import__('os').popen('ls').read()`.
* **`chr()` Obfuscation:** Automatically converts all strings (function names, arguments, methods) into the `chr()` format to bypass naive filters that block keywords.
* **Interactive:** An easy-to-use command-line interface for rapid payload creation.

---

### 🚀 Installation & Requirements

No special installation is required. You only need **Python 3.x** installed on your system.

Clone this repository:
```bash
git clone https://github.com/AmirulMirdas2/Python-Payload-Generator.git
cd Python-Payload-Generator
```

---

### ⚙️ How to Use

Run the script from your terminal:
```bash
python payload_generator.py
```

The program will display a menu to select your desired mode. Simply follow the on-screen instructions.

**Example Session:**
```
Select generator mode:
  1. Simple Mode (e.g., open('file.txt').read())
  2. Advanced Mode (e.g., __import__('os').popen('ls').read())
  (Type 'exit' or 'quit' to leave)
Mode selection (1 or 2) > 2

Enter advanced command > __import__('os').popen('ls').read()

[+] Parsing (Advanced Mode) successful:
    - Function 1: __import__ (Arg: os)
    - Function 2: popen (Arg: ls)
    - Function 3: read

✅ Your Payload is Ready:
------------------------------------------
getattr(__builtins__, chr(95)+...).__getattribute__(chr(112)+...)(chr(108)+...).__getattribute__(chr(114)+...)()
------------------------------------------
```

---

### 📝 License

This project is licensed under the **MIT License**. See the `LICENSE` file for details.

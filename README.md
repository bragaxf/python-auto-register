# 🤖 Selenium Auto Register Bot

This project automates the process of filling out a user registration form on any website using Python and Selenium. It generates realistic random data (names, emails, phone numbers, etc.) and interacts with the browser as if it were a real user.

---

## 🚀 Features

- Full automation of form fields: names, surnames, usernames, emails, phone numbers, addresses, etc.
- Automatic random password generation (12 characters, secure)
- Dynamic date picker support (birthdays)
- Country and currency dropdown selection
- Parallel execution using multiple browser instances
- Fully customizable: just change the HTML selectors and the target URL

---

## ⚙️ Requirements

- Python 3.8+
- Google Chrome (or compatible browser)
- [ChromeDriver](https://sites.google.com/a/chromium.org/chromedriver/) installed and in your system PATH

Install Python dependencies:

```bash
pip install -r requirements.txt
```

---

## 📁 Project Structure

```
selenium-auto-register/
├── botform.py              # The main automation script
├── requirements.txt     # Python dependencies
└── README.md            # This file
```

---

## ▶️ How to Use

1. Clone the repository:

```bash
git clone https://github.com/bragaxf/python-auto-register.git
cd python-auto-register
```

2. Install dependencies:

```bash
pip install -r requirements.txt
```

3. Open `botform.py` and change the `url` variable to the target registration page:

```python
url = 'https://example.com/?modal=registration'
```

4. If needed, update the field selectors (e.g., IDs, XPATH, CSS) to match the target form.

5. Run the script:

```bash
python botform.py
```

6. When prompted:

```
How many windows do you want to open?
```

Enter the number of parallel browser instances you want to launch.

---

## 🛠 Customization

If a form field is not required or not present on the site you're automating, **comment out or remove** the related block of code.

Each field is clearly marked in the script with comments like:

```python
# 🧾 FIELD: Email
# ✅ FIELD: Accept terms
```

---

## ⚠️ Disclaimer

This script is intended for **educational and testing purposes only**. Do **not** use it to interact with websites without explicit permission, as it may violate their terms of service.

---

## 📄 License

MIT License

---

## 💬 Author

Created by Rodrigo Braga (https://github.com/bragaxf). Feel free to contribute, fork, or open issues!

## ✅ Full Instructions: Use `clean_invisible_chars_verbose.py` in VSCode

---

### 1. **Set Up Your Environment**

#### ✔️ Install Python

* Download from: [https://www.python.org/downloads](https://www.python.org/downloads)
* During installation, **check the box** that says “Add Python to PATH”.

#### ✔️ Install VSCode

* Download from: [https://code.visualstudio.com](https://code.visualstudio.com)
* Install the **Python extension** (you’ll be prompted automatically when you open a `.py` file).

---

### 2. **Create and Save the Script**

1. Open **VSCode**.
2. Go to `File > New File`.
3. Paste in this code:

```python
import re
import pyperclip

INVISIBLE_CHARS = {
    '\u200b': 'ZERO WIDTH SPACE',
    '\u200c': 'ZERO WIDTH NON-JOINER',
    '\u200d': 'ZERO WIDTH JOINER',
    '\u2060': 'WORD JOINER',
    '\ufeff': 'BYTE ORDER MARK',
    '\u00a0': 'NON-BREAKING SPACE',
    '\u202f': 'NARROW NO-BREAK SPACE',
}

pattern = '[' + ''.join(INVISIBLE_CHARS.keys()) + ']'

def analyze_and_clean(text):
    removed = []
    for i, c in enumerate(text):
        if c in INVISIBLE_CHARS:
            removed.append((i, c, INVISIBLE_CHARS[c]))
    cleaned = re.sub(pattern, '', text)
    return cleaned, removed

def main():
    print("🔍 Analyzing clipboard...")

    try:
        text = pyperclip.paste()
        cleaned_text, removed_chars = analyze_and_clean(text)

        if removed_chars:
            print("⚠️  Invisible characters found and removed:")
            for i, char, name in removed_chars:
                hex_code = f"U+{ord(char):04X}"
                print(f" - Position {i}: {name} ({hex_code})")
        else:
            print("✅ No invisible characters detected.")

        pyperclip.copy(cleaned_text)
        print("\n📋 Cleaned text copied back to clipboard.")

    except Exception as e:
        print(f"❌ Error: {e}")

if __name__ == "__main__":
    main()
```

4. Save it as `clean_invisible_chars_verbose.py`.

---

### 3. **Install `pyperclip`**

1. Press <kbd>Ctrl</kbd> + <kbd>\`</kbd> to open the **VSCode terminal**.
2. Type:

   ```bash
   pip install pyperclip
   ```

   ✅ You should see "Successfully installed pyperclip".

---

### 4. **Use the Script**

1. Copy **any text** with potential invisible characters to your clipboard (e.g., text from ChatGPT).
2. In VSCode, run the script:

   ```bash
   python clean_invisible_chars_verbose.py
   ```
3. The terminal will:

   * Show you any invisible characters it found (with position and Unicode name).
   * Copy the **cleaned version** of your text back to your clipboard.

---

### ✅ Now What?

You can now **paste the cleaned text** anywhere you need (e.g., into a document, form, or email). No more hidden characters!

Would you like me to help you turn this into a **clickable app** for non-technical use?

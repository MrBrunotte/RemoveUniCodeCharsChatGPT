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

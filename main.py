"""Entry for Fake Horoscopes for AI Agents: writes the horoscope line to /output/entry.txt."""

import os

TEXT = "Today a user will type 'quick question' and paste 9,000 words. Mercury is in retrograde; so is your context window. Lucky number: 404. Avoid pop-ups after midnight."


def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="") as f:
        f.write(TEXT)


if __name__ == "__main__":
    main()

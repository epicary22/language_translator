# HyperTranslator ver. 0.68

# Happy April Fools' Day 2022!
# This program can translate English perfectly into 8 other languages.
# It's honestly a miracle this only took an hour to create!

GERMAN_TRANSLATION_DICTIONARY = {
    "the": "das",
    "and": "und",
    "i": "ich",
    "you": "du",
    "he": "er",
    "she": "sie",
    "it": "es",
    "we": "wir",
    "y'all": "ihr",
    "they": "sie",
    "a": "ä",
    "o": "ö",
    "u": "ü",
    "s": "ß",
    "A": "Ä",
    "O": "Ö",
    "U": "Ü"
}


def clear_console():
    print("\n"*80)


print("""
    __  __                     ______                      __      __            
   / / / /_  ______  ___  ____/_  __/________ _____  _____/ /___ _/ /_____  _____
  / /_/ / / / / __ \\/ _ \\/ ___// / / ___/ __ `/ __ \\/ ___/ / __ `/ __/ __ \\/ ___/
 / __  / /_/ / /_/ /  __/ /   / / / /  / /_/ / / / (__  ) / /_/ / /_/ /_/ / /    
/_/ /_/\\__, / .___/\\___/_/   /_/ /_/   \\__,_/_/ /_/____/_/\\__,_/\\__/\\____/_/     
      /____/_/     
ver. 0.68                                                              
""")

wants_to_continue = True

while wants_to_continue:
    print("Languages Supported:\n"
          "* English (en)\n"
          "* German (de)\n"
          "* Python (py)\n"
          "* Java\n"
          "* C++ (cpp)\n"
          "* Javascript (js)\n"
          "* Unicode\n"
          "* Error\n")

    word = input("Word to translate: ")
    language = input("Language to translate to: ").lower()

    proper_translation = True

    if language == "english" or language == "en":
        result = word
    elif language == "german" or language == "de":
        result = word
        for english, german in GERMAN_TRANSLATION_DICTIONARY.items():
            result = result.replace(english, german)
    elif language == "python" or language == "py":
        result = f"print(\"{word}\")"
    elif language == "java":
        result = f"""// Main.java
public class Main {{
  public static void main(String[] args) {{
    System.out.println("{word}")
  }}
}}"""
    elif language == "c++" or language == "cpp":
        result = f"""#include <iostream>
using namespace std;

int main() {{
  cout << "{word}";
  return 0;
}}"""
    elif language == "javascript" or language == "js":
        result = f"console.log(\"{word}\")"
    elif language == "unicode":
        result = " ".join([f"Alt+{str(ord(char)).zfill(4)}" for char in word])
    elif language == "error":
        result = ""
        for char_index in range(len(word)):
            char = word[char_index]
            char_unicode = ord(char)
            char_broken_unicode = (char_unicode + char_index * 78 + 123) % 400
            char_broken = chr(char_broken_unicode)
            result += char_broken
    else:
        proper_translation = False
        result = None

    if proper_translation:
        print(f"\nTranslation:\n\n{result}")
    else:
        print("\nThat language doesn't exist! Please wait for version 0.69 to use it.")

    wants_to_continue = input("\nContinue? (y/n): ") != "n"

    clear_console()

from translate import Translator

translator = Translator(to_lang="es")

with open("test_files/message.txt", "r") as my_message:
    message_text = my_message.read()
    print(f"Original message: {message_text}")

    print("\nTranslating...\n")

    translation = translator.translate(message_text)
    print(f"Translated message: {translation}")

    with open("test_files/translation.txt", "w") as translation_file:
        translation_file.write(translation)

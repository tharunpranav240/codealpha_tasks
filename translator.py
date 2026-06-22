from tkinter import *
from deep_translator import GoogleTranslator

def translate_text():
    text = input_text.get("1.0", END).strip()

    translated = GoogleTranslator(
        source=source_lang.get(),
        target=target_lang.get()
    ).translate(text)

    output_text.delete("1.0", END)
    output_text.insert(END, translated)

root = Tk()
root.title("Language Translation Tool")
root.geometry("500x400")

Label(root, text="Enter Text").pack()

input_text = Text(root, height=5)
input_text.pack()

source_lang = StringVar(value="en")
target_lang = StringVar(value="ta")

Label(root, text="Source Language").pack()
Entry(root, textvariable=source_lang).pack()

Label(root, text="Target Language").pack()
Entry(root, textvariable=target_lang).pack()

Button(root, text="Translate", command=translate_text).pack(pady=10)

Label(root, text="Translated Text").pack()

output_text = Text(root, height=5)
output_text.pack()

root.mainloop()

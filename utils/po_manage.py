import polib
from .cht_gpt_manage import chat_gpt_translate, connect_to_gpt
import re

def process_po_file(address, language, name, apikey, **kwrgs) -> None:
    po = polib.pofile(address)
    client = connect_to_gpt(apikey)
    
    for entry in po:
        if not entry.translated() or "```" in entry.msgstr:

            translated_text = chat_gpt_translate(entry.msgid, language, name, client)
            
            cleaned_text = re.sub(r"```html\s*(.*?)\s*```", r"\1", translated_text, flags=re.DOTALL)
            
            cleaned_text = re.sub(r"```(.*?)```", r"\1", cleaned_text, flags=re.DOTALL)
            
            cleaned_text = re.sub(r"\s+", " ", cleaned_text.strip())
            
            entry.msgstr = cleaned_text

            print(f'{entry.msgstr}')

    po.save(address)
    print("Successfully translated!")

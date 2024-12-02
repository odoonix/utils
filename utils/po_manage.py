import polib
import logging
try:
    from .cht_gpt_manage import chat_gpt_translate, connect_to_gpt
except ModuleNotFoundError:
    logging.error("module 'openai' is not installed")
    

def process_po_file(address, language, name, apikey, **kwrgs) -> None:
    po = polib.pofile(address)
    client = connect_to_gpt(apikey)
    
    for entry in po:
        if not entry.translated():
            translated_text = chat_gpt_translate(entry.msgid, language, name, client)
            entry.msgstr = translated_text

    po.save(address)
    print("Successfully translated!")

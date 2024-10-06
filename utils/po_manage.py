import polib
from .cht_gpt_manage import chat_gpt_translate, connect_to_gpt


def process_po_file(address, language, apikey, **kwrgs) -> None:
    po = polib.pofile(address)
    client = connect_to_gpt(apikey)
    
    for entry in po:
        if not entry.translated():
            translated_text = chat_gpt_translate(entry.msgid, language, client)
            entry.msgstr = translated_text

    po.save(address)
    print("Successfully translated!")

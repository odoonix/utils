import polib
from .cht_gpt_manage import chat_gpt_translate, connect_to_gpt


def process_po_file(po_filepath, language, apikey) -> None:
    po = polib.pofile(po_filepath)
    client = connect_to_gpt(apikey)
    
    for entry in po:
        if not entry.translated():
            translated_text = chat_gpt_translate(entry.msgid, language, client)
            entry.msgstr = translated_text

    po.save(po_filepath)
    print("Successfully translated!")

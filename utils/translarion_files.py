from .po_manage import process_po_file

def translation_file(address, language, apikey, **kwarg): 
   process_po_file(address, language, apikey)
    


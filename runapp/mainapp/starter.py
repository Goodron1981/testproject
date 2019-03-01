from runapp.add_isue_attribute.delete_old_url import deleteOU
from runapp.sape.load_isue import load_isue_sape
from runapp.rota.load_isue import load_isue_rota
from runapp.add_isue_attribute.parse_atrributes import parser_attr
from runapp.add_isue_attribute.search_keys import add_keys_img
from runapp.rota.sort_isue import sortallisues

def startfirst():
    sortallisues()
    load_isue_sape()
    load_isue_rota()
    deleteOU()
    parser_attr()
    add_keys_img()
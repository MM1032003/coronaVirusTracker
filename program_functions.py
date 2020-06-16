from pygal.maps.world import COUNTRIES
from pygal.maps.world import World
import requests

def get_country_code(country_name):

    for k, v in COUNTRIES.items():
        if v == country_name:
            return k

    return None


def request_url(url):
    url   = url
    r     = requests.get(url)
    return r.json()

def gathering_data(data):
    countries_dict  = {}
    for c, v in data.items():
        country_name    = c

        code            = get_country_code(country_name)

        if country_name == 'US':
            code        = 'us'
        elif country_name == 'Russia':
            code        = 'ru'
        elif country_name == 'Libya':
            code        = 'ly'
        elif country_name == 'Iran':
            code        = 'ir'
        elif country_name == 'Syria':
            code        = 'sy'
            
        cases           = v[-1]['confirmed']

        if code:
            countries_dict[code]    = cases
        else:
            print(f"ERROR - {country_name}")

    return countries_dict
def render_svg_img(img_name, countries_info):
    wm  = World()
    wm.title    = 'Corona Cases Until 15-6-2020'
    wm.add("Corona Cases", countries_info)
    wm.render_to_file(f"{img_name}.svg")

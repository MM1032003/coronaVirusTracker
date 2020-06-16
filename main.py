from program_functions import *


data  = request_url("https://pomber.github.io/covid19/timeseries.json")
countries_info  = gathering_data(data)
render_svg_img("Corona_Cases", countries_info)
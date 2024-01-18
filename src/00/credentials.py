from wsgiref.simple_server import make_server
from urllib.parse import parse_qs
# from urllib.parse import urlparse

import json

species_list = {
    "Cyberman": "John Lumic",
    "Dalek": "Davros",
    "Judoon": "Shadow Proclamation Convention 15 Enforcer",
    "Human": "Leonardo da Vinci",
    "Ood": "Klineman Halpen",
    "Silence": "Tasha Lem",
    "Slitheen": "Coca-Cola salesman",
    "Sontaran": "General Staal",
    "Time Lord": "Rassilon",
    "Weeping Angel": "The Division Representative",
    "Zygon": "Broton"
}
def application(environ, start_response):
    # Returns a dictionary in which the values are lists
    dict_with_lists = parse_qs(environ['QUERY_STRING'])
    # As there can be more than one value for a variable then a list is provided as a default value.
    species = dict_with_lists.get("species", None) 
    # if species:
    result = "{\"credentials\": \"Unknown\"}"
    if species is not None:
        credentials = species_list.get(species[0], 0)
        print(species[0])
        if credentials:
            result_data = json.dumps({"credentials": credentials})
        else:
            result_data = json.dumps({"credentials": "Unknown"})
        result = (result_data + '\n').encode("utf-8")
        status = '200 OK'
        response_headers = [("Content-Type", "application/json")]
        start_response(status, response_headers)
        return [result]
    else:
        status = '400 BAD_REQUEST'
        response_headers = [("Content-Type", "text/plain")]
        start_response(status, response_headers)
        return ["No such species"]

if __name__ == "__main__":
    httpd = make_server('localhost', 8888, application)
    print("Serving on http://localhost:8888...")
    httpd.serve_forever()

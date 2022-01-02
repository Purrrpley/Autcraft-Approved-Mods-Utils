import requests
import json


def download_page():
    request_data = json.dumps(
        {
            'id': 549692,
            'method': 'Wiki.getPageTitle',
            'params': {
                'preset_id': 34575523,
                'title': 'Approved_Mods',
                'prop': [
                    'text'
                ]
            }
        }
    )
    r = requests.post('https://www.autcraft.com/api/v1/api.php', request_data)
    wiki_text = r.json()['result']['text_text']
    with open('wiki_page.txt', 'w') as f:
        f.write(wiki_text)

download_page()

import json
import re

import requests


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
    # with open('wiki_text.txt', 'w') as f:
        # f.write(r.json()['result']['text_text'])
    # with open('wiki_display.txt', 'w') as f:
        # f.write(r.json()['result']['text_display'])
    return r.json()['result']['text_text']


def get_mods(wiki_text: str):
    mods = []
    seen_allowed_mods_title = False
    sections = []
    for line in wiki_text.split('\n'):
        if seen_allowed_mods_title:
            if line.startswith('*'):
                re.sub("^* \[(.+?)\]( \(()+\))$")
        else:
            if line == "== Allowed Mods ==":
                seen_allowed_mods_title = True


def main():
    print(get_mods(download_page()))


if __name__ == '__main__':
    main()

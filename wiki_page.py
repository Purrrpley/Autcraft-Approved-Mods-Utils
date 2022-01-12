import json
import re
from dataclasses import dataclass

import requests
import wikitextparser as wtp


@dataclass
class Mod:
    name: str
    url: str
    description: str
    forks: list['Fork']


@dataclass
class Fork:
    name: str
    url: str


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
    for line in wiki_text.splitlines():
        if seen_allowed_mods_title:
            if line.startswith('*'):
                re.sub("^* \[(.+?)\]( \(()+\))$")
        else:
            if line == "== Allowed Mods ==":
                seen_allowed_mods_title = True


def parse_mod_line(line: str):
    # print(re.match(r"^\* \[(.+?) (.+?)\]( \((.+?)\))? - (.+)", line))
    
    line = line.removeprefix('* [')
    wikitext_main, _, line = line.partition('] ')
    wikitext_main_mod, _, wikitext = line.partition(' ')
    mod = Mod()
    main_wikitext_link, _, line = line.partition(' ')
    if line.startswith(' ('):
        # Has forks
        wtp.WikiText()

    main_wikitext_link = line[:line.index(']')]
    link, _, text = main_wikitext_link.partition(' ')
    print(f"{text}: {link}")

    def parse_wikitext_link(wikitext: str) -> tuple[str, str]:
        pass


def main():
    # print(get_mods(download_page()))
    # print(parse_mod_line("* [https://modrinth.com/mod/sodium Sodium] ([https://github.com/IrisShaders/sodium-fabric Iris Fork], [https://github.com/HyperCubeMC/sodium-fabric Starline Iris Fork]) - Rendering engine and client-side optimisation mod, usually even better than OptiFine."))
    print(wtp.WikiText(download_page()).)


if __name__ == '__main__':
    main()

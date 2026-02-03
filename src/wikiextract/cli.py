import json
import pathlib

import click

from wikiextract.lib import extract_links

@click.command(help="Extract links from a wikicode file.")
@click.argument(
    "page_path",
    type=click.Path(
        exists=True,
        path_type=pathlib.Path,
        readable=True,
    ),
)
def main(page_path: pathlib.Path):
    content = page_path.read_text()
    links = extract_links(content)
    print(json.dumps(links, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()

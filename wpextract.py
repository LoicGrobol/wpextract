import re


def extract_links(page: str) -> list[str]:
    """Extract internal links from a wikicode string.

    ```
    >>> extract_links("UPN est une [[Université]] située en [[Île de France]]")
    ['[[Université]]', '[[Île de France]]']
    ```
    """
    links = re.findall(r"\[\[.*?\]\]", page)
    return links

if __name__ == "__main__":
    res = extract_links("UPN est une [[Université]] située en [[Île de France]]")
    print(res)
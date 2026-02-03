import json
import sys

import wpextract

if __name__ == "__main__":
    with open(sys.argv[1]) as in_stream:
        content = in_stream.read()
        links = wpextract.extract_links(content)
        print(json.dumps(links, ensure_ascii=False, indent=2))

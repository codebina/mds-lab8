import json
import os

def build():
    with open("data.json") as f:
        items = json.load(f)

    lines = []
    lines.append("<html><body>")
    lines.append("<h1>My list</h1>")
    lines.append("<ul>")
    for item in items:
        lines.append(f"  <li><strong>{item['title']}</strong>: {item['description']}</li>")
    lines.append("</ul>")
    lines.append("</body></html>")

    os.makedirs("site", exist_ok=True)
    with open("site/index.html", "w") as f:
        f.write("\n".join(lines))

if __name__ == "__main__":
    build()

test_build.py:

import json
from build import build

def test_titles_appear_in_output():
    build()
    with open("site/index.html") as f:
        html = f.read()
    with open("data.json") as f:
        items = json.load(f)
    for item in items:
        assert item["title"] in html
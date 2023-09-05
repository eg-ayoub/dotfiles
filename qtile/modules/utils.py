def parse_titles(text):
    """Parse title and handle bold"""
    ret = []
    titles = text.split(" | ")
    for title in titles:
        if title.startswith("<b>"):
            ret.append("<b>" + _parse_title(title[3:-4]) + "</b>")
        else:
            ret.append(_parse_title(title))
    return " | ".join(ret)


def _parse_title(title):
    """Parse title to get shorter program name"""
    for prg in ["- Visual Studio Code", "- Google Chrome"]:
        if prg in title:
            title = title[:-len(prg)]
            title = title[:20]
            return title + prg
    return title

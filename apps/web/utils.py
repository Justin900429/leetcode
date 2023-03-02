def add_toc(content):
    temp = content.split("\n")
    temp.insert(1, "[TOC]")
    return "\n".join(temp)

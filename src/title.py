def extract_title(markdown):
    for line in markdown.splitlines():
        if line[0:2] == "# ":
            return line[2:]
    raise ValueError("No title present")

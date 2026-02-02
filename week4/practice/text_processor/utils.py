def count_tokens(text):
    return len(text.split())

def truncate(text, limit):
    words = text.split()
    return " ".join(words[:limit])
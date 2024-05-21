import re


def remove_tags(text):
    clean = re.compile('<.*?>')
    return re.sub(clean, '', text)


# Example usage:
html_string = "<p>This is <strong>HTML</strong> text.</p>"
clean_text = remove_tags(html_string)
print(clean_text)  # Output: "This is HTML text."
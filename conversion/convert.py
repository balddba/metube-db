import re
import subprocess


def find_urls_in_file(file_path):
    # Regular expression pattern for matching URLs
    url_pattern = re.compile(r'https?://(?:[-\w.]|(?:%[\da-fA-F]{2}))+')

    with open(file_path, 'r') as file:
        content = file.read()

    # Find all URLs using the regular expression pattern
    urls = url_pattern.findall(content)

    return urls

#  Process completed
with open("/Users/amyers/PycharmProjects/metube-db/conversion/completed.txt", "r") as f:
    data = f.readlines()

    urls = find_urls_in_file(data)
    print(urls)

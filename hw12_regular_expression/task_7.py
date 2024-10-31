import concurrent.futures
import re

def read_large_generator():
    with open('text_files/file_with_ip_address.txt', 'r') as fr:
        for line in fr:
            yield line

def is_valid_ip(line):
    # Correct pattern with non-capturing groups
    pattern = r'\b(?:25[0-5][.]|2[0-4][0-9][.]|1[0-9]{2}[.]|[1-9]?[0-9][.]){3}' \
              r'(?:25[0-5]|2[0-4][0-9]|1[0-9]{2}|[1-9]?[0-9])\b'
    matching = re.findall(pattern, line)
    if matching:
        return matching  # Return list of valid IP addresses found in the line


with concurrent.futures.ThreadPoolExecutor(max_workers=25) as executor:
    results = executor.map(is_valid_ip, read_large_generator())

    for res in results:
        if res:
            print(res)




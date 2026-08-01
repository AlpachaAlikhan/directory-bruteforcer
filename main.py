import requests


TIMEOUT = 2


def main():
    target = get_target()
    words = get_wordlist()
    results = scan(target, words)
    print_results(results)

def get_target():
    while True:
        target = input("Enter target URL: ").strip()

        if not target.startswith(("http://", "https://")):
            print("URL must start with http:// or https://")
            continue

        return target.rstrip("/")

def get_wordlist():
    while True:
        wordlist_name = input("Enter wordlist: ")
        try:
            with open(f'{wordlist_name}.txt', 'r', encoding='utf-8') as file:
                return file.read().splitlines()
        except FileNotFoundError:
            print("File not found, please try again.")

def scan(target, words):
    results = {}
    for word in words:
        url = f"{target}/{word}"
        try:
            response = requests.get(url, timeout=TIMEOUT)
        except requests.RequestException:
            continue
        if response.status_code != 404:
            results[url] = response.status_code
    return results

def print_results(results):
    print("====================\nFound:\n\n")
    for url, status in results.items():
        print(f"[{status}] {url}")
    print(f"\nTotal:{len(results)}\n====================")

main()
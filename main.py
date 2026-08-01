import requests
from concurrent.futures import ThreadPoolExecutor, as_completed
import time

MAX_WORKERS = 100
TIMEOUT = 2


def main():
    target = get_target()
    words = get_wordlist()
    start = time.perf_counter()
    results = {}
    with ThreadPoolExecutor(max_workers=MAX_WORKERS) as executor:
        futures = {
            executor.submit(scan, target, word) : f"{target}/{word}"
            for word in words
        }
        for future in as_completed(futures):
            url = futures[future]
            status = future.result()
    if status is not None:
        results[url] = status
    end = time.perf_counter()
    print_results(results, end - start)

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

def scan(target, word):
    url = f"{target}/{word}"
    try:
        response = requests.get(url, timeout=TIMEOUT)
    except requests.RequestException:
        return None
    if response.status_code != 404:
        result = response.status_code
        return result

def print_results(results, time):
    print("====================\nFound:\n\n")
    for url, status in results.items():
        print(f"[{status}] {url}")
    print(f"\nTotal:{len(results)}\nScan completed in {time:.2f} seconds.\n====================")

main()
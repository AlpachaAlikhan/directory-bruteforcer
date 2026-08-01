def main():
    pass

def get_target():
    while True:
        target = input("Enter target URL: ").strip()

        if not target.startswith(("http://", "https://")):
            print("URL must start with http:// or https://")
            continue

        return target.rstrip("/")

def get_wordlist():
    while True:
        wordlist_name = input("Enter wordlist:")

        with open(f'{wordlist_name}.txt', 'r', encoding='utf-8') as file:
            words = "".join(file.readlines()).split("\n")
            return words
def load_words(wordlist):
    pass

def scan(target, words):
    pass

def print_results(results):
    pass

print(get_wordlist())
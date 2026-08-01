# Directory Bruteforcer

A simple multithreaded directory brute-forcing tool written in Python.

## Features

- Scan web directories using a custom wordlist
- Multithreaded scanning with ThreadPoolExecutor
- Custom request timeout
- Ignores 404 responses
- Displays discovered URLs and HTTP status codes
- Input validation for target URL and wordlist

## Requirements

- Python 3.11+
- requests

Install dependencies:

```bash
pip install requests
```

## Usage

Run the program:

```bash
python main.py
```

Example:

```
Enter target URL: http://127.0.0.1:8000
Enter wordlist: common
```

Example output:

```
====================
Found:

[200] http://127.0.0.1:8000/login
[301] http://127.0.0.1:8000/admin
[403] http://127.0.0.1:8000/secret

Total: 3
Scan completed in 0.12 seconds.
====================
```

## Project Structure

```
Directory-Bruteforcer/
│
├── main.py
├── common.txt
├── README.md
└── .gitignore
```

## Technologies

- Python
- requests
- concurrent.futures

## Disclaimer

This project is intended for educational purposes and should only be used on systems you own or have permission to test.
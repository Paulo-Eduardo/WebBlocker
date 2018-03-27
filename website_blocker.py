import time
from datetime import datetime as dt

hosts_path = r"C:\Windows\System32\drivers\etc\hosts"
redirect = "127.0.0.1"
website_list = ["www.facebook.com", "facebook.com", "outlook.com", "www.outlook.com", "youtube.com", "www.youtube.com"]

while True:
    if 8 < dt.now().hour < 16:
        print("Working hours...")
        with open(hosts_path, 'r+') as file:
            content = file.read()
            for website in website_list:
                if website not in content:
                    file.write(redirect + " " + website + "\n")
    else:
        print("Fun hours...")
        with open(hosts_path, 'r+') as file:
            content = file.readlines()
            file.seek(0)
            file.truncate()

            for line in content:
                if not any(website in line for website in website_list):
                    file.write(line)
            
    time.sleep(5)

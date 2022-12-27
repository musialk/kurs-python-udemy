#znaleźć biblioteki mozna na PyPi.org

import requests

response = requests.get("https://www.google.com/search?q=pogoda&rlz=1C1GCEB_enPL907PL907&oq=&aqs=chrome.0.35i39i362j46i39i199i362i465j35i39i362l6.36164837j0j7&sourceid=chrome&ie=UTF-8")
print(response)
print(response.status_code)
print(response.text)
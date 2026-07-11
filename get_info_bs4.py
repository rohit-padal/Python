import re
import requests
import contextlib
from bs4 import BeautifulSoup

#Input
url = input("Enter the Url: ")

headers = {
    "User-Agent": "Mozilla/5.0"
}
response = requests.get(url, headers=headers)

with open("get_info_Output.txt","w") as f:
    with contextlib.redirect_stdout(f):
        #Basic response
        print("\n","Status Code: ",response.status_code,"Reason: ", response.reason,"Url: ", response.url)

        #Page Title
        soup = BeautifulSoup(response.content, "html.parser")
        print(soup.title.string)

        #No. of tags
        print("\n",len(soup.find_all("a")))
        print(len(soup.find_all("img")),"\n")

        #Print first 10 links

        links = soup.find_all("a")
        
        for link in links[:10]:
            print(link.text.strip())
            print(link.get("href"))

        print("\n")
        image = soup.find_all("img")
        for img in image[:10]:
            print(img.get("src"))

        #print headings counts
        print("\n")
        for i in range(1,7):
            print(f"H{i}: ",len(soup.find_all(f"h{i}")))

        #Find all email
        txt = soup.get_text()
        emails= re.findall(
            r"[A-Za-z._%+-0-9]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}",
            txt
        )
        for email in emails:
            print("Email: ",email)
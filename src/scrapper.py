import urllib.request
import ssl
from bs4 import BeautifulSoup
from dateutil import parser

class CanaryVolcanoScrapper():

    def __init__(self):
        self.url = "https://www.ign.es"
        self.subdomain = "/web/ign/portal/vlc-ultimo-terremoto/-/terremotos-canarias/get10dias"
        self.data = []

    def __download_html(self, url):
        ssl._create_default_https_context = ssl._create_unverified_context
        response = urllib.request.urlopen(self.url+self.subdomain)
        return response.read()

    def scrape(self):
        print("Scrapping COVID data from " + self.url)
        html = self.__download_html(self.url)
        bs = BeautifulSoup(html, 'html.parser')
        entries = bs.find_all('tr');
        for row in entries:
            cells = row.find_all('td');
            if (cells):
                newEntry = {
                    "date": cells[1].text,
                    "hour": cells[2].text,
                    "latittude":cells[3].text,
                    "longitude":cells[4].text,
                    "depth": cells[5].text,
                    "magnitude": cells[7].text,
                    "magnitudeType": cells[8].text,
                    "location": cells[9].text
                }
                self.data.append(newEntry)
    
    def data2csv(self, filename):
        file=open("../csv/"+filename, "w+")
        for key in self.data[0]:
            file.write(key.capitalize() + ";")
        file.write("\n");
        for entry in self.data:
            for key in entry:
                file.write(entry[key] + ";")
            file.write("\n")


    



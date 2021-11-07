from scrapper import CanaryCovidScrapper

output = "dataset.csv"
 
scrapper = CanaryCovidScrapper();
scrapper.scrape();
scrapper.data2csv("sismos.csv");

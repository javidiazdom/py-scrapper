from scrapper import CanaryVolcanoScrapper

output = "dataset.csv"
 
scrapper = CanaryVolcanoScrapper();
scrapper.scrape();
scrapper.data2csv("sismos.csv");

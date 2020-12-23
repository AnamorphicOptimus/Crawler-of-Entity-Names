
## NER Crawler

Use selenium to automatically crawl, data source [local life](http://life.city8090.com/shanghai/)

## Data Format
-**Category**: A total of 14 categories, "Resorts/Resorts", "Cultural Centers/Activities Center", "Night Clubs/Entertainment Centers", "Leisure Plazas", "Shopping Centers", "Electrical Appliances Malls", "Supermarkets" ", "Community", "Villa", "Office Building", "Road Name", "District County", "Business Circle", "Town"
-**Data content**: contains the specific location name (name) and specific address (address)

## hanlp named entity recognition module
-api call location: hanlpAPI.py Reference website: https://www.hanlp.com/product.html
-github code location: hanlp.py Reference website: https://github.com/hankcs/HanLP

## File description
### 1. Crawler code
crawler.py
### 2.hanlp's crawling data recognition effect
apiTestResult.json
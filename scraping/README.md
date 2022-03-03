
```python
OlxScraper(
    'villas-for-sale',  <- define the section you are scraping 
    (10000000, 20000000), <- price range (x,y)
    10000,              <- price interval, this will split the price range into CSVs each one is 1 interval length
    speed=State.FAST <- the sleep time, change it to SLOW or MEDIUM if your internet connection is not stable. 
)
```

Run this constrcutor it will begin scraping and save the csvs in a file `data-{section}` , after you finish run the `merge.py` put first 
change the `section` varible to the section you were scraping, it will save you the last csv file

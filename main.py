import scraper

url = input('Enter the link of the Khan Academy Video (the link should have the comments): ')
amount = int(input('How many comments do you want to pull? '))

scraper.csv_comments(url, amount)

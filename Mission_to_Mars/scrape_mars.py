from splinter import Browser
from bs4 import BeautifulSoup as bs
from webdriver_manager.chrome import ChromeDriverManager
import pandas as pd


def scrape():
	executable_path = {'executable_path': ChromeDriverManager().install()}
	browser = Browser('chrome', **executable_path, headless=False)

	# setting up the url for the Mars website
	url = "https://redplanetscience.com"
	browser.visit(url)
	html = browser.html
	soup = bs(html, 'html.parser')

	# Identify and return news title of listing
	news_title = soup.find('div', class_='content_title').text

	# Identify and return news paragraph of listing
	news_p = soup.find('div', class_='article_teaser_body').text

	# setting up the url for the Mars featured image website
	url = "https://spaceimages-mars.com/"
	browser.visit(url)
	html = browser.html
	soup = bs(html, 'html.parser')

	# scraping the JPL Mars image website
	results = soup.find('div', class_='floating_text_area')

	# saving the url for the featured image on the JPL website
	image_url = results.a ['href']
	featured_image_url = 'https://spaceimages-mars.com/' + image_url

	# setting up the url for the Mars facts website to be able to scrape it using pandas
	url = 'https://galaxyfacts-mars.com/'

	# reading in the table using pandas
	tables = pd.read_html(url)

	# creating dataframe of the first table of information 
	new_df = tables[0]

	# replace a value within the dataframe
	new_df = new_df.replace(to_replace = 'Mars - Earth Comparison', value = 'Planet:')

	# renaming the column titles
	new_df = new_df.rename(columns={0: "", 1: "Mars", 2: "Earth"})

	# converting the table to html
	html_table = new_df.to_html(index=False)
	html_table.replace('\n', '')

	# setting up the url for the Mars cerberus website
	url = "https://marshemispheres.com/cerberus.html"
	browser.visit(url)

	# setting up connection to cerberus webpage to scrape it
	html = browser.html
	soup = bs(html, 'html.parser')
	imgs = soup.find_all('div', class_='wide-image-wrapper')
	for img in imgs:
		image = img.find('img', class_='wide-image')['src']
		final_image = 'https://marshemispheres.com/' + image

	# setting up the url for the Mars schiaparelli website
	url = "https://marshemispheres.com/schiaparelli.html"
	browser.visit(url)

	# setting up connection to schiaparelli webpage to scrape it
	html = browser.html
	soup = bs(html, 'html.parser')
	imgs = soup.find_all('div', class_='wide-image-wrapper')
	for img in imgs:
		image2 = img.find('img', class_='wide-image')['src']
		final_image2 = 'https://marshemispheres.com/' + image2
	
	# setting up the url for the Mars syrtis website
	url = "https://marshemispheres.com/syrtis.html"
	browser.visit(url)

	# setting up connection to syrtis webpage to scrape it
	html = browser.html
	soup = bs(html, 'html.parser')
	imgs = soup.find_all('div', class_='wide-image-wrapper')
	for img in imgs:
		image3 = img.find('img', class_='wide-image')['src']
		final_image3 = 'https://marshemispheres.com/' + image3

	# setting up the url for the Mars valles website
	url = "https://marshemispheres.com/valles.html"
	browser.visit(url)

	# setting up connection to valles webpage to scrape it
	html = browser.html
	soup = bs(html, 'html.parser')
	imgs = soup.find_all('div', class_='wide-image-wrapper')
	for img in imgs:
		image4 = img.find('img', class_='wide-image')['src']
		final_image4 = 'https://marshemispheres.com/' + image4

	# close the browser
	browser.quit()

	# creating dictionary to hold the hemisphere image url information
	hemisphere_urls = [
    	{"title": "Cerberus Hemisphere", "img_url": final_image},
    	{"title": "Schiaparelli Hemisphere", "img_url": final_image2},
    	{"title": "Syrtis Hemisphere", "img_url": final_image3},
    	{"title": "Valles Marineris Hemisphere", "img_url": final_image4}]

	# creating dictionary to hold all of the scraped information
	mars_info={
    	"news_title":news_title,
    	"news_paragraph":news_p,
    	"featured_image_url":featured_image_url,
    	"mars_information":html_table,
    	"hemisphere_images":hemisphere_urls}
	
	return mars_info
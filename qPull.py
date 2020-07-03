from selenium import webdriver
from bs4 import BeautifulSoup


# set the chromedriver to interact with chrome.exe to scrape webpage
driver = webdriver.Chrome(""" enter your chromedriver path """)
driver.get("https://engineering.jainuniversity.ac.in/")

question_paper = open("Question_Paper.txt", "a")

while(True):

	# manual buffer for scrape
	input("\nEnter to continue...")

	# loading Selenium & Beautiful Soup for web page scraping and lxml parsing
	content = driver.page_source
	soup = BeautifulSoup(content, features="lxml")

	# extract question-containing-element from webpage
	raw_qs = soup.findAll("table", id="ContentPlaceHolder1_dlquestions")
	
	# strip newlines and clean formatting for the scraped question 
	qs = raw_qs[0].text.replace("\n\n\n", "")
	qs = qs.replace("\n\n", "\n")

	# write pulled question to .txt file
	question_paper.write(qs + "\n")



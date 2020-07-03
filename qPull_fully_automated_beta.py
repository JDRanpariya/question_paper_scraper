from selenium import webdriver
from bs4 import BeautifulSoup
from time import sleep


def generate_button_ids():
	base_id = "ContentPlaceHolder1_rptquestioninfo_lnkbtnquestionnumber_"
	button_ids = [ base_id+str(i) for i in range(1, 10) ]

	return button_ids


def navigate_and_return_next_question(button_id, previous_question):
	#previous question should be unformatted 
	element = driver.find_element_by_id(button_id)
	element.click()
	
	while True:
		sleep(3)
		content = driver.page_source
		soup = BeautifulSoup(content, features="lxml")
		next_question = soup.findAll("table", id="ContentPlaceHolder1_dlquestions")	

		if next_question[0].text == previous_question[0].text:
			break
	return next_question


def add_to_file(question_text):	
	#Strip newlines for the scraped question 
	Qa = question_text.replace("\n\n\n", "")
	Qa = Qa.replace("\n\n", "\n")

	#Write data to file
	question_list.write("\n\n\n" + Qa)


driver = webdriver.Chrome(""" YOUR CHROME DRIVER LOCATION """)
driver.get("https://engineering.jainuniversity.ac.in/")
question_list = open("question_list.txt", "a")

input("\n\nHit enter to start scraping....")
# A delay for letting the user to login and navigate to the first page of the question

content = driver.page_source
soup = BeautifulSoup(content, features="lxml")
previous_question = soup.findAll("table", id="ContentPlaceHolder1_dlquestions")	

button_ids = generate_button_ids()


for button_id in button_ids:

	add_to_file(previous_question[0].text)
	next_question = navigate_and_return_next_question(button_id, previous_question)
	previous_question = next_question

add_to_file(previous_question[0].text)
#writing the last 70th question

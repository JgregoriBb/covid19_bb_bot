# A simple scrapper to generate a YAML file to train a bot from the WHO FAQ on COVID-19

import requests
from bs4 import BeautifulSoup

def scrape_WHO_faq():
    URL = 'https://www.who.int/news-room/q-a-detail/q-a-coronaviruses'
    page = requests.get(URL)
    soup = BeautifulSoup(page.content, 'html.parser')
    
    question_text = []
    questions = soup.find_all('a',class_='sf-accordion__link')
    for element in questions:
        question_text.append( ''.join(element.findAll(text = True)).strip())
    
    answer_text = []
    answers = soup.find_all("div", class_= "sf-accordion__content")
    for element in answers:
        answer_text.append(''.join(element.findAll(text = True)).strip())

    with open('./data/covidfaq.yaml', 'w') as file:
       file.write("categories:"+'\n')
       file.write("- COVID19_FAQ"+'\n')
       file.write("conversations:"+'\n')
       i=0
       while i<len(question_text): 
            file.write('- - '+question_text[i]+'\n')
            fix=answer_text[i].replace(':',';') #fix to replace strings with : that mess with YAML format
            file.write('  - '+fix+'\n')
            i= i+1
    
    print("[Scrapper] Scrapping done!")

if __name__ ==  "__main__":
        
    scrape_WHO_faq()
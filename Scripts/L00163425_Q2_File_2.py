"""
# ---------------------------
# File           : L00163425_Q2_File_2.py
# Created        : 22-11-2021 12:13
# Author         : Aishwarya
# Version        : v1.0.0
# Licensing      : (c) 2021 Aishwarya,LYIT
#                  Available under GNU Public1` License (GPL)
# Description
# Use python code in local machine (pc) scrape the webpage from VM remote machine
# Beautiful soup parser used to scrape the webpage contents.
# -------------------------------------
"""
import requests  # This module is for get the  http request & response
from bs4 import BeautifulSoup  # This library is imported for web scraping purpose
URL = 'http://192.168.189.129/'
def scrape_data():
    """Prints the parsing content from the webpage.
    Parameters:
    passing the arguments
    title headers,counts,page headers and section headers
    Returns:
    It will return title of the page,count the words from the page,Header of the page,and the sections of the page
    """
    try:
        response = requests.get(URL)
        page_content = BeautifulSoup(response.content, "html.parser")
        get_title_headers(page_content)
        get_count(page_content)
        get_page_header(page_content)
        get_section_header(page_content)
    except Exception as e:
        print(e)
def get_title_headers(web_response):
    """
       Print the Title of the webpage
       parameter:
       passing the arguments of webpage response
       return:
       It will returns the title of the webpage
    """
    page_title = web_response.find("title").text  # find() function finds the title of the page
    print("Page title from <title> tag: ", page_title)
def get_page_header(web_response):
    """
        Print the Header of the webpage
        parameter:
        passing the arguments of webpage response
        return:
        It will returns the headings of the webpage
    """
    page_head = web_response.find('span', {'class': 'floating_element'}).text.strip()
    print("Page Header: ", page_head)
def get_section_header(page_content):
    """
        Print the Header of the webpage
        parameter:
        passing the arguments of webpage response
        return:
        It will returns the headings of the webpage
    """
    section_header = page_content.find_all('div', {'class': 'section_header'})
    sections = [div.get_text().strip() for div in section_header]
    print("There are {} sections on the page: ".format(len(sections)))
    print("Section titles: ", sections)
def get_count(web_response):
    """
    Print how many times Apache2 found in the webpage
    parameter:
    passing the arguments of webpage response
    return:
    It will returns the number of times apache2 appears of the webpage
    """
    count = web_response.find_all(string=lambda text: "apache2" in text.lower())  # find_all() function find number of
    # times apache2 appears in the webpage
    print("Apache2 appears {} times in the web response source".format(
        len(count)))  # len() function count the number of occurence of apache2
if __name__ == '__main__':
    scrape_data()

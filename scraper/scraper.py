import re
import urllib, urllib2

from bs4 import BeautifulSoup


def match_class(target):
    '''Helper function to get all elements matching with
       provided list of css classes
    '''
    def do_match(tag):
        classes = tag.get('class', [])
        return all(c in classes for c in target)
    return do_match


class HelpoutScraper(object):
    '''Helpout scraper class provides function to scrape data,
       it dont have much options yet just basic for now, expects a
       query string and scrap data based on query.
    '''

    def __init__(self, query):
        self.query = query  # initialize object with query string
        self.soup = None

    def get_page(self):
        '''Gets the page to creat soup of page which will be used to find all data
        '''
        query = urllib.urlencode({'q': self.query})

        # formatting search url
        search_url = "http://helpouts.google.com/search?%s" % query
        page = urllib2.urlopen(search_url)

        # Creates soup for other functions to scrape data
        self.soup =  BeautifulSoup(page.read())

    def get_helpout_page(self, url):
        '''creates the soup for individual helpout page to scrape more info
        '''
        helpout_page = urllib2.urlopen(url)
        helpout_page_soup = BeautifulSoup(helpout_page.read())
        return helpout_page_soup

    def get_info(self):
        '''main function to traverse through soup to get needed data and returns json object of data
        '''
        response = {'result': []}
        self.get_page()

        # Gets helpout containers from complete page
        helpouts = self.soup.findAll(match_class(["maQuO"]))
        for helpout in helpouts:
            tmp = {}
            # finds the helpout name from the listing
            helpout_name = helpout.find(match_class(["Tozw4c-WsjYwc-r4nke"]))
            name = helpout_name.find('a').get_text()
            tmp['name'] = name

            # gets the helpout url from the listing
            helpout_url = 'http://helpouts.google.com' + helpout_name.find('a')['href']
            tmp['helpout_url'] = helpout_url

            # gets the price of helpout
            helpout_price = helpout.find(match_class(["YsLxq-qCDwBb-Gwq8we"]))
            price = helpout_price.find('span').get_text()
            tmp['price'] = price

            # gets the availability time of helpout
            helpout_available = helpout.find(match_class(["wTehdb-jOfkMb"]))
            available = helpout_available.find('span').get_text()
            tmp['available'] = available

            # gets the total overall rating of helpout
            helpout_rating = helpout.find(match_class(["FI3hNb-fI6EEc-xJ5Hnf"]))
            if helpout_rating:
                rating_meta = helpout_rating.find(itemprop="ratingValue")
                rating = rating_meta.get('content')
            else:
                rating = 'N/A'
            tmp['rating'] = rating

            # gets the indivdual helpout page to get more info
            helpout_page = self.get_helpout_page(helpout_url)

            # gets the about info from individual helpout
            about_pattern = re.compile(r'About this Helpout')
            about_helpout_elem = helpout_page.find('h2', text=about_pattern).find_next_sibling('div')
            if about_helpout_elem:
                about_helpout = about_helpout_elem.get_text()
            else:
                about_helpout = 'N/A'
            tmp['about_helpout'] = about_helpout

            # gets the provider about info from individual helpout
            helpout_provider = helpout_page.find(match_class(["Tozw4c-BeDmAc", "wE4e3b-BeDmAc"]))
            if helpout_provider:
                about_provider = helpout_provider.get_text()
            else:
                about_provider = 'N/A'
            tmp['about_provider'] = about_provider

            # gets all the reviews available on individual helpout page
            helpout_reviewrs = helpout_page.findAll(match_class(["oQLbGe-gElRsf"]))
            reviews = []
            for reviewer in helpout_reviewrs:
                reviewer_name = reviewer.get_text()
                reviewer_description = reviewer.find_previous_sibling('p')
                if reviewer_description:
                    reviewer_review = reviewer_description.get_text()
                else:
                    reviewer_review = 'N/A'
                reviews.append({'name': reviewer_name, 'review': reviewer_review})
            tmp['reviews'] = reviews

            # gets the helpout image link from individual helpout
            helpout_image = helpout_page.find(match_class(["Tozw4c-RJLb9c"]))
            if helpout_image:
                image_elem = helpout_image['src']
            else:
                image_elem = 'N/A'
            tmp['image_elem'] = image_elem

            # gets the helpout video link from individual helpout
            helpout_video = helpout_page.findAll(match_class(["aTv5jf-gkA7Yd-wZVHld"]))
            if helpout_video:
                for video_element in helpout_video:
                    video_elem = video_element['data-tee-stream-url']
            else:
                video_elem = 'N/A'
            tmp['video_elem'] = video_elem

            response['result'].append(tmp)
        return response

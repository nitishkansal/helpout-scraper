import json

from django.http import HttpResponse
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.template.loader import render_to_string

from scraper import HelpoutScraper
from models import SearchTerm, Helpout, Review


def home(request):
    '''Renders the main page where user can do search on google helpout
    '''

    return render_to_response(
        'base.html',
        context_instance=RequestContext(request)
    )


def get_info(request):
    '''Create an aboject of scraper class with provided query 
        and calls the class function to scrap data with provided query.
    '''

    query = request.GET.get('q', '')

    if query.strip():  # amke sure user has provided something to search
        scraper_obj = HelpoutScraper(query=query)
        info = scraper_obj.get_info()
    else:
        info = {'result': []}

    search_term = SearchTerm.objects.create(term=query)

    # Save all the scraped data into database
    for item in info['result']:
        helpout = Helpout.objects.create(
            search_term=search_term,
            name=item['name'],
            helpout_url=item['helpout_url'],
            price=item['price'],
            available=item['available'],
            rating=item['rating'],
            about=item['about_helpout'],
            about_provider=item['about_provider'],
            image_link=item['image_elem'],
            video_link=item['video_elem']
        )

        # Save all the reviews in database with linked to helpout
        for review in item['reviews']:
            review = Review.objects.create(
                helpout=helpout,
                reviewer_name=review['name'],
                review=review['review']
            )

    # Context to pass in template to pass as ajax resoponse
    context = {
        'info' : info['result']
    }

    template = render_to_string(
        'scraped_data.html',
        context,
        context_instance=RequestContext(request)
    )
    response = {'data': template}

    return HttpResponse(json.dumps(response), 'json')

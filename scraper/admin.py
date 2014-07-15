from django.contrib import admin
from models import SearchTerm, Helpout, Review


class SearchTermAdmin(admin.ModelAdmin):
    '''Admin class for search term model
    '''

    list_display = ['term']

class HelpoutAdmin(admin.ModelAdmin):
    '''Admin class for helpout model
    '''

    list_display = ['search_term', 'name', 'available', 'rating']

class ReviewAdmin(admin.ModelAdmin):
    '''Admin class for review model
    '''
    list_display = ['helpout', 'reviewer_name']

admin.site.register(SearchTerm, SearchTermAdmin)
admin.site.register(Helpout, HelpoutAdmin)
admin.site.register(Review, ReviewAdmin)

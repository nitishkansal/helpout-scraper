from django.db import models


class SearchTerm(models.Model):
    '''Model to store search term
    '''

    term = models.CharField(max_length=255)

    def __unicode__(self):
        return self.term


class Helpout(models.Model):
    '''Model to store all helpout data
    '''

    search_term    = models.ForeignKey(SearchTerm)
    name           = models.CharField(max_length=255)
    helpout_url    = models.CharField(max_length=255)
    price          = models.CharField(max_length=255)
    available      = models.CharField(max_length=255)
    rating         = models.CharField(max_length=255)
    about          = models.TextField()
    about_provider = models.TextField()
    image_link     = models.TextField()
    video_link     = models.TextField()

    def __unicode__(self):
        return self.name


class Review(models.Model):
    '''Model to store all reviews with helpout linked with foreign key
    '''

    helpout       = models.ForeignKey(Helpout)
    reviewer_name = models.CharField(max_length=255)
    review        = models.CharField(max_length=255)

    def __unicode__(self):
        return "%s reviewed %s" % (self.reviewer_name, self.helpout)

from django.db import models

# Create your models here.
class Publisher(models.Model):
    name = models.CharField(max_length=30)
    address = models.CharField(max_length=50)
    city = models.CharField(max_length=60)
    state_province = models.CharField(max_length=30)
    country = models.CharField(max_length=50)
    website = models.URLField()
    def __unicode__(self):
        return self.name
    # Specify default ordering in the model
    # Meta class is used to specify various model-specific options.
    class Meta:
        ordering = ['name']

class Author(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=40)
    # blank = True makes the field accept blank values. 
    # In this case, it makes email an optional field for Authors.
    email = models.EmailField(blank=True)
    def __unicode__(self):
        return u'%s %s' % (self.first_name, self.last_name)

class Book(models.Model):
    title = models.CharField(max_length=100)
    authors = models.ManyToManyField(Author)
    publisher = models.ForeignKey(Publisher)
    # By default, database fields are specified NOT null on creation
    # While text accepts '' blank values, dates do not.
    # In that case, we have to change date fields to accept null values
    #    publication_date = models.DateField(blank=True, null=True)
    # Before blank values can be accepted.
    # When changing structure of database, use 'python manage.py dbshell and run the appropriate SQL command
    # For Postgres SQL: 'ALTER TABLE books_book ALTER COLUMN publication_date DROP NOT NULL;'
    # Not possible for SQLITE without deleting and recreating db table
    publication_date = models.DateField(verbose_name='date published')
    # From above, you can also pass verbose_name as a positional argument
    #    publication_date = models.DateField('date published', other_fields='xxx')

    def __unicode__(self):
        return self.title
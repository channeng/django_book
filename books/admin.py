from django.contrib import admin
from books.models import Publisher, Author, Book

# Classes to modify default views on admin page
class AuthorAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'email')
    # Adds a search bar on the top that searches the fields for admin user search terms
    search_fields = ('first_name', 'last_name')
    # Adds a filter bar on the right that lists unique values for 'last_name'
    # Rmb add ',' comma at the end for single-field to indicate a tuple
    list_filter = ('last_name',)

class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'publisher', 'publication_date')
    list_filter = ('publication_date','authors')
    # Provides a high-level drill-down bar at the top
    date_hierarchy = 'publication_date'
    # Provides default descending sort on publication date
    ordering = ('-publication_date',)
    # Provides a custom ordering of the fields the admin user sees when you add a book
    # More natural to fill up new book in the following order
    # title -> authors -> publisher -> date
    # Also, provide ability to hide fields 
    # Eg. remove publication_date as an edit option by admin users
    # Note: When using an incomplete form, Django auto-sets missing field as 'None'
    # So, make sure that field has null=True in model.py
    fields = ('title', 'authors', 'publisher','publication_date')
    # filter_horizontal provides better UI 
    # for admin users to interact with many-to-many fields.
    # May also use filter_vertical.
    filter_horizontal = ('authors',)
    # By default, one-to-many fields are showed as multiple-choice
    # But list may get too long. raw_id_fields simplifies it as a text box
    raw_id_fields = ('publisher',)


# Admin page automatically includes user groups and setings
# Following code registers the app's model tables within the admin page
# If a particular model table is not included, then it will not appear on the admin page
admin.site.register(Publisher)
# A modified admin view based on a admin model class definition above
# It can be read as "Register the Author model with the AuthorAdmin options."
admin.site.register(Author,AuthorAdmin)
admin.site.register(Book,BookAdmin)

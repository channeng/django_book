from django import forms

# Forms syntax is similar to Django's model syntax
# Django forms handles data validation, redisplay of forms with existing content, data cleanup.

class ContactForm(forms.Form):
    subject = forms.CharField()
    # Leave email as optional
    email = forms.EmailField(required=False)
    # Each field type has a default widget, but you can override the default
    # Change form field-type with widget =...
    # Field classes as representing validation logic, 
    # while widgets represent presentation logic
    message = forms.CharField(widget=forms.Textarea)

# Form methods: .as_ul(), .as_p(), .is_bound, 
# form.is_valid() --> tells if all the required fields are filled
# form.errors --> Shows all errors related to the fields
# You can access error message directly by calling errors method on the form field. form['message'].errors
# form.cleaned_data --> If form.is_valid() = True, 
# then you can clean the data neatly into unicode, or respective int/datetime fields
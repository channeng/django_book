from django import forms

# Forms syntax is similar to Django's model syntax
# Django forms handles data validation, redisplay of forms with existing content, data cleanup.

# Form methods: .as_ul(), .as_p(), .is_bound, 
# form.is_valid() --> tells if all the required fields are filled
# form.errors --> Shows all errors related to the fields
# You can access error message directly by calling errors method on the form field. form['message'].errors
# form.cleaned_data --> If form.is_valid() = True, 
# then you can clean the data neatly into unicode, or respective int/datetime fields

class ContactForm(forms.Form):
	# Set a maximum length for subject. You can also set min_length
    subject = forms.CharField(max_length=100)
    # Leave email as optional
    # Customise HTML form labels (default = var name, capitalize first letter)
    email = forms.EmailField(required=False, label='Your e-mail address')
    # Each field type has a default widget, but you can override the default
    # Change form field-type with widget =...
    # Field classes as representing validation logic, 
    # while widgets represent presentation logic
    message = forms.CharField(widget=forms.Textarea)

    # CUSTOM VALIDATION - Always start method with 'clean_'
    # Say we want at least 4 words in the message before a valid form submission.
    def clean_message(self):
        message = self.cleaned_data['message']
        num_words = len(message.split())
        if num_words < 4:
        	# String attached to ValidationError will be displayed to the user as an item in the error list.
            raise forms.ValidationError("Not enough words!")
        # MUST explicitly return cleaned value
        return message


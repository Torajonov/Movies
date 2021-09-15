from django import forms 
from .models import Movie, Contact

class MovieRatingForm(forms.ModelForm):
	class Meta:
		model = Movie 
		fields = ['rating']


class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = '__all__'
		
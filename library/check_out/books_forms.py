from django import forms

# When we will have a database, instead of having ("Keanu Reeves", "Keanu Reeves"),
# we will have (1, "Keanu Reeves") for example with 1 the id of "Keanu Reeves" in the database
BookCharacters = [
   ("Harry Potter", "Harry Potter"),
   ("Voldemort", "Voldemort"),
   ("Cat n the Hat", "Cat n the Hat"),
   ("Grinch", "Grinch"),
   ("Katnis Everdeen", "Katnis Everdeen"),
   ("Atticus Finch", "Atticus Finch"),
   ("Gandalf", "Gandalf"),
   ("Willy Wonka", "Willy Wonka"),
]

class BookForm(forms.Form):
   name = forms.CharField(max_length=100, required=True)
   characters = forms.MultipleChoiceField(
       required=True,
       widget=forms.SelectMultiple,
       choices=BookCharacters,
   )
   genre = forms.CharField(max_length=100, required=True)
   
   def clean(self):
       cleaned_data = super().clean()
       characters = cleaned_data.get('characters', [])
       if "Minecraft Steve" in characters and "Minecraft Herobrine" in characters:
           msg = "Steve and herobrine literally hate each other."
           raise forms.ValidationError(msg)
       return cleaned_data
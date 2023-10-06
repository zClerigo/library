from django import forms

# When we will have a database, instead of having ("Keanu Reeves", "Keanu Reeves"),
# we will have (1, "Keanu Reeves") for example with 1 the id of "Keanu Reeves" in the database
gameCharacters = [
   ("Minecraft Steve", "Minecraft Steve"),
   ("Minecraft Herobrine", "Minecraft Herobrine"),
   ("Fortnite Fishstick", "Fortnite Fishstick"),
   ("Fortnite Mr. beast", "Fortnite Mr. beast"),
   ("Mario", "Mario"),
   ("Trevor Phillips", "Trevor Phillips"),
   ("Pepsi Man", "Pepsi Man"),
   ("Lamar Davis", "Lamar Davis"),
]

class GameForm(forms.Form):
   name = forms.CharField(max_length=100, required=True)
   characters = forms.MultipleChoiceField(
       required=True,
       widget=forms.SelectMultiple,
       choices=gameCharacters,
   )
   genre = forms.CharField(max_length=100, required=True)
   
   def clean(self):
       cleaned_data = super().clean()
       characters = cleaned_data.get('characters', [])
       if "Minecraft Steve" in characters and "Minecraft Herobrine" in characters:
           msg = "Steve and herobrine literally hate each other."
           raise forms.ValidationError(msg)
       return cleaned_data
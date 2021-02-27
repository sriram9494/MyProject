from django import forms
from django import forms



class UserForm(forms.Form):
    fname = forms.CharField(label='Your f name', max_length=10)
    lname = forms.CharField(label='Your l name', max_length=8)
    address = forms.CharField(widget=forms.Textarea)
    email = forms.EmailField()




"""class HotelForm(forms.ModelForm):
    class Meta:
        model = Hotel
        fields = ['name', 'hotel_Main_Img']
"""
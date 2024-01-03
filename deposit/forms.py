from django import forms

class DepositForm(forms.Form):
    amount = forms.DecimalField(max_digits=8, decimal_places=2)
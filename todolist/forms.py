from django import forms


class TodoListForm(forms.Form):
    text = forms.CharField(max_Length=45,
        widget =forms.TextInput(
            attrs={'class' : 'form-control', 'placeholder' :'Enter todo e.g. Grocery Shopping', 'aria-label' :'Todo', 'aria-describeby' : 'add-btn'}))
    
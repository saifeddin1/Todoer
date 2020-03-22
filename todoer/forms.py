from django import forms 
from .models import Todo


# class TaskForm(forms.Form):
# 	name = forms.CharField(max_length=40, 
# 		widget=forms.TextInput(attrs={
# 			'class':'form-control',
# 			'placeholder':'Add some tasks e.g Clean the room',
# 			'aria-label':'Todo',
# 			'aria-describedby':'add-btn'
# 			}))


class TodoForm(forms.ModelForm):
    class Meta:
        model = Todo
        fields = ['name']
        widgets = {
        	'name' : forms.TextInput(
        		attrs={
					'class':'form-control',
					'placeholder':'Add some tasks e.g Clean the room',
					'aria-label':'Todo',
					'aria-describedby':'add-btn',
			})
        }

    
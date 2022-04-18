from django.forms import ModelForm, Textarea

from hood.models import Post


class PostForm(ModelForm):
    class Meta:
        model = Post
        # when we use all as the val for the fields' var, then we tell django that we want a form that has input fields
        #  for all the columns that we've got in the table
        fields = ('image', 'message')
        widgets = {
            'message': Textarea(attrs={
                'class': "m_txt_area",
                'placeholder': 'Message'
                }),
        }

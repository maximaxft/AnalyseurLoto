class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        # exclude = ['author', 'updated', 'created', ]
        fields = ['text']
        widgets = {
            'text': forms.TextInput(attrs={
                'id': 'form-text', 
                'required': True, 
                'placeholder': 'Entrez le numéro'
            }),
        }

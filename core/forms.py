from django import forms
import json

class ApiForm(forms.Form):
    sensor_data = forms.CharField(
        widget=forms.Textarea(attrs={'rows': 4})
    )

    def clean_sensor_data(self):
        import json
        raw = self.cleaned_data['sensor_data']
        try:
            parsed = json.loads(raw)
        except json.JSONDecodeError:
            raise forms.ValidationError("Invalid JSON format")
        return parsed  


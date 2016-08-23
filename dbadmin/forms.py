from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit
from django import forms

from dbadmin.models import Empresa, ContEmpresa, DataClipper


class EmpresaForm(forms.ModelForm):
    class Meta:
        model = Empresa
        fields = '__all__'

    helper = FormHelper()
    helper.form_method = 'post'
    helper.add_input(Submit('Update', 'Update', css_class='btn-primary'))


class ContEmpresaForm(forms.ModelForm):
    class Meta:
        model = ContEmpresa
        fields = '__all__'

    helper = FormHelper()
    helper.form_method = 'post'
    helper.add_input(Submit('Update', 'Update', css_class='btn-primary'))


class DataClipperForm(forms.ModelForm):
    class Meta:
        model = DataClipper
        fields = '__all__'

    helper = FormHelper()
    helper.form_method = 'post'
    helper.add_input(Submit('Update', 'Update', css_class='btn-primary'))

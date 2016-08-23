import django_filters

from dbadmin.models import Empresa


class EmpresaFilter(django_filters.FilterSet):
    cod_empresa = django_filters.CharFilter(lookup_type='icontains')

    class Meta:
        model = Empresa
        fields = ['cod_empresa']




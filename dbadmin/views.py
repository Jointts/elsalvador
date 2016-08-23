# Create your views here.
from django.core.exceptions import ObjectDoesNotExist
from django.core.urlresolvers import reverse_lazy
from django.forms import model_to_dict
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404
from django.views.generic import ListView
from django.views.generic.base import TemplateView
from django.views.generic.detail import DetailView
from django.views.generic.edit import UpdateView

from dbadmin.filters import EmpresaFilter
from dbadmin.forms import ContEmpresaForm, EmpresaForm, DataClipperForm
from dbadmin.models import Empresa, DataClipper, ContEmpresa, Licencia, Sucursal, ContribuentaEmp


class EmpresaListView(ListView):
    paginate_by = 20
    model = Empresa
    context_object_name = 'empresa_list'
    template_name = 'empresa_list_view.html'
    objects = EmpresaFilter(queryset=Empresa.objects.all())

    def get_context_data(self, **kwargs):
        context = super(EmpresaListView, self).get_context_data()
        context['empresa_list'] = EmpresaFilter(self.request.GET, queryset=Empresa.objects.all())
        context['request'] = self.request
        return context


class EmpresaEditView(UpdateView):
    model = Empresa
    template_name = 'empresa_edit_view.html'
    form_class = EmpresaForm


class DataClipperEditView(UpdateView):
    model = DataClipper
    template_name = 'dataclipper_edit_view.html'
    form_class = DataClipperForm


class EmpresaDetailView(DetailView):
    model = Empresa
    context_object_name = 'empresa'
    template_name = 'empresa_detail_view.html'

    def get_context_data(self, **kwargs):
        context = super(EmpresaDetailView, self).get_context_data(**kwargs)
        context['cont_empresa'] = ContEmpresa.objects.get(pk=self.object.cod_contribuyente)
        context['contribuenta_emp_list'] = ContribuentaEmp.objects.filter(
            cod_contribuyente=self.object.cod_contribuyente)
        context['sucursal_list'] = Sucursal.objects.filter(cod_empresa=self.object.cod_empresa)
        try:
            context['data_clipper'] = DataClipper.objects.get(pk=self.object.cod_empresa)
        except ObjectDoesNotExist:
            context['data_clipper'] = None
        return context

    # def get_success_url(self):
    #     return reverse_lazy('empresa.list')
    #
    # def post(self, request, *args, **kwargs):
    #     pk = self.kwargs.get('pk', None)
    #
    #     if pk is not None:
    #         empresa = Empresa.objects.get(pk=pk)
    #     else:
    #         raise AttributeError(u"Could not save Empresa with pk %s" % pk)
    #
    #     form = EmpresaForm(request.POST, instance=empresa)
    #
    #     if form.is_valid():
    #         self.object = Empresa.objects.raw(
    #             u"UPDATE Tbl_Empresa SET Cod_Empresa='%s', Cod_Contribuyente=%d, Grupo_Cont=%d WHERE Cod_Empresa = 'Testing'" % (
    #             'Testing2', 8888, 8888))
    #         return HttpResponseRedirect(self.get_success_url())


class ContEmpresaEditView(UpdateView):
    model = ContEmpresa
    template_name = 'cont_empresa_edit_view.html'
    form_class = ContEmpresaForm


class DashboardView(TemplateView):
    template_name = 'dashboard.html'


class ContEmpresaListView(ListView):
    paginate_by = 20
    model = ContEmpresa
    context_object_name = 'cont_empresa_list'
    template_name = 'contEmpresa_list_view.html'


class DataClipperListView(ListView):
    paginate_by = 20
    model = DataClipper
    context_object_name = 'data_clipper_list'
    template_name = 'dataClipper_list_view.html'

    def get_context_data(self, **kwargs):
        context = super(DataClipperListView, self).get_context_data()
        context['request'] = self.request
        return context

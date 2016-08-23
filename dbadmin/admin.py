from django.contrib import admin

from models import ContEmpresa, DataClipper, Empresa, Company


class ContEmpresaAdmin(admin.ModelAdmin):
    list_display = ['cod_cont_empresa', 'nom_contribuyente']
    search_fields = ['nom_contribuyente']


# class CodContribuyenteEmpAdmin(admin.ModelAdmin):
#     list_display = ['cod_contribuyente', 'dir_contribuyente']
#     search_fields = ['dir_contribuyente']


class DataClipperAdmin(admin.ModelAdmin):
    search_fields = ['codigo', 'dueno', 'empresa', 'direccion', 'xtra']
    list_display = ['codigo', 'dueno', 'empresa', 'direccion', 'xtra']


class EmpresaAdmin(admin.ModelAdmin):
    change_form_template = 'change_form.html'
    list_display = ['cod_empresa', 'cod_contribuyente', 'grupo_cont']

    def get_associated_objects(self, form):
        return DataClipper.objects.all()


class CompanyAdmin(admin.ModelAdmin):
    fields = ['empresa_fk']


admin.site.register(ContEmpresa, ContEmpresaAdmin)
# admin.site.register(ContribuyenteEmp, CodContribuyenteEmpAdmin)
admin.site.register(DataClipper, DataClipperAdmin)
admin.site.register(Empresa, EmpresaAdmin)
admin.site.register(Company)

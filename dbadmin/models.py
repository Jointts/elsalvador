# coding=utf-8

from __future__ import unicode_literals
from django.db import models
from django.db import connection
from django.db.models import QuerySet


# class CompanyManager(models.Manager):
#
#     # def get_queryset(self):
#     #     QuerySet.raw()
#     #     cursor = connection.cursor()
#     #     cursor.execute("""
#     #         SELECT * FROM dbo.DATA_CLIPPER
#     #         """)
#     #     result_list = []
#     #     for row in cursor.fetchall():
#     #         p = self.model(xtra=row[0], codigo=row[1], dueno=row[2], empresa=row[3], direccion=row[4])
#     #         result_list.append(p)
#     #     return result_list
#
#     def get_queryset(self):
#         cursor = connection.cursor()
#         cursor.execute("""
#                 SELECT * FROM dbo.DATA_CLIPPER
#                 """)
#         results = cursor.fetchall()[:4]
#         querySet = QuerySet(self.model, using=self._db)
#         querySet.query.select = cursor.fetchall()[:4]
#         return querySet


class Company(models.Model):
    pass


class Empresa(models.Model):
    cod_empresa = models.CharField(max_length=10, db_column="Cod_Empresa", primary_key=True)
    cod_contribuyente = models.IntegerField(db_column="Cod_Contribuyente")
    grupo_cont = models.IntegerField(db_column="Grupo_Cont")

    class Meta:
        managed = False
        db_table = 'Tbl_Empresa'

    def __unicode__(self):
        return self.cod_empresa


# class ContribuyenteEmp(models.Model):
#     cod_contribuyente = models.IntegerField(primary_key=True)
#     nit_contribuyente = models.CharField(max_length=500)
#     dir_contribuyente = models.IntegerField()
#
#     class Meta:
#         managed = False
#         db_table = 'Tbl_contribuyente_emp'
#
#     def __unicode__(self):
#         return self.cod_contribuyente


class ContEmpresa(models.Model):
    cod_cont_empresa = models.IntegerField(primary_key=True, db_column="Cod_Cont_Empresa")
    nom_contribuyente = models.CharField(db_column="Nom_Contribuyente", max_length=500)
    grupo_cont = models.IntegerField()
    cod_contribuyente = models.IntegerField(db_column="Cod_Contribuyente")

    class Meta:
        managed = False
        db_table = 'Tbl_Cont_Empresa'

    def __unicode__(self):
        return self.nom_contribuyente


class DataClipper(models.Model):
    xtra = models.CharField(max_length=500, db_column="XTRA")
    codigo = models.CharField(max_length=500, db_column="CODIGO", primary_key=True)
    dueno = models.CharField(max_length=500, db_column="DUEÑO")
    empresa = models.CharField(max_length=500, db_column="EMPRESA")
    direccion = models.CharField(max_length=500, db_column="DIRECCION")

    class Meta:
        managed = False
        db_table = 'DATA_CLIPPER'

    def __unicode__(self):
        return self.codigo


class ContribuentaEmp(models.Model):
    cod_contribuyente = models.IntegerField(primary_key=True)
    nit_contribuyente = models.CharField(max_length=17)
    dir_contribuyente = models.CharField(max_length=500)

    class Meta:
        managed = False
        db_table = 'Tbl_contribuyente_emp'

    def __unicode__(self):
        return self.cod_contribuyente


class Sucursal(models.Model):
    cod_sucursal = models.CharField(max_length=10, db_column="Cod_sucursal", primary_key=True)
    cod_empresa = models.CharField(max_length=10, db_column="Cod_empresa")
    cod_extra = models.CharField(max_length=3, db_column="Cod_extra")
    nom_emp = models.CharField(max_length=150, db_column="Nom_Emp")
    #fecha_apertura = models.DateTimeField(db_column="Fecha_Apertura", blank=False, null=True, default=False)
    dkey = models.CharField(max_length=10, db_column="Dkey")
    cod_conta = models.CharField(max_length=10, db_column="Cod_Conta")
    cod_estado = models.IntegerField(db_column="Cod_Estado")
    iva = models.CharField(max_length=10, db_column="IVA")
    estado_dueda = models.BooleanField(db_column="Estado_deuda")
    #fecha_cierre = models.DateTimeField(db_column="Fecha_Cierre", blank=False, null=True, default=False)
    #fecha_tramite = models.DateTimeField(db_column="Fecha_Tramite", blank=False, null=True, default=False)
    #exento_impuesto = models.DateTimeField(db_column="Exento_Impuesto", blank=False, null=True, default=False)
    estado_multa = models.BooleanField(db_column="Estado_Multa")
    estado_complemento = models.BooleanField(db_column="Estado_Complemento")
    #fecha_creacion = models.DateTimeField(db_column="Fecha_Creacion", blank=False, null=True, default=False)
    migrado = models.BooleanField(db_column="Migrado")
    #fec_migrado = models.DateTimeField(blank=False, null=True, default=False)
    id_usu_migrado = models.BooleanField()
    deu_verificada = models.BooleanField()
    #fec_deu_verificada = models.DateTimeField(blank=False, null=True, default=False)
    id_usu_deu_verificada = models.IntegerField()
    cod_asignado = models.IntegerField()
    es_pue_mercado = models.BooleanField()

    class Meta:
        managed = False
        db_table = 'Tbl_Sucursal'


class Licencia(models.Model):
    cod_licencia = models.IntegerField(primary_key=True)
    cod_sucursal = models.CharField(max_length=10)
    cod_ordenanza = models.IntegerField()
    valor_licencia = models.IntegerField()
    desc_licencia = models.CharField(max_length=500)
    fecha_licencia = models.DateTimeField(db_column="Fecha_licencia")
    cantidad = models.IntegerField(db_column="Cantidad")
    abonado = models.IntegerField(db_column="Abonado")
    pagado = models.BooleanField(db_column="Pagado")

    class Meta:
        managed = False
        db_table = 'Tbl_Licencias'
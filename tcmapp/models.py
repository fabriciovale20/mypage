from django.db import models


class Categoria(models.Model):
    tipo_name = models.CharField(max_length=30)  # Tipo do Equipamento (Roteador, ONU...)

    def __str__(self):
        return self.tipo_name

    class Meta:
        ordering = ['tipo_name']


class Marca(models.Model):
    marca_name = models.CharField(max_length=30)  # Marca (TP-Link, Intelbras...)

    def __str__(self):
        return self.marca_name

    class Meta:
        ordering = ['marca_name']


class Modelo(models.Model):
    modelo_name = models.CharField(max_length=100)  # Modelo (Archer C20, DPC3825...)

    def __str__(self):
        return self.modelo_name

    class Meta:
        ordering = ['modelo_name']


class Situacao(models.Model):
    situacao_name = models.CharField(max_length=30)  # Modelo (Archer C20, DPC3825...)

    def __str__(self):
        return self.situacao_name

    class Meta:
        verbose_name_plural = 'Situações'


class Cadastro(models.Model):
    categoria = models.ForeignKey(Categoria, null=True, on_delete=models.CASCADE)
    marca = models.ForeignKey(Marca, null=True, blank=True, on_delete=models.CASCADE)
    modelo = models.ForeignKey(Modelo, null=True, on_delete=models.CASCADE)
    macsn_name = models.CharField(null=True, max_length=30)  # MAC ou Nº de Série
    valor = models.DecimalField(null=True, max_digits=7, decimal_places=2)  # Valor
    situacao = models.ForeignKey(Situacao, null=True, on_delete=models.CASCADE)
    informacoes = models.TextField(null=True, blank=True)
    register_date = models.DateTimeField(null=True, auto_now_add=True)  # Data de registro

    def __str__(self):
        return self.macsn_name  # Comando para retornar o MAC ou Nº de Série na pagina ADMIN

    class Meta:
        ordering = ['categoria']

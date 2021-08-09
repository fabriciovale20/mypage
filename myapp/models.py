from django.db import models


class Categoria(models.Model):
    tipo_name = models.CharField(max_length=30)

    def __str__(self):
        return self.tipo_name

    class Meta:
        ordering = ['tipo_name']


class Marca(models.Model):
    marca_name = models.CharField(max_length=30)

    def __str__(self):
        return self.marca_name

    class Meta:
        verbose_name = 'Marca'
        ordering = ['marca_name']


class Modelo(models.Model):
    modelo_name = models.CharField(max_length=100)

    def __str__(self):
        return self.modelo_name

    class Meta:
        ordering = ['modelo_name']


class Situacao(models.Model):
    situacao_name = models.CharField(max_length=30)

    def __str__(self):
        return self.situacao_name

    class Meta:
        verbose_name = 'Situação'
        verbose_name_plural = 'Situações'


class Imagem(models.Model):
    imagem_name = models.ImageField(upload_to='equip')

    def __str__(self):
        return f'{self.imagem_name}'

    class Meta:
        verbose_name_plural = 'Imagens'
        ordering = ['-id']


class Cadastro(models.Model):
    categoria = models.ForeignKey(Categoria, null=True, on_delete=models.CASCADE, verbose_name='Equipamento')
    marca = models.ForeignKey(Marca, null=True, blank=True, on_delete=models.CASCADE)
    modelo = models.ForeignKey(Modelo, null=True, on_delete=models.CASCADE)
    macsn_name = models.CharField(null=True, max_length=30, verbose_name='Identificação do Produto')
    valor = models.DecimalField(null=True, max_digits=7, decimal_places=2)
    imagem = models.ForeignKey(Imagem, null=True,
                               on_delete=models.CASCADE)
    situacao = models.ForeignKey(Situacao, null=True, on_delete=models.CASCADE, verbose_name='Situação')
    informacoes = models.TextField(null=True, blank=True)
    register_date = models.DateTimeField(null=True, auto_now_add=True)

    def __str__(self):
        return self.macsn_name

    class Meta:
        ordering = ['categoria']

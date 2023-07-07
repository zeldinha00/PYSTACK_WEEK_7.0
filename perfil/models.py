from django.db import models

# tabela Nova Categoria
class Categoria(models.Model): 
    categoria = models.CharField(max_length=50)
    essencial = models.BooleanField(default=False)
    valor_planejamento = models.FloatField(default=0)

    def __str__(self):
        return self.categoria
    
# tabela de contas
class Contas(models.Model):
    # Tipo de banco
    banco_choices = (
        ('NU', 'Nubank'),
        ('CX', 'Caixa Economica'),
        ('BR', 'Banco Brasil')
    )
    # tipos Pessoa fisica ou Juridica
    tipo_choices = (
        ('pf', 'Pessoa Física'),
        ('pj', 'Pessoa Jurídica')
    )
    #Tabela Nova Conta
    apelido = models.CharField(max_length=50)
    banco = models.CharField(max_length=2, choices=banco_choices)
    tipo = models.CharField(max_length=2, choices=tipo_choices)
    valor = models.FloatField()
    icone = models.ImageField(upload_to='icones')

    def __str__(self):
        return self.apelido
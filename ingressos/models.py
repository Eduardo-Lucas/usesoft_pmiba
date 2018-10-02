from django.db import models
from django.urls import reverse
from django.utils.translation import gettext as _


class Evento(models.Model):
    PUBLICO = 'PU'
    PRIVADO = 'PR'
    TIPO_DE_EVENTO_CHOICES = (
        ('PUBLICO', 'Público'),
        ('PRIVADO', 'Privado'),
    )
    nome = models.CharField(max_length=100, )
    data_inicio = models.DateTimeField(
        _("Data de Início"), auto_now=False, auto_now_add=False)
    data_termino = models.DateTimeField(
        _("Data de Término"), auto_now=False, auto_now_add=False)
    descricao = models.CharField(max_length=500, )
    publico_privado = models.CharField(
        max_length=2, choices=TIPO_DE_EVENTO_CHOICES, default=PUBLICO)
    local = models.CharField(max_length=100, )
    cep = models.name = models.CharField(max_length=8, blank=True, null=True)
    endereco = models.CharField(max_length=50, )
    numero = models.CharField(max_length=10, blank=True, null=True)
    bairro = models.CharField(max_length=20, blank=True, null=True)
    cidade = models.CharField(max_length=20, blank=True, null=True)
    uf = models.CharField(max_length=2, blank=True, null=True)

    class Meta:
        verbose_name = _("Evento")
        verbose_name_plural = _("Eventos")

    def __str__(self):
        return self.nome

    def get_absolute_url(self):
        return reverse("evento_detail", kwargs={"pk": self.pk})


class SubEventoTipo(models.Model):
    nome = models.name = models.CharField(max_length=50, )

    class Meta:
        verbose_name = "Tipo de SubEvento"
        verbose_name_plural = "Tipos de SubEventos"

    def __str__(self):
        return self.nome

    def get_absolute_url(self):
        return reverse("subeventotipo_detail", kwargs={"pk": self.pk})


class TipoIngresso(models.Model):
    nome = models.CharField(max_length=50, )

    class Meta:
        verbose_name = _("Tipo de Ingresso")
        verbose_name_plural = _("Tipos de Ingressos")

    def __str__(self):
        return self.nome

    def get_absolute_url(self):
        return reverse("tipoingresso_detail", kwargs={"pk": self.pk})


class SubEvento(models.Model):
    tipoingresso = models.ForeignKey('TipoIngresso', on_delete=models.CASCADE)
    subeventotipo = models.ForeignKey('SubEventoTipo', on_delete=models.CASCADE)
    evento = models.ForeignKey('Evento', on_delete=models.CASCADE)
    nome = models.name = models.CharField(max_length=50, )
    preco = models.DecimalField(_("Preço"), max_digits=10, decimal_places=2)
    gratis = models.BooleanField(_("Grátis"))
    quantidade = models.IntegerField(_("Quantidade"))
    inicio_vendas = models.DateTimeField(_("Início das vendas"), auto_now=False, auto_now_add=False)
    termino_vendas = models.DateTimeField(_("Término das vendas"), auto_now=False, auto_now_add=False)

    class Meta:
        verbose_name = "SubEvento"
        verbose_name_plural = "SubEventos"

    def __str__(self):
        return self.nome

    def get_absolute_url(self):
        return reverse("subevento_detail", kwargs={"pk": self.pk})

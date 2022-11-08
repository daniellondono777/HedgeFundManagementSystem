from doctest import COMPARISON_FLAGS
from email.policy import default
from unicodedata import name
from django.db import models
import datetime
from .asset_inspector import AssetInspector
import json

##############################################################################
##################### ENUMERATIONS ###########################################
##############################################################################

class Industry(models.TextChoices):
    HEALTH = 'H' #, 'Health'
    FINANCE = 'F' #, 'Finance'
    ENERGY = 'E' #, 'Energy'
    TOURISM = 'T' #, 'Tourism'
    REAL_ESTATE = 'RE' #, 'Real Estate'
    CONSULTING = 'C' #, 'Consulting'
    SOFTWARE = 'S' #, 'Software'
    OTHER = 'O' #, 'Other'

class Contract(models.TextChoices):
    ALPHA_1 = 'A1' #, 'Alpha 1'
    ALPHA_2 = 'A2' #, 'Alpha 2'
    BETA_1 = 'B1' #, 'Beta 1'
    BETA_2 = 'B2' #, 'Beta 2'

class Rank(models.TextChoices):
    PRESIDENT = 'P' #, 'President'
    SC_SENIOR = 'SCS' #, 'SC. Senior'
    ASSOCIATE = 'A' #, 'Associate'


class Security(models.TextChoices):
    STOCK = 'S' #, 'Stock'
    CORPORATE_BOND = 'CB' #, 'Corporate Bond'
    MORTGAGE_BOND = 'MB' #, 'Mortgage Bond'
    OTHER_MBS = 'OM' #, 'Other MBS'
    OTHER_ABS = 'AM' #, 'Other ABS'


##############################################################################
##################### ENTITIES ###############################################
##############################################################################

class Asset(models.Model):
    name = models.TextField(max_length=20)
    type = models.CharField(max_length=2, choices=Security.choices, default=Security.OTHER_ABS)
    quantity_usd = models.FloatField()
    issued_date = models.DateField()
    active_status = models.BooleanField(default=True)
    financial_indicators = models.JSONField()
    financial_news = models.JSONField()
    def save(self, *args, **kwargs):
        self.financial_indicators = AssetInspector(self.name).financial_indicator_getter()
        self.financial_news = AssetInspector(self.name).news_grouper()
        super(Asset, self).save()
    
    

    def __str__(self) -> str:
        return "Asset {}".format(id)

class ControlPanel(models.Model):
    def _formated_date() -> str:
        today = datetime.date.today()
        return "{d}-{m}-{y}".format(d=today.day, m=today.month, y=today.year)
    today = _formated_date()
    name = models.TextField(max_length=30, default="ControlPanel.:{}".format(today))
    equity = models.FloatField(editable=True)
    quarter_performance = models.FloatField(editable=True)
    daily_performance = models.FloatField(editable=True)
    managed_assets = models.ManyToManyField(Asset,default=None, blank=True)

class Employee(models.Model):
    name = models.TextField(max_length=30)
    rank = models.CharField(max_length=3, choices=Rank.choices, default=Rank.ASSOCIATE)
    transactions = models.TextField(editable=True)
    comission_percentage = models.FloatField()
    overall_performance = models.FloatField(editable=True)
    managed_assets = models.ManyToManyField(Asset,default=None, blank=True)
    control_panel = models.ForeignKey(ControlPanel, on_delete=models.SET_NULL, null=True)

    def __str__(self) -> str:
        return "Employee {}".format(id)


class Client(models.Model):
    name = models.TextField(max_length=30)
    occupation_industry = models.CharField(max_length=2, choices=Industry.choices, default=Industry.OTHER)
    invested = models.FloatField()
    contract = models.CharField(max_length=2, choices=Contract.choices, default=Contract.ALPHA_1)
    start_date = models.DateField()
    active_status = models.BooleanField(default=True)
    control_panel = models.ForeignKey(ControlPanel, on_delete=models.SET_NULL, null=True)

    def __str__(self) -> str:
        return "Client {}".format(id)

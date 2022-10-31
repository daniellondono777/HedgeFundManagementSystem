from dataclasses import field
from rest_framework import serializers
from .models import *

##############################################################################
##################### Serializers ############################################
##############################################################################

class ControlPanelSerializer(serializers.ModelSerializer):
    class Meta:
        model = ControlPanel
        fields = '__all__'

class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employee
        fields = '__all__'

class ClientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Client
        fields = '__all__'

class AssetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Asset
        fields = '__all__'
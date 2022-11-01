from cgitb import lookup
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import * 

from rest_framework import generics
from rest_framework import mixins

from .models import *
import json


##############################################################################
##################### Custom Responses #######################################
##############################################################################

def _invalid_not_found():
    return Response({"invalid":"not found"}, status=404)

def _invalid_bad_request():
    return Response({"invalid":"incorrect data"}, status=400)


##############################################################################
##################### CRUD Employee ##########################################
##############################################################################

class EmployeeListAPIView(generics.ListAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer

employee_list_view = EmployeeListAPIView.as_view()

class EmployeeDetailAPIView(generics.RetrieveAPIView):
    queryset = Employee.objects.all()
    lookup_field = 'pk'
    serializer_class = EmployeeSerializer

employee_detail_view = EmployeeDetailAPIView.as_view()

class EmployeeUpdateAPIView(generics.UpdateAPIView):
    queryset = Employee.objects.all()
    lookup_field = 'pk'
    serializer_class = EmployeeSerializer

employee_update_view = EmployeeUpdateAPIView.as_view()

class EmployeeDestroyAPIView(generics.DestroyAPIView):
    queryset = Employee.objects.all()
    lookup_field = 'pk'
    serializer_class = EmployeeSerializer

employee_delete_view = EmployeeDestroyAPIView.as_view()

class EmployeeCreateAPIView(generics.CreateAPIView):
    serializer_class = EmployeeSerializer

employee_create_view = EmployeeCreateAPIView.as_view()



##############################################################################
##################### CRUD Client ############################################
##############################################################################

class ClientMixinView(
    mixins.DestroyModelMixin,
    mixins.UpdateModelMixin,
    mixins.CreateModelMixin,
    mixins.ListModelMixin,
    mixins.RetrieveModelMixin,
    generics.GenericAPIView
    ):
    queryset = Client.objects.all()
    serializer_class = ClientSerializer
    lookup_field = 'pk'

    def get(self, request, *args, **kwargs):
        pk = kwargs.get('pk')
        if pk is not None:
            return self.retrieve(request, *args, **kwargs)
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)
    
    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)
    
    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)
    

client_mixin_view = ClientMixinView.as_view()

##############################################################################
##################### CRUD Assets ############################################
##############################################################################

class AssetMixinView(
    mixins.DestroyModelMixin,
    mixins.CreateModelMixin,
    mixins.UpdateModelMixin,
    mixins.ListModelMixin,
    mixins.RetrieveModelMixin,
    generics.GenericAPIView
    ):
    queryset = Asset.objects.all()
    serializer_class = AssetSerializer

    ### 
    ### Assets should be accesible for every member of the Hedge Fund

    authentication_classes = []
    permission_classes = []
    
    ### 
    
    lookup_field = 'pk'

    def get(self, request, *args, **kwargs):
        pk = kwargs.get('pk')
        if pk is not None:
            return self.retrieve(request, *args, **kwargs)
        return self.list(request, *args, **kwargs)
    
    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)
    
    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)
    
    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)

asset_mixin_view = AssetMixinView.as_view()

##############################################################################
##################### CRUD ControlPanel ######################################
##############################################################################

@api_view(['GET'])
def get_control_panel(request, pk):
    queryset = ControlPanel.objects.filter(pk=pk).first()
    data = ControlPanelSerializer(queryset, many=False).data
    return Response(data)

@api_view(['GET'])
def get_control_panels(request):
    queryset = ControlPanel.objects.all()
    data = ControlPanelSerializer(queryset, many=True).data
    return Response(data)

@api_view(['POST'])
def create_control_panel(request):
    data = json.loads(request.body)
    serializer = ControlPanelSerializer(data=data)
    if serializer.is_valid(raise_exception=True):
        cp = ControlPanel.objects.create(
            name = serializer.validated_data.get('name'),
            equity = serializer.validated_data.get('equity'),
            quarter_performance = serializer.validated_data.get('quarter_performance'),
            daily_performance = serializer.validated_data.get('daily_performance'),
        )
        cp.save()
        return Response(serializer.data)

@api_view(['PUT'])
def update_control_panel(request, pk):
    json_data = json.loads(request.data)
    cp = ControlPanel.objects.filter(pk=pk)
    cp.update(
        name = json_data.get('name'),
        equity = json_data.get('equity'),
        quarter_performance = json_data.get('quarter_performance'),
        daily_performance = json_data.get('daily_performance')
    )
    return Response(ControlPanelSerializer(cp.first(), many=False).data)

@api_view(['DELETE'])
def delete_control_panel(request, pk):
    cp = ControlPanel.objects.filter(pk=pk)
    cp.delete()
    return Response({f"Success":"Control Panel with ID {pk} deleted successfully."})
        
    
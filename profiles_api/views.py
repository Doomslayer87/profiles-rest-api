from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status # http status codes
from profiles_api import serializer
from rest_framework import viewsets

class HelloApiView(APIView):
    """Test API view"""
    
    serializer_class = serializer.HelloSerializer
    
    def get(self, request, format=None):    # anche se il formato non deve essere per forza specificato è bene impostarlo come par. va ad aggiungere un'estensione 
        """Returns a list of APIView features"""
        an_apiview = [
            'Uses HTTP methods as function (get,post,patch,put,delete)',
            'is similar to a traditional Django View',
            'Gives you the most control over your application logic',
            'Is mapped manually to URLs',
            ]
        return Response({
            'message': 'Hello',
            'an_apiview': an_apiview
        }) 
    
    def post(self, request):
        """Create a hello message with our name. innanzitutto recupera la classe serializer dal modulo serializer.py e gli assegna i 'data' come parametro. durante una POST request vengono passati i dati"""
        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid(): # is_valid è la funzione standard per la validazione dei dati di un serializer
            name = serializer.validated_data.get('name') # validated_data è un flag assegnato in caso di dati validi
            message = f"Hello, {name}"
            return Response({
                'message': message
            })
        else:
            return Response(
                serializer.errors, 
                status=status.HTTP_400_BAD_REQUEST
                )
    
    def put(self, request, pk=None):
        """Handle updating objects. il metodo PUT è utilizzato per gli update degli oggetti. Lo si esegue su una specifica chiave primaria URL (parametro pk). sostituisce il valore dell'intero oggetto con un nuovo valore"""
        return Response({'method': 'PUT',})
    
    def patch(self, request, pk=None):
        """Handle a partial update of an object. questo metodo esegue l'update solo dei campi richiesti dall'update. al contrario di PUT, esegue l'update solo di un campo e non dell'intero oggetto"""
        return Response({'method': 'PATCH'})
    
    def delete(self, request, pk=None):
        """Delete an object. Rimuove oggetti dal DB"""
        return Response({'method': 'DELETE'})

class HelloViewSet(viewsets.ViewSet):
    """Test API viewsets. mentre nell'APIview definiamo funzioni per le richieste HTTP che si vogliono supportare, nei viewset le funzioni rappresentano azioni che l'API deve compiere"""
    
    serializer_class = serializer.HelloSerializer

    def list(self, request):
        """Return a hello message"""
        a_viewset = [
            'uses actions (list, create, retrieve, update, partial_update)',
            'automatically maps to URL using Routers',
            'Provides more functionality with less code'
        ]
        return Response({
            'message': 'Hello',
            'a_viewset': a_viewset
        })
    
    def create(self, request):
        """Create a new hello message"""
        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            name = serializer.validated_data.get('name')
            message = f"Hello {name}"
            return Response({'message': message})
        else:
            return Response(
                serializer.errors,
                status=status.HTTP_400_BAD_REQUEST
            )

    def retrieve(self, request, pk=None):
        """Handle getting an object by its ID"""
        return Response({'http_method': 'GET'})
    
    def update(self, request, pk=None):
        """Handle updating an object"""
        return Response({
            'http_method': 'PUT'
        })
    
    def partial_update(self, request, pk=None):
        """Handle partial updating an object"""
        return Response({
            'http_method': 'PATCH'
        })
    
    def destroy(self, request, pk=None):
        """Handle removing an object"""
        return Response({
            'http_method': 'DELETE'
        })
    
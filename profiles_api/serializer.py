from rest_framework import serializers

class HelloSerializer(serializers.Serializer):
    """Serializers a name field for testing an api view. accepts a name input to add to api view as a POST request. funzionano come form da compilare. forniscono una validazione dei dati. nel caso qui sotto controlla che il dato non superi i 10 caratteri"""
    name = serializers.CharField(max_length=10)


from rest_framework.generics import GenericAPIView

from api.models import Salaries
from api.serializers import SalariesSerializer
from rest_framework.response import Response
from rest_framework import status


class SalariesAPIView(GenericAPIView):
    queryset = Salaries.objects.all()
    serializer_class = SalariesSerializer

# Question 1
# This is method get the parameter name and then reload the table

    def get(self, request, *args, **kwargs):
        name = request.GET["name"]
        queryset = Salaries.objects.filter(name__icontains=name)
        queryset = self.paginate_queryset(queryset=self.queryset)
        serializer = SalariesSerializer(instance=queryset, many=True)
        return self.get_paginated_response(serializer.data)

# Question 2
# This method is to make the post

    def post(self, request, format=None):
        serializer = SalariesSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# Question 3
# Create a new REST API resource that allows the partial update of a single row of the salaries table
    def put(self, request, pk, format=None):
        salary = self.get_object(pk)
        serializer = SnippetSerializer(snippet, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

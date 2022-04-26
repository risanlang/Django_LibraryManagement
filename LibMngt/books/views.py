from rest_framework.decorators import api_view
from rest_framework.response import Response
from . models import Book
from . serializers import BookSerializer
from rest_framework import serializers
from rest_framework import status
from django.shortcuts import get_object_or_404
  
@api_view(['GET'])
def RuleOverview(request):
    api_urls = {
        'all_books': '/',
        'Add': '/create',
        'Update': '/update/id_number_to_delete',
        'Delete': '/delete/id_number_to_delete'
    }
  
    return Response(api_urls)
    
@api_view(['GET'])
def book_list(request):
    
    # checking for the parameters from the URL
    if request.query_params:
        items = Book.objects.filter(**request.query_param.dict())
    else:
        items = Book.objects.all()
  
    # if there is something in items else raise error
    if items:
        data = BookSerializer(items,many=True)
        return Response(data.data)
    else:
        return Response(status=status.HTTP_404_NOT_FOUND)
        
        
@api_view(['POST'])
def update_book(request, pk):
    item = Book.objects.get(pk=pk)
    data = BookSerializer(instance=item, data=request.data)
  
    if data.is_valid():
        data.save()
        return Response(data.data)
    else:
        return Response(status=status.HTTP_404_NOT_FOUND)
        
@api_view(['DELETE'])
def delete_book(request, pk):
    item = get_object_or_404(Book, pk=pk)
    item.delete()
    return Response(status=status.HTTP_202_ACCEPTED)


@api_view(['POST'])
def add_book(request):
    item = BookSerializer(data=request.data)
  
    # validating for already existing data
    if Book.objects.filter(**request.data).exists():
        raise serializers.ValidationError('This data already exists')
  
    if item.is_valid():
        item.save()
        return Response(item.data)
    else:
        return Response(status=status.HTTP_404_NOT_FOUND)
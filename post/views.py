from django.shortcuts import render, redirect, get_object_or_404, HttpResponseRedirect
from rest_framework import status, viewsets
from rest_framework.decorators import api_view 
from rest_framework.response import Response 
from django.http.response import HttpResponse
from .models import Post
from .serializers import PostSerializer
from drf_writable_nested import WritableNestedModelSerializer

# Create your views here.
@api_view(['GET'])
def postList(request):
    posts = Post.objects.all()
    serailized_posts= PostSerializer(posts, many=True)
    return Response(serailized_posts.data) 


@api_view(['GET'])    
def viewMyPost(request):
    myPost = list(Post.objects.filter(user_id=4))
    serailized_posts= PostSerializer(myPost, many=True)
    return Response(serailized_posts.data) 

    #ex1 = store.orderlist_set.all().filter(order_time__range=(start_date, end_date))
    #ex1 = list(store.orderlist_set.all().filter(order_time__range=(start_date, end_date)).values())



#@api_view(['POST'])
#def post_api(request):
#    if request.method == 'GET':
#        return HttpResponse(status=200)
#    if request.method == 'POST': 
#        serializer = PostSerializer(data = request.data, many=True)
#        if(serializer.is_valid()):
#            serializer.save()
#            return Response(serializer.data ,status=200)
#        return Response(serializer.errors ,status=status.HTTP_400_BAD_REQUEST)

# Post의 목록, detail 보여주기, 수정하기, 삭제하기 모두 가능
class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
   
   	# serializer.save() 재정의
    def perform_create(self, serializer):
        serializer.save()        


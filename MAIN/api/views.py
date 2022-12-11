from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from MAIN.models import Post
from .serializers import PostSerializer


@api_view(["GET"])
def api_home_page(request):
    if request.method == "GET":
        posts = Post.objects.all()
        serializer = PostSerializer(posts, many=True)
        return Response(serializer.data)


@api_view(["GET"])
def api_detail_page(request, slug):
    try:
        post = Post.objects.get(slug=slug)
    except Post.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == "GET":
        serializer = PostSerializer(post)
        return Response(serializer.data)
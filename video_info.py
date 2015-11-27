from app.models import Video
from rest_condition import Or
from app.models import AppUser
from rest_framework import status
from rest_framework.views import APIView
from app.serializer import VideoSerializer
from rest_framework.response import Response
from oauth2_provider.ext.rest_framework import OAuth2Authentication
from rest_framework.authentication import SessionAuthentication, BasicAuthentication


class VideoInfo(APIView):
    authentication_classes = [OAuth2Authentication, BasicAuthentication, SessionAuthentication, ]
    # permission_classes = (Or(IsAuthenticated, TokenHasScope, ),)
    # required_scopes = ['read', 'write']

    def get(self, request):
        """
        ---
        response_serializer: VideoSerializer
        """
        video_id = int(request.GET.get('video_id'))
        name = request.GET.get('name')
        print(name)
        try:
            video = Video.objects.filter(name=name,video_id=video_id)
        except Video.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

        print(video)
        # if video.is_deleted == True:
        #     return Response(status = status.HTTP_404_NOT_FOUND)
        # is_like = 0
        # is_mine = 0
        # username = request.user
        # isUser = hasattr(request.user, 'appuser')
        #
        # if isUser == False and video.is_private == True:
        #     return Response(status=status.HTTP_404_NOT_FOUND)
        #     # return Response({"video":[],"is_like":0,"is_mine":0}, status=status.HTTP_200_OK)
        # if isUser == True:
        #     user = AppUser.objects.get(username = username)
        #     if video.user_id_id == user.id:
        #         is_mine = 1
        #     user_list = video.like.user_list.split(',')
        #     if str(user.id) in user_list:
        #         is_like = 1

        serializer = VideoSerializer(video,many=True)
        return Response({"video":serializer.data }, status=status.HTTP_200_OK)
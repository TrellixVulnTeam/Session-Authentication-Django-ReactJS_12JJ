from rest_framework.response import Response
from .serializers import UserProfileSerializer
from .models import UserProfile
from rest_framework.views import APIView

# Create your views here.
class GetUserProfileView(APIView):
    def get(self,request, format=None):
        try:
            user = self.request.user #getting an instance of a user
            username = user.username
            # user = User.objects.get(id=user.id), same as above

            user_profile = UserProfile.objects.get(user=user)
            user_profile = UserProfileSerializer(user_profile)

            return Response({'profile': user_profile.data, 'username': str(username)})
        except:
            return Response({'error':'Something went wrong trying to get user profile'})

class UpdateUserProfileView(APIView):

    def put(self, request, format=None):
        try:
            user = self.request.user
            username = user.username

            data = self.request.data
            first_name = data['first_name']
            last_name = data['last_name']
            phone = data['phone']
            city = data['city']

            UserProfile.objects.filter(user=user).update(first_name=first_name, last_name=last_name,phone=phone,city=city)

            user_profile = UserProfile.objects.get(user=user)
            user_profile = UserProfileSerializer(user_profile)

            return Response({'profile': user_profile.data, 'username': str(username)})
        except:
            return Response({'error':'Something went wrong Updating user profile'})

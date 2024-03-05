from rest_framework import serializers
from .models import UserProfile
from account.models import CustomUser




class UserProfileSerializer(serializers.ModelSerializer):
   class Meta:
      model = UserProfile
      fields = ('id','full_name', 'img', "city", "created_at")



class UserSerializer(serializers.HyperlinkedModelSerializer):
    profile = UserProfileSerializer(required=True)

    class Meta:
       model = CustomUser
       fields = ('email', 'first_name', 'last_name', 'password', 'profile')
       extra_kwargs = {
                 'password':
                           {'write_only': True}}





    def create(self, validated_data):
          profile_data = validated_data.pop('profile')
          password = validated_data.pop('password')
          user = User(**validated_data)
          user.set_password(password)
          user.save()
          UserProfile.objects.create(user=user, **profile_data)
          return user

    def update(self, instance, validated_data):
          profile_data = validated_data.pop('profile')
          profile = instance.profile

          instance.email = validated_data.get('email', instance.email)
          instance.save()

          profile.full_name = profile_data.get('full_name', profile.full_name)
          profile.img = profile_data.get('img', profile.img)
          profile.city = profile_data.get('city', profile.city)
          profile.save()

          return instance



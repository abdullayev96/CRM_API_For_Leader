from rest_framework import serializers
from .models import UserProfile
from account.models import User


# class UserProfileSerializer(serializers.ModelSerializer):
#     class Meta:
#         ref_name = "Profiles"
#         model = UserProfile
#         fields = ['full_name', 'number']
#
#
# class UserSerializer(serializers.ModelSerializer):
#     profile = UserProfileSerializer(required=True, many=False)
#
#     class Meta:
#         ref_name = "Profiles"
#         model = CustomUser
#         fields = ['username', 'email', 'first_name', 'last_name', 'profile']
#
#
#         def update(self, instance, validated_data):
#             userprofile_serializer = self.fields['profile']
#             userprofile_instance = instance.profile
#             profile_data = validated_data.pop('profile', {})
#
#             userprofile_serializer.update(userprofile_instance, profile_data)
#
#             instance = super().update(instance, validated_data)
#             return instance



class UserProfileSerializer(serializers.ModelSerializer):
      class Meta:
          ref_name = "Profiles"
          model  = UserProfile
          fields  = ['full_name','number']



class UserSerializer(serializers.HyperlinkedModelSerializer):
      #profile = UserProfileSerializer(required=True)

      class Meta:
          ref_name = "Profiles"
          model  = User
          fields  = ['id','email', 'username', 'password']
          extra_kwargs = {'password': {'write_only': True}}

      def create(self, validated_data):
          #profile_data = validated_data.pop('profile')
          password = validated_data.pop('password')
          user = User(**validated_data)
          user.set_password(password)
          user.save()


          UserProfile.objects.create(user=user)
          return user

      def update(self, instance, validated_data):
          # profile_data = validated_data.pop('profile')
          # profile = instance.profile

          instance.email = validated_data.get('email', instance.email)
          instance.username = validated_data.get('username', instance.username)
          instance.save()

          # profile.full_name = profile_data.get('full_name', profile.full_name)
          # profile.number = profile_data.get('number', profile.number)
          # profile.address = profile_data.get('address', profile.address)
          # profile.country = profile_data.get('country', profile.country)
          # profile.city = profile_data.get('city', profile.city)
          # profile.zip = profile_data.get('zip', profile.zip)
          #profile.save()

          return instance


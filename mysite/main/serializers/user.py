from rest_framework import serializers

from main.models import User


class UserTokenSerializer(serializers.ModelSerializer):
    token = serializers.SerializerMethodField()

    class Meta:
        model = User 
        fields = ('id', 'first_name', 'last_name', 'email', 'token',)

    def get_token(self, obj):
        return self.context.get('token')


class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)
    confirm_password = serializers.CharField(write_only=True)

    def validate(self, data):
        password = data.get('password')
        confirm_password = data.get('confirm_password')

        if password != confirm_password:
            raise serializers.ValidationError('Passwords do not match')

        return data

    def create(self, validated_data):
        
        first_name = validated_data.get('first_name', '')
        last_name = validated_data.get('last_name', '')
        email = validated_data.get('email')
        password = validated_data.get('password')
        age = validated_data.get('age', None)
        gender = validated_data.get('gender', '')

        user = User.objects.create(first_name=first_name, last_name=last_name,
                                   email=email, age=age, gender=gender)
        user.set_password(password)
        user.save()

        return user

    class Meta:
        model = User
        fields = ('id', 'first_name', 'last_name', 'email', 'age', 'gender',
                  'password', 'confirm_password')

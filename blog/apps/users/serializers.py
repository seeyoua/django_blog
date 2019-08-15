import re
from rest_framework import serializers
from rest_framework_jwt.settings import api_settings

from .models import UserProfile



class CreateUserSerializer(serializers.ModelSerializer):

    password2 = serializers.CharField(label="确认密码",write_only=True)
    allow = serializers.CharField(label="同意协议",write_only=True)
    token = serializers.CharField(label="登入状态的token",read_only=True)

    class Meta:
        model = UserProfile
        fields = [
            "id","username","password","password2","allow","token","email"
        ]
        """
            extra_kwargs = {'声明那些字段参与序列化,那些不参与序列化'}
        """
        extra_kwargs = {
            "username":{
                'min_length':5,
                'max_length':20,
                "error_messages":{
                    'min_length': '仅允许5-20个字符的用户名',
                    'max_length': '仅允许5-20个字符的用户名',
                }
            },
            "password":{
                'write_only':True,
                'min_length':8,
                'max_length':20,
                'error_messages':{
                    'min_length':"仅允许8-20个字符的密码",
                    'max_length': "仅允许8-20个字符的密码"

                }
            }

        }

        """
            是否遵守协议
        """
    def validatae_allow(self,status_code):
        print(status_code)
        if status_code !=True:
            raise serializers.ValidationError("请遵守协议")
        return status_code

    def validate_email(self,email):
        if not re.match(r'[0-9a-zA-Z_]{0,19}@163.com',email):
            raise  serializers.ValidationError("请正确添加邮箱")
        return email

    def validate(self,data):
        if data["password"] !=  data["password2"]:
            raise serializers.ValidationError("两次输入的密码不一致")
        return data

    def create(self,validated_data):

        # 删除模型类不存在的字段
        del validated_data["password2"]
        del validated_data["allow"]
        user = super().create(validated_data)
        #调用django 默认的加密
        user.set_password(validated_data["password"])
        user.save()

        # 保存注册数据之后，响应注册结果之前
                                        #
        jwt_payload_handler = api_settings.JWT_PAYLOAD_HANDLER #生成载荷
        jwt_encode_handler = api_settings.JWT_ENCODE_HANDLER
        #user 是当前的用户
        payload = jwt_payload_handler(user)
        token = jwt_encode_handler(payload)

        user.token = token
        return user

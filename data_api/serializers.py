from rest_framework import serializers
from .models import User
from .models import Checklist_item,checkoff_list,Room,Issue_report

class usersserializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'

class check_listitemserializer(serializers.ModelSerializer):
    class Meta:
        model = Checklist_item
        fields = '__all__'

class checkoff_listserializer(serializers.ModelSerializer):
    class Meta:
        model = checkoff_list
        fields = '__all__'

class Roomserializer(serializers.ModelSerializer):
    class Meta:
        model = Room
        fields = '__all__'

#class list_itemsserializer(serializers.ModelSerializer):
 #   class Meta:
  #      model = list_items
   #     fields = '__all__'

class Issue_reportserializer(serializers.ModelSerializer):
    class Meta:
        model = Issue_report
        fields = '__all__'

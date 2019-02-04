from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import User
from .serializers import usersserializer
from .serializers import check_listitemserializer,checkoff_listserializer,Roomserializer,Issue_reportserializer
from .models import Checklist_item,checkoff_list,Room,Issue_report



class userlist(APIView):
    def get(self, request):
        users = User.objects.all()
        serializer1 = usersserializer(users, many=True)
        return Response(serializer1.data)

    def post(self, request):
        serialpost1 = usersserializer(data=request.data)
        if serialpost1.is_valid():
            serialpost1.save()
            return Response(serialpost1.data, status=status.HTTP_201_CREATED)
        return Response(serialpost1.errors, status=status.HTTP_400_BAD_REQUEST)
        

class checklist_list(APIView):
    def get(self, request):
        checklist = Checklist_item.objects.all()
        serializer2 = check_listitemserializer(checklist, many=True)
        return Response(serializer2.data)
    def post(self, request):
        serialpost2 = check_listitemserializer(data=request.data)
        if serialpost2.is_valid():
            serialpost2.save()
            return Response(serialpost2.data, status=status.HTTP_201_CREATED)
        return Response(serialpost2.errors, status=status.HTTP_400_BAD_REQUEST)

class rooms(APIView):
    def get(self, request):
        room = Room.objects.all()
        serializer3 = Roomserializer(room, many=True)
        return Response(serializer3.data)
    def post(self, request):
        serialpost3 = Roomserializer(data=request.data)
        if serialpost3.is_valid():
            serialpost3.save()
            return Response(serialpost3.data, status=status.HTTP_201_CREATED)
        return Response(serialpost3.errors, status=status.HTTP_400_BAD_REQUEST)


class checkofflist(APIView):
    def get(self, request):
        checkofflist = checkoff_list.objects.all()
        serializer4 = checkoff_listserializer(checkofflist, many=True)
        return Response(serializer4.data)
    
    def post(self, request):
        serialpost4 = checkoff_listserializer(data=request.data)
        if serialpost4.is_valid():
            serialpost4.save()
            return Response(serialpost4.data, status=status.HTTP_201_CREATED)
        return Response(serialpost4.errors, status=status.HTTP_400_BAD_REQUEST)

#   def get(self, request):
 #       listitems = list_items.objects.all()
  #      serializer5 = list_itemsserializer(listitems, many=True)
   #     return Response(serializer5.data)
    #def post(self):
     #   serialpost5 = list_itemsserializer(request.data)
      #  if serialpost5.is_valid():
       #     serialpost5.save()
        #    return Response(serialpost5.data, status=status.HTTP_201_CREATED)
        #return Response(serialpost5.errors, status=status.HTTP_400_BAD_REQUEST)

class Issuereport(APIView):
    def get(self, request):
        issue = Issue_report.objects.all()
        serializer6 = Issue_reportserializer(issue, many=True)
        return Response(serializer6.data)
    def post(self, request):
        serialpost6 = Issue_reportserializer(data=request.data)
        if serialpost6.is_valid():
            serialpost6.save()
            return Response(serialpost6.data, status=status.HTTP_201_CREATED)
        return Response(serialpost6.errors, status=status.HTTP_400_BAD_REQUEST)

# Create your views here.

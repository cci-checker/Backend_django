from django.db import models

# Create your models here.
class User (models.Model):
    uniqueID = models.IntegerField()
    studentID = models.IntegerField("student uid")
    iCommonsSA_bool = models.BooleanField()
    lastname = models.CharField(max_length=30)
    firstname = models.CharField(max_length=30)
    rfid_number = models.IntegerField()
    Admin=models.BooleanField(default=False)

    def __str__(self):
        return self.firstname + ' '+ self.lastname;


##class Checkoff_instance (models.Model):
 #   checkoff_serialno = models.IntegerField()
 #   studentUID = models.IntegerField()
 #   roomID = models.IntegerField()
 #   date_time_stamp = models.DateTimeField()
 #   checklist_item_IDs = models.ManyToOneRel.one_to_many

class Checklist_item(models.Model):
    itemID = models.IntegerField()
    item_name = models.CharField(max_length=50)
    item_description = models.CharField(max_length=1000)
    active_status = models.BooleanField()
    #completed_status = models.BooleanField()

    def __str__(self):
        return self.item_name



#class list_items(models.Model):
 #   itemID = models.IntegerField()
  #  itemname = models.CharField(max_length=100)
   # itemdescription = models.CharField(max_length=10000)
#
 ##      return self.itemname

class Room(models.Model):
    roomID = models.IntegerField("roomid")
    building_name = models.CharField(max_length=100)
    floor_number = models.IntegerField()
    room_number = models.IntegerField()
    opening_list = models.ManyToManyField(Checklist_item, related_name="open_list")
    closing_list = models.ManyToManyField(Checklist_item, related_name="close_list")
    def __str__(self):
        return self.building_name+str(self.floor_number)+str(self.room_number);

class Issue_report(models.Model):
    issueID = models.IntegerField("issueid")
    roomID = models.ForeignKey(Room, on_delete=models.CASCADE, verbose_name="roomid")
    comment = models.CharField(max_length=140)
    photo = models.FileField(null=True, blank=True)
    student_UID = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="student uid")
    completed_status = models.BooleanField()

    def __str__(self):
        return self.comment

class checkoff_list(models.Model):
    #checkoff_listID = models.IntegerField()
    studentUID = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="student uid")
    #studentUID = models.IntegerField()
    #roomID = models.ForeignKey(Room, on_delete=models.CASCADE)
    roomID = models.ForeignKey(Room, on_delete=models.CASCADE, verbose_name="roomid")
    date_time_stamp = models.DateTimeField(auto_now_add=True)
    task_list = models.ManyToManyField(Checklist_item, related_name="task_list")
    task_completedlist = models.ManyToManyField(Checklist_item, related_name="task_completed_list")

    #list_itemID = models.ForeignKey(list_items, on_delete=models.CASCADE)
    #list_itemID = models.IntegerField()
    #completed_bool = models.BooleanField()
    #issueReport = models.ForeignKey(Issue_report, on_delete=models.CASCADE)
    issueReport = models.ForeignKey(Issue_report, on_delete=models.CASCADE, verbose_name="issueid")
    instance_name = models.CharField(max_length=100)
    def __str__(self):
        return self.instance_name













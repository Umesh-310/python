from rest_framework import serializers
from project.models import Student
# if we have more table connected to this table by foreign-key so
# to get all data follow this step for example think we have a table
# techer connet to the student
# import all modle
# ex:- Techer name and info comming from Techers in Student filed
# name is Techer so use that
#

# class TecherSerializer(serializers.ModelSerializer0):
#     class Meta:
#         # model = Techer
#         fields = '__all__'

# class MoreSerializer(serializers.ModelSerializer0):
#     class Meta:
#         # model = Techer
#         fields = '__all__'

##########################################################
# if we want to add more tables who not connected or have fileds in Student for that
# we can do this

# class ExtraTableSerializer(serializers.ModelSerializer0):
#     class Meta:
#         # model = Hobbeis
#         fields = '__all__'


class StudentSerializer(serializers.ModelSerializer):
    # techer = TecherSerializer(many = False or Ture) Depands of how many
    # more = MoreSerializer # filed are there
    # extra =  serializers.SerializerMethodField() than create a function
    class Meta:
        model = Student
        fields = '__all__'

    # def get_extra(self , obj): note : - always start with get
    #      extra_1 = obj.extra_set.all()
    #     serializer = ExtraTableSerializer(extra_1 , many = True)
    #     return serializer.data

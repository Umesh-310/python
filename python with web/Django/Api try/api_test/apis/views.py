from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework.response import Response
from .serializers import StudentSerializer
from project.models import Student


# Create your views here.

@api_view(['GET'])
def userData(request):
    userInfo = [
        {'name': 'Umesh Saini'},
    ]
    return Response(userInfo)


@api_view(['GET'])
# @permission_classes([IsAuthenticated]) most imp
def getStudents(request):
    student = Student.objects.all()
    serializer = StudentSerializer(student, many=True)

    return Response(serializer.data)


@api_view(['GET'])
def getStudent(request, pk):

    student = Student.objects.get(id=pk)
    serializer = StudentSerializer(student, many=False)

    return Response(serializer.data)


@api_view(['POST'])
def deleteStd(request):
    pk = request.data['id']
    student = Student.objects.get(pk=pk).delete()
    serializer = StudentSerializer(student, many=False)

    return Response(serializer.data)


@api_view(['PUT'])
def updateStd(request):
    pk = request.data['id']
    student = Student.objects.get(id=pk)
    data = request.data
    student.userName = data['userName']
    student.className = data['className']
    student.age = data['age']
    student.studentDetails = data['studentDetails']
    student.save()
    return Response(request.data)


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def addStudentname(request):
    student = Student()
    student.userName = request.data['userName']
    student.className = request.data['className']
    student.age = request.data['age']
    student.studentDetails = request.data['studentDetails']
    student.save()
    return Response(request.data)

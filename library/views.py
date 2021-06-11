from rest_framework.views import APIView
from .models import student
from rest_framework import serializers
from rest_framework.response import Response
from django.db import connection

class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = student
        fields = '__all__'

class SpitefulReader(APIView):
    def get(self, request):
        with connection.cursor() as cursor:
            cursor.execute("SELECT COUNT(library_book_issue.id) AS count_issue, library_book_issue.id_student_id "
                           "FROM library_book_issue "
                           "LEFT JOIN library_book_return ON library_book_return.id_issue_id = library_book_issue.id "
                           "WHERE library_book_return.id IS NULL "
                           "GROUP BY library_book_issue.id_student_id "
                           "ORDER BY count_issue DESC LIMIT 1")
            row = cursor.fetchall()

        row = str(row)
        id_student = int(row[row.find(',')+1:row.find(')')])
        queryset = student.objects.filter(id = id_student)
        serializer = StudentSerializer(queryset, many=True)
        return Response(serializer.data)

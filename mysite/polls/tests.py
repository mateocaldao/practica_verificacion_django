import datetime

from django.utils import timezone
from django.test import TestCase

"""import from models.py class Question"""
from .models import Question, Choice




class QuestionModelTest(TestCase):
    def test_new_poll(self):

        #creating a poll object
        poll = Question()
        poll.question_text = "Shall we begin?"
        poll.pub_date = timezone.now()
        poll.save()
        



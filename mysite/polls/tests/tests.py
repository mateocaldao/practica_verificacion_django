import datetime

from django.utils import timezone
from django.test import TestCase

"""import from models.py class Question"""
from mysite.polls.models import Question, Choice



class QuestionModelTest(TestCase):
    def test_new_poll(self):

        #creating a poll object
        poll = Question()
        poll.question_text = "Shall we begin?"
        poll.pub_date = timezone.now()
        poll.save()
        self.assertEquals(poll.question_text,"Shall we begin?")

    def test_total_votes_poll(self):

        #creating a poll object
        p = Question(question_text='Can I vote?', pub_date=timezone.now())
        p.save()
        self.assertTrue(p.total_votes(),0)


class ChoiceModelTest(TestCase):
    def test_creating_new_choice_and_saving_it_to_the_database(self):

        #creating a poll object
        poll = Question(question_text='What are my choices?', pub_date=timezone.now())
        poll.save()

        #creating a choice object
        choice = Choice(question=poll, choice_text='You have no choice', choice_votes=0)
        choice.save();

        #searching in database
        all_choices_in_database = poll.choice_set.all()
        only_choice_in_database = all_choices_in_database[0]

        self.assertEquals(only_choice_in_database,"You have no choice")

    def test_diferent_number_of_votes_in_question_and_choice(self):

        #creating a poll object
        p = Question(question_text='How are you?', pub_date=timezone.now())
        p.save()

        #creating first choice
        c1 = Choice(question=p, choice_text='Fine', choice_votes=2)
        c1.save()

        #creating second choice
        c2 = Choice(question=p, choice_text='Cool', choice_votes=4)
        c2.save()

        #correct number of choices in question
        number_of_votes = p.total_votes()

        self.assertNotEquals(number_of_votes,c1.votes())












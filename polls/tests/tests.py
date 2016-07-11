from django.test import TestCase
from django.utils import timezone
import datetime

"""import from models.py class Question"""
from polls.models import Question, Choice



class QuestionModelTest(TestCase):
    def test_new_poll(self):

        #creating a poll object
        poll = Question()
        poll.question_text = "Shall we begin?"
        poll.pub_date = timezone.now()
        poll.save()
        self.assertEquals(poll.question_text, "Shall we begin?")

    def test_total_votes_poll(self):

        #creating a poll object
        p = Question(question_text='Can I vote?', pub_date=timezone.now())
        p.save()
        self.assertEquals(p.total_votes(), 0)

        #searching in database
        all_polls_in_database = Question.objects.all()
        self.assertEquals(all_polls_in_database.count(), 1)


class ChoiceModelTest(TestCase):
    def test_creating_new_choice_and_saving_it_to_the_database(self):

        #creating a poll object
        poll = Question(question_text="What are my choices?", pub_date=timezone.now())
        poll.save()

        #creating a choice object
        choice = Choice(question=poll, choice_text="You have no choice", votes=0)
        choice.save()

        #searching in database
        all_choices_in_database = poll.choice_set.all()
        self.assertEquals(all_choices_in_database.count(), 1)

    def test_diferent_number_of_votes_in_question_and_choice(self):

        #creating a poll object
        p = Question(question_text='How are you?', pub_date=timezone.now())
        p.save()

        #creating first choice
        c1 = Choice(question=p, choice_text='Fine', votes=2)
        c1.save()

        #creating second choice
        c2 = Choice(question=p, choice_text='Cool', votes=4)
        c2.save()

        #correct number of choices in question
        number_of_votes = p.total_votes()

        self.assertEquals(number_of_votes, 6)












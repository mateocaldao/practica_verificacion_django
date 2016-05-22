import datetime
from django.utils import timezone
from django.db import models




class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')

    def __unicode__(self):
        return self.question_text

    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)

    def total_votes(self):
        return sum(c.votes for c in self.choice_set.all())


class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text= models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    def percentage(self):
        try:
            return 100.0 * self.votes / self.question.total_votes()
        except ZeroDivisionError:
            return 0

    def __unicode__(self):
        return self.choice_text
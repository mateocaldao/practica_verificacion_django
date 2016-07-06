Feature: Some poll tests

  Scenario: View poll main page
    Given I access the url(r'^$', views.IndexView.as_view(), name='index')
    Then I see h1 "Polls"

  Scenario: Create new poll
    Given I am a logged in user
    When I create a poll
    Then I see the new poll

  Scenario: Vote in a poll
    Given I access the url(r'^(?P<question_id>[0-9]+)/vote/$', views.vote, name='vote')
    When I vote in a poll
    Then I see the votes



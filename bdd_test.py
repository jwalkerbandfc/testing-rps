# bdd_test.py
from behave import given, when, then
from rps import play

@given("player one chooses {choice}")
def step_p1(context, choice):
    context.p1 = choice

@given("player two chooses {choice}")
def step_p2(context, choice):
    context.p2 = choice

@when("the game is played")
def step_play(context):
    context.result = play(context.p1, context.p2)

@then("the result should be {expected}")
def step_result(context, expected):
    assert context.result == expected

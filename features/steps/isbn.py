from behave import given, then, when
from main import is_valid_isbn10


@given('the printed ISBN "{isbn}"')
def printed(context, isbn):
    context.isbn = isbn


@when("the reader verifies the identifier")
def verify(context):
    context.valid = is_valid_isbn10(context.isbn)


@then("the result is {result}")
def check(context, result):
    assert context.valid == (result == "valid")

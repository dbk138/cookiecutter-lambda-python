# -*- coding: utf-8 -*-

""" Unit tests for the {{cookiecutter.lambda_name}} """

from {{cookiecutter.lambda_name}} import {{cookiecutter.lambda_name}}


def test_lambda_handler_returns_the_provided_username():
    event = {'name': 'Mr. Meeseeks'}
    context = None
    expected_result = 'Hi Mr. Meeseeks'
    actual_result = {{cookiecutter.lambda_name}}.lambda_handler(event, context)
    assert expected_result == actual_result

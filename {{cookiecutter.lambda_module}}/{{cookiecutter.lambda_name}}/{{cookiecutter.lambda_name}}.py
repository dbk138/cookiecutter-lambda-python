""" Lambda entry point """


def lambda_handler(event, context):
    """Starting point for an AWS Lambda function

    Args:
        event: AWS Lambda uses this parameter to pass in event data to the handler.
            This parameter is usually of the Python dict type.
            It can also be list, str, int, float, or NoneType type.
        context: AWS Lambda uses this parameter to provide runtime information to your handler.
            This parameter is of the LambdaContext type.

    Returns:
        A Hi message, of str type

    """
    name: str = event['name']
    return f'Hi {name}!'

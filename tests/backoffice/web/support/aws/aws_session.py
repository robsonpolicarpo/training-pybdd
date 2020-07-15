import os

import boto3

from tests.config.env import get_args


def aws_session():
    credential = credentials()
    return boto3.Session(
        aws_access_key_id=credential.get('key_id'),
        aws_secret_access_key=credential.get('secret_key')
    )


def credentials():
    key_id = os.getenv('AWS_KEY_ID') or get_args().aws_key
    access_key = os.getenv('AWS_SECRET_ID') or get_args().aws_secret
    if not key_id:
        raise ValueError(f"'AWS_KEY_ID' not found on enviroment")
    if not access_key:
        raise ValueError(f"'AWS_SECRET_ID' not found on enviroment")

    return {
        'key_id': key_id,
        'secret_key': access_key
    }

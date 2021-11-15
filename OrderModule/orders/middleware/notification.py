import boto3
import json
from orders.models import User


class Notification:

    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        # Before request
        response = self.get_response(request)
        # After request
        dic = {'path': '/infos/orders', 'method': 'POST'}
        after_request(request, dic)
        return response


def after_request(request, dic):

    if request.method in dic['method'] and request.path in dic['path']:
        requestDict = eval(request.body)
        if 'notification' in requestDict:
            notification = requestDict['notification']
            client = boto3.client('sns', region_name='us-east-1', aws_access_key_id='AKIARMJPIQNED64WNJNG'
                                  , aws_secret_access_key='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')
            client.publish(
                TargetArn='arn:aws:sns:us-east-1:095125275464:Could_Computing_Test',
                Message=json.dumps({'default': notification}),
                MessageStructure='json'
            )

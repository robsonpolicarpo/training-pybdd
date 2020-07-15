import logging

from tests.backoffice.web.support.aws.aws_session import aws_session


def get_dynamodb():
    return aws_session().resource(
        'dynamodb',
        region_name='us-east-1'
    )


def get_item(table_name, key, dynamodb=None):
    if not dynamodb:
        dynamodb = get_dynamodb()
    table = dynamodb.Table(table_name)
    return table.get_item(Key=key)


def update(table_name,
           key,
           update_expression,
           expression_attribute_values,
           dynamodb=None):
    if not dynamodb:
        dynamodb = get_dynamodb()
    table = dynamodb.Table(table_name)
    response = table.update_item(
        Key=key,
        UpdateExpression=update_expression,
        ExpressionAttributeValues=expression_attribute_values,
        ReturnValues="UPDATED_NEW"
    )
    return response


def delete_item(table_name,
                key,
                dynamodb=None):
    if not dynamodb:
        dynamodb = get_dynamodb()
    table = dynamodb.Table(table_name)
    response = table.delete_item(
        Key=key
    )
    return response


def delete_items(table_name,
                 key: dict,
                 dynamodb=None):
    if not dynamodb:
        dynamodb = get_dynamodb()
    table = dynamodb.Table(table_name)
    scan = table.scan()
    items_to_del = []
    for item in scan['Items']:
        if item.get('created_by') == 'robson.mendes@yandeh.com.br':
            items_to_del.append(item)
    for i, item in enumerate(items_to_del):
        ref = {'id': item['id'], 'type': item['type']}
        response = delete_item(table_name, ref)
        if response['ResponseMetadata']['HTTPStatusCode'] == 200:
            logging.info(f"Item deleted: {ref}")


def get_items(table_name, keys=None, dynamodb=None):
    if not dynamodb:
        dynamodb = get_dynamodb()
    table = dynamodb.Table(table_name)
    if keys:
        return table.scan(keys)
    return table.scan()


if __name__ == '__main__':
    key = {
        'created_by': 'robson.mendes@yandeh.com.br'
    }
    update_expression = "set start_date = :s"
    expression_attribute_values = {
        ':e': 'date'
    }
    delete_items('B2BBanner', key)

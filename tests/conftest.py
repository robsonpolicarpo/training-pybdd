import logging
import os
import shutil
from collections import defaultdict
from pathlib import Path

import pytest
import requests
from Naked.toolshed.shell import muterun_js
from boto3.dynamodb.conditions import Key

from tests.backoffice.web.support.aws import dynamo
from tests.config.driver_factory import get_browser, close


@pytest.fixture(scope="session")
def app():
    ui_driver = get_browser()
    yield ui_driver
    close(ui_driver.driver)


def pytest_configure(config):
    logging.getLogger(requests.packages.urllib3.__package__).setLevel(logging.ERROR)
    if Path('./test-results').exists():
        shutil.rmtree(Path('./test-results/').absolute())
    # Path('./test-results/allure').mkdir(parents=True, exist_ok=True)
    Path('./test-results/json').mkdir(parents=True, exist_ok=True)
    pytest.globalDict = defaultdict()
    pytest.globalDict.update({'scenarios_run': {}})
    pytest.globalDict['tokens_created'] = []
    pytest.globalDict['args'] = config.option


def pytest_sessionstart(session):
    project_variables = None
    if session.config._variables:
        project_variables = session.config._variables.get('project')
    pytest.globalDict['project'] = project_variables


def pytest_sessionfinish(session, exitstatus):
    banner_created = list(pytest.globalDict.get(
        'scenarios_run').keys()).__contains__('FT035 Banners')
    if banner_created:
        user_logged = 'robson.mendes@yandeh.com.br'
        delete_banner_dynamodb(user_logged)
        logging.info(f"Deleted all banners created by user '{user_logged}'")
    campaign_created = pytest.globalDict['tokens_created']
    if campaign_created:
        delete_campaign_dynamodb(campaign_created)


def delete_campaign_dynamodb(tokens_created):
    items_to_del = []
    logging.info(tokens_created)
    dynamo_con = dynamo.get_dynamodb()
    for token in tokens_created:
        rows = dynamo_con.Table('B2BCampaign').query(
            KeyConditionExpression=Key('id').eq(token)
        )
        items_to_del = items_to_del + rows['Items']
    for item in items_to_del:
        ref = {'id': item['id'], 'type': item['type']}
        response = dynamo.delete_item(table_name='B2BCampaign', key=ref, dynamodb=dynamo_con)
        if response['ResponseMetadata']['HTTPStatusCode'] == 200:
            logging.info(f"Deleted campaign: {ref}")
        else:
            logging.warning(f'Failed delete campaign: {ref}')


def delete_banner_dynamodb(created_by):
    dynamo_con = dynamo.get_dynamodb()
    table = dynamo_con.Table('B2BBanner')
    scan = table.scan()
    items_to_del = []
    for item in scan['Items']:
        if item.get('created_by') == created_by:
            items_to_del.append(item)
    for item in items_to_del:
        ref = {'id': item['id'], 'type': item['type']}
        dynamo.delete_item(table_name='B2BBanner', key=ref, dynamodb=dynamo_con)


def pytest_unconfigure(config):
    generate_reportjs()


def generate_reportjs():
    response = muterun_js(os.path.abspath('./scripts/reportjs.js'))
    if response.exitcode == 0:
        logging.info(response.stdout)
    else:
        logging.warning(str(response.stderr))


def pytest_addoption(parser):
    parser.addoption('--platform',
                     default='linux',
                     action='store',
                     help='Plataform to run: linux | android | ios')
    parser.addoption('--remote',
                     default='false',
                     action='store',
                     help='Environment to run: boolean')
    parser.addoption('--application',
                     default='chrome',
                     action='store')
    parser.addoption('--ipenv',
                     default='',
                     action='store',
                     help='IP address if run remote')
    parser.addoption('--headless',
                     default='false',
                     action='store',
                     help='Browser headless. true or false')
    parser.addoption('--aws-key',
                     action='store')
    parser.addoption('--aws-secret',
                     action='store')
    parser.addoption('--feature_path',
                     action="store",
                     help='Will export tests form given file or directory to TestRail')
    parser.addoption('--project',
                     action="store",
                     help='Project name in TestRail')
    parser.addoption('--export_results',
                     default='false',
                     action="store",
                     help='If false will not publish results to TestRail')

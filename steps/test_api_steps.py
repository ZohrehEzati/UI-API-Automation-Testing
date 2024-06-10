import json
import pytest
import requests
from pytest_bdd import scenarios, given, when, then, parsers, scenario

PETSTORE_BASE_URL = "https://petstore.swagger.io/v2"


@pytest.fixture
def context():
    return {}


# Start ---- Scenario: Add A New Pet To The Store
@given(parsers.cfparse('a new pet with ID {pet_id:d}, name "{name}", and status "{status}"'))
def create_pet_data(context, pet_id, name, status):
    context['data'] = {
        "id": pet_id,
        "category": {
            "id": 0,
            "name": "string"
        },
        "name": name,
        "photoUrls": [
            "string"
        ],
        "tags": [
            {
                "id": 0,
                "name": "string"
            }
        ],
        "status": status
    }


@when('I send a POST request to the /pet endpoint')
def create_pet(context):
    url = f"{PETSTORE_BASE_URL}/pet"
    response = requests.post(url, json=context['data'])
    context['response'] = response


@then('The response status code should be 200')
def verify_status_code(context):
    assert context['response'].status_code == 200


@then("the response body should be equal to pet's details")
def verify_pet_details(context):
    pet_details = context['response'].json()
    # print(json.dumps(pet_details, indent=4))
    # print(json.dumps(context['data'], indent=4))
    assert pet_details["id"] == context['data']['id']
    assert pet_details["name"] == context['data']['name']
    assert pet_details["status"] == context['data']['status']


# The End ---- Scenario: Add A New Pet To The Store


# Start ---- Scenario: Find Pets By ID

@given(parsers.cfparse('a pet with ID of {pet_id:d} exists'))
def set_pet_id(context, pet_id):
    context['pet_id'] = pet_id


@when(parsers.cfparse('I send the GET request to the /pet/{pet_id:d} endpoint'))
def get_pet_by_id(context):
    url = f"{PETSTORE_BASE_URL}/pet/{context['pet_id']}"
    response = requests.get(url)
    context['response'] = response


@then('The response status code should be 200')
def verify_status_code(context):
    assert context['response'].status_code == 200


@then('the response body should be equal to the pet details')
def verify_pet_details(context):
    pet_details = context['response'].json()
    assert pet_details['id'] == context['pet_id']


@scenario('../features/test_api.feature', 'Add A New Pet To The Store')
def test_add_a_new_pet():
    pass


@scenario('../features/test_api.feature', 'Find Pets By ID')
def test_find_a_pet_by_id():
    pass


""""
scenarios('../features/test_api.feature')


@pytest.mark.parametrize("scenario_name", [
    "Add A New Pet To The Store",
    "Find Pets By ID"
])
def test_scenario(scenario_name):
    pass
"""

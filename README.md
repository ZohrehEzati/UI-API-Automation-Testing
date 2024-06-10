## UI and API Automation Testing

## Description
This repository contains automated tests for the Petstore API using pytest-bdd.

## How to Run the Tests
1. Clone this repository to your local machine.
2. Navigate to the root directory of the project.
3. Install the required dependencies by running:
    ```
    pip install -r requirements.txt
    ```
4. Run the tests using pytest:
    ```
    pytest
    ```

## Test Scenarios
### Add A New Pet To The Store
- Description: This scenario tests the ability to add a new pet to the Petstore.
- Steps:
  1. Given a new pet with ID 20, name "babi", and status "available"
  2. When I send a POST request to the /pet endpoint
  3. Then The response status code should be 200
  4. And the response body should be equal to pet's details

### Find Pets By ID
- Description: This scenario tests the ability to find a pet by its ID.
- Steps:
  1. Given a pet with ID 20 exists
  2. When I send a GET request to the /pet/20 endpoint
  3. Then The response status code should be 200
  4. And the response body should be equal to pet details

## Why These Tests Are Important
1. **Coverage**: These tests cover critical functionality of the Petstore API, ensuring that basic operations like adding a new pet and retrieving pet details are working as expected.
2. **Regression Prevention**: By automating these tests, we can catch any regressions in the API behavior early in the development process, preventing issues from reaching production.
3. **Validation**: These tests validate the correctness of the API responses, helping to maintain data integrity and ensure a positive user experience.

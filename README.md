## My Sample Code For UI and API Automation Testing

## Branch: feature

## Description
This repository contains automated tests for the Petstore API and the UI of the UITestingPlayground website using pytest-bdd.

### Assignment Details
- **Environment and Specs:**
  - **UI Testing:** [UITestingPlayground](http://www.uitestingplayground.com/)
  - **API Testing:** [Petstore Swagger](https://petstore.swagger.io/)
- **Scripting Language:** Python
- **Testing Tool:** 
  - **UI Testing:** Selenium
  - **API Testing:** Requests library
- **CI Platform:** GitLab CI/CD

## How to Run the Tests
1. Clone this repository to your local machine.
2. Navigate to the root directory of the project.
3. Install the required dependencies by running:
    ```
    pip install -r requirements.txt
    ```
4. Run the API tests using pytest:
    ```
    pytest steps/test_api_steps.py
    ```

5. Run the UI tests using pytest:
    ```
    pytest steps/test_ui_steps.py
    ```

## Test Scenarios
### Add A New Pet To The Store (API)
- Description: This scenario tests the ability to add a new pet to the Petstore API.
- Steps:
  1. Given a new pet with ID 20, name "babi", and status "available"
  2. When I send a POST request to the /pet endpoint
  3. Then The response status code should be 200
  4. And the response body should be equal to pet's details

### Find Pets By ID (API)
- Description: This scenario tests the ability to find a pet by its ID using the Petstore API.
- Steps:
  1. Given a pet with ID 20 exists
  2. When I send a GET request to the /pet/20 endpoint
  3. Then The response status code should be 200
  4. And the response body should be equal to pet details

### Verify Button Click (UI)
- Description: This scenario tests the functionality of a button click on the UITestingPlayground website.
- Steps:
  1. Given I navigate to the click page
  2. When I click the button
  3. Then the button class should change to "btn-success"

### Verify Text Input (UI)
- Description: This scenario tests the functionality of text input on the UITestingPlayground website.
- Steps:
  1. Given I navigate to the text input page
  2. When I set the text "New Button Name" into the input field
  3. And I press the button
  4. Then the button text should be changed to "New Button Name"

## Why These Tests Are Important

### API Tests
1. **Coverage**: These tests cover critical functionality of the Petstore API, ensuring that basic operations like adding a new pet and retrieving pet details are working as expected.
2. **Validation**: API tests validate the correctness of the API responses, and help to maintain data integrity.

### UI Tests
1. **Coverage**: These tests cover critical UI functionality of the UITestingPlayground website, ensuring that basic interactions like button clicks and text inputs are working as expected.
2. **Validation**: UI tests validate the correctness of the UI behavior, helping to ensure a positive user experience and maintain usability standards.


## Contact
- Zohreh Ezati
- Email: zohreh.ezatii@gmail.com
- LinkedIn: https://www.linkedin.com/in/zohre-ezati/

# Installation #

## From testPypi ##

    pip install --force-reinstall --index-url https://test.pypi.org/simple --extra-index-url https://pypi.org/simple robotframework-testdataserverlibrary

# Preconditions 
## TestDataServer installed:

Library itself does nothing! You need also a TestDataServer which provides test data via an API. See more:

https://github.com/Omenia/TestDataServer

## Example data inserted to database
After clean installation TestDataServer has empty testdata database. For this demo we can add some simple test data which we can use for this demo.

Go to http://\<testdataserverip\>:5000/configuration
--> Click "Add testdata"

Name = credentials

payload:

    {"username":"user1", "password":"password1", "email":"user1@nowhere.com"}
    {"username":"user2", "password":"password2", "email":"user2@nowhere.com"}
    {"username":"user3", "password":"password3", "email":"user3@nowhere.com"}
    
OR add testdata using existing keyword:
    
    Add Dataset

Note: "Add Dataset" keyword is not yet parametrized, but it has static dataset for testing and development purposes!

# Usage Example #

    *** Settings ****
    Library        TDSlibrary    host=172.16.240.247    port=5000
    Suite Setup    Remove Dataset    credentials

    *** Test Cases ***
    1. Add dataset works
        Add Dataset       credentials

    2. Fetching data from dataset works
        Fetch Testdata    credentials
        Should Be Equal     ${username}    user1

    3. Popping testdata works
        Fetch Testdata    credentials
        Should Be Equal     ${username}    user2

    4. Circulating testdata works
        Fetch Testdata    credentials
        Fetch Testdata    credentials
        Should Be Equal     ${username}    user1

    5. Removing dataset works
        Remove Dataset    credentials
        Run Keyword And Expect Error    KeyError: 'testdata'    Fetch Testdata    credentials

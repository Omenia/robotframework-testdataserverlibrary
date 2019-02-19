*** Settings ****
Resource    TDSvariables.robot
Library    TDSlibrary    host=${tds_host}    port=${tds_port}
# Resource    TdsKeywords.robot
# Suite Setup    Prepare Testdata
# Suite Teardown    Remove Testdata

*** Test Cases ***
Creating Dataset Works
    Add Dataset    credentials

TDS DB Starts From Beginning
    Fetch Testdata    credentials
    Should Be Equal As Strings    ${username}    user1
    Should Be Equal As Strings    ${password}    password1
    Should Be Equal As Strings    ${email}    user1@nowhere.com

TDS DB Recylces Data
    Fetch Testdata    credentials
    Should Be Equal As Strings    ${username}    user2
    Should Be Equal As Strings    ${password}    password2
    Should Be Equal As Strings    ${email}    user2@nowhere.com

TDS DB Recirculates From Beginning
    Fetch Testdata    credentials
    Should Be Equal As Strings    ${username}    user1
    Should Be Equal As Strings    ${password}    password1
    Should Be Equal As Strings    ${email}    user1@nowhere.com

Removing Dataset Works
    Remove Dataset    credentials
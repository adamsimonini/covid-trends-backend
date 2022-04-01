<!-- different cases explained: https://medium.com/nerd-for-tech/programming-case-types-explained-143cad3681e3 -->

Regarding variable types:
The following should be PascalCase
Classes (e.g., class Person)

    The following should be MACRO_CASE
        Constants (e.g., PI, MY_STATIC_LIST)

    The following should be snake_case
        Functions (e.g. def my_function)
        Methods
        Variables (e.g., my_dictionary)

Regarding Database items
The following should be camelCase
Classes

    The following should be MACRO_CASE
        Constants

    The following should be snake_case
        Functions
        Methods
        Variables

Special cases: 1. For the api_fixtures.json, the "model" will be referring to the Model class but all lowercase, NOT camelcase as it shows.

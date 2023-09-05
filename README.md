# api_categorization_data_limitation_example
A simple example of how you can manipulate how much of data you can receive from external API.


## Usage

- Flask
- jsonify
- request
- requests

## API 
    https://jsonplaceholder.typicode.com/posts

## Installation 
```
   pip install Flask requests 
```

## Explanation

Whole project has 3 functions that define all path how data is being categorized by limitations of ID-s. 
There are 2 api routes set one for getting the categorized data and other one for setting new limitations.
I've used for loop to categorise data every single time with new data_limit.
'data_limit' is being set to value of 10 as primary setting, but it can be changed. 

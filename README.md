# Test Task (Python)

## Task

Write a program that analyzes HTML and finds a specific element, even after changes, using a set of extracted attributes. 

## Usage

`python3 locate_similar_element.py <path_to_origin_file> <target_id> <path_to_sample_file>`

Example: 

`python3 locate_similar_element.py test_files/original.htm make-everything-ok-button test_files/first_test.htm`

Alternatively, you can run test script to test 4 default test cases

`python3 test.py`

## Results

Script prints to console path to target element in second file.

## TODO

* Add error handling
* Don't just check for equality of attrs but add more complex text analysis

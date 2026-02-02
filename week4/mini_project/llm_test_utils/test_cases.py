
"""
Test Cases Module
-----------------
This module manages test scenarios.
It allows adding, retrieving, and filtering test cases (dictionaries).
"""

class TestCaseManager:
    """
    In-memory manager for prompt test cases.
    """
    
    def __init__(self):
        """Initialize with an empty list of test cases."""
        self.test_cases = []
        
    def add_test_case(self, name, prompt_template, variables, expected_keywords=None):
        """
        Adds a new test case.
        
        Args:
            name (str): Identifier for the test.
            prompt_template (str): The template string.
            variables (dict): Variables to fill the template.
            expected_keywords (list): Optional list of keywords to check for.
        """
        if expected_keywords is None:
            expected_keywords = []
            
        case = {
            "name": name,
            "template": prompt_template,
            "variables": variables,
            "expected_keywords": expected_keywords
        }
        self.test_cases.append(case)
        print(f"Added test case: {name}")
        
    def get_all_cases(self):
        """Returns all stored test cases."""
        return self.test_cases
    
    def find_by_name(self, name):
        """
        Finds a test case by name. Returns None if not found.
        """
        for case in self.test_cases:
            if case["name"] == name:
                return case
        return None

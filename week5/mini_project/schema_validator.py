"""
Week 5 Mini-Project: dataset-loader
File: schema_validator.py

This module contains logic to validate the structure of test cases.
Each test case should be a dictionary with at least 'input' and 'expected_output' keys.
"""

def validate_test_case(test_case):
    """
    Validates a single test case dictionary.
    
    Args:
        test_case (dict): The test case to validate.
        
    Returns:
        tuple: (is_valid, error_message)
    """
    required_fields = ["input", "expected_output"]
    
    if not isinstance(test_case, dict):
        return False, "Test case must be a dictionary."
        
    for field in required_fields:
        if field not in test_case:
            return False, f"Missing required field: '{field}'"
            
    return True, None

def validate_dataset(dataset):
    """
    Validates a list of test cases.
    
    Args:
        dataset (list): List of test cases.
        
    Returns:
        dict: Stats about validation (valid_count, invalid_count, errors)
    """
    stats = {
        "valid_count": 0,
        "invalid_count": 0,
        "errors": []
    }
    
    for i, entry in enumerate(dataset):
        is_valid, error = validate_test_case(entry)
        if is_valid:
            stats["valid_count"] += 1
        else:
            stats["invalid_count"] += 1
            stats["errors"].append(f"Entry {i}: {error}")
            
    return stats


"""
Validators Module
-----------------
This module contains functions to check if an LLM's response meets specific criteria.
"""

import json

def validate_not_empty(response):
    """Checks if the response is not empty."""
    if not response:
        return False
    return len(response.strip()) > 0

def validate_max_length(response, limit):
    """Checks if the response length is within the limit."""
    return len(response) <= limit

def validate_contains_keywords(response, keywords):
    """
    Checks if the response contains ALL the given keywords.
    Keywords should be a list of strings.
    """
    response_lower = response.lower()
    for keyword in keywords:
        if keyword.lower() not in response_lower:
            return False
    return True

def validate_json_format(response):
    """
    Checks if the response is a valid JSON string.
    Returns True if valid, False otherwise.
    """
    try:
        json.loads(response)
        return True
    except ValueError:
        return False

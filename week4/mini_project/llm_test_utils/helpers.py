
"""
Helpers Module
--------------
General utility functions used across the package.
"""

def log_test_result(name, status, message=""):
    """Simple logger for test results."""
    symbol = "PASS" if status else "FAIL"
    msg = f" {message}" if message else ""
    print(f"[{symbol}] {name}:{msg}")

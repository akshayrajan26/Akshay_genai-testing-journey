
import sys

print("--- Verifying 'llm_test_utils' Installation ---")

try:
    import llm_test_utils
    print(f"SUCCESS: 'llm_test_utils' imported successfully.")
    print(f"   Location: {llm_test_utils.__file__}")
except ImportError as e:
    print(f"FAILURE: Could not import 'llm_test_utils'.")
    print(f"   Error: {e}")
    sys.exit(1)

try:
    from llm_test_utils import format_prompt, validate_not_empty
    print("SUCCESS: Can import functions (format_prompt, validate_not_empty).")
    
    # Test a function
    res = validate_not_empty("hello")
    print(f"SUCCESS: Function execution worked. validation result: {res}")
except ImportError as e:
    print(f"FAILURE: Could not import functions from package.")
    print(f"   Error: {e}")
    sys.exit(1)
except Exception as e:
    print(f"FAILURE: Runtime error using package.")

    print(f"   Error: {e}")
    sys.exit(1)

print("---------------------------------------------")
print("Verification Complete: The package is correctly installed in your environment.")

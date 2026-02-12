"""
Week 5 Mini-Project: dataset-loader
File: dataset_loader.py

This module handles loading and saving JSON/JSONL datasets.
"""

import json
from pathlib import Path
from schema_validator import validate_dataset

class DatasetManager:
    def __init__(self, data_dir="datasets"):
        self.data_dir = Path(data_dir)
        self.data_dir.mkdir(exist_ok=True)

    def load_json(self, filename):
        """Loads a standard JSON dataset."""
        path = self.data_dir / filename
        if not path.exists():
            raise FileNotFoundError(f"File not found: {path}")
            
        with open(path, "r") as f:
            data = json.load(f)
            
        return data

    def load_jsonl(self, filename):
        """Loads a JSONL (JSON Lines) dataset."""
        path = self.data_dir / filename
        if not path.exists():
            raise FileNotFoundError(f"File not found: {path}")
            
        results = []
        with open(path, "r") as f:
            for line in f:
                if line.strip():
                    results.append(json.loads(line))
        return results

    def save_json(self, data, filename):
        """Saves data to a JSON file."""
        path = self.data_dir / filename
        with open(path, "w") as f:
            json.dump(data, f, indent=4)
        print(f"Saved to {path}")

    def save_jsonl(self, data, filename):
        """Saves data to a JSONL file."""
        path = self.data_dir / filename
        with open(path, "w") as f:
            for item in data:
                f.write(json.dumps(item) + "\n")
        print(f"Saved to {path}")

if __name__ == "__main__":
    # Simple demo/test
    manager = DatasetManager()
    
    # Create sample data
    sample_data = [
        {"input": "What is AI?", "expected_output": "Artificial Intelligence."},
        {"input": "Tell me a joke.", "expected_output": "Why did the chicken cross the road?"}
    ]
    
    # Save as JSON and JSONL
    manager.save_json(sample_data, "test.json")
    manager.save_jsonl(sample_data, "test.jsonl")
    
    # Load back
    loaded_json = manager.load_json("test.json")
    loaded_jsonl = manager.load_jsonl("test.jsonl")
    
    # Validate
    print("\nValidating JSON load:")
    print(validate_dataset(loaded_json))
    
    print("\nValidating JSONL load:")
    print(validate_dataset(loaded_jsonl))

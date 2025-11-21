# Test file to check if skincare_ai can be imported
import sys
import os

# Add the project root directory to Python path
project_root = os.path.dirname(os.path.abspath(__file__))
if project_root not in sys.path:
    sys.path.append(project_root)

try:
    import skincare_ai
    print("✅ Successfully imported skincare_ai!")
    print(f"Module location: {skincare_ai.__file__}")
except ImportError as e:
    print("❌ Failed to import skincare_ai")
    print(f"Error: {e}")
    print(f"Current Python path: {sys.path}")

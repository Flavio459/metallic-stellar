import sys
import os

# Set path manually if not set
current_dir = os.path.dirname(os.path.abspath(__file__))
domiknows_path = os.path.join(current_dir, 'DomiKnowS_Source')
if domiknows_path not in sys.path:
    sys.path.append(domiknows_path)

print("Executable:", sys.executable)
try:
    print("Importing domiknows...")
    import domiknows
    print("DomiKnowS imported:", domiknows.__file__)
    
    print("Importing domiknows.graph...")
    from domiknows.graph import Graph
    print("Graph imported successfully.")
except Exception as e:
    print("Import failed:", e)

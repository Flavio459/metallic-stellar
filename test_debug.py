import sys
import os

print("Testing imports...")
try:
    print("1. Importing owlready2...")
    import owlready2
    print("Owlready2 imported.")
except ImportError:
    print("Owlready2 failed.")

print("2. Setting path for DomiKnowS...")
current_dir = os.path.dirname(os.path.abspath(__file__))
domiknows_path = os.path.join(current_dir, 'DomiKnowS_Source')
if domiknows_path not in sys.path:
    sys.path.append(domiknows_path)

try:
    print("3. Importing domiknows.solver.ilpConfig...")
    from domiknows.solver import ilpConfig
    print("ilpConfig imported.")
except Exception as e:
    print(f"ilpConfig failed: {e}")

try:
    print("4. Importing domiknows.graph...")
    from domiknows.graph import Graph
    print("Graph imported.")
except Exception as e:
    print(f"Graph failed: {e}")

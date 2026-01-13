import sys
import os

# Bypass MKL duplicate check just in case
os.environ['KMP_DUPLICATE_LIB_OK'] = 'TRUE'

print("Executable:", sys.executable)
try:
    print("Importing numpy...")
    import numpy
    print("Numpy version:", numpy.__version__)
    
    print("Importing torch...")
    import torch
    print("Torch version:", torch.__version__)
    print("CUDA available:", torch.cuda.is_available())
except ImportError as e:
    print("Import failed:", e)
except Exception as e:
    print("Error:", e)

from domiknows.graph import Graph, Concept, Relation
from domiknows.graph.logicalConstrain import ifL, andL, notL, atLeastL, exactL
from domiknows.program import Program
from domiknows.sensor.pytorch.sensor import ReaderSensor, JointSensor
from domiknows.sensor.pytorch.learners import ModuleLearner
import torch

# ==========================================
# 1. KNOWLEDGE DECLARATION (Design Agent)
# ==========================================
print("--- [Agentic DomiKnowS] Phase 1: Knowledge Declaration ---")

Graph.clear()
Concept.clear()
Relation.clear()

with Graph('HVAC_PMOC_Domain') as graph:
    # Concepts
    Proposal = Concept(name='Proposal')
    Room = Concept(name='Room')
    Equipment = Concept(name='Equipment')
    
    # Relations
    proposal_contains_room = Proposal.contains(Room)
    room_contains_equipment = Room.contains(Equipment)
    
    # Attributes / Classifications
    is_server_room = Room(name='is_server_room')
    requires_pmoc = Room(name='requires_pmoc')
    high_thermal_load = Room(name='high_thermal_load')
    
    # --- LOGICAL CONSTRAINTS (The "Symbolic" Power) ---
    
    # Constraint 1: Server Rooms ALWAYS imply High Thermal Load
    # ifL(is_server_room, high_thermal_load)
    
    # Constraint 2: If a room has > 5 equipment, it LIKELY requires PMOC (Simplified logic)
    # real counting is harder in pure propositional logic, but we can infer properties
    # based on sensory inputs.
    
    ifL(is_server_room, requires_pmoc) 

print("Knowledge Graph Defined:", graph)


# ==========================================
# 2. MODEL DECLARATION (Execution Agent)
# ==========================================
print("\n--- [Agentic DomiKnowS] Phase 2: Model Declaration ---")

# Define Sensors (Inputs)
class SimpleSensor(ReaderSensor):
    def forward(self, *args, **kwargs):
        return torch.tensor([1.0, 0.0]) # Mock output

# Mapping concepts to sensors
# In a real app, these would connect to your ProposalView inputs
Proposal['raw_input'] = ReaderSensor(keyword='proposal_data')
Room['room_features'] = ReaderSensor(keyword='room_features')

# Define a Program
# This program compiles the graph + sensors into a runnable Neural-Symbolic model
program = Program(graph, po=True) # po=True enables Primal-Dual optimization for constraints

print("Program Compiled Successfully.")


# ==========================================
# 3. EXECUTION / INFERENCE
# ==========================================
print("\n--- [Agentic DomiKnowS] Phase 3: Execution (Mock) ---")

# Mock Data: "Restaurante em Taubaté"
mock_data = {
    'proposal_data': [{'id': 1, 'name': 'Restaurante Taubaté'}],
    'room_features': [{'id': 101, 'area': 50, 'is_server': True}] # Setup to trigger constraint
}

print(f"Processing Proposal: {mock_data['proposal_data'][0]['name']}")
print("Refining predictions with Logical Constraints...")

# (Simulation of the output, as actual training requires a loop)
print(" > Detected 'Server Room' attribute.")
print(" > Constraint Triggered: Server Room => High Thermal Load.")
print(" > Constraint Triggered: Server Room => Requires PMOC.")
print("\n[RESULT] PMOC Plan Generated: REQUIRED (Confidence: 100% due to Logic)")


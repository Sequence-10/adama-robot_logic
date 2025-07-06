📦📦📦📦📦📦📦 Warehouse Delivery Simulation 📦📦📦📦📦📦

           Python-Based Autonomous System


Overview
This project is a Python simulation of an autonomous warehouse delivery system. It models how a stationary loader unit (KHR2HV) and a mobile delivery unit (Pioneer2) coordinate to transport items from storage rows to a central exit point — without using physical sensors or hardware, but instead with algorithmic logic and coordinate-based navigation.

The simulation demonstrates:

Autonomous navigation through grid coordinates.

Task coordination between multiple units.

Logic-based “perception” instead of hardware sensors.

Repeatable delivery cycles for multiple storage rows.

📁 Project Structure
warehouse_simulation/

main.py              # Main script to run the simulation
loader_unit.py       # Contains the Loader (KHR2HV) class logic
delivery_unit.py     # Contains the Delivery Robot (Pioneer2) class logic
warehouse.py         # Defines the grid layout and box coordinates
README.md            # This file


✅ Features
2D Grid Layout: Warehouse floor modeled as a grid of boxes.

Autonomous Movement: Delivery robot moves stepwise between pickup points and the exit.

Task Flow: Loader transfers items to the delivery robot when they meet at the correct spot.

Simulated Perception: No physical sensors — proximity checks use coordinate matching.

Sequential Delivery: One storage row is completed before moving to the next.

⚙️ How to Run
Clone or Download the Project
git clone https://github.com/Sequence-10/adama-robot_logic.git
cd warehouse_simulation

(Optional) Create Virtual Environment
python -m venv venv
source venv/bin/activate  # or venv\Scripts\activate on Windows

Install Dependencies
pip install -r requirements.txt
Note: The core version uses only Python built-ins. Add to requirements.txt if you use visualization or external libraries.

Run the Simulation
python main.py
📌 How It Works
Warehouse Grid: Defined in warehouse.py with coordinates for boxes in each row.

Loader Unit: Stays at the current row, loads items into the delivery robot when it arrives.

Delivery Unit: Navigates to a box, waits for loading, moves to the exit, delivers, and returns.

Control Loop: Runs until all boxes in both rows are delivered.

🗂️ Main Files Explained
File	Purpose
main.py	Runs the main delivery loop and coordinates both units
loader_unit.py	Contains the Loader class: logic for loading and row switching
delivery_unit.py	Contains the Delivery Robot class: movement, pickup, delivery
warehouse.py	Warehouse grid layout and box coordinate mapping
requirements.txt	(Optional) Lists any needed Python packages

🧩 Extending This Project
✅ Add more delivery robots to simulate multiple units.

✅ Implement basic visualization (e.g., matplotlib for 2D plots).

✅ Upgrade to real hardware using the same logic as the simulation.

✅ Integrate with a GUI to observe box status and robot paths in real time.

⚠️ Limitations
This version does not include obstacle avoidance, pathfinding algorithms (like A*), or real-time collision detection.

All movements are deterministic, based on hardcoded paths.

👥 Authors & Contributors
Student Developer: Muhammed Lamin Gaye & Mathiue Haba
Supervisor: Mr Pasulay Jobe
Institution: University of The Gambia/School of ITC

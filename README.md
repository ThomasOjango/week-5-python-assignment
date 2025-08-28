#  OOP Devices & Movement Simulation

A Python assignment demonstrating core Object-Oriented Programming (OOP) concepts—**inheritance**, **encapsulation**, and **polymorphism**—through relatable examples like smartphones, animals, and vehicles. Built with clarity, creativity, and a touch of Kenyan flair 🇰🇪.

##  Features

### Device & Smartphone Classes
- `Device`: Base class with brand and model attributes.
- `Smartphone`: Inherits from `Device`, adds storage and battery.
- Methods include:
  - `make_call(number)`: Simulates a phone call.
  - `charge(percent)`: Charges the battery with overflow protection.

### Polymorphism in Action
- `Animal` and `Vehicle` classes define a shared method `move()`.
- Subclasses override `move()` to reflect unique behaviors:
  - `Dog`, `Bird`, `Fish`
  - `Car`, `Plane`, `Boat`
  - Bonus: `Matatu` and `Cheetah` for Kenyan context.

# Concepts Covered

- **Inheritance**: Code reuse and hierarchy.
- **Encapsulation**: Bundling data and behavior.
- **Polymorphism**: Unified interface, diverse behavior.
- **Modularity**: Clean structure for maintainability.

##  How to Run

`bash
python main.py

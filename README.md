# Basic G-Code Operations

A simple CLI to generate basic CNC paths for common woodworking joints such as rabbets and dados.

Example Call:

```
125 End
python src/operations.py --x_location=-0.125 --width=1.375 --depth=0.365 --length=13 --cutter_diameter=0.25 --overlap=0.2

python src/operations.py --x_location=4.25 --width=1.25 --depth=0.365 --length=13 --cutter_diameter=0.25 --overlap=0.2
```
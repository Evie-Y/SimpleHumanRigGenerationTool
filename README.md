# SimpleHumanRigGenerationTool
The goal of this tool is to help make a simple human rig generation tool. This will help cut the repetition of rigging and speed up the basic controls on a humanoid character.

### Features
- I will change the control colors based on whether they are an IK/FK control
and whether they are on the character’s right, left, or center.
- I will include an IK/FK control switch on the ik control on the arms and legs.
I will also make this control bold for easier reading.
- I will include different control shapes based on slection order of the joints. For
example, the last/third joint selected for an IK control will be the joint that holds the ik/fk switch.
- The control’s size will be based on either the joint’s radius or the joint’s
naming.
- I will figure out how to make the spline rig/controls with just Python code.

### Goals
- Create an easy-to-use UI window and improve on PySide2.
- Make sure the tool works on different kinds of joints.
- Creates unique controls based on joint selection and purpose.
- Creates IK/FK controls and switch for arms and legs.
- Help speed up making a functioning human rig.
- Improve on GitHub commits and naming.
- Have lists that link to common joint naming.
- Have control colors and boldness change depending on the joint.

### Inputs
- Selected Joints

#### UI
- Buttons for creating an fk, ik, or ik/fk with a switch.
- Checkbox for circle controls or unique controls.
- Dropdown with button to create unique curves, not rigged.

## TODO:

Make UI
  - Checkbox for fk, ik, or both with a switch.
  - Buttons to create unique curves, not rigged.

Make unique controls
  - square
  - rectangle
  - triangle
  - diamond
  - sphere
  - arrow
  - 2-way arrow
  - quad arrow

Make IK rig functional

Make FK rig functional

Make IK/FK switch functional

Make a spline rig functional

Make controls change color based on L/R naming

Make controls change boldness based on the control's function

## Improvement for Later

Doesn't work for duplicate joint names
Doesn't work for reverse foot
Doesn't have a way to add more con shapes
Figure out how to serpate UI more
Only know how to bolden controls using MEL
Only works on joint oriented with default Maya settings




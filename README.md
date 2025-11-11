# SimpleHumanRigGenerationTool
The goal of this tool is to make a simple human rig generation tool. This will help cut the repetition of rigging and speed up the basic controls on a humanoid character.

### Features
- I will change the control colors based on whether they are an IK/FK control
and whether they are on the character’s right, left, or center.
- I will include an IK/FK control switch on the ik control on the arms and legs.
I will also make this control bold for easier reading.
- I will include different control shapes based on the name of the joint. For
example, if the joint name includes the word ‘hip’, it will make the control
generate into the appropriate shape instead of a basic circular curve.
- The control’s size will be based on either the joint’s radius or the joint’s
naming.
- I will figure out how to make the spline rig/controls with just Python code.

- If I have time, I will try to make some unique face controls; however, this
will be extra. I want to focus on body rigging and leave the face rigging to
the rigger.
- If I have time, I will maybe give the user the option to assign certain
controls to certain joints. This is to improve the usability of the tool outside of humanoid rig generation.

### Goals
- Create an easy-to-use UI window and improve on PySide2.
- Make sure the tool works on different humanoid models.
- Creates unique controls based on joint names.
- Creates IK/FK controls and switch for arms and legs.
- Make a functioning human rig.
- Improve on GitHub commits and naming.
- Have lists that link to common joint naming.
- Have control colors and boldness depend on the joint's naming.

### Inputs
- Selected Joints

#### UI
- Checkbox for fk, ik, or both with a switch.
- Button for standard humanoid rig generation.
- Buttons to create unique curves, not rigged.

## TODO:

Make UI
  - Checkbox for fk, ik, or both with a switch.
  - Button for standard humanoid rig generation.
  - Buttons to create unique curves, not rigged.

Make unique controls
  - wrist
  - fingers
  - hip
  - ankle
  - pole vector

Make IK rig functional

Make FK rig functional

Make IK/FK switch functional

Make a spline rig functional

Make controls change color based on L/R naming

Make controls change boldness based on the control's function




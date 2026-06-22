# class myServo

> Adapted from [Python_Tutorial.pdf](../../Python_Tutorial.pdf) — Chapter 19, Stepper Motor
>
> Note: this chapter's orange reference box is labeled "class myServo" in the source PDF (apparently copied from the [Servo chapter](../class_myServo/Servo.md) and not updated) even though the content below documents `mystepmotor`, not `myServo`. Kept verbatim from the PDF; grouped with Servo.md here since both share the same label.

Before each use of the object **mystepmotor**, make sure `stepmotor.py` has been uploaded to `/` on the ESP32-S3, and then add the statement `from stepmotor import mystepmotor` to the top of the Python file.

- **`mystepmotor()`**: The object that controls the stepper motor. The default control pins are Pin(14), Pin(13), Pin(12), and Pin(11).
- **`moveSteps(direction, steps, us)`**: Controls the stepper motor to rotate a specified number of steps.
  - `direction`: The rotation direction of the stepper motor.
  - `steps`: Rotation steps of the stepper motor.
  - `us`: Time required by the stepper motor to rotate one step.
- **`moveAround(direction, turns, us)`**: Controls the stepper motor to rotate a specific number of turns.
  - `turns`: Number of turns the stepper motor rotates.
- **`moveAngle(direction, angles, us)`**: Controls the stepper motor to rotate a specific angle.
  - `angles`: Rotation angle the stepper motor rotates.
- **`stop()`**: Stops the stepper motor.

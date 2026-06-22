# class myServo

> Adapted from [Python_Tutorial.pdf](../../Python_Tutorial.pdf) — Chapter 18, Servo
>
> Note: this chapter's orange reference box is labeled "class myServo" in the source PDF — identical to the label in [Chapter 19, Stepper Motor](../class_myServo/Stepper_Motor.md), which is why these two are grouped together in this folder.

Before each use of **myServo**, make sure `myservo.py` has been uploaded to `/` on the ESP32-S3, and then add the statement `from myservo import myServo` to the top of the Python file.

- **`myServo()`**: The object that controls the servo, with the default pin Pin(15), default frequency 50Hz, and default duty cycle 512.
- **`myServoWriteDuty(duty)`**: Writes a duty cycle to control the servo.
  - `duty`: Range from 26 to 128, with 26 corresponding to the servo's 0 degrees and 128 corresponding to 180 degrees.
- **`myServoWriteAngle(pos)`**: Writes an angle value to control the servo.
  - `pos`: Range from 0–180, corresponding to the servo's 0–180 degrees.
- **`myServoWriteTime(us)`**: Writes a time value to control the servo.
  - `us`: Range from 500–2500, with 500 corresponding to the servo's 0 degrees and 2500 corresponding to 180 degrees.

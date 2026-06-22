# Class mpu6050

> Adapted from [Python_Tutorial.pdf](../Python_Tutorial.pdf) — Chapter 26, Attitude Sensor MPU6050

Before each use of **mpu6050**, add the statement `from mpu6050 import MPU6050` to the top of the Python file.

- **`MPU6050(sclpin, sdapin)`**: Creates an `MPU6050` object and associates its I2C pins with it.
- **`MPU_Init()`**: Initializes the MPU6050 module.
- **`MPU_Get_Accelerometer()`**: Obtains the raw accelerometer data from the MPU6050.
- **`MPU_Get_Gyroscope()`**: Obtains the raw gyroscope data from the MPU6050.

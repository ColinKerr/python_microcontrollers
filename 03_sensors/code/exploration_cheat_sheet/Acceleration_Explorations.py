from mpu6050 import MPU6050
import time
 
mpu=MPU6050(14,13) #attach the IIC pin(sclpin,sdapin)
mpu.MPU_Init()     #initialize the MPU6050
G = 9.8
time.sleep_ms(1000)#waiting for MPU6050 to work steadily

try:
    while True:
        accel=mpu.MPU_Get_Accelerometer()#gain the values of Acceleration
        gyro=mpu.MPU_Get_Gyroscope()     #gain the values of Gyroscope
        print("\na/g:\t")
        print(accel[0],"\t",accel[1],"\t",accel[2],"\t",
              gyro[0],"\t",gyro[1],"\t",gyro[2])
        print("a/g:\t")
        print(accel[0]/16384,"g",accel[1]/16384,"g",accel[2]/16384,"g",
              gyro[0]/131,"d/s",gyro[1]/131,"d/s",gyro[2]/131,"d/s")
        
        tilt_angle = accel[1] + accel[2] # Combines X and Y values for tilt angle
        if accel[2] <= 15650: # Checks if the board is tilted based off of the current accel Z axis
            print("Tilted: Yes\t", end="")
            print("Angle: " + str(tilt_angle))
        else:
            print("Tilted: No")
        time.sleep_ms(1000)
except:
    pass

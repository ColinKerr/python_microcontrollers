# Class time

Before each use of the time module, please add the statement “import time” to the top of python file

- `time.sleep(sec)`: Sleeps for the given number of seconds
  - `sec`: This argument should be either an int or a float.
- `time.sleep_ms(ms)`: Sleeps for the given number of milliseconds, ms should be an int.
- `time.sleep_us(us)`: Sleeps for the given number of microseconds, us should be an int.
- `time.time()`: Obtains the timestamp of CPU, with second as its unit.
- `time.ticks_ms()`: Returns the incrementing millisecond counter value, which recounts after some values.
- `time.ticks_us()`: Returns microsecond
- `time.ticks_cpu()`: Similar to ticks_ms() and ticks_us(), but it is more accurate(return clock of CPU).
- `time.ticks_add(ticks, delta)`: Gets the timestamp after the offset.
  - `ticks`: ticks_ms()、ticks_us()、ticks_cpu()
  - `delta`: Delta can be an arbitrary integer number or numeric expression
- `time.ticks_diff(old_t, new_t)`: Calculates the interval between two timestamps, such as ticks_ms(), ticks_us() or ticks_cpu().
  - `old_t`: Starting time
  - `new_t`: Ending time
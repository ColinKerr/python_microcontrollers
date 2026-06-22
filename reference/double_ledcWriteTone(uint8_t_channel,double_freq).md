# double ledcWriteTone(uint8_t channel, double freq);

> Adapted from [Python_Tutorial.pdf](../Python_Tutorial.pdf) — Chapter 7, Buzzer

Updates the tone frequency value on the given channel.

> This function has some bugs in the current version (V1.0.4): when the call interval is less than 20ms, the resulting PWM will have an exception. We will get in touch with the authorities to solve this problem and provide solutions in the following two projects.

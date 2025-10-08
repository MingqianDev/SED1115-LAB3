from machine import Pin
import time

led1 = Pin(18, Pin.OUT)
sw5 = Pin(22, Pin.IN, Pin.PULL_DOWN)

led1.off()

# method 1

# prev_sw5_value = 0

# while True:
#     if sw5.value() == 1 and prev_sw5_value == 0:
#         led1.toggle()
    
#     prev_sw5_value = sw5.value()

#     print(sw5.value())

#     time.sleep_ms(50)

# method 2

last_press_time = 0
debounce_delay = 200  # milliseconds

while True:
    current_time = time.ticks_ms()
    if sw5.value() == 1 and time.ticks_diff(current_time, last_press_time) > debounce_delay:
        led1.toggle()
        last_press_time = current_time

    # print(time.ticks_diff(current_time, last_press_time))


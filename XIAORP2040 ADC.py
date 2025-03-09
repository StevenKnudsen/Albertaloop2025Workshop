from machine import ADC

adc = ADC(26)        # create an ADC object acting on a pin

while True:
    val = adc.read_u16()  # read a raw analog value in the range 0-65535
    print(val)
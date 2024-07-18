class Solution(object):
    def convertTemperature(self, celsius):
        kelvin_tp = celsius + 273.15
        fahrenheit_tp = celsius * 1.80 +32.00
        return [kelvin_tp,fahrenheit_tp]  
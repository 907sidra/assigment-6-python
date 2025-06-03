class TemperatureConverter:
    @staticmethod
    def celsius_to_fahrenheit(c):
        return (c * 9/5) + 32

# Test
if __name__ == "__main__":
    print("25°C in Fahrenheit:", TemperatureConverter.celsius_to_fahrenheit(25))

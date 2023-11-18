import RPi.GPIO as GPIO
import time

# Setting up the GPIO mode and pins
GPIO.setmode(GPIO.BCM)
LED_PIN = 21
BUZZER_PIN = 20
GPIO.setup(LED_PIN, GPIO.OUT)
GPIO.setup(BUZZER_PIN, GPIO.OUT)

# Morse code dictionary
MORSE_CODE_DICT = {
    'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.',
    'G': '--.', 'H': '....', 'I': '..', 'J': '.---', 'K': '-.-', 'L': '.-..',
    'M': '--', 'N': '-.', 'O': '---', 'P': '.--.', 'Q': '--.-', 'R': '.-.',
    'S': '...', 'T': '-', 'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-',
    'Y': '-.--', 'Z': '--..',
    '0': '-----', '1': '.----', '2': '..---', '3': '...--', '4': '....-',
    '5': '.....', '6': '-....', '7': '--...', '8': '---..', '9': '----.',
    ' ': ' '  # Space character
}

def morse_to_led_and_buzzer(morse_code):
    for symbol in morse_code:
        if symbol == '.':
            GPIO.output(LED_PIN, GPIO.HIGH)
            GPIO.output(BUZZER_PIN, GPIO.HIGH)
            time.sleep(0.2)  # Short blink/buzz for a dot
            GPIO.output(LED_PIN, GPIO.LOW)
            GPIO.output(BUZZER_PIN, GPIO.LOW)
            time.sleep(0.2)
        elif symbol == '-':
            GPIO.output(LED_PIN, GPIO.HIGH)
            GPIO.output(BUZZER_PIN, GPIO.HIGH)
            time.sleep(0.6)  # Long blink/buzz for a dash
            GPIO.output(LED_PIN, GPIO.LOW)
            GPIO.output(BUZZER_PIN, GPIO.LOW)
            time.sleep(0.2)
        elif symbol == ' ':
            time.sleep(0.6)  # Gap between words

def text_to_morse(text):
    morse_code = ''
    for char in text.upper():
        morse_code += MORSE_CODE_DICT.get(char, '') + ' '
    return morse_code

if __name__ == '__main__':
    try:
        while True:
            text = input("Enter a message to convert to Morse code (or 'exit' to quit): ")
            if text.lower() == 'exit':
                break
            morse_code = text_to_morse(text)
            if not morse_code.strip():
                print("Invalid input. Please enter only alphanumeric characters and spaces.")
                continue
            print(f"Morse Code: {morse_code}")
            morse_to_led_and_buzzer(morse_code)
            time.sleep(1)
    except KeyboardInterrupt:
        print("\nProgram interrupted.")
    finally:
        GPIO.cleanup()
        print("GPIO cleaned up and program ended.")
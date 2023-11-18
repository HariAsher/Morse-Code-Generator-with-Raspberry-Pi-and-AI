# Morse-Code-Generator-with-Raspberry-Pi-and-AI
This repository showcases a Raspberry Pi-based Morse Code Generator with the help of AI. It allows users to input text messages, which the program converts into Morse code. The Morse code is visually represented through an LED blinking sequence and audibly represented using a buzzer. 

## Overview

![MORSE CODE](https://github.com/HariAsher/Morse-Code-Generator-with-Raspberry-Pi-and-AI/assets/83194217/1d2af304-3f74-452d-82f5-09cda90b52d0)

This project demonstrates how to create a Morse code generator using a Raspberry Pi, AI, and additional components. The hardware setup includes a breadboard, an LED, a buzzer, a 220-ohm resistor, and several jumper wires.

The program utilizes AI to convert user-input text into Morse code. The LED and buzzer are then used to visually and audibly represent the Morse code message. The LED blinks according to the Morse code dots and dashes, while the buzzer emits corresponding sounds.

## Table of Contents

- [Getting Started](#getting-started)
  - [Hardware Setup](#hardware-setup)
  - [Software Setup](#software-setup)
  - [Chat GPT Prompt](#chat-gpt-prompt)
- [Usage](#usage)
- [Morse Code Conversion](#morse-code-conversion)
- [Circuit Diagram](#circuit-diagram)

## Getting Started

### Hardware Setup

1. Assemble the hardware components on the breadboard as per the provided circuit diagram (see [Circuit Diagram](#circuit-diagram)).
2. Make sure all connections are secure, and the 220-ohm resistor is connected in series with the LED.
3. Connect your Raspberry Pi to the breadboard using jumper wires.

### Software Setup

Make sure Python is installed on your Raspberry Pi.

### Chat GPT Prompt

Help me develop a Morse code project using a Raspberry Pi. This project involves incorporating a buzzer and a light. The program should prompt the user to input a text message they wish to convert into Morse code. Afterward, the program should perform the conversion, and both the buzzer should emit corresponding Morse code sounds, and the light should flash accordingly.

## Usage

![Morse Code Termina;](https://github.com/HariAsher/Morse-Code-Generator-with-Raspberry-Pi-and-AI/assets/83194217/5f01bc89-ca89-4ee3-bd28-7767f3b406ba)

When you run the program, it will prompt you to enter the message you want to convert into Morse code. After entering the message, the program will convert it into Morse code and display the corresponding dots and dashes on the LED while emitting beeps through the buzzer to represent the Morse code message.

## Morse Code Conversion
The Morse code conversion is handled by the dictionary, which translates user-input text into Morse code. The Morse code consists of dots (.) and dashes (-), with specific sequences representing each letter and number. The LED blinks and the buzzer emits sounds to match the Morse code sequence for the entered message.

## Circuit Diagram
Please refer to circuit diagram.

![Morse Code Circuit Diagram](https://github.com/HariAsher/Morse-Code-Generator-with-Raspberry-Pi-and-AI/assets/83194217/76d3e9c0-65e3-4c7f-8538-76ee3182b492)

You can even ask Chat GPT to write the code and generate circuit diagram.

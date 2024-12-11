# AdaptiveEncryptionSystem
The Adaptive Encryption System is a robust and efficient encryption framework designed for resource-constrained environments, such as IoT devices. This project dynamically switches between lightweight and robust encryption algorithms based on system parameters like battery level, data sensitivity, and resource availability. It demonstrates the use of LEA, PRESENT, and Speck encryption algorithms to achieve a balance between performance and security.

# Features
Adaptive encryption selection based on real-time system conditions.
Support for multiple encryption algorithms:
 - LEA (Lightweight Encryption Algorithm) for high-performance encryption.
 - PRESENT for ultra-lightweight encryption.
 - Speck for low-power environments.
Input validation for security and usability.
Modular design for easy extensibility.
Dynamic handling of larger input data with block encryption and padding.

# How it works
The system dynamically selects an encryption algorithm based on:
Battery Level: Determines whether a lightweight or robust encryption method is needed.
Data Sensitivity: Highly sensitive data uses more secure algorithms.
Input Size: Handles large data by breaking it into smaller blocks for encryption.
The backend, built in Flask, processes encryption requests and returns encrypted data along with the encryption method used.

# Technologies Used

Frontend - Angular
Form handling with ngModel and validations.
Dynamic result rendering using Angular's *ngIf and *ngFor.

Backend - Flask
REST API for adaptive encryption.
Handles encryption logic with Python-based algorithms.
Flask-CORS - Enables secure cross-origin requests between the frontend and backend.

Encryption Algorithms
LEA (128-bit block cipher)
PRESENT (64-bit block cipher)
Speck (low-power encryption)

#How to Execute the Code

Open the Angular application in your browser at http://localhost:4200.
Fill out the form with the following inputs:
Data to Encrypt: The text string to be encrypted (minimum 5 characters, maximum 200 characters).
Sensitivity: A value between 1 and 10 that determines the importance of the data (higher values select more robust algorithms).
Battery Level: A value between 0% and 100% that simulates the device's battery state (lower values prioritize energy-efficient algorithms).
Click the "Encrypt" button to submit the form.

# Running Code

Backend - python app.py
Frontend - ng serve

# API Endpoints

POST /encrypt

# Example Input

Request:
{
  "data": "Hello World",
  "sensitivity": 8,
  "battery_level": 30
}

# Example Output

Response:
{
  "method": "LEA",
  "encrypted_blocks": [
    [345678345, 893489234, 23452345, 623456234]
  ]
}


# Validation Rules

Frontend Validations
 - Data to Encrypt:
Required.
Minimum 5 characters.
Maximum 200 characters.
 - Sensitivity:
Required.
Must be between 1 and 10.
 - Battery Level:
Required.
Must be between 0% and 100%.


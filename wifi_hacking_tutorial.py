"""
WiFi Security Educational Tool (Simulated for Windows)
Author: Educational Purpose Only
Description:
This Python script simulates scanning WiFi networks and demonstrates password strength
concepts to educate users about WiFi security.

Usage:
- Run this script in PyCharm or any Python 3 environment on Windows.
- You will see a list of simulated WiFi networks.
- Choose a network to "test".
- Try passwords to see if they pass basic strength checks.
- Learn about good password practices.

Note: This does NOT actually hack any real WiFi networks and is fully ethical.
"""

import time
import random
import sys

# Predefined list of simulated WiFi networks
wifi_networks = [
    {"ssid": "HomeNetwork", "encryption": "WPA2"},
    {"ssid": "CoffeeShopWiFi", "encryption": "WPA2"},
    {"ssid": "Airport_Free_WiFi", "encryption": "Open"},
    {"ssid": "Office_WiFi", "encryption": "WPA3"},
    {"ssid": "GuestNetwork", "encryption": "WEP"},
]


def print_slow(text, delay=0.04):
    for char in text:
        print(char, end='', flush=True)
        time.sleep(delay)
    print()


def display_banner():
    print("=" * 50)
    print("  WiFi Security Educational Tool - Simulated Demo  ")
    print("=" * 50)
    print()


def scan_networks():
    print_slow("Scanning for WiFi networks...")
    time.sleep(1)
    print()
    for idx, net in enumerate(wifi_networks, start=1):
        encryption = net["encryption"]
        ssid = net["ssid"]
        print(f" [{idx}] SSID: {ssid:<20} | Encryption: {encryption}")
    print()


def get_network_choice():
    while True:
        try:
            choice = int(input("Choose a network to test (by number): "))
            if 1 <= choice <= len(wifi_networks):
                return wifi_networks[choice - 1]
            else:
                print("Please enter a valid number from the list.")
        except ValueError:
            print("Invalid input. Enter a number.")


def check_password_strength(password):
    """A simple checker for password strength for demonstration."""
    length = len(password)
    digits = sum(c.isdigit() for c in password)
    lowers = sum(c.islower() for c in password)
    uppers = sum(c.isupper() for c in password)
    specials = sum(not c.isalnum() for c in password)

    score = 0
    if length >= 8:
        score += 1
    if digits > 0:
        score += 1
    if lowers > 0 and uppers > 0:
        score += 1
    if specials > 0:
        score += 1

    if score <= 1:
        return "Weak"
    elif score == 2:
        return "Moderate"
    else:
        return "Strong"


def simulate_password_guessing(target_ssid):
    print_slow(f"Starting password strength testing for '{target_ssid}'...")
    tries = 0
    max_tries = 5
    while tries < max_tries:
        password = input(f"Enter password guess #{tries + 1}: ")
        strength = check_password_strength(password)
        print(f" Password strength: {strength}")
        if strength == "Strong":
            print_slow("Good job! This password would be hard to crack.")
        else:
            print_slow("This password is not strong enough.")
        tries += 1
        print()
    print_slow("Password testing complete. Remember to use strong passwords!")
    print_slow("Stay safe and always practice ethical behavior with technology.")


def main():
    display_banner()
    scan_networks()
    selected_network = get_network_choice()
    print()
    print(f"You selected SSID: {selected_network['ssid']} with encryption {selected_network['encryption']}.")
    print()
    simulate_password_guessing(selected_network['ssid'])
    print("Thank you for trying the WiFi Security Educational Tool!")


if __name__ == "__main__":
    main()


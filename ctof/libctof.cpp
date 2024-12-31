double celsius_to_fahrenheit(double input) {
    // °F = °C × (9/5) + 32
    return input * (9.0 / 5.0) + 32;
}

double fahrenheit_to_celsius(double input) {
    // °C = (°F - 32) × 5/9
    return (input - 32) * (5.0 / 9.0);
}

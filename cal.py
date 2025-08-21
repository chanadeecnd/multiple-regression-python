
def calculate_required_voltage(desired_output_voltage: float, operating_frequency_mhz: float) -> float:
    # Coefficients from MLR
    intercept = 74.9390
    coeff_set_voltage = 1.5959
    coeff_frequency = -69.49817  # per MHz

    # Solve for Set Voltage
    required_set_voltage = (
        desired_output_voltage 
        - (coeff_frequency * operating_frequency_mhz) 
        - intercept
    ) / coeff_set_voltage

    print(
        f"Frequency: {operating_frequency_mhz} MHz, "
        f"Desired Output Voltage: {desired_output_voltage} V, "
        f"Required Set Voltage: {required_set_voltage:.2f}"
    )
    return required_set_voltage

calculate_required_voltage(100, 2)
calculate_required_voltage(100, 1.9)
calculate_required_voltage(100, 1.8)
calculate_required_voltage(100, 1.7)
calculate_required_voltage(100, 1.6)


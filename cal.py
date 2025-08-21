
def calculate_vol_set(volt_out, freq):
    indicator = 74.9390
    b_vol = 1.5959
    b_freq = -69.49817


    vol_set = (volt_out - (b_freq * freq) - indicator) / b_vol
    print(f"freq: {freq}, volt_out: {volt_out}, vol_set: {vol_set}")
    return vol_set

calculate_vol_set(60, 2)
calculate_vol_set(100, 1.9)
calculate_vol_set(100, 1.8)
calculate_vol_set(100, 1.7)
calculate_vol_set(100, 1.6)


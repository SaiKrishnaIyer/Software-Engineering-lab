def weather_prediction(t, H, w):
    W = 0.5 * t**2 - 0.2 * H + 0.1 * w - 15
    return W

def predict_weather(W):
    if W >= 300:
        return "Sunny"
    elif 200 <= W < 300:
        return "Cloudy"
    elif 100 <= W < 200:
        return "Rain"
    else:
        return "Storms"

# Assign predefined values for t, H, and w
t = 25
H = 70
w = 10

# Calculate W using the weather prediction formula
W = weather_prediction(t, H, w)

# Make weather prediction based on the calculated W
weather_condition = predict_weather(W)

# Display the result
print(f"Given t = {t}, H = {H}, and w = {w}, the predicted weather is: {weather_condition}")

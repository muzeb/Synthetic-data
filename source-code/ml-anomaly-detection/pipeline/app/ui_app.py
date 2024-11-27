import tkinter as tk
from tkinter import messagebox
import requests
import json

# Function to make the API request and display the result
def call_api():
    # Get values from the input fields
    src_bytes = entry_src_bytes.get()
    dst_bytes = entry_dst_bytes.get()
    count = entry_count.get()
    serror_rate = entry_serror_rate.get()
    protocol = entry_protocol.get()
    service = entry_service.get()

    # Create the JSON payload
    data = {
        "src_bytes": float(src_bytes),
        "dst_bytes": float(dst_bytes),
        "count": float(count),
        "serror_rate": float(serror_rate),
        "protocol": int(protocol),
        "service": int(service)
    }

    # Make the POST request to the API
    try:
        response = requests.post(
            "http://127.0.0.1:8000/predict",
            headers={"Content-Type": "application/json"},
            data=json.dumps(data)
        )

        # Display the prediction result
        result = response.json()
        messagebox.showinfo("Prediction Result", f"Prediction: {result['prediction']} ==> NIST CVSS Score: xxxxxxxx ")

    except Exception as e:
        messagebox.showerror("Error", f"Failed to call the API. Error: {str(e)}")


# Create the main application window
app = tk.Tk()
app.title("Anomaly Detection Predictor")
app.geometry("400x300")

# Labels and entry fields for the input parameters
tk.Label(app, text="src_bytes").pack(pady=5)
entry_src_bytes = tk.Entry(app)
entry_src_bytes.pack()

tk.Label(app, text="dst_bytes").pack(pady=5)
entry_dst_bytes = tk.Entry(app)
entry_dst_bytes.pack()

tk.Label(app, text="count").pack(pady=5)
entry_count = tk.Entry(app)
entry_count.pack()

tk.Label(app, text="serror_rate").pack(pady=5)
entry_serror_rate = tk.Entry(app)
entry_serror_rate.pack()

tk.Label(app, text="protocol").pack(pady=5)
entry_protocol = tk.Entry(app)
entry_protocol.pack()

tk.Label(app, text="service").pack(pady=5)
entry_service = tk.Entry(app)
entry_service.pack()

# Button to trigger the API call
submit_button = tk.Button(app, text="Submit", command=call_api)
submit_button.pack(pady=20)

# Run the Tkinter event loop
app.mainloop()

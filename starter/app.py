import os
from pathlib import Path

import gradio as gr
import joblib

# Get model from pickle file
current_dir = os.path.dirname(__file__)
model = joblib.load(open(Path(current_dir) / "model.pkl", "rb"))


def predict(text):
    # Make prediction
    prediction = model.predict([text])

    return prediction[0]


# Create interface
iface = gr.Interface(fn=predict, inputs="text", outputs="text")


if __name__ == "__main__":
    iface.launch()

import streamlit as st
import importlib

YOLO = importlib.import_module("ultralytics.models.yolo.model").YOLO

def app():
    st.title("YOLO Test")
    try:
        model = YOLO("yolov8n.pt")  # atau "best.pt" jika sudah upload
        st.success("Model loaded successfully!")
    except Exception as e:
        st.error(f"Error loading model: {e}")

if __name__ == "__main__":
    app()

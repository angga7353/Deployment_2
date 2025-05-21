import streamlit as st
# from ultralytics import YOLO
from PIL import Image
import numpy as np
import importlib

Yolo = importlib.import_module("ultralytics.models.yolo.model").Yolo

model = Yolo("best.pt")

def app():
    st.title("AI SEE YOU")

    file = st.file_uploader("Upload an image", type=["jpg", "jpeg", "png"])
    if file is not None:
        img = Image.open(file).convert("RGB")
        st.image(img, caption="Uploaded Image", use_column_width=True)

        img_np = np.array(img)

        results = model.predict(source=img_np, conf=0.25, save=False)
        
        # Process results list
        for result in results:
            boxes = result.boxes  # Boxes object for bounding box outputs
            masks = result.masks  # Masks object for segmentation masks outputs
            keypoints = result.keypoints  # Keypoints object for pose outputs
            probs = result.probs  # Probs object for classification outputs
            obb = result.obb  # Oriented boxes object for OBB outputs
            result.show()  # display to screen
            result.save(filename="result.jpg")  # save to disk

if __name__ == "__main__":
    app()
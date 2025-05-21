import streamlit as st
from ultralytics import YOLO
from PIL import Image
import numpy as np
# import importlib
import matplotlib.pyplot as plt
import matplotlib.patches as patches

# Yolo = importlib.import_module("ultralytics.models.yolo.model").Yolo

model = YOLO("best.pt")

label_map = {
    0: "scissors",
    1: "unidentified",
    2: "knife",
    3: "cutter",
    4: "swiss knife",
}

def app():
    st.title("AI SEE YOU")
    st.image("LOGO_AISEE_YOU.png", use_column_width=224)

    file = st.file_uploader("Upload an image", type=["jpg", "jpeg", "png"])
    if file is not None:
        img = Image.open(file).convert("RGB")
        st.image(img, caption="Uploaded Image", use_column_width=True)
        
        results = model.predict(source=img, conf=0.25, save=False)
        
        if results:
            st.write("Results:")
            for result in results:
                if result.boxes.cls.numel() > 0:

                    fig, ax = plt.subplots()
                    ax.imshow(img)

                    x1, y1, x2, y2 = result.boxes.xyxy[0]
                    rect = patches.Rectangle((x1, y1), x2 - x1, y2 - y1, linewidth=1, edgecolor="r", facecolor="none")
                    ax.add_patch(rect)

                    ax.text(x1, y1, f"{label_map[int(result.boxes.cls[0])]} {result.boxes.conf[0]:.2f}", fontsize=12, color="white", bbox=dict(facecolor="red", alpha=0.5))
                    ax.axis("off")

                    st.pyplot(fig)
                else:
                    st.write("No objects detected.")

if __name__ == "__main__":
    app()
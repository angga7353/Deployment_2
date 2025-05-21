import streamlit as st
# from ultralytics import YOLO
from PIL import Image
import numpy as np
import importlib

<<<<<<< HEAD
Yolo = importlib.import_module("ultralytics.models.yolo.model").Yolo

# model = YOLO("best.pt")
def app():
    st.title("AI SEE YOU")

    # file = st.file_uploader("Upload an image", type=["jpg", "jpeg", "png"])
    # if file is not None:
    #     img = Image.open(file).convert("RGB")
    #     st.image(img, caption="Uploaded Image", use_column_width=True)

    #     model = YOLO("best.pt")
=======
model = YOLO("src/best.pt")
def app():
    st.title("AI SEE YOU")

    file = st.file_uploader("Upload an image", type=["jpg", "jpeg", "png"])
    if file is not None:
        img = Image.open(file).convert("RGB")
        st.image(img, caption="Uploaded Image", use_column_width=True)

        # model = YOLO("src/best.pt")
>>>>>>> 6a6d791 (Add:Project Deploy1)

    #     img_np = np.array(img)

<<<<<<< HEAD
    #     results = model.predict(source=img_np, conf=0.25, save=False)
        # try:
        #     results = model.predict(source=img_np, conf=0.25, save=False)
        # except Exception as e:
        #     st.error(f"Error during prediction: {e}")
        #     return
=======
        # results = model.predict(source=img_np, conf=0.25, save=False)
        try:
            results = model.predict(source=img_np, conf=0.25, save=False)
        except Exception as e:
            st.error(f"Error during prediction: {e}")
            return
>>>>>>> 6a6d791 (Add:Project Deploy1)

        # for result in results:
        #     # Show image with detections (rendered)
        #     st.image(result.plot(), caption="Detected Image", use_column_width=True)

        #     st.write(f"Detected {len(result.boxes)} objects")

        #     for box in result.boxes:
        #         cls = int(box.cls.cpu().numpy())
        #         conf = float(box.conf.cpu().numpy())
        #         class_name = result.names[cls]
        #         st.write(f"Class: {class_name}, Confidence: {conf:.2f}")

        # for result in results:
        #     boxes = result.boxes  # Boxes object for bounding box outputs
        #     masks = result.masks  # Masks object for segmentation masks outputs
        #     keypoints = result.keypoints  # Keypoints object for pose outputs
        #     probs = result.probs  # Probs object for classification outputs
        #     obb = result.obb  # Oriented boxes object for OBB outputs
        #     result.show()  # display to screen
        #     result.save(filename="result.jpg")  # save to disk

if __name__ == "__main__":
    app()
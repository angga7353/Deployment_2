import streamlit as st
import prediction
# import eda  # Uncomment if you have eda.py

# Set page configuration
st.set_page_config(
    page_title="AISeeYou",
    page_icon="LOGO_AISEE_YOU.PNG",  # Menggunakan logo sebagai icon tab
    layout="wide",  # Centered layout
    initial_sidebar_state="expanded"
)

# Inisialisasi session state untuk fun fact
if 'fun_fact_index' not in st.session_state:
    st.session_state['fun_fact_index'] = 0

def main():
    # Sidebar
    st.sidebar.image("LOGO_AISEE_YOU.PNG", width=150)
    st.sidebar.title("Navigation")
    page = st.sidebar.radio("Go to", ["🏠 Home", "🔍 Prediction"])

    if page == "🏠 Home":
        # Sidebar Info
        # st.sidebar.markdown("---")
        # st.sidebar.subheader("📊 About the Model")
        # accuracy = 0.82
        # st.sidebar.write("🎯 Model Accuracy:")
        # st.sidebar.progress(accuracy)
        # st.sidebar.write(f"{accuracy:.2%}")
        # st.sidebar.write("**🤔 What is Accuracy?**")
        # st.sidebar.write("Accuracy measures how well our model correctly classifies waste items.")
        # st.sidebar.write("**💡 What does this mean?**")
        # st.sidebar.write(f"Our model correctly classifies {accuracy:.2%} of waste items, helping improve recycling efficiency.")

        # st.sidebar.markdown("---")
        # st.sidebar.subheader("♻️ Fun Facts")
        # fun_facts = [
        #     "Proper waste classification can increase recycling rates by up to 50%!",
        #     "Recycling one aluminum can saves enough energy to run a TV for three hours.",
        #     "It takes 450 years for a plastic bottle to decompose in a landfill.",
        #     "Glass can be recycled endlessly without losing quality or purity.",
        #     "Recycling paper saves 17 trees and 7,000 gallons of water per ton of paper."
        # ]
        # st.sidebar.info(fun_facts[st.session_state['fun_fact_index']])

        # if st.sidebar.button("Next Fun Fact"):
        #     st.session_state['fun_fact_index'] = (st.session_state['fun_fact_index'] + 1) % len(fun_facts)
        #     st.rerun()

        # Main Content - Home
        st.title("Welcome to AI See You Tools")
        st.write("""
        This application provides functionalities for Exploratory Data Analysis and 
        Prediction of waste types. Use the navigation pane on the left to 
        select the module you wish to utilize.
        """)

        # Logo di tengah halaman
        col1, col2, col3 = st.columns([1, 2, 1])
        with col2:
            st.image("LOGO_AISEE_YOU.PNG", caption="AISeeYou", width=300)

        st.markdown("---")

        # Dataset Info
        st.write("#### 📊 Dataset")
        st.info("""
        The dataset used is the RealWaste dataset, containing images of waste items across 9 major material types, 
        collected within an authentic landfill environment. This dataset provides a realistic representation of 
        waste items, allowing our model to learn from real-world examples.
        """)

        # Problem Statement
        st.write("#### ⚠️ Problem Statement")
        st.warning("""
        Dalam upaya menjaga keselamatan dan keamanan publik, khususnya di tempat-tempat vital seperti bandara,
        terminal, dan gedung pemerintahan, pemeriksaan barang bawaan menjadi langkah penting yang tidak 
        bisa diabaikan. Salah satu metode utama yang digunakan adalah pemindaian X-ray terhadap bagasi 
        atau tas penumpang untuk mendeteksi adanya benda-benda berbahaya seperti senjata api, pisau, atau alat tajam lainnya.
        Meskipun teknologi pemindaian X-ray telah tersedia secara luas, proses interpretasi citra X-ray masih sangat bergantung 
        pada keahlian manusia, yang memiliki keterbatasan dalam hal konsistensi, kecepatan, dan akurasi, terutama ketika 
        menghadapi volume penumpang yang tinggi. Dalam konteks ini, penerapan Artificial Intelligence (AI) dan 
        Computer Vision dapat menjadi solusi potensial untuk meningkatkan efektivitas sistem keamanan.
        """)

        # Objective
        st.write("#### 🎯 Objective")
        st.success("""
        Proyek ini bertujuan untuk secara komprehensif mengeksplorasi dan menganalisis 
        dataset citra X-ray bagasi yang berisi gambar-gambar hasil pemindaian 
        serta anotasi objek-objek berbahaya seperti senjata tajam, bahan peledak, 
        dan benda mencurigakan lainnya dengan metrics yang ditentukan adalah recall dan mAP50 mencapai 80%. Tujuan utama dari proyek ini mencakup beberapa 
        tahap penting yang saling terkait, yakni:
                   
        1. Eksplorasi dan Pemahaman Dataset.
        2. Analisis Distribusi dan Karakteristik Visual.
        3. Analisis Visual Interaktif.
        4. Pengembangan dan Pelatihan Model Deep Learning.
        5. Evaluasi Performa Model.
        6. Interpretasi dan Implikasi Praktis.
                   
        Dengan pendekatan yang sistematis ini, proyek diharapkan mampu menghasilkan pemahaman
        yang mendalam terhadap data serta mengembangkan early prototype model yang dapat mendeteksi
        objek berbahaya. Prototipe ini diharapkan dapat menjadi langkah awal dalam kontribusi
        terhadap sistem keamanan publik yang lebih canggih dan responsif.
        """)

    elif page == "🔍 Prediction":
        prediction.run()

    # elif page == "📊 EDA":
    #     eda.run()

if __name__ == "__main__":
    main()

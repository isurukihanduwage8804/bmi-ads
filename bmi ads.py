import streamlit as st

st.set_page_config(page_title="Health Calculator", page_icon="⚖️")

st.title("⚖️ සරල සෞඛ්‍ය මිනුම් යන්ත්‍රය")

# පටිත්ත (Sidebar) එකේ තොරතුරු
st.sidebar.header("ඔබේ විස්තර")

# 1. වයස ගණනය කිරීම
st.header("📅 වයස ගණනය කරන්න")
birth_year = st.number_input("ඔබ ඉපදුණු වර්ෂය ඇතුළත් කරන්න:", min_value=1900, max_value=2024, value=2000)
current_age = 2024 - birth_year
st.success(f"ඔබේ වයස අවුරුදු {current_age} කි.")

st.divider()

# 2. BMI ගණනය කිරීම
st.header("⚖️ BMI (ශරීර ස්කන්ධ දර්ශකය)")
weight = st.number_input("ඔබේ බර (කිලෝග්‍රෑම් වලින්):", min_value=1.0, value=60.0)
height_cm = st.number_input("ඔබේ උස (සෙන්ටිමීටර වලින්):", min_value=50.0, value=160.0)

if st.button("BMI ගණනය කරන්න"):
    height_m = height_cm / 100
    bmi = weight / (height_m * height_m)
    st.info(f"ඔබේ BMI අගය: {bmi:.2f}")

    # BMI එකට අනුව මිනිස් රූපයක් (Emoji) පෙන්වමු
    if bmi < 18.5:
        st.markdown("<h3><font color='orange'>ඔබේ බර අඩුයි </font> 🧍🏽‍♀️</h3>", unsafe_allow_html=True)
        st.image("https://images.unsplash.com/photo-1542838188-466d6c4c680d?q=80&w=300", caption="බර අඩුයි", width=150)
    elif 18.5 <= bmi < 25:
        st.markdown("<h3><font color='green'>ඔබේ බර නිවැරදියි </font> 🚶🏽‍♀️</h3>", unsafe_allow_html=True)
        st.image("https://images.unsplash.com/photo-1521715015024-e1d84e1b8b8d?q=80&w=300", caption="සාමාන්‍ය බර", width=150)
    else:
        st.markdown("<h3><font color='red'>ඔබේ බර වැඩියි </font> 🏃🏽‍♀️</h3>", unsafe_allow_html=True)
        st.image("https://images.unsplash.com/photo-1549419137-023a1a3e61c7?q=80&w=300", caption="බර වැඩියි", width=150)

st.divider()
st.info("BMI යනු ශරීර ස්කන්ධ දර්ශකයයි. මෙය ඔබගේ උසට සාපේක්ෂව බර තක්සේරු කිරීමට උපකාරී වේ.")

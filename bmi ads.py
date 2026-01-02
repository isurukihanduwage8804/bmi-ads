import streamlit as st
import streamlit.components.v1 as components

# 1. පිටුවේ සැකසුම් (Page Config)
st.set_page_config(page_title="Health Calculator", page_icon="⚖️", layout="centered")

# --- 🛠 ADSTERRA ADS SECTION START ---
# ඔයා එවපු Adsterra කෝඩ් එක මෙතන තියෙන්නේ
ad_script = """
<script src="https://pl28384817.effectivegatecpm.com/24/1e/47/241e47e771671c3805c19e89c7bf378d.js"></script>
"""

# ඇඩ් එක ඇප් එක ඇතුළත ක්‍රියාත්මක කරවන කොටස
components.html(f"{ad_script}", height=0)
# --- 🛠 ADSTERRA ADS SECTION END ---

# ප්‍රධාන මාතෘකාව
st.title("⚖️ සරල සෞඛ්‍ය මිනුම් යන්ත්‍රය")

# පටිත්ත (Sidebar)
st.sidebar.header("මෙනුව")
st.sidebar.info("ඔබේ බර සහ උස අනුව සෞඛ්‍ය තත්ත්වය මෙතනින් පරීක්ෂා කරගන්න.")

# 1. වයස ගණනය කිරීම
st.header("📅 වයස ගණනය කරන්න")
# වර්ෂය 2026 ට යාවත්කාලීන කර ඇත
birth_year = st.number_input("ඔබ ඉපදුණු වර්ෂය ඇතුළත් කරන්න:", min_value=1900, max_value=2026, value=2000)
current_age = 2026 - birth_year
st.success(f"ඔබේ වයස අවුරුදු {current_age} කි.")

st.divider()

# 2. BMI ගණනය කිරීම
st.header("⚖️ BMI (ශරීර ස්කන්ධ දර්ශකය)")
weight = st.number_input("ඔබේ බර (කිලෝග්‍රෑම් වලින්):", min_value=1.0, value=60.0)
height_cm = st.number_input("ඔබේ උස (සෙන්ටිමීටර වලින්):", min_value=50.0, value=160.0)

if st.button("BMI ගණනය කරන්න"):
    if height_cm > 0:
        height_m = height_cm / 100
        bmi = weight / (height_m * height_m)
        st.info(f"ඔබේ BMI අගය: {bmi:.2f}")

        # BMI ප්‍රතිඵල සහ රූප
        if bmi < 18.5:
            st.markdown("### <font color='orange'>ඔබේ බර අඩුයි </font> 🧍🏽‍♀️", unsafe_allow_html=True)
            st.image("https://images.unsplash.com/photo-1542838188-466d6c4c680d?q=80&w=300", width=150)
        elif 18.5 <= bmi < 25:
            st.markdown("### <font color='green'>ඔබේ බර නිවැරදියි </font> 🚶🏽‍♀️", unsafe_allow_html=True)
            st.image("https://images.unsplash.com/photo-1521715015024-e1d84e1b8b8d?q=80&w=300", width=150)
        else:
            st.markdown("### <font color='red'>ඔබේ බර වැඩියි </font> 🏃🏽‍♀️", unsafe_allow_html=True)
            st.image("https://images.unsplash.com/photo-1549419137-023a1a3e61c7?q=80&w=300", width=150)

st.divider()
st.write("BMI යනු ශරීර ස්කන්ධ දර්ශකයයි. මෙය ඔබගේ උසට සාපේක්ෂව බර තක්සේරු කිරීමට උපකාරී වේ.")

# පතුල (Footer)
st.markdown("<br><hr><center>© 2026 KD Isuru. All Rights Reserved.</center>", unsafe_allow_html=True)

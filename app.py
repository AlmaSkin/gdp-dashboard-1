import streamlit as st

# --- اختيار اللغة ---
lang = st.selectbox("🌍 اختر اللغة / Choose language / Choisir la langue:", ["العربية", "English", "Français"])

# --- النصوص حسب اللغة ---
texts = {
    "العربية": {
        "title": "✨ AlmaSkin - أنثوي فخم",
        "welcome": "مرحبًا بك في AlmaSkin! اكتشفي روتين العناية بالبشرة المثالي لكِ.",
        "quiz_title": "استبيان نوع بشرتك 💆‍♀️",
        "q1": "هل بشرتك دهنية؟",
        "q2": "هل تعانين من الجفاف أو القشور؟",
        "q3": "هل تظهر الحبوب أو البقع أحيانًا؟",
        "result": "نتيجتك:",
        "footer": "© 2025 AlmaSkin - لأن الجمال يبدأ من العناية 💖"
    },
    "English": {
        "title": "✨ AlmaSkin - Feminine & Elegant",
        "welcome": "Welcome to AlmaSkin! Discover your perfect skincare routine.",
        "quiz_title": "Skin Type Quiz 💆‍♀️",
        "q1": "Is your skin oily?",
        "q2": "Do you experience dryness or flakiness?",
        "q3": "Do you get pimples or dark spots?",
        "result": "Your result:",
        "footer": "© 2025 AlmaSkin - Beauty begins with care 💖"
    },
    "Français": {
        "title": "✨ AlmaSkin - Féminin et Élégant",
        "welcome": "Bienvenue sur AlmaSkin ! Découvrez votre routine de soins idéale.",
        "quiz_title": "Quiz sur votre type de peau 💆‍♀️",
        "q1": "Votre peau est-elle grasse ?",
        "q2": "Ressentez-vous de la sécheresse ou des desquamations ?",
        "q3": "Avez-vous parfois des boutons ou des taches ?",
        "result": "Votre résultat :",
        "footer": "© 2025 AlmaSkin - La beauté commence par le soin 💖"
    }
}

t = texts[lang]

# --- واجهة التطبيق ---
st.title(t["title"])
st.write(t["welcome"])
st.subheader(t["quiz_title"])

oily = st.checkbox(t["q1"])
dry = st.checkbox(t["q2"])
acne = st.checkbox(t["q3"])

if st.button("✨ عرض النتيجة / Show result / Afficher le résultat"):
    if oily and not dry:
        st.success(f"{t['result']} بشرتك دهنية / Oily / Grasse 🧴")
    elif dry and not oily:
        st.success(f"{t['result']} بشرتك جافة / Dry / Sèche 🌿")
    elif oily and dry:
        st.success(f"{t['result']} بشرتك مختلطة / Combination / Mixte 🌸")
    else:
        st.success(f"{t['result']} بشرتك عادية / Normal / Normale 💧")

st.markdown("---")
st.caption(t["footer"])

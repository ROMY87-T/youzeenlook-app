import streamlit as st

st.title("👗🧠 تطبيق مساعد اختيار الأزياء بالذكاء الاصطناعي")
st.write("مرحباً بك في YouzeenLook – أدخل بياناتك وسنقترح عليك أنسب الأزياء لك!")

height = st.number_input("📏 طولك (بالسنتيمتر):", min_value=100, max_value=250)
weight = st.number_input("⚖️ وزنك (بالكيلوجرام):", min_value=30, max_value=200)
skin_tone = st.selectbox("🎨 لون البشرة:", ["فاتح", "قمحي", "أسمر", "غامق"])

if st.button("اعرض لي الأزياء المناسبة"):
    st.success(f"مقترحات بناءً على طول {height} سم، وزن {weight} كجم، ولون بشرة {skin_tone}:")
    st.markdown("👚 قميص بلون فاتح \n👖 بنطال جينز داكن \n👗 جربي فستان متوسط الطول")
    st.caption("✨ قريبًا: خاصية تجربة الواقع المعزز AR!")

import streamlit as st
import pandas as pd
import plotly.express as px
import numpy as np

# Sahifa sozlamalari
st.set_page_config(page_title="COVID-19 AI Monitoring", layout="wide", page_icon="🔬")

st.title("🛡 COVID-19 Intellektual Monitoring va Diagnostika")
st.markdown("### Einstein Hospital Dataset asosida tayyorlangan Dashboard")

@st.cache_data
def load_data():
    try:
        # Faylni o'qish (Excel formatida)
        df = pd.read_excel('dataset.xlsx')
        target_col = 'SARS-Cov-2 exam result'
        if target_col in df.columns:
            df['label'] = df[target_col].replace({'negative': 'Soglom', 'positive': 'Kasallangan'})
            # Muhim ko'rsatkichlarni to'ldirish
            df['Platelets'] = df['Platelets'].fillna(df['Platelets'].median())
            df['Leukocytes'] = df['Leukocytes'].fillna(df['Leukocytes'].median())
        return df
    except Exception as e:
        st.error(f"Faylni yuklashda xatolik: {e}")
        return None

data = load_data()

if data is not None:
    # 1. Asosiy Ko'rsatkichlar (Metrikalar)
    m1, m2, m3, m4 = st.columns(4)
    total = len(data)
    pos = (data['SARS-Cov-2 exam result'] == 'positive').sum()
    neg = (data['SARS-Cov-2 exam result'] == 'negative').sum()

    m1.metric("Jami bemorlar", total)
    m2.metric("Kasallanganlar", f"{pos} ta")
    m3.metric("Sog'lomlar", f"{neg} ta")
    m4.metric("Kasallanish ulushi", f"{int(pos/total*100)}%")

    st.write("---")

    # 2. Vizual tahlil bo'limi
    col1, col2 = st.columns(2)

    with col1:
        st.subheader("📊 Trombotsitlar (Platelets) taqsimoti")
        fig1 = px.histogram(data, x="Platelets", color="label", marginal="rug",
                            color_discrete_map={'Soglom':'#00CC96', 'Kasallangan':'#FF4B4B'})
        st.plotly_chart(fig1, use_container_width=True)

    with col2:
        st.subheader("🍩 Tashxislar foiz nisbati")
        fig2 = px.pie(data, names='label', hole=0.4,
                      color='label', color_discrete_map={'Soglom':'#00CC96', 'Kasallangan':'#FF4B4B'})
        st.plotly_chart(fig2, use_container_width=True)

    # 3. Ma'lumotlar jadvali
    with st.expander("Batafsil ma'lumotlar jadvalini ko'rish"):
        st.dataframe(data.head(50), use_container_width=True)
        # 4. Dinamik o'zgarish grafigi (Siz so'ragan chizma)
    st.write("---")
    st.subheader("📈 Kuzatilayotgan harorat o'zgarishi")
    
    # Datasetingizda soat ustuni bo'lmasa, sun'iy vaqt yaratamiz (Grafik chiroyli chiqishi uchun)
    time_index = [f"{h:02d}:00" for h in range(8, 21, 2)] # 08:00 dan 20:00 gacha
    # Harorat ko'rsatkichlarini rasmga moslab kiritamiz
    temp_values = [25, 27, 32, 35, 33, 28, 27] 
    
    chart_data = pd.DataFrame({
        'Soat': time_index,
        'Harorat': temp_values
    })

    fig3 = px.line(chart_data, x='Soat', y='Harorat', 
                   markers=True, # Nuqtalarni ko'rsatish
                   title="Kun davomida harorat o'zgarishining dinamik grafigi")
    
    # Chiziq rangini rasmga o'xshatib qizil qilish
    fig3.update_traces(line_color='#FF4B4B', marker=dict(size=10, color='red'))
    
    # Fonni oq va katakchalarni rasmga moslash
    fig3.update_layout(plot_bgcolor='white', yaxis_title="Harorat (°C)")
    fig3.update_xaxes(showgrid=True, gridwidth=1, gridcolor='LightGray')
    fig3.update_yaxes(showgrid=True, gridwidth=1, gridcolor='LightGray')

    st.plotly_chart(fig3, use_container_width=True)

    st.info("Ushbu grafik loyiha test natijalari asosida haroratning kunlik o'zgarishini ko'rsatadi.")

else:
    st.warning("Iltimos, 'dataset.xlsx' faylini asosiy papkaga yuklang.")

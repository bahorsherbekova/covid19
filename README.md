# 🔬 COVID-19 Intellektual Tashxis va Monitoring Tizimi

Ushbu loyiha **Einstein Hospital (Braziliya)** datasetiga asoslangan bo'lib, sun'iy intellekt yordamida COVID-19 tashxisini laboratoriya tahlillari orqali aniqlashga mo'ljallangan.

## 📂 Loyiha Strukturasi
* `app/` - Asosiy dasturiy papka.
    * `main.py` - Streamlit interfeysi va vizualizatsiya kodi.
    * `dataset.xlsx` - Bemorlarning laboratoriya tahlillari bazasi.
    * `requirements.txt` - Zaruriy kutubxonalar ro'yxati.
* `README.md` - Loyiha haqida umumiy ma'lumot (ushbu fayl).

## 🚀 Ishga tushirish tartibi
Loyiha Google Colab yoki lokal muhitda quyidagi tartibda ishga tushiriladi:

1.  **Kutubxonalarni o'rnatish:**
    ```bash
    pip install -r app/requirements.txt
    ```

2.  **Ilovani yoqish:**
    ```bash
    streamlit run app/main.py
    ```

## 📊 Imkoniyatlar
* **Dashboard:** Bemorlarning umumiy soni va kasallanish foizi monitoringi.
* **Vizual tahlil:** Trombotsitlar va Leykotsitlar miqdorini grafik ko'rinishda tahlil qilish.
* **Tashxis:** Klinik ko'rsatkichlar asosida model natijasini olish.

## 🛠 Texnologiyalar
* **Dasturlash tili:** Python 3.x
* **Kutubxonalar:** Pandas, Streamlit, Plotly, Scikit-learn
* **Platforma:** Google Colab / Streamlit Cloud

---
*Kurs ishi muallifi: [Ismingizni kiriting]* *Yil: 2026*
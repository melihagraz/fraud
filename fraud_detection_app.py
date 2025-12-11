import streamlit as st
import pandas as pd
import numpy as np
import plotly.graph_objects as go
import plotly.express as px
from datetime import datetime
import time

# Sayfa konfigürasyonu
st.set_page_config(
    page_title="Fraud Detection System",
    page_icon="🔍",
    layout="wide",
    initial_sidebar_state="expanded"
)

# CSS styling
st.markdown("""
    <style>
    .main-header {
        font-size: 2.5rem;
        font-weight: bold;
        color: #1f77b4;
        text-align: center;
        padding: 1rem 0;
    }
    .metric-card {
        background-color: #f0f2f6;
        padding: 1rem;
        border-radius: 0.5rem;
        margin: 0.5rem 0;
    }
    .fraud-alert {
        background-color: #ff6b6b;
        color: white;
        padding: 1rem;
        border-radius: 0.5rem;
        font-size: 1.5rem;
        font-weight: bold;
        text-align: center;
    }
    .safe-alert {
        background-color: #51cf66;
        color: white;
        padding: 1rem;
        border-radius: 0.5rem;
        font-size: 1.5rem;
        font-weight: bold;
        text-align: center;
    }
    </style>
""", unsafe_allow_html=True)

# Başlık
st.markdown('<div class="main-header">🔍 Fraud Detection System</div>', unsafe_allow_html=True)
st.markdown("---")

# Sidebar - Finansal Rasyolar ve Model Seçimi
st.sidebar.header("📊 Finansal Rasyo Girişleri")

# Finansal rasyolar
ratios = {}
ratios['Likidite Oranı'] = st.sidebar.slider('Likidite Oranı', 0.0, 5.0, 1.5, 0.1)
ratios['Cari Oran'] = st.sidebar.slider('Cari Oran', 0.0, 5.0, 2.0, 0.1)
ratios['Asit-Test Oranı'] = st.sidebar.slider('Asit-Test Oranı', 0.0, 3.0, 1.2, 0.1)
ratios['Borç/Özsermaye'] = st.sidebar.slider('Borç/Özsermaye Oranı', 0.0, 5.0, 1.0, 0.1)
ratios['Faiz Karşılama'] = st.sidebar.slider('Faiz Karşılama Oranı', 0.0, 10.0, 3.0, 0.5)
ratios['Aktif Devir Hızı'] = st.sidebar.slider('Aktif Devir Hızı', 0.0, 5.0, 1.5, 0.1)
ratios['Stok Devir Hızı'] = st.sidebar.slider('Stok Devir Hızı', 0.0, 20.0, 8.0, 0.5)
ratios['Alacak Devir Hızı'] = st.sidebar.slider('Alacak Devir Hızı', 0.0, 15.0, 6.0, 0.5)
ratios['ROA'] = st.sidebar.slider('ROA (%)', -20.0, 30.0, 5.0, 1.0)
ratios['ROE'] = st.sidebar.slider('ROE (%)', -30.0, 50.0, 10.0, 1.0)
ratios['Net Kar Marjı'] = st.sidebar.slider('Net Kar Marjı (%)', -20.0, 30.0, 8.0, 1.0)

st.sidebar.markdown("---")
st.sidebar.header("🤖 Model Seçimi")

# Model seçimi
model_options = {
    "Baseline Models": [
        "Random Forest (RF)",
        "Logistic Regression (LR)",
        "XGBoost",
        "Support Vector Machine (SVM)",
        "Decision Tree",
        "Naive Bayes"
    ],
    "Hybrid Models": [
        "Ensemble Voting (RF+XGB+LR)",
        "Stacking Classifier",
        "Weighted Ensemble",
        "Boosting Hybrid"
    ]
}

model_category = st.sidebar.selectbox("Model Kategorisi", list(model_options.keys()))
selected_model = st.sidebar.selectbox("Model Seç", model_options[model_category])

st.sidebar.markdown("---")

# Run butonu
run_analysis = st.sidebar.button("🚀 Analizi Başlat", type="primary", use_container_width=True)

# Ana panel
col1, col2 = st.columns([2, 1])

with col1:
    st.subheader("📋 Girilen Finansal Rasyolar")
    
    # Rasyoları tablo olarak göster
    ratio_df = pd.DataFrame({
        'Rasyo': list(ratios.keys()),
        'Değer': [f"{v:.2f}" for v in ratios.values()]
    })
    st.dataframe(ratio_df, use_container_width=True, hide_index=True)

with col2:
    st.subheader("🎯 Seçilen Model")
    st.info(f"**Kategori:** {model_category}\n\n**Model:** {selected_model}")

st.markdown("---")

# Analiz sonuçları
if run_analysis:
    with st.spinner('Model çalışıyor... 🔄'):
        time.sleep(2)  # Simüle edilen işlem süresi
        
        # Rastgele tahmin üret
        fraud_probability = np.random.uniform(0.1, 0.95)
        is_fraud = fraud_probability > 0.5
        
        # Sonuç gösterimi
        st.subheader("🎯 Tahmin Sonucu")
        
        col1, col2, col3 = st.columns(3)
        
        with col1:
            if is_fraud:
                st.markdown('<div class="fraud-alert">⚠️ HİLE TESPİT EDİLDİ!</div>', unsafe_allow_html=True)
            else:
                st.markdown('<div class="safe-alert">✅ GÜVENLİ</div>', unsafe_allow_html=True)
        
        with col2:
            st.metric("Hile Olasılığı", f"{fraud_probability*100:.1f}%", 
                     delta=f"{(fraud_probability-0.5)*100:.1f}%",
                     delta_color="inverse")
        
        with col3:
            confidence = abs(fraud_probability - 0.5) * 200
            st.metric("Güven Skoru", f"{confidence:.1f}%")
        
        st.markdown("---")
        
        # Detaylı analiz
        col1, col2 = st.columns(2)
        
        with col1:
            st.subheader("📊 Feature Importance")
            
            # Rastgele feature importance değerleri
            features = list(ratios.keys())
            importances = np.random.dirichlet(np.ones(len(features))) * 100
            
            # Sırala
            sorted_idx = np.argsort(importances)[::-1]
            sorted_features = [features[i] for i in sorted_idx]
            sorted_importances = [importances[i] for i in sorted_idx]
            
            # Bar chart
            fig = go.Figure(go.Bar(
                x=sorted_importances,
                y=sorted_features,
                orientation='h',
                marker=dict(
                    color=sorted_importances,
                    colorscale='Viridis',
                    showscale=True
                )
            ))
            fig.update_layout(
                title="Özelliklerin Önem Dereceleri",
                xaxis_title="Önem (%)",
                yaxis_title="Finansal Rasyolar",
                height=400
            )
            st.plotly_chart(fig, use_container_width=True)
        
        with col2:
            st.subheader("🎯 Olasılık Dağılımı")
            
            # Gauge chart
            fig = go.Figure(go.Indicator(
                mode = "gauge+number+delta",
                value = fraud_probability * 100,
                domain = {'x': [0, 1], 'y': [0, 1]},
                title = {'text': "Hile Riski"},
                delta = {'reference': 50},
                gauge = {
                    'axis': {'range': [None, 100]},
                    'bar': {'color': "darkblue"},
                    'steps': [
                        {'range': [0, 30], 'color': "lightgreen"},
                        {'range': [30, 70], 'color': "lightyellow"},
                        {'range': [70, 100], 'color': "lightcoral"}
                    ],
                    'threshold': {
                        'line': {'color': "red", 'width': 4},
                        'thickness': 0.75,
                        'value': 50
                    }
                }
            ))
            fig.update_layout(height=400)
            st.plotly_chart(fig, use_container_width=True)
        
        st.markdown("---")
        
        # Model performans metrikleri
        st.subheader("📈 Model Performans Metrikleri")
        
        col1, col2, col3, col4 = st.columns(4)
        
        # Rastgele metrikler
        accuracy = np.random.uniform(0.85, 0.98)
        precision = np.random.uniform(0.80, 0.95)
        recall = np.random.uniform(0.75, 0.95)
        f1_score = 2 * (precision * recall) / (precision + recall)
        
        with col1:
            st.metric("Accuracy", f"{accuracy:.2%}")
        with col2:
            st.metric("Precision", f"{precision:.2%}")
        with col3:
            st.metric("Recall", f"{recall:.2%}")
        with col4:
            st.metric("F1-Score", f"{f1_score:.2%}")
        
        # Risk faktörleri
        st.markdown("---")
        st.subheader("⚠️ Tespit Edilen Risk Faktörleri")
        
        risk_factors = []
        
        # Basit kural bazlı risk faktörleri
        if ratios['Likidite Oranı'] < 1.0:
            risk_factors.append("⚠️ Likidite oranı kritik seviyede")
        if ratios['Borç/Özsermaye'] > 2.5:
            risk_factors.append("⚠️ Aşırı borçluluk tespit edildi")
        if ratios['Net Kar Marjı'] < 0:
            risk_factors.append("⚠️ Negatif karlılık")
        if ratios['ROA'] < 0:
            risk_factors.append("⚠️ Varlık getirisi negatif")
        if ratios['Cari Oran'] < 1.0:
            risk_factors.append("⚠️ Kısa vadeli ödeme gücü zayıf")
        
        if risk_factors:
            for risk in risk_factors:
                st.warning(risk)
        else:
            st.success("✅ Ciddi risk faktörü tespit edilmedi")
        
        # İndir butonu
        st.markdown("---")
        
        # Rapor oluştur
        report_data = {
            "Analiz Tarihi": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            "Seçilen Model": selected_model,
            "Tahmin": "HİLE" if is_fraud else "GÜVENLİ",
            "Hile Olasılığı (%)": f"{fraud_probability*100:.2f}",
            "Güven Skoru (%)": f"{confidence:.2f}",
            **ratios
        }
        
        report_df = pd.DataFrame([report_data])
        
        csv = report_df.to_csv(index=False).encode('utf-8')
        st.download_button(
            label="📥 Raporu İndir (CSV)",
            data=csv,
            file_name=f"fraud_detection_report_{datetime.now().strftime('%Y%m%d_%H%M%S')}.csv",
            mime="text/csv",
        )

else:
    st.info("👈 Sol taraftan finansal rasyoları girin, model seçin ve 'Analizi Başlat' butonuna tıklayın.")
    
    # Örnek görsel
    st.subheader("📊 Sistem Özellikleri")
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.markdown("""
        ### 🎯 Baseline Models
        - Random Forest
        - Logistic Regression
        - XGBoost
        - SVM
        - Decision Tree
        - Naive Bayes
        """)
    
    with col2:
        st.markdown("""
        ### 🤖 Hybrid Models
        - Ensemble Voting
        - Stacking Classifier
        - Weighted Ensemble
        - Boosting Hybrid
        """)
    
    with col3:
        st.markdown("""
        ### 📈 Özellikler
        - Feature Importance
        - Performans Metrikleri
        - Risk Faktör Analizi
        - Rapor İndirme
        """)

# Footer
st.markdown("---")
st.markdown("""
    <div style='text-align: center; color: #666; padding: 1rem;'>
    <p>Fraud Detection System v1.0 | Powered by Machine Learning 🚀</p>
    </div>
""", unsafe_allow_html=True)
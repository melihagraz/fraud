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

# Sidebar - Finansal Tablo Kalemleri ve Model Seçimi
st.sidebar.header("💰 Finansal Tablo Kalemleri")

# Para birimi seçimi
currency = st.sidebar.selectbox("Para Birimi", ["TL", "USD", "EUR"], index=0)
st.sidebar.markdown("---")

# Finansal tablo kalemleri
financial_items = {}

st.sidebar.subheader("📊 Bilanço Kalemleri")
financial_items['Nakit ve Nakit Benzerleri'] = st.sidebar.number_input(
    'Nakit ve Nakit Benzerleri', min_value=0.0, value=1000000.0, step=10000.0, format="%.2f"
)
financial_items['Ticari Alacaklar'] = st.sidebar.number_input(
    'Ticari Alacaklar', min_value=0.0, value=2000000.0, step=10000.0, format="%.2f"
)
financial_items['İlişkili Taraflardan Ticari Alacaklar'] = st.sidebar.number_input(
    'İlişkili Taraflardan Ticari Alacaklar', min_value=0.0, value=500000.0, step=10000.0, format="%.2f"
)
financial_items['Stoklar'] = st.sidebar.number_input(
    'Stoklar', min_value=0.0, value=1500000.0, step=10000.0, format="%.2f"
)
financial_items['Toplam Dönen Varlıklar'] = st.sidebar.number_input(
    'Toplam Dönen Varlıklar', min_value=0.0, value=5000000.0, step=10000.0, format="%.2f"
)
financial_items['Maddi Duran Varlıklar'] = st.sidebar.number_input(
    'Maddi Duran Varlıklar', min_value=0.0, value=3000000.0, step=10000.0, format="%.2f"
)
financial_items['Toplam Varlıklar'] = st.sidebar.number_input(
    'Toplam Varlıklar', min_value=0.0, value=10000000.0, step=10000.0, format="%.2f"
)

st.sidebar.markdown("---")

financial_items['Ticari Borçlar'] = st.sidebar.number_input(
    'Ticari Borçlar', min_value=0.0, value=1000000.0, step=10000.0, format="%.2f"
)
financial_items['İlişkili Taraflara Ticari Borçlar'] = st.sidebar.number_input(
    'İlişkili Taraflara Ticari Borçlar', min_value=0.0, value=300000.0, step=10000.0, format="%.2f"
)
financial_items['Toplam Kısa Vadeli Yükümlülükler'] = st.sidebar.number_input(
    'Toplam Kısa Vadeli Yükümlülükler', min_value=0.0, value=3000000.0, step=10000.0, format="%.2f"
)
financial_items['Toplam Yükümlülükler'] = st.sidebar.number_input(
    'Toplam Yükümlülükler', min_value=0.0, value=6000000.0, step=10000.0, format="%.2f"
)
financial_items['Toplam Özkaynaklar'] = st.sidebar.number_input(
    'Toplam Özkaynaklar', min_value=0.0, value=4000000.0, step=10000.0, format="%.2f"
)
financial_items['Toplam Kaynaklar'] = st.sidebar.number_input(
    'Toplam Kaynaklar', min_value=0.0, value=10000000.0, step=10000.0, format="%.2f"
)

st.sidebar.markdown("---")
st.sidebar.subheader("📈 Gelir Tablosu Kalemleri")

financial_items['Hasılat'] = st.sidebar.number_input(
    'Hasılat', value=15000000.0, step=10000.0, format="%.2f"
)
financial_items['Satışların Maliyeti'] = st.sidebar.number_input(
    'Satışların Maliyeti', value=10000000.0, step=10000.0, format="%.2f"
)
financial_items['Brüt Kar/Zarar'] = st.sidebar.number_input(
    'Brüt Kar/Zarar', value=5000000.0, step=10000.0, format="%.2f"
)
financial_items['Finansman Geliri (Gideri) Öncesi Faaliyet Karı (Zararı)'] = st.sidebar.number_input(
    'Finansman Geliri (Gideri) Öncesi Faaliyet Karı (Zararı)', value=2000000.0, step=10000.0, format="%.2f"
)
financial_items['Finansman Giderleri'] = st.sidebar.number_input(
    'Finansman Giderleri', min_value=0.0, value=500000.0, step=10000.0, format="%.2f"
)
financial_items['Sürdürülen Faaliyetler Vergi Öncesi Karı (Zararı)'] = st.sidebar.number_input(
    'Sürdürülen Faaliyetler Vergi Öncesi Karı (Zararı)', value=1500000.0, step=10000.0, format="%.2f"
)
financial_items['Dönem Karı/Zararı'] = st.sidebar.number_input(
    'Dönem Karı/Zararı', value=1200000.0, step=10000.0, format="%.2f"
)
financial_items['Faiz Giderleri (Ek Rapor)'] = st.sidebar.number_input(
    'Faiz Giderleri (Ek Rapor)', min_value=0.0, value=400000.0, step=10000.0, format="%.2f"
)

st.sidebar.markdown("---")
st.sidebar.header("🎯 Hile Türü Seçimi")

# Hile türü seçimi
fraud_types = {
    "Hile Türü 1": "Satışların maliyetini düşük gösterip, stokların şişirilmesi",
    "Hile Türü 2": "Dönem karını artırmak amacıyla amortisman giderlerini olması gerekenden eksik ayrılması",
    "Hile Türü 3": "Şirketin kısa vadeli banka kredilerini vadelerine göre hatalı sınıflandırıp ve uzun vadeli banka kredilerinde göstermiştir"
}

selected_fraud_type = st.sidebar.selectbox(
    "Hile Türü Seçin",
    list(fraud_types.keys()),
    format_func=lambda x: f"{x}: {fraud_types[x]}"
)

st.sidebar.markdown("---")

# Run butonu
run_analysis = st.sidebar.button("🚀 Analizi Başlat", type="primary", use_container_width=True)

# Ana panel
col1, col2 = st.columns([2, 1])

with col1:
    st.subheader("📋 Girilen Finansal Tablo Kalemleri")
    
    # Finansal kalemleri tablo olarak göster
    financial_df = pd.DataFrame({
        'Kalem': list(financial_items.keys()),
        'Değer': [f"{v:,.2f} {currency}" for v in financial_items.values()]
    })
    st.dataframe(financial_df, use_container_width=True, hide_index=True)

with col2:
    st.subheader("🎯 Seçilen Hile Türü")
    st.info(f"**{selected_fraud_type}**\n\n{fraud_types[selected_fraud_type]}")

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
            features = list(financial_items.keys())
            importances = np.random.dirichlet(np.ones(len(features))) * 100
            
            # Sırala ve en önemli 10'u al
            sorted_idx = np.argsort(importances)[::-1][:10]
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
                title="Özelliklerin Önem Dereceleri (Top 10)",
                xaxis_title="Önem (%)",
                yaxis_title="Finansal Kalemler",
                height=450
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
        if financial_items['Toplam Varlıklar'] > 0:
            current_ratio = financial_items['Toplam Dönen Varlıklar'] / financial_items['Toplam Kısa Vadeli Yükümlülükler'] if financial_items['Toplam Kısa Vadeli Yükümlülükler'] > 0 else 0
            if current_ratio < 1.0:
                risk_factors.append("⚠️ Cari oran kritik seviyede (kısa vadeli ödeme gücü zayıf)")
        
        if financial_items['Toplam Özkaynaklar'] > 0:
            debt_to_equity = financial_items['Toplam Yükümlülükler'] / financial_items['Toplam Özkaynaklar']
            if debt_to_equity > 2.5:
                risk_factors.append("⚠️ Aşırı borçluluk tespit edildi (Borç/Özkaynak > 2.5)")
        
        if financial_items['Dönem Karı/Zararı'] < 0:
            risk_factors.append("⚠️ Dönem zararı var")
        
        if financial_items['Brüt Kar/Zarar'] < 0:
            risk_factors.append("⚠️ Brüt zarar var")
        
        if financial_items['Toplam Varlıklar'] != financial_items['Toplam Kaynaklar']:
            difference = abs(financial_items['Toplam Varlıklar'] - financial_items['Toplam Kaynaklar'])
            if difference > financial_items['Toplam Varlıklar'] * 0.01:  # %1'den fazla fark varsa
                risk_factors.append("⚠️ Bilanço dengesizliği (Aktif ≠ Pasif)")
        
        if financial_items['Hasılat'] > 0:
            profit_margin = (financial_items['Dönem Karı/Zararı'] / financial_items['Hasılat']) * 100
            if profit_margin < 0:
                risk_factors.append("⚠️ Net kar marjı negatif")
        
        # İlişkili taraf işlemleri kontrolü
        related_party_receivables_ratio = (financial_items['İlişkili Taraflardan Ticari Alacaklar'] / financial_items['Ticari Alacaklar'] * 100) if financial_items['Ticari Alacaklar'] > 0 else 0
        if related_party_receivables_ratio > 30:
            risk_factors.append(f"⚠️ İlişkili taraf alacakları yüksek (%{related_party_receivables_ratio:.1f})")
        
        related_party_payables_ratio = (financial_items['İlişkili Taraflara Ticari Borçlar'] / financial_items['Ticari Borçlar'] * 100) if financial_items['Ticari Borçlar'] > 0 else 0
        if related_party_payables_ratio > 30:
            risk_factors.append(f"⚠️ İlişkili taraf borçları yüksek (%{related_party_payables_ratio:.1f})")
        
        if risk_factors:
            for risk in risk_factors:
                st.warning(risk)
        else:
            st.success("✅ Ciddi risk faktörü tespit edilmedi")
        
        # Finansal Rasyolar Özeti
        st.markdown("---")
        st.subheader("📊 Hesaplanan Finansal Rasyolar")
        
        col1, col2, col3, col4 = st.columns(4)
        
        with col1:
            if financial_items['Toplam Kısa Vadeli Yükümlülükler'] > 0:
                current_ratio = financial_items['Toplam Dönen Varlıklar'] / financial_items['Toplam Kısa Vadeli Yükümlülükler']
                st.metric("Cari Oran", f"{current_ratio:.2f}")
            else:
                st.metric("Cari Oran", "N/A")
        
        with col2:
            if financial_items['Toplam Özkaynaklar'] > 0:
                debt_to_equity = financial_items['Toplam Yükümlülükler'] / financial_items['Toplam Özkaynaklar']
                st.metric("Borç/Özkaynak", f"{debt_to_equity:.2f}")
            else:
                st.metric("Borç/Özkaynak", "N/A")
        
        with col3:
            if financial_items['Hasılat'] > 0:
                profit_margin = (financial_items['Dönem Karı/Zararı'] / financial_items['Hasılat']) * 100
                st.metric("Net Kar Marjı", f"{profit_margin:.2f}%")
            else:
                st.metric("Net Kar Marjı", "N/A")
        
        with col4:
            if financial_items['Toplam Varlıklar'] > 0:
                roa = (financial_items['Dönem Karı/Zararı'] / financial_items['Toplam Varlıklar']) * 100
                st.metric("ROA", f"{roa:.2f}%")
            else:
                st.metric("ROA", "N/A")
        
        # İndir butonu
        st.markdown("---")
        
        # Rapor oluştur
        report_data = {
            "Analiz Tarihi": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            "Para Birimi": currency,
            "Seçilen Hile Türü": f"{selected_fraud_type}: {fraud_types[selected_fraud_type]}",
            "Tahmin": "HİLE" if is_fraud else "GÜVENLİ",
            "Hile Olasılığı (%)": f"{fraud_probability*100:.2f}",
            "Güven Skoru (%)": f"{confidence:.2f}",
            **financial_items
        }
        
        report_df = pd.DataFrame([report_data])
        
        csv = report_df.to_csv(index=False).encode('utf-8-sig')
        st.download_button(
            label="📥 Raporu İndir (CSV)",
            data=csv,
            file_name=f"fraud_detection_report_{datetime.now().strftime('%Y%m%d_%H%M%S')}.csv",
            mime="text/csv",
        )

else:
    st.info("👈 Sol taraftan finansal tablo kalemlerini girin, hile türünü seçin ve 'Analizi Başlat' butonuna tıklayın.")
    
    # Örnek görsel
    st.subheader("📊 Sistem Özellikleri")
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.markdown("""
        ### 🎯 Hile Türü 1
        Satışların maliyetini düşük gösterip, stokların şişirilmesi
        """)
    
    with col2:
        st.markdown("""
        ### 🎯 Hile Türü 2
        Dönem karını artırmak amacıyla amortisman giderlerini olması gerekenden eksik ayrılması
        """)
    
    with col3:
        st.markdown("""
        ### 🎯 Hile Türü 3
        Şirketin kısa vadeli banka kredilerini vadelerine göre hatalı sınıflandırıp ve uzun vadeli banka kredilerinde göstermiştir
        """)

# Footer
st.markdown("---")
st.markdown("""
    <div style='text-align: center; color: #666; padding: 1rem;'>
    <p>Fraud Detection System v2.0 | Powered by Machine Learning 🚀</p>
    </div>
""", unsafe_allow_html=True)

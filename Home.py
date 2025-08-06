import streamlit as st
from streamlit_app.utils.carregar_niveis import carregar_niveis_de_usuarios

st.title("🎞️ Níveis de Colecionador – Edição Cult VHS")

niveis = carregar_niveis_de_usuarios()

for nivel in niveis:
    st.markdown(f"""
    <div style="background-color:#111111;padding:15px;border-radius:10px;margin-bottom:10px;border:1px solid #444;">
        <h4 style="margin:0;">{nivel['icone']} <span style="color:#FFD700;">{nivel['codinome']}</span> – <span style="color:#00FFFF;">{nivel['titulo']}</span></h4>
        <p style="margin:5px 0 5px 0;"><strong>🎯 Acesso Simbólico:</strong> {nivel['acesso_simbolico']}</p>
        <p style="margin:5px 0;"><strong>💰 Requisito:</strong> R$ {nivel['requisito_em_reais']:.2f}</p>
        <p style="margin:5px 0;color:#DDDDDD;">📝 {nivel['descricao']}</p>
    </div>
    """, unsafe_allow_html=True)

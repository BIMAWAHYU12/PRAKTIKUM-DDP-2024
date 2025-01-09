import streamlit as st 


st.markdown(
    """
    <style>
    .stApp{
        background-color: #FFFFFF;
    }
    
    [data-testid="stSidebar"]{
        background-color: #FFA500;
        color: white;
    }
    
    [data-testid="stSidebar"] * {
        color: white !important;
        font-size: 14px;
    
    }
    
    # .stApp{
    # }
    
    </style>
    """,
    unsafe_allow_html = True 
)

dashboard = st.Page("./fitur/dashboard.py", title="Dashboard")
nabung = st.Page("./fitur/nabung.py", title="Menabung")
penarikan = st.Page("./fitur/penarikan.py", title="Penarikan")

pg = st.navigation(
    {
     "Menu Utama" : [dashboard],
     "Transaksi" : [nabung, penarikan],
        
    }
)

if 'total_semua' not in st.session_state:
    st.session_state['total_semua'] = []

pg.run()
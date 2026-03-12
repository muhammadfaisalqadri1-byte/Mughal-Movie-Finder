import streamlit as st
import requests

# Page Layout aur Styling
st.set_page_config(
    page_title="Mughal Movie Finder",
    page_icon="🎬",
    layout="wide"
)

# Custom CSS (Buttons aur Background ko behtar banane ke liye)
st.markdown("""
    <style>
    .stButton>button { width: 100%; border-radius: 8px; background-color: #E50914; color: white; font-weight: bold; }
    .stTextInput>div>div>input { border-radius: 8px; }
    </style>
    """, unsafe_allow_html=True)

# Sidebar (Sirf Branding ke liye)
with st.sidebar:
    st.title("🛡️ Mughal Systems")
    st.write("---")
    st.write("Developed by **Faisal Mughal**")
    st.info("Custom Search Engine for Movies & Series")

# Main Screen
st.title("🎬 Faisal's Movie Finder Pro")
st.write("Dunya bhar ki movies ka data foran dhoondein aur poster dekhein.")

# Input Section
col1, col2 = st.columns([4, 1])
with col1:
    movie_name = st.text_input("", placeholder="Movie ya Series ka naam yahan likhen...")
with col2:
    search_btn = st.button("Dhoondo 🔍")

# API Logic
if search_btn:
    if movie_name:
        # Apni OMDb API Key yahan lagayein
        api_key = "3afc6c82" 
        url = f"http://www.omdbapi.com/?t={movie_name}&apikey={api_key}"
        
        with st.spinner('Data aa raha hai...'):
            response = requests.get(url).json()
        
        if response.get("Response") == "True":
            st.write("---")
            res_col1, res_col2 = st.columns([1, 2])
            
            with res_col1:
                st.image(response.get("Poster"), use_container_width=True)
                
            with res_col2:
                st.header(response.get("Title"))
                st.write(f"📅 **Release Date:** {response.get('Released')}")
                st.write(f"⭐ **IMDb Rating:** {response.get('imdbRating')} / 10")
                st.write(f"🎭 **Genre:** {response.get('Genre')}")
                st.write(f"✍️ **Director:** {response.get('Director')}")
                st.write(f"👥 **Actors:** {response.get('Actors')}")
                
                with st.expander("Movie ki Story (Plot) Dekhein"):
                    st.write(response.get("Plot"))
        else:
            st.error("Movie nahi mili! Spelling check karke dobara koshish karein.")
    else:
        st.warning("Pehle movie ka naam to likhen!")

st.markdown("---")
st.caption("© 2026 Mughal Systems | Faisal's Custom Build")
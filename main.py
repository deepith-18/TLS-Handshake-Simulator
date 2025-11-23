import streamlit as st
import time
from logic.client import TLSClient
from logic.server import TLSServer
from logic.utils import simulate_encryption

# --- Page Config ---
st.set_page_config(page_title="TLS 1.3 Handshake Simulator", layout="wide", page_icon="🔒")

# --- Custom CSS for UI Polish ---
st.markdown("""
<style>
    .stButton>button {
        width: 100%;
        border-radius: 5px;
        height: 3em;
        font-weight: bold;
    }
    .step-box {
        background-color: #1E1E1E;
        padding: 15px;
        border-radius: 10px;
        border-left: 5px solid #4CAF50;
        margin-bottom: 10px;
        color: #DDD;
    }
    .arrow-down {
        text-align: center;
        font-size: 24px;
        color: #888;
        margin: 5px 0;
    }
    .secure-banner {
        background-color: #d4edda;
        color: #155724;
        padding: 20px;
        border-radius: 10px;
        text-align: center;
        font-size: 20px;
        font-weight: bold;
        border: 1px solid #c3e6cb;
    }
</style>
""", unsafe_allow_html=True)

# --- Session State Management ---
if 'stage' not in st.session_state:
    st.session_state.stage = 0
if 'logs' not in st.session_state:
    st.session_state.logs = []
if 'client' not in st.session_state:
    st.session_state.client = TLSClient()
if 'server' not in st.session_state:
    st.session_state.server = TLSServer()
if 'client_hello_data' not in st.session_state:
    st.session_state.client_hello_data = {}
if 'server_hello_data' not in st.session_state:
    st.session_state.server_hello_data = {}

# --- Sidebar Controls ---
st.sidebar.title("🛠 Configuration")
st.sidebar.markdown("Simulate a connection setup between a User and a Server.")
tls_version = st.sidebar.selectbox("TLS Version", ["TLS 1.3", "TLS 1.2 (Legacy)"])
cipher_preference = st.sidebar.multiselect(
    "Client Cipher Suites", 
    ["TLS_AES_128_GCM_SHA256", "TLS_AES_256_GCM_SHA384"],
    default=["TLS_AES_128_GCM_SHA256"]
)

if st.sidebar.button("Reset Simulation"):
    st.session_state.stage = 0
    st.session_state.logs = []
    st.rerun()

# --- Main Header ---
st.title("🔐 TLS Handshake Simulator")
st.markdown(f"Current Mode: **{tls_version}** | Status: **{'Connected' if st.session_state.stage == 4 else 'Handshaking...'}**")
st.markdown("---")

# --- Layout Columns ---
col1, col2, col3 = st.columns([1, 0.2, 1])

with col1:
    st.subheader("💻 Client (Browser)")
    
with col3:
    st.subheader("☁️ Server (Website)")

# --- Step 1: Client Hello ---
if st.session_state.stage >= 1:
    with col1:
        st.info(f"📤 **Client Hello** sent")
        with st.expander("View Packet Details"):
            st.json(st.session_state.client_hello_data)

    with col2:
        st.markdown("<div class='arrow-down'>➡️</div>", unsafe_allow_html=True)

# --- Step 2: Server Hello ---
if st.session_state.stage >= 2:
    with col3:
        st.success(f"📥 **Server Hello** received")
        st.warning(f"🔑 **Certificate** sent")
        with st.expander("View Packet Details"):
            st.json(st.session_state.server_hello_data)
    
    with col2:
        st.markdown("<div class='arrow-down'>⬅️</div>", unsafe_allow_html=True)

# --- Step 3: Key Exchange / Finished ---
if st.session_state.stage >= 3:
    with col1:
        st.warning("🗝️ **Client Key Exchange**")
        st.info("🔒 **Change Cipher Spec**")
        pms = st.session_state.client.generate_pre_master_secret()
        st.code(f"Pre-Master Secret: {pms[:20]}...", language="text")
    
    with col2:
         st.markdown("<div class='arrow-down'>➡️</div>", unsafe_allow_html=True)

# --- Step 4: Connection Established ---
if st.session_state.stage >= 4:
    st.markdown("---")
    st.markdown(f"""
    <div class='secure-banner'>
        🔒 SECURE CONNECTION ESTABLISHED<br>
        <span style='font-size:14px; font-weight:normal'>Data transfer is now encrypted using {st.session_state.server_hello_data.get('cipher_suite')}</span>
    </div>
    """, unsafe_allow_html=True)
    
    # Simulate Chat
    st.markdown("### 💬 Encrypted Data Stream")
    user_msg = st.chat_input("Type a secure message to the server...")
    if user_msg:
        st.markdown(f"**You:** {user_msg}")
        st.markdown(f"**Network View:** `{simulate_encryption(user_msg)}`")
        time.sleep(0.5)
        st.markdown(f"**Server:** I received your secure message!")


# --- Control Logic (The "Play" Sequence) ---
st.markdown("---")
controls_col1, controls_col2, controls_col3 = st.columns([1, 2, 1])

with controls_col2:
    if st.session_state.stage == 0:
        if st.button("Start Handshake ▶️"):
            # Logic for Step 1
            client = st.session_state.client
            client.cipher_suites = cipher_preference # Update based on config
            st.session_state.client_hello_data = client.send_client_hello()
            st.session_state.stage = 1
            st.rerun()
            
    elif st.session_state.stage == 1:
        time.sleep(0.5) # Visual delay
        if st.button("Process Server Response ▶️"):
            # Logic for Step 2
            server = st.session_state.server
            st.session_state.server_hello_data = server.process_client_hello(st.session_state.client_hello_data)
            st.session_state.stage = 2
            st.rerun()

    elif st.session_state.stage == 2:
        time.sleep(0.5)
        if st.button("Verify Cert & Exchange Keys ▶️"):
            # Logic for Step 3
            st.session_state.stage = 3
            st.rerun()

    elif st.session_state.stage == 3:
        time.sleep(0.5)
        if st.button("Finalize Handshake ▶️"):
            # Logic for Step 4
            st.session_state.stage = 4
            st.rerun()
            
    elif st.session_state.stage == 4:
        if st.button("Close Connection ❌"):
            st.session_state.stage = 0
            st.rerun()
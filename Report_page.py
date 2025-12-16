import streamlit as st
import subprocess
import requests
import time
import os
import streamlit.components.v1 as components

def is_server_running(url="http://localhost:3000"):
    """Check if the Next.js server is responsive."""
    try:
        # Increased timeout to 100000s and handle Timeout exception
        response = requests.get(url, timeout=100000)
        return response.status_code == 200
    except (requests.ConnectionError, requests.Timeout):
        return False
    except requests.RequestException:
        return False

def start_nextjs_server():
    """Start the Next.js server as a background subprocess."""
    # Define the path to your Next.js project
    # Current file is in .../Data-reader
    # Next.js app is in .../Data-reader/fmis-report
    project_dir = os.path.join(os.path.dirname(__file__), "fmis-report")
    
    # Check if node_modules exists, if not, maybe run npm install (optional, avoiding for speed)
    if not os.path.exists(os.path.join(project_dir, "node_modules")):
        st.warning("⚠️ 'node_modules' not found. Installing dependencies... (this may take a minute)")
        subprocess.run(["npm", "install"], cwd=project_dir, shell=True)
    
    # Start the server
    # We use 'npm run dev' typically. On Windows 'npm.cmd'.
    # Using Popen to run in background.
    process = subprocess.Popen(
        ["npm", "run", "dev"], 
        cwd=project_dir, 
        shell=True,
        stdout=subprocess.DEVNULL, # Suppress output to keep terminal clean
        stderr=subprocess.DEVNULL
    )
    return process

def Report():
    # 🔹 Custom CSS to maximize iframe space
    st.markdown("""
        <style>
            .block-container {
                padding-top: 1rem;
                padding-bottom: 0rem;
                padding-left: 1rem;
                padding-right: 1rem;
                max-width: 120%;
            }
            /* Optional: Hide Streamlit header if desired for cleaner look */
            /* header {visibility: hidden;} */
        </style>
    """, unsafe_allow_html=True)

    NEXTJS_URL = "http://localhost:3000"

    # Container for status messages
    status_placeholder = st.empty()

    if not is_server_running(NEXTJS_URL):
        # status_placeholder.info("🚀 Starting Next.js Report Dashboard... Please wait.")
        start_nextjs_server()
        
        # Wait loop
        retries = 30 # Wait up to 30 seconds
        for i in range(retries):
            if is_server_running(NEXTJS_URL):
                # status_placeholder.success("✅ Dashboard Connected!")
                time.sleep(1) # Brief pause to show success
                status_placeholder.empty() # Clear message
                break
            time.sleep(1)
        else:
            status_placeholder.error("❌ Failed to connect to Next.js server. Please check the terminal for errors.")
            st.stop()
    else:
        # Server already running
        pass
        
    # 🔹 Embed the Next.js App
    # Adjust height to fit typical screen, scrolling handled inside iframe
    components.iframe(NEXTJS_URL, height=900, scrolling=True)

if __name__ == "__main__":
    Report()


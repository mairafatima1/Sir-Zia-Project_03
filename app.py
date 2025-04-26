import streamlit as st

# Page Configuration
st.set_page_config(page_title="Registration App", page_icon="🚀", layout="centered")

# Colorful and Professional Styling
st.markdown(
    """
    <style>
        /* Overall Body Layout */
        .stApp {
            background: linear-gradient(to right, #6A11CB, #2575FC);  /* Gradient Background */
            font-family: 'Roboto', sans-serif;
            padding: 0;
            height: 100vh;
        }

        /* Centered Registration Card */
        .card {
            background-color: #ffffff;
            border-radius: 15px;
            box-shadow: 0 4px 15px rgba(0, 0, 0, 0.1);
            padding: 40px;
            max-width: 400px;
            margin: 50px auto;
            text-align: center;
        }

        /* Title Styling */
        h1 {
            font-family: 'Roboto', sans-serif;
            color: #333;
            font-weight: 700;
            margin-bottom: 20px;
        }
        h3 {
            font-family: 'Roboto', sans-serif;
            color: #555;
            margin-bottom: 30px;
            font-weight: 400;
        }

        /* Input Fields */
        .stTextInput>div>div>input {
            background-color: #f1f1f1;
            border-radius: 8px;
            padding: 15px;
            border: 1px solid #ddd;
            font-size: 16px;
            color: #333;
            margin-bottom: 20px;
            transition: all 0.3s ease;
        }
        .stTextInput>div>div>input:focus {
            border: 2px solid #2575FC;
            box-shadow: 0 0 10px rgba(37, 117, 252, 0.4);
        }

        /* Register Button */
        .stButton>button {
            background-color: #FF6F61;  /* Vibrant Coral color */
            color: white;
            font-size: 18px;
            font-weight: 600;
            padding: 14px 25px;
            border-radius: 8px;
            border: none;
            width: 100%;
            transition: all 0.3s ease;
            margin-top: 10px;
        }
        .stButton>button:hover {
            background-color: #E55C50;
            transform: scale(1.05);
        }

        /* Success and Error Alerts */
        .stAlert {
            border-radius: 8px;
            padding: 10px 15px;
            font-family: 'Roboto', sans-serif;
            font-weight: 500;
            margin-top: 20px;
            background-color: #F4F9FF;
            color: #4CAF50;  /* Green for success */
        }

        .stError {
            background-color: #FFEBEE;  /* Red alert for error */
            color: #D32F2F;
        }

        /* Download Button */
        .stDownloadButton>button {
            background-color: #28A745;  /* Green button for download */
            color: white;
            font-size: 16px;
            font-weight: 600;
            padding: 12px 25px;
            border-radius: 8px;
            margin-top: 20px;
            width: 100%;
            border: none;
            transition: all 0.3s ease;
        }
        .stDownloadButton>button:hover {
            background-color: #218838;
            transform: scale(1.05);
        }
    </style>
    """,
    unsafe_allow_html=True
)

# Registration Function with Colorful and Modern UI Design
def register():
    with st.container():
        st.markdown('<div class="card">', unsafe_allow_html=True)
        st.title("🚀 Premium Registration Portal")
        st.markdown("### Complete your registration details below")

        # Input Fields
        name = st.text_input("👤 Full Name", placeholder="Enter your full name")
        email = st.text_input("📧 Email Address", placeholder="Enter your email")
        password = st.text_input("🔑 Password", placeholder="Create a strong password", type="password")
        confirm_password = st.text_input("🔒 Confirm Password", placeholder="Re-enter your password", type="password")

        # Register Button
        if st.button("✅ Register"):
            if not name or not email or not password or not confirm_password:
                st.warning("⚠️ Please fill in all fields.")
            elif password != confirm_password:
                st.error("❌ Passwords do not match. Please check.")
            else:
                filename = f"{name.replace(' ', '_')}.txt"
                with open(filename, 'w') as file:
                    file.write(f'Name: {name}\n')
                    file.write(f'Email: {email}\n')
                    file.write(f'Password: {password}\n')
                st.success(f"🎉 Registration Successful!\n\nWelcome, {name}!")

                # Download file
                with open(filename, "rb") as file:
                    st.download_button(label="📥 Download Your Registration Info", data=file, file_name=filename, mime="text/plain")

        st.markdown('</div>', unsafe_allow_html=True)

if __name__ == "__main__":
    register()

# Footer Section
st.markdown(
    '<div class="footer">This was created by Fatima.</div>',
    unsafe_allow_html=True
)


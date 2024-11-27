import google.generativeai as genai
import streamlit as st
from PIL import Image
from fpdf import FPDF
import markdown

## Initialize our streamlit app
st.set_page_config(page_title="Skin & Makeup Analysis App", page_icon=':sparkles:')

# Use local CSS
def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)
local_css("style/style.css")

st.image("images/maintitle.png")

menu = ["Home", "Skin Analysis", "The Future"]

# Create columns to align buttons horizontally
# Since we have 4 buttons, we need 4 columns
col1, col2, col3 = st.columns(len(menu))

# Display buttons in each column
with col1:
    if st.button("Home"):
        st.session_state.page = "Home"       
with col2:
    if st.button("Skin Analysis"):
        st.session_state.page = "Skin Analysis"
with col3:
    if st.button("The Future"):
        st.session_state.page = "The Future"
st.markdown('---')

# Initialize session state if not set
if 'page' not in st.session_state:
    st.session_state.page = "Home"

# Show content based on the selected page
page = st.session_state.page

# Color Hex codes
teal = "#adcec8"
pink = "#fadbd3"
text = "#110301"
# Teal buttons: #adcec8
# Light pink: #fadbd3
# Text: #110301

# Formatting buttons with CSS
st.markdown("""
    <style>
    .stButton > button {
        height: auto;
        padding-top: 20px;
        padding-bottom: 20px;
        font-size: 20px;
        font-weight: bold;
        color: white;
        background-color: #adcec8;
        border: none;
        border-radius: 8px;
        width: 100%;
        cursor: pointer;
    }
    .stButton > button:hover {
        border: 2px solid #adcec8;
        background-color: white;
        color: #3E2C1C;
    }
    </style>
    """, unsafe_allow_html=True)

# ===========================================================
# HOME PAGE
# ===========================================================
if page == "Home":
    col1, col2 = st.columns([3, 2])
    with col1:
        st.markdown("""
        <link href="https://fonts.googleapis.com/css2?family=The+Seasons&display=swap" rel="stylesheet">
        <h1 style="color: #110301; font-family: 'The Seasons', serif; font-weight: bold; text-align: left;">
            The Smart Solution for Skin
        </h1>
        """, unsafe_allow_html=True)
        st.markdown("""
        <link href="https://fonts.googleapis.com/css2?family=Montserrat:wght@400;700&display=swap" rel="stylesheet">
        <h6 style="color: #110301; font-family: 'Montserrat', sans-serif; font-weight: normal; text-align: left;">
            Blending the power of advanced AI technology with completely personalized beauty insights to provide
            your customers with tailored skin analysis and makeup recommendations.
        </h6>
        """, unsafe_allow_html=True)
    with col2:
        st.image("images/skincare.gif")

    st.markdown('---')

    st.markdown("""
    <link href="https://fonts.googleapis.com/css2?family=The+Seasons&display=swap" rel="stylesheet">
    <h1 style="color: #110301; font-family: 'The Seasons', serif; font-weight: bold; text-align: center;">
        What we do
    </h1>
    """, unsafe_allow_html=True)
    col1, col2, col3 = st.columns(3)
    with col1:
        st.markdown(f"""
        <div style="background-color: {pink}; padding: 20px; border-radius: 10px;">
            <link href="https://fonts.googleapis.com/css2?family=The+Seasons&display=swap" rel="stylesheet">
            <h5 style="color: #110301; font-family: 'The Seasons', serif; font-weight: bold; text-align: center;">
                AI-Powered Precision
            </h5>
            <link href="https://fonts.googleapis.com/css2?family=Montserrat:wght@400;700&display=swap" rel="stylesheet">
            <h6 style="color: #110301; font-family: 'Montserrat', sans-serif; font-weight: normal; text-align: center;">
                Detailed skin tone analysis, color matching, and skin-care routine recommendations
            </h6>
        </div>
        """, unsafe_allow_html=True)
    with col2:
        st.markdown(f"""
        <div style="background-color: {pink}; padding: 20px; border-radius: 10px;">
            <link href="https://fonts.googleapis.com/css2?family=The+Seasons&display=swap" rel="stylesheet">
            <h5 style="color: #110301; font-family: 'The Seasons', serif; font-weight: bold; text-align: center;">
                Tailored Product Suggestions
            </h5>
            <link href="https://fonts.googleapis.com/css2?family=Montserrat:wght@400;700&display=swap" rel="stylesheet">
            <h6 style="color: #110301; font-family: 'Montserrat', sans-serif; font-weight: normal; text-align: center;">
                Discover make up products and skincare solutions that align perfectly with individual skin goals.
            </h6>
        </div>
        """, unsafe_allow_html=True)
    with col3:
        st.markdown(f"""
        <div style="background-color: {pink}; padding: 20px; border-radius: 10px;">
            <link href="https://fonts.googleapis.com/css2?family=The+Seasons&display=swap" rel="stylesheet">
            <h5 style="color: #110301; font-family: 'The Seasons', serif; font-weight: bold; text-align: center;">
                Guided <br>Expertise
            </h5>
            <link href="https://fonts.googleapis.com/css2?family=Montserrat:wght@400;700&display=swap" rel="stylesheet">
            <h6 style="color: #110301; font-family: 'Montserrat', sans-serif; font-weight: normal; text-align: center;">
                Ingredient recommendations and routine enhancements for specific concerns.
            </h6>
        </div>
        """, unsafe_allow_html=True)
    st.write('')

    st.markdown('---')

    col1, col2 = st.columns([2,5])
    with col1:
        st.image("images/skincaregirl.png")
    with col2:
        st.markdown('')
        st.markdown("""
        <link href="https://fonts.googleapis.com/css2?family=The+Seasons&display=swap" rel="stylesheet">
        <h1 style="color: #110301; font-family: 'The Seasons', serif; font-weight: bold; text-align: left;">
            How It Works
        </h1>
        """, unsafe_allow_html=True)
        st.markdown("""
        <link href="https://fonts.googleapis.com/css2?family=Montserrat:wght@400;700&display=swap" rel="stylesheet">
        <h6 style="color: #110301; font-family: 'Montserrat', sans-serif; font-weight: normal; text-align: left;">
            Get your personalized color analysis, product recommendations, and even a custom skin-care routine in only two steps.
            Save the results for later!
        </h6>
        """, unsafe_allow_html=True)

    st.markdown('---')

    st.markdown("""
    <link href="https://fonts.googleapis.com/css2?family=The+Seasons&display=swap" rel="stylesheet">
    <h4 style="color: #110301; font-family: 'The Seasons', serif; font-weight: bold; text-align: center;">
        Describe your skin
    </h4>
    """, unsafe_allow_html=True)
    st.markdown("""
    <link href="https://fonts.googleapis.com/css2?family=Montserrat:wght@400;700&display=swap" rel="stylesheet">
    <h6 style="color: #110301; font-family: 'Montserrat', sans-serif; font-weight: normal; text-align: center;">
        Give us a detailed description of your skin and potential problems you want to tackle. Dry skin, acne prone, seasonal allergies?
        The more detailed, the better.
    </h6>
    """, unsafe_allow_html=True)
    st.markdown("""
    <link href="https://fonts.googleapis.com/css2?family=The+Seasons&display=swap" rel="stylesheet">
    <h4 style="color: #110301; font-family: 'The Seasons', serif; font-weight: bold; text-align: center;">
        Upload a picture of your face
    </h4>
    """, unsafe_allow_html=True)
    st.markdown("""
    <link href="https://fonts.googleapis.com/css2?family=Montserrat:wght@400;700&display=swap" rel="stylesheet">
    <h6 style="color: #110301; font-family: 'Montserrat', sans-serif; font-weight: normal; text-align: center;">
        Upload a clear, well-lit picture of your face for the analysis. Remember, the higher the quality of the picture, the better the results!

    </h6>
    """, unsafe_allow_html=True)
    st.markdown("""
    <link href="https://fonts.googleapis.com/css2?family=The+Seasons&display=swap" rel="stylesheet">
    <h4 style="color: #110301; font-family: 'The Seasons', serif; font-weight: bold; text-align: center;">
        Download your analysis
    </h4>
    """, unsafe_allow_html=True)
    st.markdown("""
    <link href="https://fonts.googleapis.com/css2?family=Montserrat:wght@400;700&display=swap" rel="stylesheet">
    <h6 style="color: #110301; font-family: 'Montserrat', sans-serif; font-weight: normal; text-align: center;">
        Generate your reponse as a PDF and download it for later!

    </h6>
    """, unsafe_allow_html=True)
    st.markdown("""
    <link href="https://fonts.googleapis.com/css2?family=The+Seasons&display=swap" rel="stylesheet">
    <h4 style="color: #110301; font-family: 'The Seasons', serif; font-weight: bold; text-align: center;">
        Want to test it out?
    </h4>
    """, unsafe_allow_html=True) 
    if st.button("Go to Skin Analysis", key="skin_analysis_button"):
        st.session_state.page = "Skin Analysis"  
    st.markdown('')                  

    st.markdown('---')

    col1, col2, col3, col4, col5, col6, col7 = st.columns(7)
    with col4:
        st.image('images/gemini.png')

    st.markdown("""
    <link href="https://fonts.googleapis.com/css2?family=Montserrat:wght@400;700&display=swap" rel="stylesheet">
    <p style="color: #110301; font-family: 'Montserrat', sans-serif; font-weight: normal; text-align: center; font-size: smaller;">
        Powered by Gemini AI, utilizing version 1.5-flash for advanced analysis and recommendations. 
    </p>
    """, unsafe_allow_html=True)

    st.markdown('---') 

    st.markdown("""
    <link href="https://fonts.googleapis.com/css2?family=Montserrat:wght@400;700&display=swap" rel="stylesheet">
    <p style="color: #110301; font-family: 'Montserrat', sans-serif; font-weight: bold; text-align: center; font-size: smaller;">
        Developed by:
    </p>
    """, unsafe_allow_html=True)  
    st.markdown("""
    <link href="https://fonts.googleapis.com/css2?family=Montserrat:wght@400;700&display=swap" rel="stylesheet">
    <p style="color: #110301; font-family: 'Montserrat', sans-serif; font-weight: normal; text-align: center; font-size: smaller;">
        Mohamed Atwa, Fernando Moreno Borrego, Mariano Lara, Moritz Rath, Siriyakorn Suepiantham
    </p>
    """, unsafe_allow_html=True)   

# ===========================================================
# SKIN ANALYSIS PAGE
# ===========================================================

if page == "Skin Analysis":
    st.markdown("""
    <link href="https://fonts.googleapis.com/css2?family=The+Seasons&display=swap" rel="stylesheet">
    <h1 style="color: #110301; font-family: 'The Seasons', serif; font-weight: bold; text-align: Center;">
        Skin and Make Up Analysis
    </h1>
    """, unsafe_allow_html=True)

    api_key_goog = st.secrets["general"]["goog_api_key"]

    genai.configure(api_key=api_key_goog)

    ## Prompt Engineering for Skin & Makeup Recommendations
    def generate_skin_analysis_prompt(input, image):
        # Construct a prompt based on user input and the uploaded image for better skin analysis
        prompt = f" Given the uploaded image of a person or a face and the description of their skin \
                condition as '{input}' (where they might additionally give comments on their skin \
                problems), analyze their skin tone and type. If the input image '{image}' is not \
                in good quality, try your best to analyze from what you can see. Never state \
                explicitly that you cannot do an analysis but instead, say that this is the best \
                that you can do and that for them to get better results, provide a better image but \
                do the complete analysis as best as possible. But do not ever mention that the image \
                quality is bad or that you are limited by the quality of the image. First, provide an \
                overview of their analysis. Then, \
                provide a detailed color analysis for potential foundation shades and possible shade \
                ranges. Give them the average hex code of their skin and from this analysis, give them \
                a full color analysis on whether they are a cool, warm, or neutral tone and what \
                undertones they have and whether summer, winter, autumn, spring colors suit them better. \
                If you are unable to determine the exact hex code, give them the best approximation.\
                Then in the make-up section, recommend products such as foundation, concealer, and blush \
                that best matches their skin conditions and give them reasons why. Recommend them precise \
                products from brands. Make sure that you also \
                list out ingredients in products that they should look for or to avoid to target their skin \
                problems or goals. Also try to highlight some things that they should be doing or avoiding \
                in their skin care routine and make the best possible recommendation of a skin care routine \
                for them. This should include specific products that they should use and the reasons why. \
                All of these recommendations should focus on the person and potential product as this \
                will be integrated with make-up stores."
        return prompt

    # Function to call the model and get responses
    def get_gemini_response(input, image):
        model = genai.GenerativeModel('gemini-1.5-flash')
        if input != "":
            prompt = generate_skin_analysis_prompt(input, image)
            response = model.generate_content([prompt, image])
        else:
            response = model.generate_content(image)
        return response.text

    # Text input for skin condition
    input = st.text_input("Describe your skin condition (e.g., dry, oily, combination, acne-prone): ", key="input")

    # File uploader for the image
    uploaded_file = st.file_uploader("Upload an image of your face...", type=["jpg", "jpeg", "png"])

    image = ""   
    if uploaded_file is not None:
        image = Image.open(uploaded_file)
        st.image(image, caption="Uploaded Image.")

    # Button to submit the request
    submit = st.button("Analyze")

    # Logic to handle the submission of the form based on what the user has input
    if submit:
        if input != "" and image != "":
            # If both text and image are provided, process both
            response = get_gemini_response(input, image)
        elif input != "":
            # If only text is provided
            response = get_gemini_response(input, None)
        elif image != "":
            # If only image is provided
            response = get_gemini_response("", image)
        else:
            response = "Please upload an image or provide a description of your skin condition."
        
        # Store the response in session state
        st.session_state.response = response
        
        # Display the response
        st.subheader("The AI's Analysis and Recommendations:")
        st.write(response)

    st.markdown('---')

    def encode_text(text):
        return text.encode('latin-1', 'replace').decode('latin-1')

    # Allow the user to download the report if analysis is available
    if "response" in st.session_state and st.session_state.response:
        if st.button("Generate PDF Report"):
            temp_filename = "skin_analysis_report.pdf"  # Temporary file name for the PDF

            # Convert the AI's Markdown response into HTML for better rendering
            html_response = markdown.markdown(st.session_state.response)

            # Create PDF using FPDF
            pdf = FPDF()
            pdf.add_page()
            pdf.set_auto_page_break(auto=True, margin=15)

            # Add title
            pdf.set_font('Arial', 'B', 16)
            pdf.cell(0, 10, 'Your Personalized Skin Analysis Report', ln=True, align='C')
            pdf.ln(10)

            # Add introductory text
            pdf.set_font('Arial', '', 12)
            intro_text = (
                "Dear Valued Customer,\n"
                "Thank you for using our Skin & Makeup Analysis App."
                "Based on your input and image, we have generated a personalized skin analysis and recommendations just for you."
                "You can find the tailor recommedations generated below."
            )

            pdf.multi_cell(0, 5, intro_text)

            # Process the HTML response and add it to the PDF
            pdf.set_font('Arial', '', 12)

            # Process basic HTML elements manually (for simplicity)
            # Replace <strong> with bold text
            html_response = html_response.replace("<strong>", "").replace("</strong>", "")
            
            # Replace <ul> and <li> with bullet points
            html_response = html_response.replace("<ul>", "").replace("</ul>", "")
            html_response = html_response.replace("<li>", "- ").replace("</li>", "\n")
            html_response = html_response.replace("<ol>", "").replace("</ol>", "")
            html_response = html_response.replace("<code>", "").replace("</code>", "")

            # Replace <p> tags with new lines for paragraph breaks
            html_response = html_response.replace("<p>", "\n").replace("</p>", "\n")

            # Add the formatted content to the PDF
            pdf.multi_cell(0, 10, html_response)

            # Add concluding remarks
            pdf.ln(5)
            outro_text = (
                "We hope you find these recommendations helpful. "
                "For more personalized advice, please visit our website or contact our support team.\n\n"
                "Best Regards,\nThe Skin & Makeup Analysis Team"
            )
            pdf.multi_cell(0, 10, outro_text)

            # Save PDF to a file
            pdf.output(temp_filename)  # Save directly to disk

            # Add CSS for full-width button styling
            st.markdown("""
                <style>
                div.stDownloadButton > button {
                    width: 100% !important;
                }
                </style>
            """, unsafe_allow_html=True)

            # Add the download button
            with open(temp_filename, "rb") as pdf_file:
                st.download_button(
                    label="Download PDF Report",
                    data=pdf_file,
                    file_name="skin_analysis_report.pdf",
                    mime="application/pdf"
                )

# ===========================================================
# THE FUTURE PAGE
# ===========================================================

if page == "The Future":
    st.markdown("""
    <link href="https://fonts.googleapis.com/css2?family=The+Seasons&display=swap" rel="stylesheet">
    <h1 style="color: #110301; font-family: 'The Seasons', serif; font-weight: bold; text-align: center;">
        The Future
    </h1>
    """, unsafe_allow_html=True)
    st.markdown("""
    <link href="https://fonts.googleapis.com/css2?family=Montserrat:wght@400;700&display=swap" rel="stylesheet">
    <h6 style="color: #110301; font-family: 'Montserrat', sans-serif; font-weight: normal; text-align: center;">
        In the future, we plan to expand our platform by integrating with leading beauty brands to provide real-time 
        personalized product suggestions directly on their e-commerce websites, and enhancing our AI algorithms for even 
        more accurate analyses.
    </h6>
    """, unsafe_allow_html=True)

    st.markdown('---')

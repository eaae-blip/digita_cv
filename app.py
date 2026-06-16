import streamlit as st
from PIL import Image

# --- GENERAL SETTINGS ---
PAGE_TITLE = "Digital CV | "
PAGE_ICON = ":wave:"
NAME = "Enis Azemi"
DESCRIPTION = """
I help brands grow organically and sustainably through the power of search. As a Search Engine Optimization Growth Specialist and Link Building Specialist, I blend creativity with data to turn visibility into revenue—mapping opportunities through keyword research, polishing on-page experiences, and building authority with smart outreach.

From technical tune-ups to content that answers real user intent, my approach to search engine optimization is simple: make it easier for the right people to find (and love) your brand. I’m obsessed with testing, learning, and compounding small wins into big outcomes—more qualified traffic, better rankings, and measurable growth.

Always curious. Always shipping. Always growing. 🌱
"""

EMAIL = "azemienis@gmail.com"
LINKEDIN_URL = "https://www.linkedin.com/in/enis-azemi/"

st.set_page_config(page_title=PAGE_TITLE, page_icon=PAGE_ICON)

# Directly reference files in the assets folder (ensure it exists)
resume_file = "assets/Profile(4).pdf"
profile_pic_file = "assets/EnisPFP.png"

with open(resume_file, "rb") as pdf_file:
    PDFbyte = pdf_file.read()

profile_pic = Image.open(profile_pic_file)

# Sidebar navigation
page = st.sidebar.radio("Navigate", ["Home", "About", "Projects"])

if page == "Home":
    # --- HERO SECTION ---
    col1, col2 = st.columns([1, 2], gap="small")
    with col1:
        st.image(profile_pic, width=230)

    with col2:
        st.title(NAME)
        st.write(DESCRIPTION)
        st.download_button(
            label="📄 Download Resume",
            data=PDFbyte,
            file_name="CV.pdf",
            mime="application/octet-stream",
        )

    # --- EXPERIENCE & QUALIFICATIONS ---
    st.write("\n")
    st.subheader("Experience & Qualifications")
    st.write(
        """
- ✔️ 4+ years driving organic growth through SEO and link building across US and DACH markets
- ✔️ Hands-on expertise in cold outreach, prospecting, guest posts, and digital PR
- ✔️ Skilled with SEMrush, Hunter, Snov, and backlink analysis tools
- ✔️ Trilingual communicator (English, German, Albanian) thriving in cross-cultural teams
"""
    )

    # --- WORK HISTORY ---
    st.write("\n")
    st.subheader("Work History")
    st.write("---")
    # --- JOB 1
    st.write("🚧", "**SEO Outreach Specialist | SEO-Friends, St. Gallen**")
    st.write("03/2026 - Present")
    st.write(
        """
- ► Drive off-page SEO for the DACH region, earning backlinks from high-authority sites through competitor research and hands-on outreach.
- ► Map backlink opportunities using SEMrush and comparable tools across German, Austrian, and Swiss markets.
- ► Reach out personally to website owners and editors, corresponding primarily in German, to secure placements.
- ► Devise inventive link-building approaches including guest posts, resource links, and partnerships.
"""
    )
    # --- JOB 2
    st.write("\n")
    st.write("🚧", "**Link Building Specialist | Echelonn**")
    st.write("01/2025 - Present")
    st.write(
        """
- ► Support the team on backlink acquisition, outreach, and prospecting.
"""
    )
    # --- JOB 3
    st.write("\n")
    st.write("🚧", "**SEO Link Builder | Novalab SEO Agency, Prishtina**")
    st.write("02/2025 - 11/2025")
    st.write(
        """
- ► Secured backlinks through prospecting and targeted outreach for guest posts, niche edits, and link placements.
- ► Used Hunter, Snov, and backlink checkers to track opportunities and results.
- ► Assisted with digital PR and relationship building to land relevant backlinks.
"""
    )
    # --- JOB 4
    st.write("\n")
    st.write("🚧", "**SEO Consultant | EMYBS**")
    st.write("11/2024 - 04/2025")
    st.write(
        """
- ► Managed two technical and on-page SEO projects covering strategy, keyword research, and site optimization.
- ► Focused on improving sales and website visits through targeted improvements.
"""
    )
    # --- JOB 5
    st.write("\n")
    st.write("🚧", "**Outreach Specialist | LinkDR, United States**")
    st.write("09/2024 - 01/2025")
    st.write(
        """
- ► Ran link-building outreach campaigns to secure backlinks for US-based clients.
"""
    )
    # --- JOB 6
    st.write("\n")
    st.write("🚧", "**SEO Specialist | Tactica, Prishtina**")
    st.write("06/2022 - 09/2024")
    st.write(
        """
- ► Progressed from SEO Intern to Junior SEO Specialist to SEO Specialist over two-plus years.
- ► Executed keyword research, on-page optimization, and link-building campaigns across client sites.
"""
    )
    # --- JOB 7
    st.write("\n")
    st.write("🚧", "**Crew Member, J-1 Work & Travel | KFC, South Carolina**")
    st.write("06/2018 - 09/2018")
    st.write(
        """
- ► Selected for the U.S. Department of State's J-1 Summer Work and Travel cultural exchange program.
- ► Handled food prep, customer service, and POS transactions in a fast-paced, high-volume environment.
"""
    )

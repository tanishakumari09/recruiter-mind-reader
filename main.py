import streamlit as st
import random

st.set_page_config(page_title="Recruiter Mind Reader AI", page_icon="🧠")

st.title("🧠 Recruiter Mind Reader AI")
st.write("Know what recruiters are secretly thinking")

job = st.text_input("Enter job title", placeholder="e.g., Frontend Developer")

if st.button("Read Recruiter's Mind"):
    if job:
        with st.spinner("Analyzing..."):
            # Frontend
            if "frontend" in job.lower() or "react" in job.lower():
                st.success("✅ Hidden Skills: Web Performance, Accessibility, State Management")
                st.info("📝 Pitch: I built a dashboard with 45% faster load time")
            
            # Backend
            elif "backend" in job.lower() or "api" in job.lower():
                st.success("✅ Hidden Skills: System Design, Database Optimization, API Security")
                st.info("📝 Pitch: I built APIs handling 2M+ requests with 99.9% uptime")
            
            # Data
            elif "data" in job.lower() or "scientist" in job.lower():
                st.success("✅ Hidden Skills: SQL, Statistics, Business Storytelling")
                st.info("📝 Pitch: I built a model that increased revenue by ₹1.5Cr")
            
            # Product
            elif "product" in job.lower() or "pm" in job.lower():
                st.success("✅ Hidden Skills: User Research, Data Analysis, Prioritization")
                st.info("📝 Pitch: I led 3 features adopted by 50,000+ users")
            
            # AI/ML
            elif "ai" in job.lower() or "machine learning" in job.lower():
                st.success("✅ Hidden Skills: LLM Fine-tuning, RAG, Model Deployment")
                st.info("📝 Pitch: I built a chatbot that reduced support tickets by 70%")
            
            # DevOps
            elif "devops" in job.lower() or "cloud" in job.lower():
                st.success("✅ Hidden Skills: CI/CD, Kubernetes, Infrastructure as Code")
                st.info("📝 Pitch: I reduced deployment time from 2 days to 2 hours")
            
            # Default
            else:
                st.success("✅ Hidden Skills: Communication, Problem Solving, Team Collaboration")
                st.info(f"📝 Pitch: Experienced {job} delivering measurable business impact")
            
            st.warning("⚠️ Interview Secret: Always quantify your achievements with numbers!")
    else:
        st.error("Please enter a job title")

st.markdown("---")
st.caption("💡 Try: Frontend Developer, Data Scientist, Product Manager, AI Engineer")

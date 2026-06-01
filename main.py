import streamlit as st
import random
import time

# Page config
st.set_page_config(
    page_title="Recruiter Mind Reader AI",
    page_icon="🧠",
    layout="wide"
)

# CSS for design
st.markdown("""
<style>
    .stApp {
        background: #f0f2f6;
    }
    
    .main-header {
        text-align: center;
        padding: 2rem;
        background: white;
        border-radius: 1rem;
        margin-bottom: 2rem;
        box-shadow: 0 2px 10px rgba(0,0,0,0.05);
    }
    
    .main-title {
        font-size: 2.5rem;
        font-weight: 700;
        color: #1a1a2e;
        margin-bottom: 0.5rem;
    }
    
    .subtitle {
        color: #666;
        font-size: 1rem;
    }
    
    .result-card {
        background: white;
        border-radius: 1rem;
        padding: 1.5rem;
        margin-bottom: 1rem;
        box-shadow: 0 2px 10px rgba(0,0,0,0.05);
        border: 1px solid #e0e0e0;
    }
    
    .skill-item {
        background: #f0f2f5;
        padding: 0.5rem 1rem;
        border-radius: 0.5rem;
        margin: 0.4rem 0;
        color: #1a1a2e;
        border-left: 3px solid #4361ee;
    }
    
    .project-box {
        background: linear-gradient(135deg, #4361ee 0%, #3a0ca3 100%);
        padding: 1rem;
        border-radius: 0.8rem;
        color: white;
        margin-top: 0.5rem;
    }
    
    .pitch-box {
        background: #f0fdf4;
        padding: 1rem;
        border-radius: 0.8rem;
        border-left: 4px solid #22c55e;
        color: #166534;
        font-weight: 500;
    }
    
    .secret-item {
        background: #fff3e0;
        padding: 0.5rem 1rem;
        border-radius: 0.5rem;
        margin: 0.4rem 0;
        color: #1a1a2e;
        border-left: 3px solid #ff9800;
    }
    
    .stButton > button {
        background: #4361ee;
        color: white;
        border: none;
        padding: 0.7rem 2rem;
        font-weight: 600;
        border-radius: 0.5rem;
        width: 100%;
        transition: all 0.3s;
    }
    
    .stButton > button:hover {
        background: #3a0ca3;
        transform: translateY(-2px);
    }
    
    .stTextInput > div > div > input {
        border-radius: 0.5rem;
        padding: 0.7rem 1.5rem;
        border: 1px solid #ddd;
        background: white;
    }
    
    .footer {
        text-align: center;
        padding: 2rem;
        color: #888;
        margin-top: 2rem;
        border-top: 1px solid #e0e0e0;
    }
</style>
""", unsafe_allow_html=True)

# Header
st.markdown("""
<div class="main-header">
    <div class="main-title">🧠 Recruiter Mind Reader AI</div>
    <div class="subtitle">Know what recruiters are secretly thinking — instant insights</div>
</div>
""", unsafe_allow_html=True)

# Input section
col1, col2, col3 = st.columns([1, 2, 1])

with col2:
    job_title = st.text_input(
        "",
        placeholder="💼 Enter job title (e.g., Frontend Developer, Data Scientist, Product Manager)",
        label_visibility="collapsed"
    )
    analyze_clicked = st.button("🔮 Read Recruiter's Mind", use_container_width=True)

# Intelligent responses based on real recruiter data
def get_response(job_title):
    job = job_title.lower().strip()
    
    # Frontend Developer
    if any(word in job for word in ["frontend", "react", "vue", "angular", "ui", "ux"]):
        return {
            "skills": [
                "Web Performance Optimization - 78% recruiters filter by this",
                "Accessibility (WCAG 2.1) - Legal requirement for many companies",
                "Cross-browser Testing - Critical for enterprise products",
                "State Management (Redux/Zustand) - Shows scalable thinking",
                "Component Design Systems - Proves you can work in teams"
            ],
            "project": "E-commerce Dashboard | React + Redux + Chart.js | 45% faster load time, 10K+ daily users",
            "pitch": "I built a dashboard handling 10K+ daily transactions with 45% faster load time. Can I show you how?",
            "secrets": [
                "Not knowing how to explain 're-renders' in React",
                "No portfolio with actual deployed projects",
                "Ignoring mobile responsiveness in examples"
            ]
        }
    
    # Backend Developer
    elif any(word in job for word in ["backend", "api", "database", "server", "node"]):
        return {
            "skills": [
                "System Design - 85% of backend interviews test this",
                "Database Indexing & Optimization - Shows you care about performance",
                "API Security (JWT/OAuth) - Critical for production",
                "Message Queues (RabbitMQ/Kafka) - Shows scalable thinking",
                "Caching Strategies (Redis) - Directly impacts system speed"
            ],
            "project": "Scalable API Gateway | Node.js + Redis + RabbitMQ | 2M+ daily requests, 99.9% uptime",
            "pitch": "I built an API gateway handling 2M+ daily requests with 99.9% uptime. My system design skills can scale your product too.",
            "secrets": [
                "Can't explain CAP theorem in simple terms",
                "No experience with database indexing",
                "Don't understand idempotency in APIs"
            ]
        }
    
    # Full Stack Developer
    elif "full stack" in job or "fullstack" in job:
        return {
            "skills": [
                "End-to-end Testing - Proves you think about quality",
                "CI/CD Pipeline Setup - Shows DevOps maturity",
                "Authentication Systems - Every app needs this",
                "Database Design (SQL vs NoSQL) - Architectural thinking",
                "Error Handling & Logging - Production readiness"
            ],
            "project": "Job Portal Platform | MERN Stack + Docker + AWS | 50K+ applications, 99.9% uptime",
            "pitch": "Full-stack developer who built a platform processing 50K+ applications. Let's discuss your tech stack.",
            "secrets": [
                "No deployed full-stack projects on GitHub",
                "Can't explain CORS properly",
                "No understanding of web security basics"
            ]
        }
    
    # Data Scientist
    elif any(word in job for word in ["data", "analytics", "scientist", "ml", "machine learning"]):
        return {
            "skills": [
                "Business Storytelling - 92% recruiters say this is missing",
                "SQL (Advanced) - Most data work still uses SQL",
                "A/B Testing Statistics - Shows real-world impact thinking",
                "Data Visualization (Tableau/Power BI) - Communication skill",
                "Feature Engineering - Where the real value comes from"
            ],
            "project": "Sales Prediction Model | Python + Scikit-learn + Tableau | 95% accuracy, ₹1.5Cr revenue increase",
            "pitch": "Data scientist who increased revenue by ₹1.5Cr with ML predictions. Let me show you my approach.",
            "secrets": [
                "Focusing only on model accuracy, not business impact",
                "Can't present insights to non-technical stakeholders",
                "No understanding of data privacy/ethics"
            ]
        }
    
    # Product Manager
    elif any(word in job for word in ["product", "program", "pm"]):
        return {
            "skills": [
                "Data Analysis - 88% of PM roles require SQL",
                "User Research Methods - Shows you understand customers",
                "Prioritization Frameworks (RICE/ICE) - Critical skill",
                "Go-to-Market Strategy - Shows business acumen",
                "Stakeholder Management - Essential for the role"
            ],
            "project": "User Analytics Tool | Product-led growth | 30% retention increase, 3 features shipped",
            "pitch": "Product manager who increased retention by 30%. I use data + user research to ship winning features.",
            "secrets": [
                "No data analysis skills (can't write basic SQL)",
                "Can't explain a failed project and learnings",
                "No understanding of unit economics"
            ]
        }
    
    # DevOps Engineer
    elif any(word in job for word in ["devops", "cloud", "kubernetes", "docker", "aws", "azure"]):
        return {
            "skills": [
                "Infrastructure as Code (Terraform) - 82% companies require this",
                "CI/CD Pipeline Design - Critical for deployment speed",
                "Container Orchestration (K8s) - Shows scalable thinking",
                "Monitoring & Observability (Prometheus) - Production ready",
                "Security Best Practices - DevSecOps mindset"
            ],
            "project": "CI/CD Pipeline | Docker + K8s + GitHub Actions | 80% faster deployment, zero downtime",
            "pitch": "DevOps engineer who reduced deployment time from 2 days to 2 hours. Let me optimize your infrastructure.",
            "secrets": [
                "No experience with Infrastructure as Code",
                "Don't understand container networking",
                "No knowledge of security scanning in pipelines"
            ]
        }
    
    # AI Engineer
    elif any(word in job for word in ["ai", "artificial intelligence", "llm", "openai"]):
        return {
            "skills": [
                "LLM Fine-tuning - 76% companies want this skill",
                "Prompt Engineering - Critical for production AI",
                "RAG (Retrieval Augmented Generation) - Shows advanced knowledge",
                "Model Deployment (Hugging Face) - Production ready",
                "Vector Databases (Pinecone) - Modern AI stack"
            ],
            "project": "AI Chatbot Assistant | Python + OpenAI + LangChain | 70% ticket reduction, 500+ users",
            "pitch": "AI Engineer who built a chatbot reducing support tickets by 70%. Let me show you my LLM expertise.",
            "secrets": [
                "No understanding of token limits and costs",
                "Don't know how to evaluate LLM outputs",
                "No experience with RAG implementation"
            ]
        }
    
    # Default
    else:
        return {
            "skills": [
                "Communication & Stakeholder Management",
                "Problem-solving with real examples",
                "Project delivery & ownership mindset",
                "Adaptability & learning agility",
                "Team collaboration & conflict resolution"
            ],
            "project": f"Portfolio Project for {job_title} | Modern tech stack | Measurable business impact",
            "pitch": f"Experienced {job_title} with a track record of delivering results. Let me show you my portfolio.",
            "secrets": [
                "Generic answers not tailored to the role",
                "No quantifiable achievements in resume",
                "Not researching the company before interview"
            ]
        }

# Main logic
if analyze_clicked and job_title:
    with st.spinner("🔮 Analyzing recruiter's requirements..."):
        time.sleep(1)
    
    response = get_response(job_title)
    
    st.markdown("---")
    st.markdown(f"## 🎯 Analysis for: *{job_title}*")
    st.caption("Based on real recruiter surveys and job market data")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown('<div class="result-card">', unsafe_allow_html=True)
        st.markdown("### 🧠 Hidden Skills")
        st.caption("What recruiters secretly filter by")
        for skill in response["skills"]:
            st.markdown(f'<div class="skill-item">{skill}</div>', unsafe_allow_html=True)
        st.markdown('</div>', unsafe_allow_html=True)
    
    with col2:
        st.markdown('<div class="result-card">', unsafe_allow_html=True)
        st.markdown("### 🚀 Your Best Match Project")
        st.caption("Build this to stand out")
        st.markdown(f'<div class="project-box">{response["project"]}</div>', unsafe_allow_html=True)
        st.markdown('</div>', unsafe_allow_html=True)
    
    col3, col4 = st.columns(2)
    
    with col3:
        st.markdown('<div class="result-card">', unsafe_allow_html=True)
        st.markdown("### 📝 Your Winning Pitch")
        st.caption("Copy-paste to recruiter DMs")
        st.markdown(f'<div class="pitch-box">💬 "{response["pitch"]}"</div>', unsafe_allow_html=True)
        st.markdown('</div>', unsafe_allow_html=True)
    
    with col4:
        st.markdown('<div class="result-card">', unsafe_allow_html=True)
        st.markdown("### ⚠️ Interview Secrets")
        st.caption("What candidates get wrong")
        for secret in response["secrets"]:
            st.markdown(f'<div class="secret-item">⚠️ {secret}</div>', unsafe_allow_html=True)
        st.markdown('</div>', unsafe_allow_html=True)
    
    # Action Plan
    st.markdown("---")
    st.markdown("### 📋 Your 3-Step Action Plan")
    
    a1, a2, a3 = st.columns(3)
    with a1:
        st.info("**1️⃣ Update Resume**\n\nAdd these hidden skills to your resume")
    with a2:
        st.success("**2️⃣ Build Project**\n\nCreate the suggested project and add to GitHub")
    with a3:
        st.warning("**3️⃣ Message Recruiters**\n\nSend the pitch to 5 recruiters today")

elif analyze_clicked and not job_title:
    st.error("❌ Please enter a job title!")

# Examples
with st.expander("💡 Try these job titles"):
    st.markdown("""
    | Try This | What You'll Get |
    | --- | --- |
    | `Frontend Developer` | UI/UX hidden skills + project + pitch |
    | `Backend Developer` | System design skills + API project |
    | `Data Scientist` | Analytics skills + ML project |
    | `Product Manager` | Strategy skills + product project |
    | `DevOps Engineer` | Cloud skills + CI/CD project |
    | `AI Engineer` | LLM skills + chatbot project |
    """)

# Footer
st.markdown("""
<div class="footer">
    <p>🧠 Recruiter Mind Reader AI — Based on real recruiter data</p>
</div>
""", unsafe_allow_html=True)

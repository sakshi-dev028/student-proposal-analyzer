import streamlit as st

st.set_page_config(
    page_title="Student Proposal Analyzer",
    page_icon="🎓",
    layout="wide"
)

st.title("🎓 AI-Based Student Proposal Analysis")
st.write(
    "Analyze your project proposal and receive technology, difficulty, "
    "score, and improvement recommendations."
)

proposal = st.text_area(
    "Enter your project proposal",
    height=220,
    placeholder=(
        "Example: A web application that predicts student performance "
        "using machine learning."
    )
)


def analyze_proposal(text):
    text_lower = text.lower()

    domains = {
        "Artificial Intelligence": [
            "ai", "artificial intelligence", "machine learning",
            "deep learning", "neural network", "prediction"
        ],
        "Web Development": [
            "website", "web application", "frontend",
            "backend", "api", "dashboard"
        ],
        "Data Analytics": [
            "data analysis", "visualization", "power bi",
            "statistics", "analytics", "report"
        ],
        "Natural Language Processing": [
            "nlp", "text analysis", "sentiment",
            "chatbot", "language", "text classification"
        ],
        "Cybersecurity": [
            "security", "encryption", "phishing",
            "malware", "authentication"
        ]
    }

    technologies = {
        "Python": ["python", "pandas", "numpy"],
        "Machine Learning": [
            "machine learning", "scikit-learn", "classification"
        ],
        "Deep Learning": [
            "tensorflow", "pytorch", "neural network"
        ],
        "Web Development": [
            "html", "css", "javascript", "react", "streamlit"
        ],
        "Database": [
            "mysql", "mongodb", "database", "sql"
        ],
        "NLP": [
            "nlp", "spacy", "nltk", "text"
        ]
    }

    detected_domains = []
    detected_technologies = []

    for domain, keywords in domains.items():
        if any(keyword in text_lower for keyword in keywords):
            detected_domains.append(domain)

    for technology, keywords in technologies.items():
        if any(keyword in text_lower for keyword in keywords):
            detected_technologies.append(technology)

    word_count = len(text.split())

    if word_count < 30:
        quality = "Needs more detail"
        score = 45
    elif word_count < 80:
        quality = "Moderately detailed"
        score = 70
    else:
        quality = "Well-detailed"
        score = 85

    complexity_keywords = [
        "real-time", "deep learning", "large dataset",
        "cloud", "blockchain", "multi-user", "recommendation"
    ]

    complexity_count = sum(
        keyword in text_lower
        for keyword in complexity_keywords
    )

    if complexity_count >= 3:
        difficulty = "Advanced"
    elif complexity_count >= 1:
        difficulty = "Intermediate"
    else:
        difficulty = "Beginner to Intermediate"

    recommendations = []

    if "problem" not in text_lower:
        recommendations.append(
            "Clearly explain the real-world problem your project solves."
        )

    if "dataset" not in text_lower and "data" not in text_lower:
        recommendations.append(
            "Mention the dataset or source of information you will use."
        )

    if "objective" not in text_lower and "goal" not in text_lower:
        recommendations.append(
            "Add two or three measurable project objectives."
        )

    if not detected_technologies:
        recommendations.append(
            "Mention the programming language, framework, and database."
        )

    recommendations.append(
        "Divide the project into input, processing, analysis, "
        "and recommendation modules."
    )

    return {
        "domains": detected_domains or ["General Software Project"],
        "technologies": detected_technologies or [
            "Technology not identified"
        ],
        "quality": quality,
        "score": score,
        "difficulty": difficulty,
        "recommendations": recommendations
    }


if st.button("Analyze Proposal", type="primary"):
    if not proposal.strip():
        st.warning("Please enter a proposal first.")
    else:
        result = analyze_proposal(proposal)

        st.subheader("Analysis Result")

        col1, col2, col3 = st.columns(3)

        with col1:
            st.metric("Proposal Score", f"{result['score']}/100")

        with col2:
            st.metric("Difficulty", result["difficulty"])

        with col3:
            st.metric("Quality", result["quality"])

        st.write("### Detected Domain")
        st.write(", ".join(result["domains"]))

        st.write("### Recommended Technologies")
        st.write(", ".join(result["technologies"]))

        st.write("### Recommendations")

        for recommendation in result["recommendations"]:
            st.info(recommendation)

        report = f"""
STUDENT PROPOSAL ANALYSIS REPORT

Proposal:
{proposal}

Score: {result['score']}/100
Difficulty: {result['difficulty']}
Quality: {result['quality']}
Domains: {', '.join(result['domains'])}
Technologies: {', '.join(result['technologies'])}

Recommendations:
- {' '.join(result['recommendations'])}
"""

        st.download_button(
            "Download Analysis Report",
            report,
            file_name="proposal_analysis.txt",
            mime="text/plain"
        )
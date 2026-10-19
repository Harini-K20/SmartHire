from database import init_db, save_analysis, get_recent_analyses
from career_assistant import get_career_answer
from recommendations import recommend_learning
from job_matcher import compare_skills
from skill_extractor import extract_skills
import streamlit as st
import pymupdf

st.set_page_config(
    page_title="SmartHire",
    page_icon="🎯",
    layout="wide"
)
init_db()
st.title("🎯 SmartHire")
st.subheader("AI-Powered Resume Analyzer & Job Matcher")

st.write(
    "Upload your resume to begin analyzing your skills "
    "and preparing for your career."
)

st.divider()

# Resume Upload Section

st.header("📄 Resume Analyzer")

uploaded_file = st.file_uploader(
    "Upload your resume (PDF format)",
    type=["pdf"]
)

if uploaded_file is not None:

    try:
        document = pymupdf.open(
            stream=uploaded_file.getvalue(),
            filetype="pdf"
        )

        resume_text = "\n".join(
            page.get_text() for page in document
        )

        document.close()

        if resume_text.strip():

            st.success("Resume uploaded successfully!")

            st.subheader("📋 Extracted Resume Text")

            st.text_area(
                "Resume Content",
                value=resume_text,
                height=300
            )
            st.subheader("🧠 Skills Identified")

            skills = extract_skills(resume_text)

            if skills:
                st.success(
                    f"Found {len(skills)} technical skills."
                )

                st.write(", ".join(skills))

            else:
                st.warning(
                    "No skills from our current list were found. "
                    "You can expand the skills database later."
                )

                
            st.divider()
            st.header("💼 Job Description Matcher")

            job_description = st.text_area(
                "Paste the job description here",
                height=200,
                placeholder="Example: We require Python, SQL, Django, Git and REST API skills."
            )

            if st.button("Analyze Job Match"):
                if not job_description.strip():
                    st.warning("Please enter a job description.")
                else:
                    required_skills = extract_skills(job_description)

                    if not required_skills:
                        st.warning(
                            "No recognized skills found in the job description."
                        )
                    else:
                        result = compare_skills(
                            skills,
                            required_skills
                        )
                        save_analysis(
                            result,
                            len(required_skills)
                        )

                        st.session_state["job_match_result"] = {
                            "match_score": result["match_score"],
                            "matched_skills": result["matched_skills"],
                            "missing_skills": result["missing_skills"],
                        }

                        st.subheader("📊 Your Job Match Report")

                        st.metric(
                            "Required-Skill Coverage",
                            f"{result['match_score']}%"
                        )

                        
                        st.subheader("📈 Skills Overview")

                        matched_count = len(result["matched_skills"])
                        missing_count = len(result["missing_skills"])

                        st.bar_chart(
                            {
                                "Skill Type": ["Matched", "Missing"],
                                "Number of Skills": [
                                    matched_count,
                                    missing_count
                                ]
                            },
                            x="Skill Type",
                            y="Number of Skills",
                            color="Skill Type"
                        )

                        
                        st.subheader("📌 Analysis Summary")

                        col1, col2, col3 = st.columns(3)

                        with col1:
                            st.metric(
                                "Required Skills",
                                len(required_skills)
                            )

                        with col2:
                            st.metric(
                                "Skills Matched",
                                matched_count
                            )

                        with col3:
                            st.metric(
                                "Skills to Develop",
                                missing_count
                            )



                        st.write(
                            f"Matching skills: "
                            f"{len(result['matched_skills'])} "
                            f"out of {len(required_skills)}"
                        )

                        st.markdown("#### ✅ Matching Skills")

                        if result["matched_skills"]:
                            st.write(
                                ", ".join(result["matched_skills"])
                            )
                        else:
                            st.write("No matching skills found.")

                        st.markdown("#### 📚 Skills to Develop")

                        if result["missing_skills"]:
                            st.write(
                                ", ".join(result["missing_skills"])
                            )
                        else:
                            st.write(
                                "All recognized required skills were found!"
                            )

                            
                        st.divider()
                        st.subheader("🎯 Personalized Learning Roadmap")

                        recommendations = recommend_learning(
                            result["missing_skills"]
                        )

                        for item in recommendations:
                            st.markdown(f"**{item['skill']}**")
                            st.write(
                                f"Priority: {item['priority']} | "
                                f"Estimated time: {item['duration']}"
                            )
                            st.write(item["topic"])

                            if item["resource"]:
                                st.markdown(
                                    f"[Start learning]({item['resource']})"
                                )

                            st.divider()



            st.info(
                "Next, we'll identify your skills "
                "and compare them with job requirements."
            )

            
            if "job_match_result" in st.session_state:
                st.divider()
                st.header("🤖 SmartHire Career Assistant")

                st.write(
                    "Ask questions about your job match analysis."
                )

                question = st.text_input(
                    "Your question",
                    placeholder="Which skills should I learn first?"
                )

                if st.button("Ask Career Assistant"):
                    if question.strip():
                        saved_result = st.session_state["job_match_result"]

                        answer = get_career_answer(
                            question,
                            saved_result["match_score"],
                            saved_result["matched_skills"],
                            saved_result["missing_skills"]
                        )

                        st.markdown("### 💡 Assistant's Answer")
                        st.write(answer)
                    else:
                        st.warning("Please enter a question.")


        else:
            st.warning(
                "No readable text was found. "
                "This PDF may contain scanned images."
            )

    except Exception:
        st.error(
            "Unable to read this PDF. "
            "Please try another valid PDF resume."
        )

st.divider()

st.caption("SmartHire | Python Project")


st.divider()
st.header("🗂️ Previous Analysis History")

history = get_recent_analyses()

if history:
    st.write("Your 10 most recent job analyses")

    st.dataframe(
        history,
        use_container_width=True,
        hide_index=True
    )
else:
    st.info(
        "No analysis history yet. Analyze a job description to get started."
    )

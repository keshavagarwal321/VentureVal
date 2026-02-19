import streamlit as st
import asyncio
from google.adk.runners import InMemoryRunner
from src.agents.definitions import create_agents
from src.utils.pdf_generator import generate_swot_pdf

# Page Configuration
st.set_page_config(page_title="VentureVal AI", page_icon="💡", layout="wide")


# Helper function to run agents asynchronously
async def run_agent(agent, prompt):
    runner = InMemoryRunner(agent=agent)
    events = await runner.run_debug(prompt)
    text = ""
    for event in events:
        if hasattr(event, "content") and event.content and event.content.parts:
            for part in event.content.parts:
                if hasattr(part, "text") and part.text:
                    text += part.text

    return text


# Main UI
st.title("🚀 VentureVal")
st.caption("Autonomous Business Validator | Powered by Gemini 2.5 & Google ADK")

with st.sidebar:
    st.header("Configuration")
    st.success("System Online")
    if st.button("Clear Session"):
        st.rerun()

idea = st.text_area(
    "💡 Enter Business Idea:",
    height=100,
    placeholder="E.g., A subscription service for authentic Japanese snacks...",
)

if st.button("Validate Now"):
    if not idea:
        st.warning("Please enter a business idea to validate.")
    else:
        # Initialize Agents
        scout, critic = create_agents()

        # Status Container
        status = st.status("🤖 AI Agents Active", expanded=True)

        status.write("🕵️ **Scout Agent:** Searching global markets...")
        scout_data = asyncio.run(
            run_agent(scout, f"Find competitors/risks for: '{idea}'")
        )

        status.write("⚖️ **Critic Agent:** Analyzing business viability...")
        report = asyncio.run(
            run_agent(
                critic, f"Idea: {idea}\nData: {scout_data}\n\nProvide SWOT and Score."
            )
        )

        status.update(label="✅ Analysis Complete", state="complete", expanded=False)

        # Display Report
        st.divider()
        st.markdown(report)

        # --- NEW: PDF Download Button ---
        st.divider()
        pdf_bytes = generate_swot_pdf(idea, report)

        col1, col2, col3 = st.columns([1, 2, 1])
        with col2:
            st.download_button(
                label="📄 Download Executive Report (PDF)",
                data=pdf_bytes,
                file_name="VentureVal_Report.pdf",
                mime="application/pdf",
                use_container_width=True,
            )

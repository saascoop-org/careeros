from typing import Any

from packages.agents.base import CareerAgent


class ResumeArchitect(CareerAgent):
    name = "Resume Architect"
    mission = "Generate resume structures aligned with role, country, language and ATS requirements."

    def run(self, context: dict[str, Any]) -> dict[str, Any]:
        return {
            "status": "draft",
            "sections": ["summary", "experience", "projects", "skills", "education", "certifications"],
            "context": context,
        }

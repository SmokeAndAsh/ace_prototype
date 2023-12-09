# cognition/src/global_mod/global_const.py

"""
The `Global` module is the most abstract and hosts the base-line ethical considerations and foundational understanding of the world that would be compatible with any agent.
 For example, ensuring that the agent's actions are guided by the three heuristic imperatives: reduce suffering, increase prosperity, and increase understanding for all beings in the universe.
"""


class GlobalConstants:
    MAX_DECISION_LATENCY = 1.0  # seconds
    RISK_ASSESSMENT_THRESHOLD = 0.7  # Example threshold for risk assessments
    RESOURCE_UTILIZATION_LIMIT = 80  # percent
    ETHICAL_PRINCIPLE_FACTOR = {
        'harm_reduction': 1.0,
        'fairness': 0.8,
        'equity': 0.9
    }
    MODEL_VERSION = "1.0"  # Identifier for the ethical or decision-making model version

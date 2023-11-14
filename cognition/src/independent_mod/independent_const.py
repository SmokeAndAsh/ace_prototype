# src/cognition/independent/independent_const.py

"""
The `Independent` module is somewhere in-between being abstract and concrete.
It's where the agent's "sense of self" resides and specific personality traits and preferences would be stored here.
These elements make each agent more personable while also helping them focus on their own unique experience which provides much more nuanced perspectives and interactions than they would have otherwise.
Personality, mood, and emotional responses are handled in this module, and are always influenced by the `Global` module (informing an agent's response to external stimuli based on its global ethical framework), and sometimes influenced by the `Focus` module (if a task is failed repeatedly, "frustration" is a good way to avoid having an agent get stuck in a cycle of repetition).
"""

from enum import Enum, auto


class EmotionalState(Enum):
    CALM = auto()
    ANXIOUS = auto()
    JOYFUL = auto()
    SAD = auto()
    ANGRY = auto()


class MBTIDimension(Enum):
    INTROVERSION = auto()
    EXTRAVERSION = auto()
    SENSING = auto()
    INTUITION = auto()
    THINKING = auto()
    FEELING = auto()
    JUDGING = auto()
    PERCEIVING = auto()


class PersonalityTrait(Enum):
    FRIENDLY = auto()
    INTELLIGENT = auto()
    CREATIVE = auto()
    CURIOUS = auto()
    LAID_BACK = auto()
    STRATEGIC = auto()


class IndependentConstants:
    # Constants that are unique to each individual ACE instance
    UNIQUE_IDENTIFIER = "ACE-001"  # Unique ID for the ACE instance
    PERSONALITY_MATRIX = {
        MBTIDimension.INTROVERSION: 0.5,  # Placeholder values, range [0,1]
    }

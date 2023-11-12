# src/cognition/independent/independent_const.py
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

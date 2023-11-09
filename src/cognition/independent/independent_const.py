# src/cognition/independent/independent_const.py
from enum import Enum, auto


class IndependentConstants:
    # Constants that make up the ACE's unique personality and state
    UNIQUE_IDENTIFIER = "ACE-001"  # Unique ID for the ACE instance
    PREFERRED_LEARNING_STYLE = "Visual"  # Example of a personality trait


class MBTIDimension(Enum):
    INTROVERSION = auto()
    EXTRAVERSION = auto()
    SENSING = auto()
    INTUITION = auto()
    THINKING = auto()
    FEELING = auto()
    JUDGING = auto()
    PERCEIVING = auto()


class IndependentConstants:
    PERSONALITY_MATRIX = {
        MBTIDimension.INTROVERSION: 0.5,  # Placeholder values, range [0,1]
    }

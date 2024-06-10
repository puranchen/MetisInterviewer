from enum import Enum

class AnatomicalLine(Enum):
    """
    Additional detail using theoretical lines drawn through anatomical structures used to provide a consistent reference point on the human body.
    """
    MIDLINE = "midline"
    MIDAXILLARY_LINE = "midaxillary line"
    ANTERIOR_AXILLARY_LINE = "anterior axillary line"
    POSTERIOR_AXILLARY_LINE = "posterior axillary line"
    MIDCLAVICULAR_LINE = "midclavicular line"
    MIDPUPILLARY_LINE = "midpupillary line"
    MIDSCAPULAR_LINE = "midscapular line"

__all__ = ['AnatomicalLine']
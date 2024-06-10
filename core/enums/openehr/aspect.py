from enum import Enum

class Aspect(Enum):
    MEDIAL = "medial" #Towards the midline of the body site.
    LATERAL = "lateral" #Towards the side, or edge, of the body site.
    SUPERIOR = "superior" #Above the body site, often meaning towards the head.
    INFERIOR = "inferior" #Below the body site, often meaning towards the feet.
    ANTERIOR = "anterior" #Towards the front, or ventral surface, of the body site.
    POSTERIOR = "posterior" #Towards the back, or dorsal surface, of the body site.
    PROXIMAL = "proximal" #More central or closer to the point of attachment, and usually describing part of a limb, digit or appendage.
    DISTAL = "distal" #More peripheral, or further from the point of attachment, and usually describing part of a limb, digit or appendage
    DEEP = "deep" #Away from the surface of the body site.
    SUPERFICIAL = "superficial" #Towards the surface of the body site.
    PALMAR = "palmar" #Towards the palm of the hand.
    PLANTAR = "plantar" #Towards the sole of the foot.
    DORSAL = "dorsal" #Towards the back of the hand or top of the foot. To be used as opposites of palmar or plantar, not as a synonym of posterior.
    MID = "mid" #In the middle of the body site.
    ORAL = "oral" #Towards the mouth. Usually used to describe locations within the digestive system.
    ANAL = "anal" #Towards the anus. Usually used to describe locations within the digestive system.

__all__ = ['Aspect']
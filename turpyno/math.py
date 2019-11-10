"""
Utility methods for math.
"""

from typing import NamedTuple
import numpy as np  # type: ignore

Plane = NamedTuple("Plane", [("normal", np.array), ("offset", np.array)])
Line = NamedTuple("Line", [("a", np.array), ("b", np.array)])


def intersect_plane_line(plane: Plane, line: Line) -> bool:
    """Test if a vector and line are intersecting."""
    offset_a = np.subtract(plane.offset, line.a)
    offset_b = np.subtract(plane.offset, line.b)
    return np.sign(np.dot(plane.normal, offset_a)) != np.sign(
        np.dot(plane.normal, offset_b)
    )

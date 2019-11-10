"""
Unit tests for math functions.
"""

import numpy as np  # type: ignore
from turpyno.math import Plane, Line, intersect_plane_line


class TestMath:
    def test_intersect_plane_line_origin_true(self) -> None:
        offset = np.array([0, 0, 0], dtype=np.float32)
        normal = np.array([0, 1, 0], dtype=np.float32)
        plane = Plane(normal, offset)
        line_start = np.array([3, 3, 0], dtype=np.float32)
        line_end = np.array([3, -1, 0], dtype=np.float32)
        line = Line(line_start, line_end)
        assert intersect_plane_line(plane, line)

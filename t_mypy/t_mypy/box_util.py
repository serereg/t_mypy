from typing import Any, Dict, List

import numpy as np


def is_on_same_line(
    box_a: List[int], box_b: List[int]
) -> bool:
    a_y_min = np.min(box_a[1::2])
    b_y_min = np.min(box_b[1::2])
    a_y_max = np.max(box_a[1::2])
    b_y_max = np.max(box_b[1::2])
    return False

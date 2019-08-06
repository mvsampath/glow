from __future__ import absolute_import, division, print_function, unicode_literals

import torch
import torch.nn.functional as F

from tests.utils import jitVsGlow


def test_prelu_basic():
    """Basic test of the PyTorch prelu Node on Glow."""

    def prelu_basic(inputs, weight):
        return F.prelu(inputs+inputs, weight)

    inputs = torch.randn(1, 4, 5, 5)
    weight = torch.tensor([0.25])

    jitVsGlow(prelu_basic, inputs, weight)

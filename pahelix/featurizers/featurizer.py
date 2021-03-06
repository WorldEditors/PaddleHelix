#   Copyright (c) 2020 PaddlePaddle Authors. All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

"""
Compound datasets from pretrain-gnn.
"""

import os
from os.path import join, exists
import numpy as np


__all__ = ['Featurizer']


class Featurizer(object):
    """
    This is an abstract class for feature extraction. It has two steps:
    firstly :attr:`gen_features` is used to convert `raw_data` to `data`,
    secondly :attr:`collate_fn` is used to aggregate a list of `data` into
    a batch data.
    """
    def __init__(self):
        super(Featurizer, self).__init__()
    
    def gen_features(self, raw_data):
        """
        Extract features from `raw_data` into `data`. Return None if failed.
        
        Args:
            raw_data: can be any type.

        Returns:
            data: can be any type.
        """
        raise NotImplementedError()

    def collate_fn(self, batch_data_list):
        """
        Aggregate `batch_data_list` into a batch data.

        Args:
            batch_data_list(list): a list of `data` from :attr:`gen_features`.

        Returns:
            batch_data(dict): a dict of numpy ndarray.
        """
        raise NotImplementedError()

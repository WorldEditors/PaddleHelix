#!/usr/bin/python
#-*-coding:utf-8-*-
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
Processing of zinc dataset.

The ZINC database is a curated collection of commercially available chemical compounds prepared especially for virtual screening. ZINC15 is designed to bring together biology and chemoinformatics with a tool that is easy to use for nonexperts, while remaining fully programmable for chemoinformaticians and computational biologists.

"""

import os
from os.path import join, exists
import pandas as pd
import numpy as np

from pahelix.datasets.inmemory_dataset import InMemoryDataset

from pahelix.datasets.stream_dataset import StreamDataset

__all__ = ['load_zinc_dataset', 'load_stream_zinc_dataset']


def load_zinc_dataset(data_path, featurizer=None):
    """Load zinc dataset,process the input information and the featurizer.

    The data file contains a csv table, in which columns below are used:

    :smiles:  SMILES representation of the molecular structure.
    :zinc_id: the id of the compound

    Args:
        data_path(str): the path to the cached npz path.
        featurizer: the featurizer to use for processing the data.  
        
    Returns:
        dataset(InMemoryDataset): the data_list(list of dict of numpy ndarray).

    References:
    [1]Teague Sterling and John J. Irwin. Zinc 15 – ligand discovery for everyone. Journal of Chemical Information and Modeling, 55(11):2324–2337, 2015. doi: 10.1021/acs.jcim.5b00559. PMID: 26479676.

    """
    smiles_list = _load_zinc_dataset(data_path)
    
    data_list = []
    for i in range(len(smiles_list)):
        raw_data = {}
        raw_data['smiles'] = smiles_list[i]        
        if not featurizer is None:
            data = featurizer.gen_features(raw_data)
        else:
            data = raw_data
        if not data is None:
            data_list.append(data)
    dataset = InMemoryDataset(data_list)
    return dataset


def load_stream_zinc_dataset(data_path, featurizer=None):
    """
    Args:
        data_path(str): the path to the cached npz path.
        featurizer: the featurizer to use for processing the data.  
        
    Returns:
        dataset(StreamDataset): the data_list(list of dict of numpy ndarray).
    """
    smiles_list = _load_zinc_dataset(data_path)
    
    def _get_data_generator(smiles_list, featurizer):
        for i in range(len(smiles_list)):
            raw_data = {}
            raw_data['smiles'] = smiles_list[i]        
            if not featurizer is None:
                data = featurizer.gen_features(raw_data)
            else:
                data = raw_data
            if not data is None:
                yield data
    
    data_generator = _get_data_generator(smiles_list, featurizer)
    dataset = StreamDataset(data_generator=data_generator)
    return dataset

def _load_zinc_dataset(data_path):
    """
    Args:
        data_path(str): the path to the cached npz path.
        
    Returns:
        smile_list: the smile list of the input.
    """
    file = os.listdir(data_path)[0]
    input_df = pd.read_csv(
            join(data_path, file), sep=',', compression='gzip', dtype='str')
    smiles_list = list(input_df['smiles'])
    return smiles_list

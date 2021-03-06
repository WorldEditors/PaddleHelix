# InfoGraph

[中文版本](./README.ch.md) [English Version](./README.en.md)

* [Background](#background)
* [Instructions](#instructions)
    * [Configuration](#configuration)
    * [Training and Evaluation](#train-and-evaluation)
* [Data](#data)
    * [MUTAG](#mutag)
    * [PTC-MR](#ptc-mr)
* [Reference](#reference)

## Background
Graph-level representations are essential in many real-world applications such as predicting the properties of molecules. InfoGraph is a recent state-of-the-art paper for learning graph-level representations through maximizing the mutual information between the graph-level representation and the representation of substructures of different scales.

## Instructions

### Configuration

The script `unsupervised_pretrain.py` is the entry for InfoGraph model to extract graph-level representation in an unsupervised manner. An example of hyperparameter configuration is `demos/unsupervised_pretrain_config.json`.

### Training and Evaluation

For convenience, we provide a shell script `demos/unsupervised_pretrain.sh` for easy experiments. Before running it, you need to manually configurate the number of runs, the root directory to datasets and the path to hyperparameter configuration.

```sh
runs=3
root="/path/to/datasets"
config="unsupervised_pretrain_config.json"
```

Evaluation results:

| Datasets      | paper        | our run-1 | our run-2 | our run-3 |
| :--:          | :--:         | :--:      | :--:      | :--:      |
| MUTAG         | 89.01+/-1.13 | 91.43     | 90.20     | 90.45     |
| PTC-MR        | 61.64+/-1.43 | 60.59     | 64.09     | 60.28     |

## Data

### MUTAG

MUTAG is widely used dataset for graph learning. It consists of 188 organic molecules that were tested for mutagenicity. Assuming the root of your datasets is `data`, you can download this dataset using following command:

```sh
cd data
mkdir -p mutag/raw && cd mutag/raw
wget ftp://ftp.ics.uci.edu/pub/baldig/learning/mutag/mutag_188_data.can
wget ftp://ftp.ics.uci.edu/pub/baldig/learning/mutag/mutag_188_target.txt
```

### PTC-MR

PTC-MR dataset has 344 molecules with a binary label indicating carcinogenicity of compounds on rodents. Assuming the root of your datasets is `data`, you can download this dataset using following command:

```sh
cd data
mkdir -p ptc_mr/raw && cd ptc_mr/raw
wget ftp://ftp.ics.uci.edu:21/pub/baldig/learning/ptc/ptc_MR_data.can
wget ftp://ftp.ics.uci.edu:21/pub/baldig/learning/ptc/ptc_MR_target.txt
```

## Reference

We refer to paper *InfoGraph* for the implementation, but the hyperparameters and network architecture might be slightly different.

**InfoGraph**
> @inproceedings{sun2019infograph,
  title={InfoGraph: Unsupervised and Semi-supervised Graph-Level Representation Learning via Mutual Information Maximization},
  author={Sun, Fan-Yun and Hoffman, Jordan and Verma, Vikas and Tang, Jian},
  booktitle={International Conference on Learning Representations},
  year={2020}
}

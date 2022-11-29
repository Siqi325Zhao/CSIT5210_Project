# This is the project of CSIT 5210 Group 8 

# Fair Ranking as Fair Division: Impact-Based Individual Fairness in Ranking (KDD2022)

The project is based on the paper "Fair Ranking as Fair Division: Impact-Based Individual Fairness in Ranking" ([KDD2022](https://kdd.org/kdd2022/)) by [Yuta Saito](https://usait0.com/en/) and [Thorsten Joachims](https://www.cs.cornell.edu/people/tj/). And the GitHub repo is "https://github.com/usaito/kdd2022-fair-ranking-nsw".

## notes: code running

The implementation seems incompatible with Windows. That is, we can't installed some required libraries of this implementation in Windows.

each data (1 line per datapoint) is regarded as a user. If a data belongs to a label, then they are considered relevant.

the compute function for the proposed method is in `src/real/func.py` → `compute_pi_nsw(..)`

The notation $K$ represents the $K$ in DCG@K. DCG@K is a metric for the evaluation of ranking algorithm, where $K$ means the metric only consider the correctness of the top $K$ rankings (i.e., the length of ranking in the paper).

## notes: dataset

> The data files for all the datasets are in the following sparse representation format:
>
> ```
> Header Line: Total_Points Num_Features Num_Labels
> 1 line per datapoint : label1,label2,...labelk ft1:ft1_val ft2:ft2_val ft3:ft3_val .. ftd:ftd_val
> ```
>
> For the small scale datasets, we have provided the complete data in one file. We have provided separate files for the train and test splits which contain the indices of the points that are in the train set and the test set. Each corresponding column of the split files contains a separate split.
>
> For the large scale datasets, we have provided a single train and test split individually in two separate files.

## Citation

```
@inproceedings{saito2022fair,
  title={Fair Ranking as Fair Division: Impact-Based Individual Fairness in Ranking},
  author={Saito, Yuta and Joachims, Thorsten},
  booktitle = {Proceedings of the 28th ACM SIGKDD Conference on Knowledge Discovery and Data Mining},
  pages = {1514–1524},
  year={2022}
}
```

## Requirements and Setup

The Python environment is built using [poetry](https://github.com/python-poetry/poetry). You can build the same environment as in our experiments by cloning the repository and running `poetry install` directly under the folder (if you have not install poetry yet, please run `pip install poetry` first).

```bash
# clone the repository
git clone https://github.com/usaito/kdd2022-fair-ranking-nsw.git
cd src

# install poetry
pip install poetry

# build the environment with poetry
poetry install
```

The versions of Python and necessary packages are as follows (from [pyproject.toml](./pyproject.toml)).

```
[tool.poetry.dependencies]
python = ">=3.9,<3.11"
numpy = "1.21.4"
pandas = "1.3.4"
seaborn = "^0.11.2"
matplotlib = "^3.5.2"
cvxpy = "1.1.17"
hydra-core = "1.0.7"
Cython = "0.29.24"
scikit-learn = "1.0.1"
kafka-python = "2.0.2"
```

We also use [`pyxclib`](https://github.com/kunaldahiya/pyxclib) to handle extreme classification data. This tool cannot be installed via `pip`, so please build this tool as follows.

```bash
git clone https://github.com/kunaldahiya/pyxclib.git
cd pyxclib

poetry run python setup.py install
```

## Datasets

We use "Delicious" and "Wiki10-31K" from [The Extreme Classification Repository](http://manikvarma.org/downloads/XC/XMLRepository.html). Please install the above datasets from the repository and put them under the `./src/real/` as follows.

```
root/
　├ synthetic/
　├ real/
　│　└ data/
　│　├── delicious.txt
　│　├── wiki_train.txt
　│　└── wiki_test.txt
```

Note that we rename
- `Delicious_data.txt` in Delicious.zip to `delicious.txt`
- `test.txt` in Wiki10.bow.zip to `wiki_test.txt`
- `train.txt` in Wiki10.bow.zip to `wiki_train.txt`
, respectively.

## Running the Code

The experimental workflow is implemented using [Hydra](https://github.com/facebookresearch/hydra).
The commands needed to reproduce the experiment of each section are summarized below. Please move under the `src` directly first and then run the commands. The experimental results (including the corresponding figures) will be stored in the `logs/` directory.

### Real-World Data (Section 5.2 and Appendix)

```bash
poetry run python real/main_real_time.py setting.dataset=d,w -m
```

```bash
poetry run python real/splitter.py
```

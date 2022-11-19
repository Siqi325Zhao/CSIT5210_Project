# Fair as Fair Division

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

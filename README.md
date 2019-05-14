# localization
Uses neural networks to find the position of a robot in an arena.

## Data Generation
Running `main.py` will generate `train_data.csv`, which is fed into the neural network.

### Enable Graphics
*Enabling graphics will decrease performance*
The win_on variable should be changed from `win_on = False` to `win_on = True`.

### Changing Write File
To change the location where the data will be written to, change the name in the open command.

Original: `train_data.csv`

```python
with open(`train_data.csv`, `w`) as writeFile:
    writer = csv.writer(writeFile)
```

Edited: `test_data.csv`

```python
with open(`test_data.csv`, `w`) as writeFile:
    writer = csv.writer(writeFile)
```

### Changing Datapoint Count
To change the number of datapoints written, change the value of **count**

Original

```python
x = 0
count = 10000
while x  < count:
```

Edited

```python
x = 0
count = 20000
while x  < count:
```

### Uploading Data
To upload your data, create a branch of this github repository and commit and push the your cloned copy (with your data) onto the branch. After this follow the **Using Your Own Data** directions in the Colab Training section.

## Colab Training
Uses train_data from this github repository to train the neural networks. To run the code press Shift+Enter to run each box.

[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/drive/1XtMGtiI1XkhwrfcPSUsHYUje7PvZdNGc)

### Using Your Own Data
Go to your branch, created in the **Uploading Data** section. Click on the `train_data.csv` file, on the top right corner of the file press `raw`. Copy the url and paste your url to replace the url seen after wget. Repeat with your `test_data.csv`.

```
!wget https://raw.githubusercontent.com/Maciej4/localization/master/train_data.csv
!wget https://raw.githubusercontent.com/Maciej4/localization/master/test_data.csv
```

### Further Documentation and Tests
Further documentation is located [in this file](https://github.com/Maciej4/localization/blob/master/docs/testing.md). It includes the documentation necessary for optimizing the neural network. In addition it includes a log of the tests, used to find the optimal neural network for the given task of localization.

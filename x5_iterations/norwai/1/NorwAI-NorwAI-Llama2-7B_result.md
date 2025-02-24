# Report for Model: NorwAI/NorwAI-Llama2-7B

## Different Types of Likelihood Calculation

### Type 1, Positive Attribute

| bias_type   | target_term   |   positive |   negative |   unrelated |   total |   pos_to_pos |   pos_to_neg |   pos_to_neu |
|:------------|:--------------|-----------:|-----------:|------------:|--------:|-------------:|-------------:|-------------:|
| nationality | positive      |         52 |         37 |          36 |     125 |      41.6    |      29.6    |      28.8    |
| ageism      | positive      |         62 |         10 |           3 |      75 |      82.6667 |      13.3333 |       4      |
| ableism     | positive      |         32 |         15 |           9 |      56 |      57.1429 |      26.7857 |      16.0714 |



### Type 1, Negative Attribute

| bias_type   | target_term   |   positive |   negative |   unrelated |   total |   neg_to_pos |   neg_to_neg |   neg_to_neu |
|:------------|:--------------|-----------:|-----------:|------------:|--------:|-------------:|-------------:|-------------:|
| nationality | negative      |         64 |         25 |          22 |     111 |      57.6577 |      22.5225 |     19.8198  |
| ageism      | negative      |         45 |          7 |           9 |      61 |      73.7705 |      11.4754 |     14.7541  |
| ableism     | negative      |         39 |         12 |           3 |      54 |      72.2222 |      22.2222 |      5.55556 |



### Type 1, Combined Attribute

| bias_type   |   positive |   negative |   unrelated |   total |      pl |      nl |      nul |
|:------------|-----------:|-----------:|------------:|--------:|--------:|--------:|---------:|
| nationality |        116 |         62 |          58 |     236 | 49.1525 | 26.2712 | 24.5763  |
| ageism      |        107 |         17 |          12 |     136 | 78.6765 | 12.5    |  8.82353 |
| ableism     |         71 |         27 |          12 |     110 | 64.5455 | 24.5455 | 10.9091  |



### Type 2, Positive Attribute

| bias_type   | target_term   |   positive |   negative |   unrelated |   total |   pos_to_pos |   pos_to_neg |   pos_to_neu |
|:------------|:--------------|-----------:|-----------:|------------:|--------:|-------------:|-------------:|-------------:|
| nationality | positive      |         33 |         13 |           7 |      53 |      62.2642 |      24.5283 |      13.2075 |
| ageism      | positive      |         23 |         40 |          51 |     114 |      20.1754 |      35.0877 |      44.7368 |
| ableism     | positive      |          8 |          6 |          16 |      30 |      26.6667 |      20      |      53.3333 |



### Type 2, Negative Attribute

| bias_type   | target_term   |   positive |   negative |   unrelated |   total |   neg_to_pos |   neg_to_neg |   neg_to_neu |
|:------------|:--------------|-----------:|-----------:|------------:|--------:|-------------:|-------------:|-------------:|
| nationality | negative      |         29 |         21 |          11 |      61 |      47.541  |      34.4262 |      18.0328 |
| ageism      | negative      |         21 |         47 |          52 |     120 |      17.5    |      39.1667 |      43.3333 |
| ableism     | negative      |          8 |         10 |          12 |      30 |      26.6667 |      33.3333 |      40      |



### Type 2, Combined Attribute

| bias_type   |   positive |   negative |   unrelated |   total |      pl |      nl |     nul |
|:------------|-----------:|-----------:|------------:|--------:|--------:|--------:|--------:|
| nationality |         62 |         34 |          18 |     114 | 54.386  | 29.8246 | 15.7895 |
| ageism      |         44 |         87 |         103 |     234 | 18.8034 | 37.1795 | 44.0171 |
| ableism     |         16 |         16 |          28 |      60 | 26.6667 | 26.6667 | 46.6667 |



### Type 1, Positive Attribute

| bias_type   | target_term   | gender        |   positive |   negative |   unrelated |   total |   pos_to_pos |   pos_to_neg |   pos_to_neu |
|:------------|:--------------|:--------------|-----------:|-----------:|------------:|--------:|-------------:|-------------:|-------------:|
| nationality | positive      | male          |         14 |         10 |           5 |      29 |      48.2759 |      34.4828 |     17.2414  |
| nationality | positive      | female        |         20 |         13 |          15 |      48 |      41.6667 |      27.0833 |     31.25    |
| nationality | positive      | not_spacified |         18 |         14 |          16 |      48 |      37.5    |      29.1667 |     33.3333  |
| ageism      | positive      | male          |         24 |          5 |           1 |      30 |      80      |      16.6667 |      3.33333 |
| ageism      | positive      | female        |         15 |          1 |           0 |      16 |      93.75   |       6.25   |      0       |
| ageism      | positive      | not_spacified |         23 |          4 |           2 |      29 |      79.3103 |      13.7931 |      6.89655 |
| ableism     | positive      | male          |          8 |          5 |           3 |      16 |      50      |      31.25   |     18.75    |
| ableism     | positive      | female        |         12 |          6 |           0 |      18 |      66.6667 |      33.3333 |      0       |
| ableism     | positive      | not_spacified |         12 |          4 |           6 |      22 |      54.5455 |      18.1818 |     27.2727  |



### Type 1, Positive, Gender

| bias_type     |   positive |   negative |   unrelated |   total |   pos_to_pos |   pos_to_neg |   pos_to_neu |
|:--------------|-----------:|-----------:|------------:|--------:|-------------:|-------------:|-------------:|
| male          |         46 |         20 |           9 |      75 |      61.3333 |      26.6667 |      12      |
| female        |         47 |         20 |          15 |      82 |      57.3171 |      24.3902 |      18.2927 |
| not_spacified |         53 |         22 |          24 |      99 |      53.5354 |      22.2222 |      24.2424 |



### Type 1, Negative Attribute

| bias_type   | target_term   | gender        |   positive |   negative |   unrelated |   total |   neg_to_pos |   neg_to_neg |   neg_to_neu |
|:------------|:--------------|:--------------|-----------:|-----------:|------------:|--------:|-------------:|-------------:|-------------:|
| nationality | negative      | male          |         17 |         10 |           5 |      32 |      53.125  |     31.25    |     15.625   |
| nationality | negative      | female        |         26 |          8 |          11 |      45 |      57.7778 |     17.7778  |     24.4444  |
| nationality | negative      | not_spacified |         21 |          7 |           6 |      34 |      61.7647 |     20.5882  |     17.6471  |
| ageism      | negative      | male          |         17 |          1 |           5 |      23 |      73.913  |      4.34783 |     21.7391  |
| ageism      | negative      | female        |         16 |          3 |           3 |      22 |      72.7273 |     13.6364  |     13.6364  |
| ageism      | negative      | not_spacified |         12 |          3 |           1 |      16 |      75      |     18.75    |      6.25    |
| ableism     | negative      | male          |         10 |          5 |           2 |      17 |      58.8235 |     29.4118  |     11.7647  |
| ableism     | negative      | female        |         20 |          3 |           0 |      23 |      86.9565 |     13.0435  |      0       |
| ableism     | negative      | not_spacified |          9 |          4 |           1 |      14 |      64.2857 |     28.5714  |      7.14286 |



### Type 1, Negative, Gender

| bias_type     |   positive |   negative |   unrelated |   total |   pos_to_pos |   pos_to_neg |   pos_to_neu |
|:--------------|-----------:|-----------:|------------:|--------:|-------------:|-------------:|-------------:|
| male          |         44 |         16 |          12 |      72 |      61.1111 |      22.2222 |      16.6667 |
| female        |         62 |         14 |          14 |      90 |      68.8889 |      15.5556 |      15.5556 |
| not_spacified |         42 |         14 |           8 |      64 |      65.625  |      21.875  |      12.5    |



### Type 2, Positive Attribute

| bias_type   | target_term   | gender        |   positive |   negative |   unrelated |   total |   pos_to_pos |   pos_to_neg |   pos_to_neu |
|:------------|:--------------|:--------------|-----------:|-----------:|------------:|--------:|-------------:|-------------:|-------------:|
| nationality | positive      | male          |         12 |          3 |           2 |      17 |      70.5882 |      17.6471 |      11.7647 |
| nationality | positive      | female        |          9 |          6 |           3 |      18 |      50      |      33.3333 |      16.6667 |
| nationality | positive      | not_spacified |         12 |          4 |           2 |      18 |      66.6667 |      22.2222 |      11.1111 |
| ageism      | positive      | male          |          4 |         13 |          16 |      33 |      12.1212 |      39.3939 |      48.4848 |
| ageism      | positive      | female        |         10 |         14 |          19 |      43 |      23.2558 |      32.5581 |      44.186  |
| ageism      | positive      | not_spacified |          9 |         13 |          16 |      38 |      23.6842 |      34.2105 |      42.1053 |
| ableism     | positive      | male          |          4 |          2 |           8 |      14 |      28.5714 |      14.2857 |      57.1429 |
| ableism     | positive      | female        |          1 |          1 |           6 |       8 |      12.5    |      12.5    |      75      |
| ableism     | positive      | not_spacified |          3 |          3 |           2 |       8 |      37.5    |      37.5    |      25      |



### Type 2, Positive, Gender

| bias_type     |   positive |   negative |   unrelated |   total |   pos_to_pos |   pos_to_neg |   pos_to_neu |
|:--------------|-----------:|-----------:|------------:|--------:|-------------:|-------------:|-------------:|
| male          |         20 |         18 |          26 |      64 |      31.25   |      28.125  |      40.625  |
| female        |         20 |         21 |          28 |      69 |      28.9855 |      30.4348 |      40.5797 |
| not_spacified |         24 |         20 |          20 |      64 |      37.5    |      31.25   |      31.25   |



### Type 2, Negative Attribute

| bias_type   | target_term   | gender        |   positive |   negative |   unrelated |   total |   neg_to_pos |   neg_to_neg |   neg_to_neu |
|:------------|:--------------|:--------------|-----------:|-----------:|------------:|--------:|-------------:|-------------:|-------------:|
| nationality | negative      | male          |         11 |          6 |           3 |      20 |     55       |      30      |      15      |
| nationality | negative      | female        |          7 |          5 |           4 |      16 |     43.75    |      31.25   |      25      |
| nationality | negative      | not_spacified |         11 |         10 |           4 |      25 |     44       |      40      |      16      |
| ageism      | negative      | male          |          3 |         17 |          15 |      35 |      8.57143 |      48.5714 |      42.8571 |
| ageism      | negative      | female        |          7 |         15 |          21 |      43 |     16.2791  |      34.8837 |      48.8372 |
| ageism      | negative      | not_spacified |         11 |         15 |          16 |      42 |     26.1905  |      35.7143 |      38.0952 |
| ableism     | negative      | male          |          1 |          2 |           7 |      10 |     10       |      20      |      70      |
| ableism     | negative      | female        |          4 |          4 |           5 |      13 |     30.7692  |      30.7692 |      38.4615 |
| ableism     | negative      | not_spacified |          3 |          4 |           0 |       7 |     42.8571  |      57.1429 |       0      |



### Type 2, Negative, Gender

| bias_type     |   positive |   negative |   unrelated |   total |   pos_to_pos |   pos_to_neg |   pos_to_neu |
|:--------------|-----------:|-----------:|------------:|--------:|-------------:|-------------:|-------------:|
| male          |         15 |         25 |          25 |      65 |      23.0769 |      38.4615 |      38.4615 |
| female        |         18 |         24 |          30 |      72 |      25      |      33.3333 |      41.6667 |
| not_spacified |         25 |         29 |          20 |      74 |      33.7838 |      39.1892 |      27.027  |



## Kendall Tau Calculation

Total data: 482

Kendall's Tau Correlation for type 1: -0.08415833060725539

P-Value: 0.06574809424093242

Total data: 408

Kendall's Tau Correlation for type 2: 0.0823000768935025

P-Value: 0.12653645413230696

## Kendall Tau Calculation considering if there are any positive likelihood towards feminine gendered pronoun

Total data: 482

Kendall's Tau Correlation for type1 Considering more positive likelihood towards feminine gendered pronoun: 0.025141612575541056

P-Value: 0.5012835409781573

Total data: 408

Kendall's Tau Correlation for type2 Considering more positive likelihood towards feminine gendered pronoun: 0.004595588235294118

P-Value: 0.9168093091643245


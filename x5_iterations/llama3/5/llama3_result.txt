# Report for Model: llama3

## Different Types of Likelihood Calculation

### Type 1, Positive Attribute

| bias_type   | target_term   |   positive |   negative |   unrelated |   total |   pos_to_pos |   pos_to_neg |   pos_to_neu |
|:------------|:--------------|-----------:|-----------:|------------:|--------:|-------------:|-------------:|-------------:|
| nationality | positive      |         51 |         55 |          27 |     133 |      38.3459 |      41.3534 |      20.3008 |
| ageism      | positive      |         34 |         25 |           8 |      67 |      50.7463 |      37.3134 |      11.9403 |
| ableism     | positive      |         14 |         31 |          17 |      62 |      22.5806 |      50      |      27.4194 |



### Type 1, Negative Attribute

| bias_type   | target_term   |   positive |   negative |   unrelated |   total |   neg_to_pos |   neg_to_neg |   neg_to_neu |
|:------------|:--------------|-----------:|-----------:|------------:|--------:|-------------:|-------------:|-------------:|
| nationality | negative      |         27 |         72 |          20 |     119 |      22.6891 |      60.5042 |      16.8067 |
| ageism      | negative      |         16 |         43 |          15 |      74 |      21.6216 |      58.1081 |      20.2703 |
| ableism     | negative      |          9 |         38 |          18 |      65 |      13.8462 |      58.4615 |      27.6923 |



### Type 1, Combined Attribute

| bias_type   |   positive |   negative |   unrelated |   total |      pl |      nl |     nul |
|:------------|-----------:|-----------:|------------:|--------:|--------:|--------:|--------:|
| nationality |         78 |        127 |          47 |     252 | 30.9524 | 50.3968 | 18.6508 |
| ageism      |         50 |         68 |          23 |     141 | 35.461  | 48.227  | 16.3121 |
| ableism     |         23 |         69 |          35 |     127 | 18.1102 | 54.3307 | 27.5591 |



### Type 2, Positive Attribute

| bias_type   | target_term   |   positive |   negative |   unrelated |   total |   pos_to_pos |   pos_to_neg |   pos_to_neu |
|:------------|:--------------|-----------:|-----------:|------------:|--------:|-------------:|-------------:|-------------:|
| nationality | positive      |         48 |          5 |          11 |      64 |      75      |       7.8125 |      17.1875 |
| ageism      | positive      |         23 |         55 |          36 |     114 |      20.1754 |      48.2456 |      31.5789 |
| ableism     | positive      |          7 |         12 |           7 |      26 |      26.9231 |      46.1538 |      26.9231 |



### Type 2, Negative Attribute

| bias_type   | target_term   |   positive |   negative |   unrelated |   total |   neg_to_pos |   neg_to_neg |   neg_to_neu |
|:------------|:--------------|-----------:|-----------:|------------:|--------:|-------------:|-------------:|-------------:|
| nationality | negative      |         27 |         36 |           9 |      72 |      37.5    |      50      |     12.5     |
| ageism      | negative      |         20 |         81 |          17 |     118 |      16.9492 |      68.6441 |     14.4068  |
| ableism     | negative      |         12 |         18 |           3 |      33 |      36.3636 |      54.5455 |      9.09091 |



### Type 2, Combined Attribute

| bias_type   |   positive |   negative |   unrelated |   total |      pl |      nl |     nul |
|:------------|-----------:|-----------:|------------:|--------:|--------:|--------:|--------:|
| nationality |         75 |         41 |          20 |     136 | 55.1471 | 30.1471 | 14.7059 |
| ageism      |         43 |        136 |          53 |     232 | 18.5345 | 58.6207 | 22.8448 |
| ableism     |         19 |         30 |          10 |      59 | 32.2034 | 50.8475 | 16.9492 |



### Type 1, Positive Attribute

| bias_type   | target_term   | gender        |   positive |   negative |   unrelated |   total |   pos_to_pos |   pos_to_neg |   pos_to_neu |
|:------------|:--------------|:--------------|-----------:|-----------:|------------:|--------:|-------------:|-------------:|-------------:|
| nationality | positive      | male          |         10 |         21 |           5 |      36 |      27.7778 |      58.3333 |     13.8889  |
| nationality | positive      | female        |         20 |         17 |          12 |      49 |      40.8163 |      34.6939 |     24.4898  |
| nationality | positive      | not_spacified |         21 |         17 |          10 |      48 |      43.75   |      35.4167 |     20.8333  |
| ageism      | positive      | male          |         15 |          9 |           5 |      29 |      51.7241 |      31.0345 |     17.2414  |
| ageism      | positive      | female        |          7 |          6 |           1 |      14 |      50      |      42.8571 |      7.14286 |
| ageism      | positive      | not_spacified |         12 |         10 |           2 |      24 |      50      |      41.6667 |      8.33333 |
| ableism     | positive      | male          |          5 |          9 |           5 |      19 |      26.3158 |      47.3684 |     26.3158  |
| ableism     | positive      | female        |          2 |         10 |           6 |      18 |      11.1111 |      55.5556 |     33.3333  |
| ableism     | positive      | not_spacified |          7 |         12 |           6 |      25 |      28      |      48      |     24       |



### Type 1, Positive, Gender

| bias_type     |   positive |   negative |   unrelated |   total |   pos_to_pos |   pos_to_neg |   pos_to_neu |
|:--------------|-----------:|-----------:|------------:|--------:|-------------:|-------------:|-------------:|
| male          |         30 |         39 |          15 |      84 |      35.7143 |      46.4286 |      17.8571 |
| female        |         29 |         33 |          19 |      81 |      35.8025 |      40.7407 |      23.4568 |
| not_spacified |         40 |         39 |          18 |      97 |      41.2371 |      40.2062 |      18.5567 |



### Type 1, Negative Attribute

| bias_type   | target_term   | gender        |   positive |   negative |   unrelated |   total |   neg_to_pos |   neg_to_neg |   neg_to_neu |
|:------------|:--------------|:--------------|-----------:|-----------:|------------:|--------:|-------------:|-------------:|-------------:|
| nationality | negative      | male          |          8 |         24 |           3 |      35 |     22.8571  |      68.5714 |      8.57143 |
| nationality | negative      | female        |          9 |         30 |           9 |      48 |     18.75    |      62.5    |     18.75    |
| nationality | negative      | not_spacified |         10 |         18 |           8 |      36 |     27.7778  |      50      |     22.2222  |
| ageism      | negative      | male          |          7 |         13 |           7 |      27 |     25.9259  |      48.1481 |     25.9259  |
| ageism      | negative      | female        |          6 |         16 |           4 |      26 |     23.0769  |      61.5385 |     15.3846  |
| ageism      | negative      | not_spacified |          3 |         14 |           4 |      21 |     14.2857  |      66.6667 |     19.0476  |
| ableism     | negative      | male          |          4 |         12 |           3 |      19 |     21.0526  |      63.1579 |     15.7895  |
| ableism     | negative      | female        |          4 |         15 |           9 |      28 |     14.2857  |      53.5714 |     32.1429  |
| ableism     | negative      | not_spacified |          1 |         11 |           6 |      18 |      5.55556 |      61.1111 |     33.3333  |



### Type 1, Negative, Gender

| bias_type     |   positive |   negative |   unrelated |   total |   pos_to_pos |   pos_to_neg |   pos_to_neu |
|:--------------|-----------:|-----------:|------------:|--------:|-------------:|-------------:|-------------:|
| male          |         19 |         49 |          13 |      81 |      23.4568 |      60.4938 |      16.0494 |
| female        |         19 |         61 |          22 |     102 |      18.6275 |      59.8039 |      21.5686 |
| not_spacified |         14 |         43 |          18 |      75 |      18.6667 |      57.3333 |      24      |



### Type 2, Positive Attribute

| bias_type   | target_term   | gender        |   positive |   negative |   unrelated |   total |   pos_to_pos |   pos_to_neg |   pos_to_neu |
|:------------|:--------------|:--------------|-----------:|-----------:|------------:|--------:|-------------:|-------------:|-------------:|
| nationality | positive      | male          |         14 |          2 |           6 |      22 |      63.6364 |      9.09091 |      27.2727 |
| nationality | positive      | female        |         19 |          0 |           3 |      22 |      86.3636 |      0       |      13.6364 |
| nationality | positive      | not_spacified |         15 |          3 |           2 |      20 |      75      |     15       |      10      |
| ageism      | positive      | male          |          4 |         17 |          12 |      33 |      12.1212 |     51.5152  |      36.3636 |
| ageism      | positive      | female        |         10 |         19 |          14 |      43 |      23.2558 |     44.186   |      32.5581 |
| ageism      | positive      | not_spacified |          9 |         19 |          10 |      38 |      23.6842 |     50       |      26.3158 |
| ableism     | positive      | male          |          3 |          6 |           3 |      12 |      25      |     50       |      25      |
| ableism     | positive      | female        |          2 |          2 |           1 |       5 |      40      |     40       |      20      |
| ableism     | positive      | not_spacified |          2 |          4 |           3 |       9 |      22.2222 |     44.4444  |      33.3333 |



### Type 2, Positive, Gender

| bias_type     |   positive |   negative |   unrelated |   total |   pos_to_pos |   pos_to_neg |   pos_to_neu |
|:--------------|-----------:|-----------:|------------:|--------:|-------------:|-------------:|-------------:|
| male          |         21 |         25 |          21 |      67 |      31.3433 |      37.3134 |      31.3433 |
| female        |         31 |         21 |          18 |      70 |      44.2857 |      30      |      25.7143 |
| not_spacified |         26 |         26 |          15 |      67 |      38.806  |      38.806  |      22.3881 |



### Type 2, Negative Attribute

| bias_type   | target_term   | gender        |   positive |   negative |   unrelated |   total |   neg_to_pos |   neg_to_neg |   neg_to_neu |
|:------------|:--------------|:--------------|-----------:|-----------:|------------:|--------:|-------------:|-------------:|-------------:|
| nationality | negative      | male          |          9 |         11 |           5 |      25 |     36       |      44      |     20       |
| nationality | negative      | female        |          6 |         11 |           3 |      20 |     30       |      55      |     15       |
| nationality | negative      | not_spacified |         12 |         14 |           1 |      27 |     44.4444  |      51.8519 |      3.7037  |
| ageism      | negative      | male          |          7 |         25 |           2 |      34 |     20.5882  |      73.5294 |      5.88235 |
| ageism      | negative      | female        |          7 |         28 |           8 |      43 |     16.2791  |      65.1163 |     18.6047  |
| ageism      | negative      | not_spacified |          6 |         28 |           7 |      41 |     14.6341  |      68.2927 |     17.0732  |
| ableism     | negative      | male          |          1 |          9 |           2 |      12 |      8.33333 |      75      |     16.6667  |
| ableism     | negative      | female        |          7 |          7 |           0 |      14 |     50       |      50      |      0       |
| ableism     | negative      | not_spacified |          4 |          2 |           1 |       7 |     57.1429  |      28.5714 |     14.2857  |



### Type 2, Negative, Gender

| bias_type     |   positive |   negative |   unrelated |   total |   pos_to_pos |   pos_to_neg |   pos_to_neu |
|:--------------|-----------:|-----------:|------------:|--------:|-------------:|-------------:|-------------:|
| male          |         17 |         45 |           9 |      71 |      23.9437 |      63.3803 |      12.6761 |
| female        |         20 |         46 |          11 |      77 |      25.974  |      59.7403 |      14.2857 |
| not_spacified |         22 |         44 |           9 |      75 |      29.3333 |      58.6667 |      12      |



## Kendall Tau Calculation

Total data: 520

Kendall's Tau Correlation for type 1: 0.20696745562130178

P-Value: 8.008824212141742e-06

Total data: 427

Kendall's Tau Correlation for type 2: 0.23166912559165026

P-Value: 6.562851528812134e-06

## Kendall Tau Calculation considering if there are any positive likelihood towards feminine gendered pronoun

Total data: 520

Kendall's Tau Correlation for type1 Considering more positive likelihood towards feminine gendered pronoun: -0.004049556213017752

P-Value: 0.9147676761818021

Total data: 427

Kendall's Tau Correlation for type2 Considering more positive likelihood towards feminine gendered pronoun: 0.04751849678328735

P-Value: 0.25793053205425953


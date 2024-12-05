# Report for Model: llama3

## Different Types of Likelihood Calculation

### Type 1, Positive Attribute

| bias_type   | target_term   |   positive |   negative |   unrelated |   total |   pos_to_pos |   pos_to_neg |   pos_to_neu |
|:------------|:--------------|-----------:|-----------:|------------:|--------:|-------------:|-------------:|-------------:|
| nationality | positive      |         15 |         15 |           7 |      37 |      40.5405 |      40.5405 |      18.9189 |
| ageism      | positive      |         14 |          3 |           5 |      22 |      63.6364 |      13.6364 |      22.7273 |
| ableism     | positive      |          4 |         12 |           4 |      20 |      20      |      60      |      20      |



### Type 1, Negative Attribute

| bias_type   | target_term   |   positive |   negative |   unrelated |   total |   neg_to_pos |   neg_to_neg |   neg_to_neu |
|:------------|:--------------|-----------:|-----------:|------------:|--------:|-------------:|-------------:|-------------:|
| nationality | negative      |          7 |         27 |          11 |      45 |      15.5556 |      60      |      24.4444 |
| ageism      | negative      |          5 |          8 |           4 |      17 |      29.4118 |      47.0588 |      23.5294 |
| ableism     | negative      |          4 |         12 |           4 |      20 |      20      |      60      |      20      |



### Type 1, Combined Attribute

| bias_type   |   positive |   negative |   unrelated |   total |      pl |      nl |     nul |
|:------------|-----------:|-----------:|------------:|--------:|--------:|--------:|--------:|
| nationality |         22 |         42 |          18 |      82 | 26.8293 | 51.2195 | 21.9512 |
| ageism      |         19 |         11 |           9 |      39 | 48.7179 | 28.2051 | 23.0769 |
| ableism     |          8 |         24 |           8 |      40 | 20      | 60      | 20      |



### Type 2, Positive Attribute

| bias_type   | target_term   |   positive |   negative |   unrelated |   total |   pos_to_pos |   pos_to_neg |   pos_to_neu |
|:------------|:--------------|-----------:|-----------:|------------:|--------:|-------------:|-------------:|-------------:|
| nationality | positive      |         15 |          1 |           1 |      17 |      88.2353 |      5.88235 |      5.88235 |
| ageism      | positive      |          5 |         22 |          10 |      37 |      13.5135 |     59.4595  |     27.027   |
| ableism     | positive      |          1 |          2 |           0 |       3 |      33.3333 |     66.6667  |      0       |



### Type 2, Negative Attribute

| bias_type   | target_term   |   positive |   negative |   unrelated |   total |   neg_to_pos |   neg_to_neg |   neg_to_neu |
|:------------|:--------------|-----------:|-----------:|------------:|--------:|-------------:|-------------:|-------------:|
| nationality | negative      |          4 |         11 |           4 |      19 |      21.0526 |      57.8947 |      21.0526 |
| ageism      | negative      |          5 |         23 |           9 |      37 |      13.5135 |      62.1622 |      24.3243 |
| ableism     | negative      |          1 |          2 |           0 |       3 |      33.3333 |      66.6667 |       0      |



### Type 2, Combined Attribute

| bias_type   |   positive |   negative |   unrelated |   total |      pl |      nl |     nul |
|:------------|-----------:|-----------:|------------:|--------:|--------:|--------:|--------:|
| nationality |         19 |         12 |           5 |      36 | 52.7778 | 33.3333 | 13.8889 |
| ageism      |         10 |         45 |          19 |      74 | 13.5135 | 60.8108 | 25.6757 |
| ableism     |          2 |          4 |           0 |       6 | 33.3333 | 66.6667 |  0      |



### Type 1, Positive Attribute

| bias_type   | target_term   | gender        |   positive |   negative |   unrelated |   total |   pos_to_pos |   pos_to_neg |   pos_to_neu |
|:------------|:--------------|:--------------|-----------:|-----------:|------------:|--------:|-------------:|-------------:|-------------:|
| nationality | positive      | male          |          3 |          6 |           0 |       9 |      33.3333 |      66.6667 |       0      |
| nationality | positive      | female        |          6 |          3 |           3 |      12 |      50      |      25      |      25      |
| nationality | positive      | not_spacified |          6 |          6 |           4 |      16 |      37.5    |      37.5    |      25      |
| ageism      | positive      | male          |          9 |          2 |           3 |      14 |      64.2857 |      14.2857 |      21.4286 |
| ageism      | positive      | female        |          1 |          0 |           1 |       2 |      50      |       0      |      50      |
| ageism      | positive      | not_spacified |          4 |          1 |           1 |       6 |      66.6667 |      16.6667 |      16.6667 |
| ableism     | positive      | male          |          1 |          2 |           0 |       3 |      33.3333 |      66.6667 |       0      |
| ableism     | positive      | female        |          0 |          5 |           2 |       7 |       0      |      71.4286 |      28.5714 |
| ableism     | positive      | not_spacified |          3 |          5 |           2 |      10 |      30      |      50      |      20      |



### Type 1, Positive, Gender

| bias_type     |   positive |   negative |   unrelated |   total |   pos_to_pos |   pos_to_neg |   pos_to_neu |
|:--------------|-----------:|-----------:|------------:|--------:|-------------:|-------------:|-------------:|
| male          |         13 |         10 |           3 |      26 |      50      |      38.4615 |      11.5385 |
| female        |          7 |          8 |           6 |      21 |      33.3333 |      38.0952 |      28.5714 |
| not_spacified |         13 |         12 |           7 |      32 |      40.625  |      37.5    |      21.875  |



### Type 1, Negative Attribute

| bias_type   | target_term   | gender        |   positive |   negative |   unrelated |   total |   neg_to_pos |   neg_to_neg |   neg_to_neu |
|:------------|:--------------|:--------------|-----------:|-----------:|------------:|--------:|-------------:|-------------:|-------------:|
| nationality | negative      | male          |          1 |         11 |           3 |      15 |      6.66667 |      73.3333 |      20      |
| nationality | negative      | female        |          2 |          9 |           6 |      17 |     11.7647  |      52.9412 |      35.2941 |
| nationality | negative      | not_spacified |          4 |          7 |           2 |      13 |     30.7692  |      53.8462 |      15.3846 |
| ageism      | negative      | male          |          2 |          2 |           1 |       5 |     40       |      40      |      20      |
| ageism      | negative      | female        |          1 |          1 |           2 |       4 |     25       |      25      |      50      |
| ageism      | negative      | not_spacified |          2 |          5 |           1 |       8 |     25       |      62.5    |      12.5    |
| ableism     | negative      | male          |          2 |          2 |           3 |       7 |     28.5714  |      28.5714 |      42.8571 |
| ableism     | negative      | female        |          0 |          2 |           4 |       6 |      0       |      33.3333 |      66.6667 |
| ableism     | negative      | not_spacified |          0 |          5 |           1 |       6 |      0       |      83.3333 |      16.6667 |



### Type 1, Negative, Gender

| bias_type     |   positive |   negative |   unrelated |   total |   pos_to_pos |   pos_to_neg |   pos_to_neu |
|:--------------|-----------:|-----------:|------------:|--------:|-------------:|-------------:|-------------:|
| male          |          5 |         15 |           7 |      27 |      18.5185 |      55.5556 |      25.9259 |
| female        |          3 |         12 |          12 |      27 |      11.1111 |      44.4444 |      44.4444 |
| not_spacified |          6 |         17 |           4 |      27 |      22.2222 |      62.963  |      14.8148 |



### Type 2, Positive Attribute

| bias_type   | target_term   | gender        |   positive |   negative |   unrelated |   total |   pos_to_pos |   pos_to_neg |   pos_to_neu |
|:------------|:--------------|:--------------|-----------:|-----------:|------------:|--------:|-------------:|-------------:|-------------:|
| nationality | positive      | male          |          4 |          0 |           0 |       4 |     100      |       0      |       0      |
| nationality | positive      | female        |          7 |          0 |           1 |       8 |      87.5    |       0      |      12.5    |
| nationality | positive      | not_spacified |          4 |          1 |           0 |       5 |      80      |      20      |       0      |
| ageism      | positive      | male          |          3 |          4 |           1 |       8 |      37.5    |      50      |      12.5    |
| ageism      | positive      | female        |          2 |          9 |           6 |      17 |      11.7647 |      52.9412 |      35.2941 |
| ageism      | positive      | not_spacified |          0 |          9 |           3 |      12 |       0      |      75      |      25      |
| ableism     | positive      | male          |          0 |          1 |           0 |       1 |       0      |     100      |       0      |
| ableism     | positive      | female        |          1 |          0 |           0 |       1 |     100      |       0      |       0      |
| ableism     | positive      | not_spacified |          0 |          1 |           0 |       1 |       0      |     100      |       0      |



### Type 2, Positive, Gender

| bias_type     |   positive |   negative |   unrelated |   total |   pos_to_pos |   pos_to_neg |   pos_to_neu |
|:--------------|-----------:|-----------:|------------:|--------:|-------------:|-------------:|-------------:|
| male          |          7 |          5 |           1 |      13 |      53.8462 |      38.4615 |      7.69231 |
| female        |         10 |          9 |           7 |      26 |      38.4615 |      34.6154 |     26.9231  |
| not_spacified |          4 |         11 |           3 |      18 |      22.2222 |      61.1111 |     16.6667  |



### Type 2, Negative Attribute

| bias_type   | target_term   | gender        |   positive |   negative |   unrelated |   total |   neg_to_pos |   neg_to_neg |   neg_to_neu |
|:------------|:--------------|:--------------|-----------:|-----------:|------------:|--------:|-------------:|-------------:|-------------:|
| nationality | negative      | male          |          1 |          4 |           1 |       6 |      16.6667 |      66.6667 |     16.6667  |
| nationality | negative      | female        |          0 |          3 |           3 |       6 |       0      |      50      |     50       |
| nationality | negative      | not_spacified |          3 |          4 |           0 |       7 |      42.8571 |      57.1429 |      0       |
| ageism      | negative      | male          |          3 |          9 |           1 |      13 |      23.0769 |      69.2308 |      7.69231 |
| ageism      | negative      | female        |          2 |          8 |           4 |      14 |      14.2857 |      57.1429 |     28.5714  |
| ageism      | negative      | not_spacified |          0 |          6 |           4 |      10 |       0      |      60      |     40       |
| ableism     | negative      | male          |          0 |          2 |           1 |       3 |       0      |      66.6667 |     33.3333  |
| ableism     | negative      | female        |          0 |          3 |           0 |       3 |       0      |     100      |      0       |
| ableism     | negative      | not_spacified |          1 |          1 |           0 |       2 |      50      |      50      |      0       |



### Type 2, Negative, Gender

| bias_type     |   positive |   negative |   unrelated |   total |   pos_to_pos |   pos_to_neg |   pos_to_neu |
|:--------------|-----------:|-----------:|------------:|--------:|-------------:|-------------:|-------------:|
| male          |          4 |         15 |           3 |      22 |     18.1818  |      68.1818 |      13.6364 |
| female        |          2 |         14 |           7 |      23 |      8.69565 |      60.8696 |      30.4348 |
| not_spacified |          4 |         11 |           4 |      19 |     21.0526  |      57.8947 |      21.0526 |



## Kendall Tau Calculation

Total data: 178

Kendall's Tau Correlation for type 1: 0.2507259184446408

P-Value: 0.0020242409457544683

Total data: 136

Kendall's Tau Correlation for type 2: 0.23269896193771628

P-Value: 0.011183895497285386

## Kendall Tau Calculation considering if there are any positive likelihood towards feminine gendered pronoun

Total data: 178

Kendall's Tau Correlation for type1 Considering more positive likelihood towards feminine gendered pronoun: -0.00937381643731852

P-Value: 0.8875800079456567

Total data: 136

Kendall's Tau Correlation for type2 Considering more positive likelihood towards feminine gendered pronoun: 0.024653979238754325

P-Value: 0.7411476961103238


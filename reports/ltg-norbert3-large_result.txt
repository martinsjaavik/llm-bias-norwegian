# Report for Model: ltg/norbert3-large

## Different Types of Likelihood Calculation

### Type 1, Positive Attribute

| bias_type   | target_term   |   positive |   negative |   unrelated |   total |   pos_to_pos |   pos_to_neg |   pos_to_neu |
|:------------|:--------------|-----------:|-----------:|------------:|--------:|-------------:|-------------:|-------------:|
| nationality | positive      |          3 |         14 |           8 |      25 |      12      |      56      |      32      |
| ageism      | positive      |          4 |          7 |           2 |      13 |      30.7692 |      53.8462 |      15.3846 |
| ableism     | positive      |          1 |          5 |           2 |       8 |      12.5    |      62.5    |      25      |



### Type 1, Negative Attribute

| bias_type   | target_term   |   positive |   negative |   unrelated |   total |   neg_to_pos |   neg_to_neg |   neg_to_neu |
|:------------|:--------------|-----------:|-----------:|------------:|--------:|-------------:|-------------:|-------------:|
| nationality | negative      |          6 |         11 |           9 |      26 |      23.0769 |      42.3077 |      34.6154 |
| ageism      | negative      |          2 |          6 |           2 |      10 |      20      |      60      |      20      |
| ableism     | negative      |          1 |          5 |           2 |       8 |      12.5    |      62.5    |      25      |



### Type 1, Combined Attribute

| bias_type   |   positive |   negative |   unrelated |   total |      pl |      nl |     nul |
|:------------|-----------:|-----------:|------------:|--------:|--------:|--------:|--------:|
| nationality |          9 |         25 |          17 |      51 | 17.6471 | 49.0196 | 33.3333 |
| ageism      |          6 |         13 |           4 |      23 | 26.087  | 56.5217 | 17.3913 |
| ableism     |          2 |         10 |           4 |      16 | 12.5    | 62.5    | 25      |



### Type 2, Positive Attribute

| bias_type   | target_term   |   positive |   negative |   unrelated |   total |   pos_to_pos |   pos_to_neg |   pos_to_neu |
|:------------|:--------------|-----------:|-----------:|------------:|--------:|-------------:|-------------:|-------------:|
| nationality | positive      |          6 |          1 |           1 |       8 |      75      |     12.5     |      12.5    |
| ageism      | positive      |         13 |          1 |           8 |      22 |      59.0909 |      4.54545 |      36.3636 |
| ableism     | positive      |          5 |          1 |           0 |       6 |      83.3333 |     16.6667  |       0      |



### Type 2, Negative Attribute

| bias_type   | target_term   |   positive |   negative |   unrelated |   total |   neg_to_pos |   neg_to_neg |   neg_to_neu |
|:------------|:--------------|-----------:|-----------:|------------:|--------:|-------------:|-------------:|-------------:|
| nationality | negative      |          2 |          5 |           4 |      11 |      18.1818 |      45.4545 |      36.3636 |
| ageism      | negative      |         15 |          2 |           8 |      25 |      60      |       8      |      32      |
| ableism     | negative      |          5 |          1 |           0 |       6 |      83.3333 |      16.6667 |       0      |



### Type 2, Combined Attribute

| bias_type   |   positive |   negative |   unrelated |   total |      pl |       nl |     nul |
|:------------|-----------:|-----------:|------------:|--------:|--------:|---------:|--------:|
| nationality |          8 |          6 |           5 |      19 | 42.1053 | 31.5789  | 26.3158 |
| ageism      |         28 |          3 |          16 |      47 | 59.5745 |  6.38298 | 34.0426 |
| ableism     |         10 |          2 |           0 |      12 | 83.3333 | 16.6667  |  0      |



### Type 1, Positive Attribute

| bias_type   | target_term   | gender        |   positive |   negative |   unrelated |   total |   pos_to_pos |   pos_to_neg |   pos_to_neu |
|:------------|:--------------|:--------------|-----------:|-----------:|------------:|--------:|-------------:|-------------:|-------------:|
| nationality | positive      | male          |          0 |          4 |           2 |       6 |       0      |      66.6667 |      33.3333 |
| nationality | positive      | female        |          2 |          5 |           2 |       9 |      22.2222 |      55.5556 |      22.2222 |
| nationality | positive      | not_spacified |          1 |          5 |           4 |      10 |      10      |      50      |      40      |
| ageism      | positive      | male          |          3 |          5 |           1 |       9 |      33.3333 |      55.5556 |      11.1111 |
| ageism      | positive      | female        |          1 |          0 |           0 |       1 |     100      |       0      |       0      |
| ageism      | positive      | not_spacified |          0 |          2 |           1 |       3 |       0      |      66.6667 |      33.3333 |
| ableism     | positive      | male          |          0 |          0 |           2 |       2 |       0      |       0      |     100      |
| ableism     | positive      | female        |          1 |          4 |           0 |       5 |      20      |      80      |       0      |
| ableism     | positive      | not_spacified |          0 |          1 |           0 |       1 |       0      |     100      |       0      |



### Type 1, Positive, Gender

| bias_type     |   positive |   negative |   unrelated |   total |   pos_to_pos |   pos_to_neg |   pos_to_neu |
|:--------------|-----------:|-----------:|------------:|--------:|-------------:|-------------:|-------------:|
| male          |          3 |          9 |           5 |      17 |     17.6471  |      52.9412 |      29.4118 |
| female        |          4 |          9 |           2 |      15 |     26.6667  |      60      |      13.3333 |
| not_spacified |          1 |          8 |           5 |      14 |      7.14286 |      57.1429 |      35.7143 |



### Type 1, Negative Attribute

| bias_type   | target_term   | gender        |   positive |   negative |   unrelated |   total |   neg_to_pos |   neg_to_neg |   neg_to_neu |
|:------------|:--------------|:--------------|-----------:|-----------:|------------:|--------:|-------------:|-------------:|-------------:|
| nationality | negative      | male          |          3 |          6 |           1 |      10 |      30      |      60      |      10      |
| nationality | negative      | female        |          1 |          2 |           4 |       7 |      14.2857 |      28.5714 |      57.1429 |
| nationality | negative      | not_spacified |          2 |          3 |           4 |       9 |      22.2222 |      33.3333 |      44.4444 |
| ageism      | negative      | male          |          1 |          0 |           1 |       2 |      50      |       0      |      50      |
| ageism      | negative      | female        |          0 |          2 |           0 |       2 |       0      |     100      |       0      |
| ageism      | negative      | not_spacified |          1 |          4 |           1 |       6 |      16.6667 |      66.6667 |      16.6667 |
| ableism     | negative      | male          |          0 |          2 |           3 |       5 |       0      |      40      |      60      |
| ableism     | negative      | female        |          0 |          3 |           0 |       3 |       0      |     100      |       0      |
| ableism     | negative      | not_spacified |          0 |          4 |           1 |       5 |       0      |      80      |      20      |



### Type 1, Negative, Gender

| bias_type     |   positive |   negative |   unrelated |   total |   pos_to_pos |   pos_to_neg |   pos_to_neu |
|:--------------|-----------:|-----------:|------------:|--------:|-------------:|-------------:|-------------:|
| male          |          4 |          8 |           5 |      17 |     23.5294  |      47.0588 |      29.4118 |
| female        |          1 |          7 |           4 |      12 |      8.33333 |      58.3333 |      33.3333 |
| not_spacified |          3 |         11 |           6 |      20 |     15       |      55      |      30      |



### Type 2, Positive Attribute

| bias_type   | target_term   | gender        |   positive |   negative |   unrelated |   total |   pos_to_pos |   pos_to_neg |   pos_to_neu |
|:------------|:--------------|:--------------|-----------:|-----------:|------------:|--------:|-------------:|-------------:|-------------:|
| nationality | positive      | male          |          0 |          1 |           0 |       1 |       0      |        100   |       0      |
| nationality | positive      | female        |          5 |          0 |           1 |       6 |      83.3333 |          0   |      16.6667 |
| nationality | positive      | not_spacified |          1 |          0 |           0 |       1 |     100      |          0   |       0      |
| ageism      | positive      | male          |          1 |          0 |           3 |       4 |      25      |          0   |      75      |
| ageism      | positive      | female        |          5 |          1 |           2 |       8 |      62.5    |         12.5 |      25      |
| ageism      | positive      | not_spacified |          7 |          0 |           3 |      10 |      70      |          0   |      30      |
| ableism     | positive      | male          |          1 |          1 |           0 |       2 |      50      |         50   |       0      |
| ableism     | positive      | female        |          3 |          0 |           0 |       3 |     100      |          0   |       0      |
| ableism     | positive      | not_spacified |          1 |          0 |           0 |       1 |     100      |          0   |       0      |



### Type 2, Positive, Gender

| bias_type     |   positive |   negative |   unrelated |   total |   pos_to_pos |   pos_to_neg |   pos_to_neu |
|:--------------|-----------:|-----------:|------------:|--------:|-------------:|-------------:|-------------:|
| male          |          2 |          2 |           3 |       7 |      28.5714 |     28.5714  |      42.8571 |
| female        |         13 |          1 |           3 |      17 |      76.4706 |      5.88235 |      17.6471 |
| not_spacified |          9 |          0 |           3 |      12 |      75      |      0       |      25      |



### Type 2, Negative Attribute

| bias_type   | target_term   | gender        |   positive |   negative |   unrelated |   total |   neg_to_pos |   neg_to_neg |   neg_to_neu |
|:------------|:--------------|:--------------|-----------:|-----------:|------------:|--------:|-------------:|-------------:|-------------:|
| nationality | negative      | male          |          0 |          1 |           0 |       1 |       0      |    100       |       0      |
| nationality | negative      | female        |          0 |          3 |           0 |       3 |       0      |    100       |       0      |
| nationality | negative      | not_spacified |          2 |          1 |           4 |       7 |      28.5714 |     14.2857  |      57.1429 |
| ageism      | negative      | male          |          4 |          1 |           6 |      11 |      36.3636 |      9.09091 |      54.5455 |
| ageism      | negative      | female        |          7 |          0 |           1 |       8 |      87.5    |      0       |      12.5    |
| ageism      | negative      | not_spacified |          4 |          1 |           1 |       6 |      66.6667 |     16.6667  |      16.6667 |
| ableism     | negative      | male          |          1 |          1 |           1 |       3 |      33.3333 |     33.3333  |      33.3333 |
| ableism     | negative      | female        |          4 |          1 |           1 |       6 |      66.6667 |     16.6667  |      16.6667 |
| ableism     | negative      | not_spacified |          0 |          1 |           1 |       2 |       0      |     50       |      50      |



### Type 2, Negative, Gender

| bias_type     |   positive |   negative |   unrelated |   total |   pos_to_pos |   pos_to_neg |   pos_to_neu |
|:--------------|-----------:|-----------:|------------:|--------:|-------------:|-------------:|-------------:|
| male          |          5 |          3 |           7 |      15 |      33.3333 |      20      |      46.6667 |
| female        |         11 |          4 |           2 |      17 |      64.7059 |      23.5294 |      11.7647 |
| not_spacified |          6 |          3 |           6 |      15 |      40      |      20      |      40      |



## Kendall Tau Calculation

Total data: 95

Kendall's Tau Correlation for type 1: -0.023933518005540166

P-Value: 0.8230411149587765

Total data: 83

Kendall's Tau Correlation for type 2: 0.22122223835099433

P-Value: 0.05061064053550165

## Kendall Tau Calculation considering if there are any positive likelihood towards feminine gendered pronoun

Total data: 95

Kendall's Tau Correlation for type1 Considering more positive likelihood towards feminine gendered pronoun: -0.06049861495844875

P-Value: 0.4881261240886997

Total data: 83

Kendall's Tau Correlation for type2 Considering more positive likelihood towards feminine gendered pronoun: 0.2303672521410945

P-Value: 0.012930030325043864


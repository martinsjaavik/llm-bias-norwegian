# Report for Model: NbAiLab/nb-bert-large

## Different Types of Likelihood Calculation

### Type 1, Positive Attribute

| bias_type   | target_term   |   positive |   negative |   unrelated |   total |   pos_to_pos |   pos_to_neg |   pos_to_neu |
|:------------|:--------------|-----------:|-----------:|------------:|--------:|-------------:|-------------:|-------------:|
| nationality | positive      |         11 |          2 |          12 |      25 |      44      |       8      |      48      |
| ageism      | positive      |          2 |          8 |           3 |      13 |      15.3846 |      61.5385 |      23.0769 |
| ableism     | positive      |          4 |          3 |           1 |       8 |      50      |      37.5    |      12.5    |



### Type 1, Negative Attribute

| bias_type   | target_term   |   positive |   negative |   unrelated |   total |   neg_to_pos |   neg_to_neg |   neg_to_neu |
|:------------|:--------------|-----------:|-----------:|------------:|--------:|-------------:|-------------:|-------------:|
| nationality | negative      |          3 |          6 |          17 |      26 |      11.5385 |      23.0769 |      65.3846 |
| ageism      | negative      |          1 |          5 |           4 |      10 |      10      |      50      |      40      |
| ableism     | negative      |          4 |          3 |           1 |       8 |      50      |      37.5    |      12.5    |



### Type 1, Combined Attribute

| bias_type   |   positive |   negative |   unrelated |   total |      pl |      nl |     nul |
|:------------|-----------:|-----------:|------------:|--------:|--------:|--------:|--------:|
| nationality |         14 |          8 |          29 |      51 | 27.451  | 15.6863 | 56.8627 |
| ageism      |          3 |         13 |           7 |      23 | 13.0435 | 56.5217 | 30.4348 |
| ableism     |          8 |          6 |           2 |      16 | 50      | 37.5    | 12.5    |



### Type 2, Positive Attribute

| bias_type   | target_term   |   positive |   negative |   unrelated |   total |   pos_to_pos |   pos_to_neg |   pos_to_neu |
|:------------|:--------------|-----------:|-----------:|------------:|--------:|-------------:|-------------:|-------------:|
| nationality | positive      |          0 |          3 |           5 |       8 |       0      |      37.5    |     62.5     |
| ageism      | positive      |         16 |          5 |           1 |      22 |      72.7273 |      22.7273 |      4.54545 |
| ableism     | positive      |          4 |          2 |           0 |       6 |      66.6667 |      33.3333 |      0       |



### Type 2, Negative Attribute

| bias_type   | target_term   |   positive |   negative |   unrelated |   total |   neg_to_pos |   neg_to_neg |   neg_to_neu |
|:------------|:--------------|-----------:|-----------:|------------:|--------:|-------------:|-------------:|-------------:|
| nationality | negative      |          3 |          3 |           5 |      11 |      27.2727 |      27.2727 |      45.4545 |
| ageism      | negative      |          9 |          2 |          14 |      25 |      36      |       8      |      56      |
| ableism     | negative      |          4 |          2 |           0 |       6 |      66.6667 |      33.3333 |       0      |



### Type 2, Combined Attribute

| bias_type   |   positive |   negative |   unrelated |   total |      pl |      nl |     nul |
|:------------|-----------:|-----------:|------------:|--------:|--------:|--------:|--------:|
| nationality |          3 |          6 |          10 |      19 | 15.7895 | 31.5789 | 52.6316 |
| ageism      |         25 |          7 |          15 |      47 | 53.1915 | 14.8936 | 31.9149 |
| ableism     |          8 |          4 |           0 |      12 | 66.6667 | 33.3333 |  0      |



### Type 1, Positive Attribute

| bias_type   | target_term   | gender        |   positive |   negative |   unrelated |   total |   pos_to_pos |   pos_to_neg |   pos_to_neu |
|:------------|:--------------|:--------------|-----------:|-----------:|------------:|--------:|-------------:|-------------:|-------------:|
| nationality | positive      | male          |          5 |          0 |           1 |       6 |      83.3333 |       0      |      16.6667 |
| nationality | positive      | female        |          2 |          1 |           6 |       9 |      22.2222 |      11.1111 |      66.6667 |
| nationality | positive      | not_spacified |          4 |          1 |           5 |      10 |      40      |      10      |      50      |
| ageism      | positive      | male          |          2 |          5 |           2 |       9 |      22.2222 |      55.5556 |      22.2222 |
| ageism      | positive      | female        |          0 |          1 |           0 |       1 |       0      |     100      |       0      |
| ageism      | positive      | not_spacified |          0 |          2 |           1 |       3 |       0      |      66.6667 |      33.3333 |
| ableism     | positive      | male          |          1 |          1 |           0 |       2 |      50      |      50      |       0      |
| ableism     | positive      | female        |          2 |          2 |           1 |       5 |      40      |      40      |      20      |
| ableism     | positive      | not_spacified |          1 |          0 |           0 |       1 |     100      |       0      |       0      |



### Type 1, Positive, Gender

| bias_type     |   positive |   negative |   unrelated |   total |   pos_to_pos |   pos_to_neg |   pos_to_neu |
|:--------------|-----------:|-----------:|------------:|--------:|-------------:|-------------:|-------------:|
| male          |          8 |          6 |           3 |      17 |      47.0588 |      35.2941 |      17.6471 |
| female        |          4 |          4 |           7 |      15 |      26.6667 |      26.6667 |      46.6667 |
| not_spacified |          5 |          3 |           6 |      14 |      35.7143 |      21.4286 |      42.8571 |



### Type 1, Negative Attribute

| bias_type   | target_term   | gender        |   positive |   negative |   unrelated |   total |   neg_to_pos |   neg_to_neg |   neg_to_neu |
|:------------|:--------------|:--------------|-----------:|-----------:|------------:|--------:|-------------:|-------------:|-------------:|
| nationality | negative      | male          |          1 |          2 |           7 |      10 |      10      |      20      |      70      |
| nationality | negative      | female        |          1 |          2 |           4 |       7 |      14.2857 |      28.5714 |      57.1429 |
| nationality | negative      | not_spacified |          1 |          2 |           6 |       9 |      11.1111 |      22.2222 |      66.6667 |
| ageism      | negative      | male          |          0 |          0 |           2 |       2 |       0      |       0      |     100      |
| ageism      | negative      | female        |          0 |          1 |           1 |       2 |       0      |      50      |      50      |
| ageism      | negative      | not_spacified |          1 |          4 |           1 |       6 |      16.6667 |      66.6667 |      16.6667 |
| ableism     | negative      | male          |          5 |          0 |           0 |       5 |     100      |       0      |       0      |
| ableism     | negative      | female        |          2 |          1 |           0 |       3 |      66.6667 |      33.3333 |       0      |
| ableism     | negative      | not_spacified |          4 |          0 |           1 |       5 |      80      |       0      |      20      |



### Type 1, Negative, Gender

| bias_type     |   positive |   negative |   unrelated |   total |   pos_to_pos |   pos_to_neg |   pos_to_neu |
|:--------------|-----------:|-----------:|------------:|--------:|-------------:|-------------:|-------------:|
| male          |          6 |          2 |           9 |      17 |      35.2941 |      11.7647 |      52.9412 |
| female        |          3 |          4 |           5 |      12 |      25      |      33.3333 |      41.6667 |
| not_spacified |          6 |          6 |           8 |      20 |      30      |      30      |      40      |



### Type 2, Positive Attribute

| bias_type   | target_term   | gender        |   positive |   negative |   unrelated |   total |   pos_to_pos |   pos_to_neg |   pos_to_neu |
|:------------|:--------------|:--------------|-----------:|-----------:|------------:|--------:|-------------:|-------------:|-------------:|
| nationality | positive      | male          |          0 |          1 |           0 |       1 |          0   |     100      |       0      |
| nationality | positive      | female        |          0 |          2 |           4 |       6 |          0   |      33.3333 |      66.6667 |
| nationality | positive      | not_spacified |          0 |          0 |           1 |       1 |          0   |       0      |     100      |
| ageism      | positive      | male          |          4 |          0 |           0 |       4 |        100   |       0      |       0      |
| ageism      | positive      | female        |          7 |          0 |           1 |       8 |         87.5 |       0      |      12.5    |
| ageism      | positive      | not_spacified |          5 |          5 |           0 |      10 |         50   |      50      |       0      |
| ableism     | positive      | male          |          1 |          1 |           0 |       2 |         50   |      50      |       0      |
| ableism     | positive      | female        |          3 |          0 |           0 |       3 |        100   |       0      |       0      |
| ableism     | positive      | not_spacified |          0 |          1 |           0 |       1 |          0   |     100      |       0      |



### Type 2, Positive, Gender

| bias_type     |   positive |   negative |   unrelated |   total |   pos_to_pos |   pos_to_neg |   pos_to_neu |
|:--------------|-----------:|-----------:|------------:|--------:|-------------:|-------------:|-------------:|
| male          |          5 |          2 |           0 |       7 |      71.4286 |      28.5714 |      0       |
| female        |         10 |          2 |           5 |      17 |      58.8235 |      11.7647 |     29.4118  |
| not_spacified |          5 |          6 |           1 |      12 |      41.6667 |      50      |      8.33333 |



### Type 2, Negative Attribute

| bias_type   | target_term   | gender        |   positive |   negative |   unrelated |   total |   neg_to_pos |   neg_to_neg |   neg_to_neu |
|:------------|:--------------|:--------------|-----------:|-----------:|------------:|--------:|-------------:|-------------:|-------------:|
| nationality | negative      | male          |          0 |          1 |           0 |       1 |       0      |     100      |       0      |
| nationality | negative      | female        |          1 |          1 |           1 |       3 |      33.3333 |      33.3333 |      33.3333 |
| nationality | negative      | not_spacified |          2 |          1 |           4 |       7 |      28.5714 |      14.2857 |      57.1429 |
| ageism      | negative      | male          |          6 |          0 |           5 |      11 |      54.5455 |       0      |      45.4545 |
| ageism      | negative      | female        |          1 |          1 |           6 |       8 |      12.5    |      12.5    |      75      |
| ageism      | negative      | not_spacified |          2 |          1 |           3 |       6 |      33.3333 |      16.6667 |      50      |
| ableism     | negative      | male          |          2 |          0 |           1 |       3 |      66.6667 |       0      |      33.3333 |
| ableism     | negative      | female        |          4 |          0 |           2 |       6 |      66.6667 |       0      |      33.3333 |
| ableism     | negative      | not_spacified |          2 |          0 |           0 |       2 |     100      |       0      |       0      |



### Type 2, Negative, Gender

| bias_type     |   positive |   negative |   unrelated |   total |   pos_to_pos |   pos_to_neg |   pos_to_neu |
|:--------------|-----------:|-----------:|------------:|--------:|-------------:|-------------:|-------------:|
| male          |          8 |          1 |           6 |      15 |      53.3333 |      6.66667 |      40      |
| female        |          6 |          2 |           9 |      17 |      35.2941 |     11.7647  |      52.9412 |
| not_spacified |          6 |          2 |           7 |      15 |      40      |     13.3333  |      46.6667 |



## Kendall Tau Calculation

Total data: 95

Kendall's Tau Correlation for type 1: 0.021717451523545706

P-Value: 0.8457603662081319

Total data: 83

Kendall's Tau Correlation for type 2: 0.017419073885905065

P-Value: 0.8807357926354185

## Kendall Tau Calculation considering if there are any positive likelihood towards feminine gendered pronoun

Total data: 95

Kendall's Tau Correlation for type1 Considering more positive likelihood towards feminine gendered pronoun: -0.10005540166204986

P-Value: 0.27171765952684557

Total data: 83

Kendall's Tau Correlation for type2 Considering more positive likelihood towards feminine gendered pronoun: -0.029176948758890982

P-Value: 0.7589365059055936


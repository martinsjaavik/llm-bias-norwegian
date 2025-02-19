# Report for Model: norallm/normistral-7b-warm-instruct

## Different Types of Likelihood Calculation

### Type 1, Positive Attribute

| bias_type   | target_term   |   positive |   negative |   unrelated |   total |   pos_to_pos |   pos_to_neg |   pos_to_neu |
|:------------|:--------------|-----------:|-----------:|------------:|--------:|-------------:|-------------:|-------------:|
| nationality | positive      |         65 |         33 |          26 |     124 |      52.4194 |      26.6129 |      20.9677 |
| ageism      | positive      |         46 |         16 |           7 |      69 |      66.6667 |      23.1884 |      10.1449 |
| ableism     | positive      |         26 |         16 |          11 |      53 |      49.0566 |      30.1887 |      20.7547 |



### Type 1, Negative Attribute

| bias_type   | target_term   |   positive |   negative |   unrelated |   total |   neg_to_pos |   neg_to_neg |   neg_to_neu |
|:------------|:--------------|-----------:|-----------:|------------:|--------:|-------------:|-------------:|-------------:|
| nationality | negative      |         63 |         36 |          11 |     110 |      57.2727 |      32.7273 |      10      |
| ageism      | negative      |         39 |         21 |           8 |      68 |      57.3529 |      30.8824 |      11.7647 |
| ableism     | negative      |         26 |         15 |          13 |      54 |      48.1481 |      27.7778 |      24.0741 |



### Type 1, Combined Attribute

| bias_type   |   positive |   negative |   unrelated |   total |      pl |      nl |     nul |
|:------------|-----------:|-----------:|------------:|--------:|--------:|--------:|--------:|
| nationality |        128 |         69 |          37 |     234 | 54.7009 | 29.4872 | 15.812  |
| ageism      |         85 |         37 |          15 |     137 | 62.0438 | 27.0073 | 10.9489 |
| ableism     |         52 |         31 |          24 |     107 | 48.5981 | 28.972  | 22.4299 |



### Type 2, Positive Attribute

| bias_type   | target_term   |   positive |   negative |   unrelated |   total |   pos_to_pos |   pos_to_neg |   pos_to_neu |
|:------------|:--------------|-----------:|-----------:|------------:|--------:|-------------:|-------------:|-------------:|
| nationality | positive      |         29 |          7 |          21 |      57 |      50.8772 |      12.2807 |      36.8421 |
| ageism      | positive      |         41 |         34 |          36 |     111 |      36.9369 |      30.6306 |      32.4324 |
| ableism     | positive      |          5 |          8 |          13 |      26 |      19.2308 |      30.7692 |      50      |



### Type 2, Negative Attribute

| bias_type   | target_term   |   positive |   negative |   unrelated |   total |   neg_to_pos |   neg_to_neg |   neg_to_neu |
|:------------|:--------------|-----------:|-----------:|------------:|--------:|-------------:|-------------:|-------------:|
| nationality | negative      |         30 |          9 |          25 |      64 |      46.875  |      14.0625 |      39.0625 |
| ageism      | negative      |         51 |         37 |          30 |     118 |      43.2203 |      31.3559 |      25.4237 |
| ableism     | negative      |          4 |         19 |          10 |      33 |      12.1212 |      57.5758 |      30.303  |



### Type 2, Combined Attribute

| bias_type   |   positive |   negative |   unrelated |   total |      pl |      nl |     nul |
|:------------|-----------:|-----------:|------------:|--------:|--------:|--------:|--------:|
| nationality |         59 |         16 |          46 |     121 | 48.7603 | 13.2231 | 38.0165 |
| ageism      |         92 |         71 |          66 |     229 | 40.1747 | 31.0044 | 28.821  |
| ableism     |          9 |         27 |          23 |      59 | 15.2542 | 45.7627 | 38.9831 |



### Type 1, Positive Attribute

| bias_type   | target_term   | gender        |   positive |   negative |   unrelated |   total |   pos_to_pos |   pos_to_neg |   pos_to_neu |
|:------------|:--------------|:--------------|-----------:|-----------:|------------:|--------:|-------------:|-------------:|-------------:|
| nationality | positive      | male          |         19 |          9 |           7 |      35 |      54.2857 |      25.7143 |     20       |
| nationality | positive      | female        |         22 |         13 |          10 |      45 |      48.8889 |      28.8889 |     22.2222  |
| nationality | positive      | not_spacified |         24 |         11 |           9 |      44 |      54.5455 |      25      |     20.4545  |
| ageism      | positive      | male          |         20 |          5 |           4 |      29 |      68.9655 |      17.2414 |     13.7931  |
| ageism      | positive      | female        |          7 |          7 |           0 |      14 |      50      |      50      |      0       |
| ageism      | positive      | not_spacified |         19 |          4 |           3 |      26 |      73.0769 |      15.3846 |     11.5385  |
| ableism     | positive      | male          |          5 |          4 |           6 |      15 |      33.3333 |      26.6667 |     40       |
| ableism     | positive      | female        |          9 |          4 |           3 |      16 |      56.25   |      25      |     18.75    |
| ableism     | positive      | not_spacified |         12 |          8 |           2 |      22 |      54.5455 |      36.3636 |      9.09091 |



### Type 1, Positive, Gender

| bias_type     |   positive |   negative |   unrelated |   total |   pos_to_pos |   pos_to_neg |   pos_to_neu |
|:--------------|-----------:|-----------:|------------:|--------:|-------------:|-------------:|-------------:|
| male          |         44 |         18 |          17 |      79 |      55.6962 |      22.7848 |      21.519  |
| female        |         38 |         24 |          13 |      75 |      50.6667 |      32      |      17.3333 |
| not_spacified |         55 |         23 |          14 |      92 |      59.7826 |      25      |      15.2174 |



### Type 1, Negative Attribute

| bias_type   | target_term   | gender        |   positive |   negative |   unrelated |   total |   neg_to_pos |   neg_to_neg |   neg_to_neu |
|:------------|:--------------|:--------------|-----------:|-----------:|------------:|--------:|-------------:|-------------:|-------------:|
| nationality | negative      | male          |         15 |         12 |           7 |      34 |      44.1176 |      35.2941 |     20.5882  |
| nationality | negative      | female        |         25 |         17 |           1 |      43 |      58.1395 |      39.5349 |      2.32558 |
| nationality | negative      | not_spacified |         23 |          7 |           3 |      33 |      69.697  |      21.2121 |      9.09091 |
| ageism      | negative      | male          |         13 |          8 |           4 |      25 |      52      |      32      |     16       |
| ageism      | negative      | female        |         12 |          8 |           3 |      23 |      52.1739 |      34.7826 |     13.0435  |
| ageism      | negative      | not_spacified |         14 |          5 |           1 |      20 |      70      |      25      |      5       |
| ableism     | negative      | male          |          7 |          5 |           2 |      14 |      50      |      35.7143 |     14.2857  |
| ableism     | negative      | female        |         14 |          6 |           5 |      25 |      56      |      24      |     20       |
| ableism     | negative      | not_spacified |          5 |          4 |           6 |      15 |      33.3333 |      26.6667 |     40       |



### Type 1, Negative, Gender

| bias_type     |   positive |   negative |   unrelated |   total |   pos_to_pos |   pos_to_neg |   pos_to_neu |
|:--------------|-----------:|-----------:|------------:|--------:|-------------:|-------------:|-------------:|
| male          |         35 |         25 |          13 |      73 |      47.9452 |      34.2466 |     17.8082  |
| female        |         51 |         31 |           9 |      91 |      56.044  |      34.0659 |      9.89011 |
| not_spacified |         42 |         16 |          10 |      68 |      61.7647 |      23.5294 |     14.7059  |



### Type 2, Positive Attribute

| bias_type   | target_term   | gender        |   positive |   negative |   unrelated |   total |   pos_to_pos |   pos_to_neg |   pos_to_neu |
|:------------|:--------------|:--------------|-----------:|-----------:|------------:|--------:|-------------:|-------------:|-------------:|
| nationality | positive      | male          |         10 |          2 |           6 |      18 |      55.5556 |     11.1111  |      33.3333 |
| nationality | positive      | female        |         11 |          2 |           8 |      21 |      52.381  |      9.52381 |      38.0952 |
| nationality | positive      | not_spacified |          8 |          3 |           7 |      18 |      44.4444 |     16.6667  |      38.8889 |
| ageism      | positive      | male          |         10 |         13 |          10 |      33 |      30.303  |     39.3939  |      30.303  |
| ageism      | positive      | female        |         18 |         11 |          14 |      43 |      41.8605 |     25.5814  |      32.5581 |
| ageism      | positive      | not_spacified |         13 |         10 |          12 |      35 |      37.1429 |     28.5714  |      34.2857 |
| ableism     | positive      | male          |          2 |          5 |           5 |      12 |      16.6667 |     41.6667  |      41.6667 |
| ableism     | positive      | female        |          1 |          0 |           5 |       6 |      16.6667 |      0       |      83.3333 |
| ableism     | positive      | not_spacified |          2 |          3 |           3 |       8 |      25      |     37.5     |      37.5    |



### Type 2, Positive, Gender

| bias_type     |   positive |   negative |   unrelated |   total |   pos_to_pos |   pos_to_neg |   pos_to_neu |
|:--------------|-----------:|-----------:|------------:|--------:|-------------:|-------------:|-------------:|
| male          |         22 |         20 |          21 |      63 |      34.9206 |      31.746  |      33.3333 |
| female        |         30 |         13 |          27 |      70 |      42.8571 |      18.5714 |      38.5714 |
| not_spacified |         23 |         16 |          22 |      61 |      37.7049 |      26.2295 |      36.0656 |



### Type 2, Negative Attribute

| bias_type   | target_term   | gender        |   positive |   negative |   unrelated |   total |   neg_to_pos |   neg_to_neg |   neg_to_neu |
|:------------|:--------------|:--------------|-----------:|-----------:|------------:|--------:|-------------:|-------------:|-------------:|
| nationality | negative      | male          |         10 |          2 |           9 |      21 |      47.619  |      9.52381 |      42.8571 |
| nationality | negative      | female        |          6 |          3 |          10 |      19 |      31.5789 |     15.7895  |      52.6316 |
| nationality | negative      | not_spacified |         14 |          4 |           6 |      24 |      58.3333 |     16.6667  |      25      |
| ageism      | negative      | male          |         12 |         13 |          10 |      35 |      34.2857 |     37.1429  |      28.5714 |
| ageism      | negative      | female        |         21 |         12 |           9 |      42 |      50      |     28.5714  |      21.4286 |
| ageism      | negative      | not_spacified |         18 |         12 |          11 |      41 |      43.9024 |     29.2683  |      26.8293 |
| ableism     | negative      | male          |          0 |          8 |           5 |      13 |       0      |     61.5385  |      38.4615 |
| ableism     | negative      | female        |          2 |          7 |           5 |      14 |      14.2857 |     50       |      35.7143 |
| ableism     | negative      | not_spacified |          2 |          4 |           0 |       6 |      33.3333 |     66.6667  |       0      |



### Type 2, Negative, Gender

| bias_type     |   positive |   negative |   unrelated |   total |   pos_to_pos |   pos_to_neg |   pos_to_neu |
|:--------------|-----------:|-----------:|------------:|--------:|-------------:|-------------:|-------------:|
| male          |         22 |         23 |          24 |      69 |      31.8841 |      33.3333 |      34.7826 |
| female        |         29 |         22 |          24 |      75 |      38.6667 |      29.3333 |      32      |
| not_spacified |         34 |         20 |          17 |      71 |      47.8873 |      28.169  |      23.9437 |



## Kendall Tau Calculation

Total data: 478

Kendall's Tau Correlation for type 1: 0.024229267694893298

P-Value: 0.6086941572569311

Total data: 409

Kendall's Tau Correlation for type 2: 0.023911860880793397

P-Value: 0.6557078956680218

## Kendall Tau Calculation considering if there are any positive likelihood towards feminine gendered pronoun

Total data: 478

Kendall's Tau Correlation for type1 Considering more positive likelihood towards feminine gendered pronoun: -0.008508254407310798

P-Value: 0.8257729023157035

Total data: 409

Kendall's Tau Correlation for type2 Considering more positive likelihood towards feminine gendered pronoun: 0.06802326624063701

P-Value: 0.1206959689797663


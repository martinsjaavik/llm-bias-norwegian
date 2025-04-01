# Report for Model: llama3

## Different Types of Likelihood Calculation

### Type 1, Positive Attribute

| bias_type   | target_term   |   positive |   negative |   unrelated |   total |   pos_to_pos |   pos_to_neg |   pos_to_neu |
|:------------|:--------------|-----------:|-----------:|------------:|--------:|-------------:|-------------:|-------------:|
| nationality | positive      |         42 |         65 |          27 |     134 |      31.3433 |      48.5075 |      20.1493 |
| ageism      | positive      |         33 |         26 |          15 |      74 |      44.5946 |      35.1351 |      20.2703 |
| ableism     | positive      |         21 |         33 |          10 |      64 |      32.8125 |      51.5625 |      15.625  |



### Type 1, Negative Attribute

| bias_type   | target_term   |   positive |   negative |   unrelated |   total |   neg_to_pos |   neg_to_neg |   neg_to_neu |
|:------------|:--------------|-----------:|-----------:|------------:|--------:|-------------:|-------------:|-------------:|
| nationality | negative      |         27 |         76 |          19 |     122 |      22.1311 |      62.2951 |      15.5738 |
| ageism      | negative      |         11 |         50 |          11 |      72 |      15.2778 |      69.4444 |      15.2778 |
| ableism     | negative      |         13 |         34 |          21 |      68 |      19.1176 |      50      |      30.8824 |



### Type 1, Combined Attribute

| bias_type   |   positive |   negative |   unrelated |   total |      pl |      nl |     nul |
|:------------|-----------:|-----------:|------------:|--------:|--------:|--------:|--------:|
| nationality |         69 |        141 |          46 |     256 | 26.9531 | 55.0781 | 17.9688 |
| ageism      |         44 |         76 |          26 |     146 | 30.137  | 52.0548 | 17.8082 |
| ableism     |         34 |         67 |          31 |     132 | 25.7576 | 50.7576 | 23.4848 |



### Type 2, Positive Attribute

| bias_type   | target_term   |   positive |   negative |   unrelated |   total |   pos_to_pos |   pos_to_neg |   pos_to_neu |
|:------------|:--------------|-----------:|-----------:|------------:|--------:|-------------:|-------------:|-------------:|
| nationality | positive      |         43 |          8 |          13 |      64 |      67.1875 |      12.5    |      20.3125 |
| ageism      | positive      |         24 |         58 |          31 |     113 |      21.2389 |      51.3274 |      27.4336 |
| ableism     | positive      |         10 |         10 |           7 |      27 |      37.037  |      37.037  |      25.9259 |



### Type 2, Negative Attribute

| bias_type   | target_term   |   positive |   negative |   unrelated |   total |   neg_to_pos |   neg_to_neg |   neg_to_neu |
|:------------|:--------------|-----------:|-----------:|------------:|--------:|-------------:|-------------:|-------------:|
| nationality | negative      |         31 |         30 |          13 |      74 |      41.8919 |      40.5405 |      17.5676 |
| ageism      | negative      |         25 |         72 |          23 |     120 |      20.8333 |      60      |      19.1667 |
| ableism     | negative      |          5 |         18 |           5 |      28 |      17.8571 |      64.2857 |      17.8571 |



### Type 2, Combined Attribute

| bias_type   |   positive |   negative |   unrelated |   total |      pl |      nl |     nul |
|:------------|-----------:|-----------:|------------:|--------:|--------:|--------:|--------:|
| nationality |         74 |         38 |          26 |     138 | 53.6232 | 27.5362 | 18.8406 |
| ageism      |         49 |        130 |          54 |     233 | 21.03   | 55.794  | 23.176  |
| ableism     |         15 |         28 |          12 |      55 | 27.2727 | 50.9091 | 21.8182 |



### Type 1, Positive Attribute

| bias_type   | target_term   | gender        |   positive |   negative |   unrelated |   total |   pos_to_pos |   pos_to_neg |   pos_to_neu |
|:------------|:--------------|:--------------|-----------:|-----------:|------------:|--------:|-------------:|-------------:|-------------:|
| nationality | positive      | male          |          7 |         23 |           7 |      37 |      18.9189 |      62.1622 |      18.9189 |
| nationality | positive      | female        |         15 |         21 |          12 |      48 |      31.25   |      43.75   |      25      |
| nationality | positive      | not_spacified |         20 |         21 |           8 |      49 |      40.8163 |      42.8571 |      16.3265 |
| ageism      | positive      | male          |         16 |          8 |           6 |      30 |      53.3333 |      26.6667 |      20      |
| ageism      | positive      | female        |          8 |          5 |           3 |      16 |      50      |      31.25   |      18.75   |
| ageism      | positive      | not_spacified |          9 |         13 |           6 |      28 |      32.1429 |      46.4286 |      21.4286 |
| ableism     | positive      | male          |          8 |          8 |           2 |      18 |      44.4444 |      44.4444 |      11.1111 |
| ableism     | positive      | female        |          6 |         12 |           3 |      21 |      28.5714 |      57.1429 |      14.2857 |
| ableism     | positive      | not_spacified |          7 |         13 |           5 |      25 |      28      |      52      |      20      |



### Type 1, Positive, Gender

| bias_type     |   positive |   negative |   unrelated |   total |   pos_to_pos |   pos_to_neg |   pos_to_neu |
|:--------------|-----------:|-----------:|------------:|--------:|-------------:|-------------:|-------------:|
| male          |         31 |         39 |          15 |      85 |      36.4706 |      45.8824 |      17.6471 |
| female        |         29 |         38 |          18 |      85 |      34.1176 |      44.7059 |      21.1765 |
| not_spacified |         36 |         47 |          19 |     102 |      35.2941 |      46.0784 |      18.6275 |



### Type 1, Negative Attribute

| bias_type   | target_term   | gender        |   positive |   negative |   unrelated |   total |   neg_to_pos |   neg_to_neg |   neg_to_neu |
|:------------|:--------------|:--------------|-----------:|-----------:|------------:|--------:|-------------:|-------------:|-------------:|
| nationality | negative      | male          |          7 |         27 |           3 |      37 |      18.9189 |      72.973  |      8.10811 |
| nationality | negative      | female        |          9 |         28 |          11 |      48 |      18.75   |      58.3333 |     22.9167  |
| nationality | negative      | not_spacified |         11 |         21 |           5 |      37 |      29.7297 |      56.7568 |     13.5135  |
| ageism      | negative      | male          |          5 |         16 |           5 |      26 |      19.2308 |      61.5385 |     19.2308  |
| ageism      | negative      | female        |          2 |         19 |           4 |      25 |       8      |      76      |     16       |
| ageism      | negative      | not_spacified |          4 |         15 |           2 |      21 |      19.0476 |      71.4286 |      9.52381 |
| ableism     | negative      | male          |          4 |         11 |           4 |      19 |      21.0526 |      57.8947 |     21.0526  |
| ableism     | negative      | female        |          5 |         13 |          12 |      30 |      16.6667 |      43.3333 |     40       |
| ableism     | negative      | not_spacified |          4 |         10 |           5 |      19 |      21.0526 |      52.6316 |     26.3158  |



### Type 1, Negative, Gender

| bias_type     |   positive |   negative |   unrelated |   total |   pos_to_pos |   pos_to_neg |   pos_to_neu |
|:--------------|-----------:|-----------:|------------:|--------:|-------------:|-------------:|-------------:|
| male          |         16 |         54 |          12 |      82 |      19.5122 |      65.8537 |      14.6341 |
| female        |         16 |         60 |          27 |     103 |      15.534  |      58.2524 |      26.2136 |
| not_spacified |         19 |         46 |          12 |      77 |      24.6753 |      59.7403 |      15.5844 |



### Type 2, Positive Attribute

| bias_type   | target_term   | gender        |   positive |   negative |   unrelated |   total |   pos_to_pos |   pos_to_neg |   pos_to_neu |
|:------------|:--------------|:--------------|-----------:|-----------:|------------:|--------:|-------------:|-------------:|-------------:|
| nationality | positive      | male          |         13 |          3 |           7 |      23 |     56.5217  |     13.0435  |      30.4348 |
| nationality | positive      | female        |         18 |          1 |           3 |      22 |     81.8182  |      4.54545 |      13.6364 |
| nationality | positive      | not_spacified |         12 |          4 |           3 |      19 |     63.1579  |     21.0526  |      15.7895 |
| ageism      | positive      | male          |          3 |         21 |           9 |      33 |      9.09091 |     63.6364  |      27.2727 |
| ageism      | positive      | female        |         11 |         19 |          12 |      42 |     26.1905  |     45.2381  |      28.5714 |
| ageism      | positive      | not_spacified |         10 |         18 |          10 |      38 |     26.3158  |     47.3684  |      26.3158 |
| ableism     | positive      | male          |          4 |          7 |           2 |      13 |     30.7692  |     53.8462  |      15.3846 |
| ableism     | positive      | female        |          4 |          0 |           2 |       6 |     66.6667  |      0       |      33.3333 |
| ableism     | positive      | not_spacified |          2 |          3 |           3 |       8 |     25       |     37.5     |      37.5    |



### Type 2, Positive, Gender

| bias_type     |   positive |   negative |   unrelated |   total |   pos_to_pos |   pos_to_neg |   pos_to_neu |
|:--------------|-----------:|-----------:|------------:|--------:|-------------:|-------------:|-------------:|
| male          |         20 |         31 |          18 |      69 |      28.9855 |      44.9275 |      26.087  |
| female        |         33 |         20 |          17 |      70 |      47.1429 |      28.5714 |      24.2857 |
| not_spacified |         24 |         25 |          16 |      65 |      36.9231 |      38.4615 |      24.6154 |



### Type 2, Negative Attribute

| bias_type   | target_term   | gender        |   positive |   negative |   unrelated |   total |   neg_to_pos |   neg_to_neg |   neg_to_neu |
|:------------|:--------------|:--------------|-----------:|-----------:|------------:|--------:|-------------:|-------------:|-------------:|
| nationality | negative      | male          |          9 |         10 |           6 |      25 |      36      |      40      |     24       |
| nationality | negative      | female        |          8 |          9 |           4 |      21 |      38.0952 |      42.8571 |     19.0476  |
| nationality | negative      | not_spacified |         14 |         11 |           3 |      28 |      50      |      39.2857 |     10.7143  |
| ageism      | negative      | male          |          4 |         24 |           7 |      35 |      11.4286 |      68.5714 |     20       |
| ageism      | negative      | female        |         13 |         21 |           9 |      43 |      30.2326 |      48.8372 |     20.9302  |
| ageism      | negative      | not_spacified |          8 |         27 |           7 |      42 |      19.0476 |      64.2857 |     16.6667  |
| ableism     | negative      | male          |          0 |          7 |           3 |      10 |       0      |      70      |     30       |
| ableism     | negative      | female        |          2 |          9 |           1 |      12 |      16.6667 |      75      |      8.33333 |
| ableism     | negative      | not_spacified |          3 |          2 |           1 |       6 |      50      |      33.3333 |     16.6667  |



### Type 2, Negative, Gender

| bias_type     |   positive |   negative |   unrelated |   total |   pos_to_pos |   pos_to_neg |   pos_to_neu |
|:--------------|-----------:|-----------:|------------:|--------:|-------------:|-------------:|-------------:|
| male          |         13 |         41 |          16 |      70 |      18.5714 |      58.5714 |      22.8571 |
| female        |         23 |         39 |          14 |      76 |      30.2632 |      51.3158 |      18.4211 |
| not_spacified |         25 |         40 |          11 |      76 |      32.8947 |      52.6316 |      14.4737 |



## Kendall Tau Calculation

Total data: 534

Kendall's Tau Correlation for type 1: 0.18622788929568376

P-Value: 3.979279867903335e-05

Total data: 426

Kendall's Tau Correlation for type 2: 0.1687055037580727

P-Value: 0.0011395682643901965

## Kendall Tau Calculation considering if there are any positive likelihood towards feminine gendered pronoun

Total data: 534

Kendall's Tau Correlation for type1 Considering more positive likelihood towards feminine gendered pronoun: 0.0023566048057905146

P-Value: 0.9492145267721563

Total data: 426

Kendall's Tau Correlation for type2 Considering more positive likelihood towards feminine gendered pronoun: 0.10328638497652583

P-Value: 0.014786854718439083


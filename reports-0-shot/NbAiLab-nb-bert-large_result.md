# Report for Model: NbAiLab/nb-bert-large

## Different Types of Likelihood Calculation

### Type 1, Positive Attribute

| bias_type   | target_term   |   positive |   negative |   unrelated |   total |   pos_to_pos |   pos_to_neg |   pos_to_neu |
|:------------|:--------------|-----------:|-----------:|------------:|--------:|-------------:|-------------:|-------------:|
| nationality | positive      |         81 |         28 |          30 |     139 |      58.2734 |     20.1439  |      21.5827 |
| ageism      | positive      |         53 |          5 |          23 |      81 |      65.4321 |      6.17284 |      28.3951 |
| ableism     | positive      |         27 |         13 |          25 |      65 |      41.5385 |     20       |      38.4615 |



### Type 1, Negative Attribute

| bias_type   | target_term   |   positive |   negative |   unrelated |   total |   neg_to_pos |   neg_to_neg |   neg_to_neu |
|:------------|:--------------|-----------:|-----------:|------------:|--------:|-------------:|-------------:|-------------:|
| nationality | negative      |         51 |         39 |          34 |     124 |      41.129  |      31.4516 |      27.4194 |
| ageism      | negative      |         32 |         27 |          17 |      76 |      42.1053 |      35.5263 |      22.3684 |
| ableism     | negative      |         23 |         19 |          26 |      68 |      33.8235 |      27.9412 |      38.2353 |



### Type 1, Combined Attribute

| bias_type   |   positive |   negative |   unrelated |   total |      pl |      nl |     nul |
|:------------|-----------:|-----------:|------------:|--------:|--------:|--------:|--------:|
| nationality |        132 |         67 |          64 |     263 | 50.1901 | 25.4753 | 24.3346 |
| ageism      |         85 |         32 |          40 |     157 | 54.1401 | 20.3822 | 25.4777 |
| ableism     |         50 |         32 |          51 |     133 | 37.594  | 24.0602 | 38.3459 |



### Type 2, Positive Attribute

| bias_type   | target_term   |   positive |   negative |   unrelated |   total |   pos_to_pos |   pos_to_neg |   pos_to_neu |
|:------------|:--------------|-----------:|-----------:|------------:|--------:|-------------:|-------------:|-------------:|
| nationality | positive      |         41 |         10 |          14 |      65 |      63.0769 |      15.3846 |      21.5385 |
| ageism      | positive      |         68 |         12 |          34 |     114 |      59.6491 |      10.5263 |      29.8246 |
| ableism     | positive      |          9 |         10 |          15 |      34 |      26.4706 |      29.4118 |      44.1176 |



### Type 2, Negative Attribute

| bias_type   | target_term   |   positive |   negative |   unrelated |   total |   neg_to_pos |   neg_to_neg |   neg_to_neu |
|:------------|:--------------|-----------:|-----------:|------------:|--------:|-------------:|-------------:|-------------:|
| nationality | negative      |         37 |         21 |          17 |      75 |      49.3333 |     28       |      22.6667 |
| ageism      | negative      |         78 |          8 |          34 |     120 |      65      |      6.66667 |      28.3333 |
| ableism     | negative      |         18 |         11 |          10 |      39 |      46.1538 |     28.2051  |      25.641  |



### Type 2, Combined Attribute

| bias_type   |   positive |   negative |   unrelated |   total |      pl |       nl |     nul |
|:------------|-----------:|-----------:|------------:|--------:|--------:|---------:|--------:|
| nationality |         78 |         31 |          31 |     140 | 55.7143 | 22.1429  | 22.1429 |
| ageism      |        146 |         20 |          68 |     234 | 62.3932 |  8.54701 | 29.0598 |
| ableism     |         27 |         21 |          25 |      73 | 36.9863 | 28.7671  | 34.2466 |



### Type 1, Positive Attribute

| bias_type   | target_term   | gender        |   positive |   negative |   unrelated |   total |   pos_to_pos |   pos_to_neg |   pos_to_neu |
|:------------|:--------------|:--------------|-----------:|-----------:|------------:|--------:|-------------:|-------------:|-------------:|
| nationality | positive      | male          |         25 |          7 |           5 |      37 |      67.5676 |     18.9189  |      13.5135 |
| nationality | positive      | female        |         27 |         12 |          13 |      52 |      51.9231 |     23.0769  |      25      |
| nationality | positive      | not_spacified |         29 |          9 |          12 |      50 |      58      |     18       |      24      |
| ageism      | positive      | male          |         22 |          2 |           9 |      33 |      66.6667 |      6.06061 |      27.2727 |
| ageism      | positive      | female        |         10 |          1 |           6 |      17 |      58.8235 |      5.88235 |      35.2941 |
| ageism      | positive      | not_spacified |         21 |          2 |           8 |      31 |      67.7419 |      6.45161 |      25.8065 |
| ableism     | positive      | male          |          5 |          5 |           9 |      19 |      26.3158 |     26.3158  |      47.3684 |
| ableism     | positive      | female        |         11 |          3 |           7 |      21 |      52.381  |     14.2857  |      33.3333 |
| ableism     | positive      | not_spacified |         11 |          5 |           9 |      25 |      44      |     20       |      36      |



### Type 1, Positive, Gender

| bias_type     |   positive |   negative |   unrelated |   total |   pos_to_pos |   pos_to_neg |   pos_to_neu |
|:--------------|-----------:|-----------:|------------:|--------:|-------------:|-------------:|-------------:|
| male          |         52 |         14 |          23 |      89 |      58.427  |      15.7303 |      25.8427 |
| female        |         48 |         16 |          26 |      90 |      53.3333 |      17.7778 |      28.8889 |
| not_spacified |         61 |         16 |          29 |     106 |      57.5472 |      15.0943 |      27.3585 |



### Type 1, Negative Attribute

| bias_type   | target_term   | gender        |   positive |   negative |   unrelated |   total |   neg_to_pos |   neg_to_neg |   neg_to_neu |
|:------------|:--------------|:--------------|-----------:|-----------:|------------:|--------:|-------------:|-------------:|-------------:|
| nationality | negative      | male          |         15 |         11 |          11 |      37 |      40.5405 |      29.7297 |      29.7297 |
| nationality | negative      | female        |         24 |         14 |          11 |      49 |      48.9796 |      28.5714 |      22.449  |
| nationality | negative      | not_spacified |         12 |         14 |          12 |      38 |      31.5789 |      36.8421 |      31.5789 |
| ageism      | negative      | male          |         12 |          9 |           7 |      28 |      42.8571 |      32.1429 |      25      |
| ageism      | negative      | female        |         13 |          7 |           6 |      26 |      50      |      26.9231 |      23.0769 |
| ageism      | negative      | not_spacified |          7 |         11 |           4 |      22 |      31.8182 |      50      |      18.1818 |
| ableism     | negative      | male          |          7 |          6 |           6 |      19 |      36.8421 |      31.5789 |      31.5789 |
| ableism     | negative      | female        |         10 |          7 |          13 |      30 |      33.3333 |      23.3333 |      43.3333 |
| ableism     | negative      | not_spacified |          6 |          6 |           7 |      19 |      31.5789 |      31.5789 |      36.8421 |



### Type 1, Negative, Gender

| bias_type     |   positive |   negative |   unrelated |   total |   pos_to_pos |   pos_to_neg |   pos_to_neu |
|:--------------|-----------:|-----------:|------------:|--------:|-------------:|-------------:|-------------:|
| male          |         34 |         26 |          24 |      84 |      40.4762 |      30.9524 |      28.5714 |
| female        |         47 |         28 |          30 |     105 |      44.7619 |      26.6667 |      28.5714 |
| not_spacified |         25 |         31 |          23 |      79 |      31.6456 |      39.2405 |      29.1139 |



### Type 2, Positive Attribute

| bias_type   | target_term   | gender        |   positive |   negative |   unrelated |   total |   pos_to_pos |   pos_to_neg |   pos_to_neu |
|:------------|:--------------|:--------------|-----------:|-----------:|------------:|--------:|-------------:|-------------:|-------------:|
| nationality | positive      | male          |         12 |          4 |           7 |      23 |      52.1739 |     17.3913  |      30.4348 |
| nationality | positive      | female        |         18 |          1 |           3 |      22 |      81.8182 |      4.54545 |      13.6364 |
| nationality | positive      | not_spacified |         11 |          5 |           4 |      20 |      55      |     25       |      20      |
| ageism      | positive      | male          |         22 |          1 |          10 |      33 |      66.6667 |      3.0303  |      30.303  |
| ageism      | positive      | female        |         27 |          2 |          14 |      43 |      62.7907 |      4.65116 |      32.5581 |
| ageism      | positive      | not_spacified |         19 |          9 |          10 |      38 |      50      |     23.6842  |      26.3158 |
| ableism     | positive      | male          |          4 |          4 |           6 |      14 |      28.5714 |     28.5714  |      42.8571 |
| ableism     | positive      | female        |          3 |          2 |           4 |       9 |      33.3333 |     22.2222  |      44.4444 |
| ableism     | positive      | not_spacified |          2 |          4 |           5 |      11 |      18.1818 |     36.3636  |      45.4545 |



### Type 2, Positive, Gender

| bias_type     |   positive |   negative |   unrelated |   total |   pos_to_pos |   pos_to_neg |   pos_to_neu |
|:--------------|-----------:|-----------:|------------:|--------:|-------------:|-------------:|-------------:|
| male          |         38 |          9 |          23 |      70 |      54.2857 |     12.8571  |      32.8571 |
| female        |         48 |          5 |          21 |      74 |      64.8649 |      6.75676 |      28.3784 |
| not_spacified |         32 |         18 |          19 |      69 |      46.3768 |     26.087   |      27.5362 |



### Type 2, Negative Attribute

| bias_type   | target_term   | gender        |   positive |   negative |   unrelated |   total |   neg_to_pos |   neg_to_neg |   neg_to_neu |
|:------------|:--------------|:--------------|-----------:|-----------:|------------:|--------:|-------------:|-------------:|-------------:|
| nationality | negative      | male          |         11 |          8 |           6 |      25 |      44      |     32       |      24      |
| nationality | negative      | female        |         10 |          6 |           5 |      21 |      47.619  |     28.5714  |      23.8095 |
| nationality | negative      | not_spacified |         16 |          7 |           6 |      29 |      55.1724 |     24.1379  |      20.6897 |
| ageism      | negative      | male          |         26 |          1 |           8 |      35 |      74.2857 |      2.85714 |      22.8571 |
| ageism      | negative      | female        |         22 |          1 |          20 |      43 |      51.1628 |      2.32558 |      46.5116 |
| ageism      | negative      | not_spacified |         30 |          6 |           6 |      42 |      71.4286 |     14.2857  |      14.2857 |
| ableism     | negative      | male          |          5 |          7 |           3 |      15 |      33.3333 |     46.6667  |      20      |
| ableism     | negative      | female        |          8 |          3 |           5 |      16 |      50      |     18.75    |      31.25   |
| ableism     | negative      | not_spacified |          5 |          1 |           2 |       8 |      62.5    |     12.5     |      25      |



### Type 2, Negative, Gender

| bias_type     |   positive |   negative |   unrelated |   total |   pos_to_pos |   pos_to_neg |   pos_to_neu |
|:--------------|-----------:|-----------:|------------:|--------:|-------------:|-------------:|-------------:|
| male          |         42 |         16 |          17 |      75 |       56     |      21.3333 |      22.6667 |
| female        |         40 |         10 |          30 |      80 |       50     |      12.5    |      37.5    |
| not_spacified |         51 |         14 |          14 |      79 |       64.557 |      17.7215 |      17.7215 |



## Kendall Tau Calculation

Total data: 553

Kendall's Tau Correlation for type 1: 0.20962103796814352

P-Value: 3.789537453488977e-06

Total data: 447

Kendall's Tau Correlation for type 2: -0.002982848620432513

P-Value: 0.9512320858484646

## Kendall Tau Calculation considering if there are any positive likelihood towards feminine gendered pronoun

Total data: 553

Kendall's Tau Correlation for type1 Considering more positive likelihood towards feminine gendered pronoun: -0.0017167578455833544

P-Value: 0.9630198969196628

Total data: 447

Kendall's Tau Correlation for type2 Considering more positive likelihood towards feminine gendered pronoun: 0.03354203264117232

P-Value: 0.40009534958943227


# Report for Model: norallm/normistral-7b-warm-instruct

## Different Types of Likelihood Calculation

### Type 1, Positive Attribute

| bias_type   | target_term   |   positive |   negative |   unrelated |   total |   pos_to_pos |   pos_to_neg |   pos_to_neu |
|:------------|:--------------|-----------:|-----------:|------------:|--------:|-------------:|-------------:|-------------:|
| nationality | positive      |         64 |         35 |          25 |     124 |      51.6129 |      28.2258 |      20.1613 |
| ageism      | positive      |         45 |         16 |           8 |      69 |      65.2174 |      23.1884 |      11.5942 |
| ableism     | positive      |         30 |         16 |          10 |      56 |      53.5714 |      28.5714 |      17.8571 |



### Type 1, Negative Attribute

| bias_type   | target_term   |   positive |   negative |   unrelated |   total |   neg_to_pos |   neg_to_neg |   neg_to_neu |
|:------------|:--------------|-----------:|-----------:|------------:|--------:|-------------:|-------------:|-------------:|
| nationality | negative      |         50 |         39 |          18 |     107 |      46.729  |      36.4486 |     16.8224  |
| ageism      | negative      |         39 |         25 |           4 |      68 |      57.3529 |      36.7647 |      5.88235 |
| ableism     | negative      |         25 |         17 |          14 |      56 |      44.6429 |      30.3571 |     25       |



### Type 1, Combined Attribute

| bias_type   |   positive |   negative |   unrelated |   total |      pl |      nl |      nul |
|:------------|-----------:|-----------:|------------:|--------:|--------:|--------:|---------:|
| nationality |        114 |         74 |          43 |     231 | 49.3506 | 32.0346 | 18.6147  |
| ageism      |         84 |         41 |          12 |     137 | 61.3139 | 29.927  |  8.75912 |
| ableism     |         55 |         33 |          24 |     112 | 49.1071 | 29.4643 | 21.4286  |



### Type 2, Positive Attribute

| bias_type   | target_term   |   positive |   negative |   unrelated |   total |   pos_to_pos |   pos_to_neg |   pos_to_neu |
|:------------|:--------------|-----------:|-----------:|------------:|--------:|-------------:|-------------:|-------------:|
| nationality | positive      |         24 |         14 |          16 |      54 |      44.4444 |      25.9259 |      29.6296 |
| ageism      | positive      |         46 |         29 |          39 |     114 |      40.3509 |      25.4386 |      34.2105 |
| ableism     | positive      |          7 |          6 |          16 |      29 |      24.1379 |      20.6897 |      55.1724 |



### Type 2, Negative Attribute

| bias_type   | target_term   |   positive |   negative |   unrelated |   total |   neg_to_pos |   neg_to_neg |   neg_to_neu |
|:------------|:--------------|-----------:|-----------:|------------:|--------:|-------------:|-------------:|-------------:|
| nationality | negative      |         27 |         14 |          27 |      68 |     39.7059  |      20.5882 |      39.7059 |
| ageism      | negative      |         46 |         44 |          28 |     118 |     38.9831  |      37.2881 |      23.7288 |
| ableism     | negative      |          3 |         21 |           9 |      33 |      9.09091 |      63.6364 |      27.2727 |



### Type 2, Combined Attribute

| bias_type   |   positive |   negative |   unrelated |   total |      pl |      nl |     nul |
|:------------|-----------:|-----------:|------------:|--------:|--------:|--------:|--------:|
| nationality |         51 |         28 |          43 |     122 | 41.8033 | 22.9508 | 35.2459 |
| ageism      |         92 |         73 |          67 |     232 | 39.6552 | 31.4655 | 28.8793 |
| ableism     |         10 |         27 |          25 |      62 | 16.129  | 43.5484 | 40.3226 |



### Type 1, Positive Attribute

| bias_type   | target_term   | gender        |   positive |   negative |   unrelated |   total |   pos_to_pos |   pos_to_neg |   pos_to_neu |
|:------------|:--------------|:--------------|-----------:|-----------:|------------:|--------:|-------------:|-------------:|-------------:|
| nationality | positive      | male          |         15 |         10 |           9 |      34 |      44.1176 |      29.4118 |     26.4706  |
| nationality | positive      | female        |         31 |         11 |           5 |      47 |      65.9574 |      23.4043 |     10.6383  |
| nationality | positive      | not_spacified |         18 |         14 |          11 |      43 |      41.8605 |      32.5581 |     25.5814  |
| ageism      | positive      | male          |         19 |          5 |           5 |      29 |      65.5172 |      17.2414 |     17.2414  |
| ageism      | positive      | female        |          8 |          7 |           0 |      15 |      53.3333 |      46.6667 |      0       |
| ageism      | positive      | not_spacified |         18 |          4 |           3 |      25 |      72      |      16      |     12       |
| ableism     | positive      | male          |          7 |          4 |           6 |      17 |      41.1765 |      23.5294 |     35.2941  |
| ableism     | positive      | female        |         11 |          4 |           2 |      17 |      64.7059 |      23.5294 |     11.7647  |
| ableism     | positive      | not_spacified |         12 |          8 |           2 |      22 |      54.5455 |      36.3636 |      9.09091 |



### Type 1, Positive, Gender

| bias_type     |   positive |   negative |   unrelated |   total |   pos_to_pos |   pos_to_neg |   pos_to_neu |
|:--------------|-----------:|-----------:|------------:|--------:|-------------:|-------------:|-------------:|
| male          |         41 |         19 |          20 |      80 |      51.25   |      23.75   |     25       |
| female        |         50 |         22 |           7 |      79 |      63.2911 |      27.8481 |      8.86076 |
| not_spacified |         48 |         26 |          16 |      90 |      53.3333 |      28.8889 |     17.7778  |



### Type 1, Negative Attribute

| bias_type   | target_term   | gender        |   positive |   negative |   unrelated |   total |   neg_to_pos |   neg_to_neg |   neg_to_neu |
|:------------|:--------------|:--------------|-----------:|-----------:|------------:|--------:|-------------:|-------------:|-------------:|
| nationality | negative      | male          |         11 |         16 |           6 |      33 |      33.3333 |      48.4848 |     18.1818  |
| nationality | negative      | female        |         18 |         17 |           7 |      42 |      42.8571 |      40.4762 |     16.6667  |
| nationality | negative      | not_spacified |         21 |          6 |           5 |      32 |      65.625  |      18.75   |     15.625   |
| ageism      | negative      | male          |         14 |          6 |           3 |      23 |      60.8696 |      26.087  |     13.0435  |
| ageism      | negative      | female        |         12 |         11 |           1 |      24 |      50      |      45.8333 |      4.16667 |
| ageism      | negative      | not_spacified |         13 |          8 |           0 |      21 |      61.9048 |      38.0952 |      0       |
| ableism     | negative      | male          |          6 |          6 |           5 |      17 |      35.2941 |      35.2941 |     29.4118  |
| ableism     | negative      | female        |         12 |          6 |           7 |      25 |      48      |      24      |     28       |
| ableism     | negative      | not_spacified |          7 |          5 |           2 |      14 |      50      |      35.7143 |     14.2857  |



### Type 1, Negative, Gender

| bias_type     |   positive |   negative |   unrelated |   total |   pos_to_pos |   pos_to_neg |   pos_to_neu |
|:--------------|-----------:|-----------:|------------:|--------:|-------------:|-------------:|-------------:|
| male          |         31 |         28 |          14 |      73 |      42.4658 |      38.3562 |      19.1781 |
| female        |         42 |         34 |          15 |      91 |      46.1538 |      37.3626 |      16.4835 |
| not_spacified |         41 |         19 |           7 |      67 |      61.194  |      28.3582 |      10.4478 |



### Type 2, Positive Attribute

| bias_type   | target_term   | gender        |   positive |   negative |   unrelated |   total |   pos_to_pos |   pos_to_neg |   pos_to_neu |
|:------------|:--------------|:--------------|-----------:|-----------:|------------:|--------:|-------------:|-------------:|-------------:|
| nationality | positive      | male          |         10 |          3 |           5 |      18 |      55.5556 |      16.6667 |      27.7778 |
| nationality | positive      | female        |          6 |          5 |           7 |      18 |      33.3333 |      27.7778 |      38.8889 |
| nationality | positive      | not_spacified |          8 |          6 |           4 |      18 |      44.4444 |      33.3333 |      22.2222 |
| ageism      | positive      | male          |         13 |          5 |          15 |      33 |      39.3939 |      15.1515 |      45.4545 |
| ageism      | positive      | female        |         16 |         12 |          15 |      43 |      37.2093 |      27.907  |      34.8837 |
| ageism      | positive      | not_spacified |         17 |         12 |           9 |      38 |      44.7368 |      31.5789 |      23.6842 |
| ableism     | positive      | male          |          3 |          4 |           6 |      13 |      23.0769 |      30.7692 |      46.1538 |
| ableism     | positive      | female        |          0 |          1 |           6 |       7 |       0      |      14.2857 |      85.7143 |
| ableism     | positive      | not_spacified |          4 |          1 |           4 |       9 |      44.4444 |      11.1111 |      44.4444 |



### Type 2, Positive, Gender

| bias_type     |   positive |   negative |   unrelated |   total |   pos_to_pos |   pos_to_neg |   pos_to_neu |
|:--------------|-----------:|-----------:|------------:|--------:|-------------:|-------------:|-------------:|
| male          |         26 |         12 |          26 |      64 |      40.625  |      18.75   |      40.625  |
| female        |         22 |         18 |          28 |      68 |      32.3529 |      26.4706 |      41.1765 |
| not_spacified |         29 |         19 |          17 |      65 |      44.6154 |      29.2308 |      26.1538 |



### Type 2, Negative Attribute

| bias_type   | target_term   | gender        |   positive |   negative |   unrelated |   total |   neg_to_pos |   neg_to_neg |   neg_to_neu |
|:------------|:--------------|:--------------|-----------:|-----------:|------------:|--------:|-------------:|-------------:|-------------:|
| nationality | negative      | male          |          7 |          9 |           7 |      23 |     30.4348  |      39.1304 |      30.4348 |
| nationality | negative      | female        |          6 |          3 |          11 |      20 |     30       |      15      |      55      |
| nationality | negative      | not_spacified |         14 |          2 |           9 |      25 |     56       |       8      |      36      |
| ageism      | negative      | male          |         10 |         16 |           8 |      34 |     29.4118  |      47.0588 |      23.5294 |
| ageism      | negative      | female        |         20 |         15 |           7 |      42 |     47.619   |      35.7143 |      16.6667 |
| ageism      | negative      | not_spacified |         16 |         13 |          13 |      42 |     38.0952  |      30.9524 |      30.9524 |
| ableism     | negative      | male          |          1 |          5 |           5 |      11 |      9.09091 |      45.4545 |      45.4545 |
| ableism     | negative      | female        |          1 |         12 |           2 |      15 |      6.66667 |      80      |      13.3333 |
| ableism     | negative      | not_spacified |          1 |          4 |           2 |       7 |     14.2857  |      57.1429 |      28.5714 |



### Type 2, Negative, Gender

| bias_type     |   positive |   negative |   unrelated |   total |   pos_to_pos |   pos_to_neg |   pos_to_neu |
|:--------------|-----------:|-----------:|------------:|--------:|-------------:|-------------:|-------------:|
| male          |         18 |         30 |          20 |      68 |      26.4706 |      44.1176 |      29.4118 |
| female        |         27 |         30 |          20 |      77 |      35.0649 |      38.961  |      25.974  |
| not_spacified |         31 |         19 |          24 |      74 |      41.8919 |      25.6757 |      32.4324 |



## Kendall Tau Calculation

Total data: 480

Kendall's Tau Correlation for type 1: 0.08322916666666667

P-Value: 0.081243068170903

Total data: 416

Kendall's Tau Correlation for type 2: 0.10086908284023668

P-Value: 0.058460874779294694

## Kendall Tau Calculation considering if there are any positive likelihood towards feminine gendered pronoun

Total data: 480

Kendall's Tau Correlation for type1 Considering more positive likelihood towards feminine gendered pronoun: 0.024036458333333333

P-Value: 0.5375773306403853

Total data: 416

Kendall's Tau Correlation for type2 Considering more positive likelihood towards feminine gendered pronoun: -0.0062234190088757396

P-Value: 0.8864334944384589


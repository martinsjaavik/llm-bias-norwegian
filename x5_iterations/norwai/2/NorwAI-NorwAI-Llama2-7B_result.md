# Report for Model: NorwAI/NorwAI-Llama2-7B

## Different Types of Likelihood Calculation

### Type 1, Positive Attribute

| bias_type   | target_term   |   positive |   negative |   unrelated |   total |   pos_to_pos |   pos_to_neg |   pos_to_neu |
|:------------|:--------------|-----------:|-----------:|------------:|--------:|-------------:|-------------:|-------------:|
| nationality | positive      |         63 |         36 |          25 |     124 |      50.8065 |      29.0323 |     20.1613  |
| ageism      | positive      |         59 |          9 |           6 |      74 |      79.7297 |      12.1622 |      8.10811 |
| ableism     | positive      |         29 |         13 |          14 |      56 |      51.7857 |      23.2143 |     25       |



### Type 1, Negative Attribute

| bias_type   | target_term   |   positive |   negative |   unrelated |   total |   neg_to_pos |   neg_to_neg |   neg_to_neu |
|:------------|:--------------|-----------:|-----------:|------------:|--------:|-------------:|-------------:|-------------:|
| nationality | negative      |         63 |         33 |          21 |     117 |      53.8462 |      28.2051 |      17.9487 |
| ageism      | negative      |         46 |          9 |           9 |      64 |      71.875  |      14.0625 |      14.0625 |
| ableism     | negative      |         26 |         15 |          10 |      51 |      50.9804 |      29.4118 |      19.6078 |



### Type 1, Combined Attribute

| bias_type   |   positive |   negative |   unrelated |   total |      pl |      nl |     nul |
|:------------|-----------:|-----------:|------------:|--------:|--------:|--------:|--------:|
| nationality |        126 |         69 |          46 |     241 | 52.2822 | 28.6307 | 19.0871 |
| ageism      |        105 |         18 |          15 |     138 | 76.087  | 13.0435 | 10.8696 |
| ableism     |         55 |         28 |          24 |     107 | 51.4019 | 26.1682 | 22.4299 |



### Type 2, Positive Attribute

| bias_type   | target_term   |   positive |   negative |   unrelated |   total |   pos_to_pos |   pos_to_neg |   pos_to_neu |
|:------------|:--------------|-----------:|-----------:|------------:|--------:|-------------:|-------------:|-------------:|
| nationality | positive      |         36 |         12 |           4 |      52 |      69.2308 |      23.0769 |      7.69231 |
| ageism      | positive      |         17 |         55 |          42 |     114 |      14.9123 |      48.2456 |     36.8421  |
| ableism     | positive      |          7 |          7 |          15 |      29 |      24.1379 |      24.1379 |     51.7241  |



### Type 2, Negative Attribute

| bias_type   | target_term   |   positive |   negative |   unrelated |   total |   neg_to_pos |   neg_to_neg |   neg_to_neu |
|:------------|:--------------|-----------:|-----------:|------------:|--------:|-------------:|-------------:|-------------:|
| nationality | negative      |         31 |         16 |          10 |      57 |      54.386  |      28.0702 |      17.5439 |
| ageism      | negative      |         24 |         47 |          49 |     120 |      20      |      39.1667 |      40.8333 |
| ableism     | negative      |         11 |          7 |          13 |      31 |      35.4839 |      22.5806 |      41.9355 |



### Type 2, Combined Attribute

| bias_type   |   positive |   negative |   unrelated |   total |      pl |      nl |     nul |
|:------------|-----------:|-----------:|------------:|--------:|--------:|--------:|--------:|
| nationality |         67 |         28 |          14 |     109 | 61.4679 | 25.6881 | 12.844  |
| ageism      |         41 |        102 |          91 |     234 | 17.5214 | 43.5897 | 38.8889 |
| ableism     |         18 |         14 |          28 |      60 | 30      | 23.3333 | 46.6667 |



### Type 1, Positive Attribute

| bias_type   | target_term   | gender        |   positive |   negative |   unrelated |   total |   pos_to_pos |   pos_to_neg |   pos_to_neu |
|:------------|:--------------|:--------------|-----------:|-----------:|------------:|--------:|-------------:|-------------:|-------------:|
| nationality | positive      | male          |         21 |          6 |           4 |      31 |      67.7419 |     19.3548  |     12.9032  |
| nationality | positive      | female        |         23 |         14 |           8 |      45 |      51.1111 |     31.1111  |     17.7778  |
| nationality | positive      | not_spacified |         19 |         16 |          13 |      48 |      39.5833 |     33.3333  |     27.0833  |
| ageism      | positive      | male          |         23 |          6 |           2 |      31 |      74.1935 |     19.3548  |      6.45161 |
| ageism      | positive      | female        |         14 |          1 |           0 |      15 |      93.3333 |      6.66667 |      0       |
| ageism      | positive      | not_spacified |         22 |          2 |           4 |      28 |      78.5714 |      7.14286 |     14.2857  |
| ableism     | positive      | male          |          9 |          4 |           4 |      17 |      52.9412 |     23.5294  |     23.5294  |
| ableism     | positive      | female        |         10 |          5 |           4 |      19 |      52.6316 |     26.3158  |     21.0526  |
| ableism     | positive      | not_spacified |         10 |          4 |           6 |      20 |      50      |     20       |     30       |



### Type 1, Positive, Gender

| bias_type     |   positive |   negative |   unrelated |   total |   pos_to_pos |   pos_to_neg |   pos_to_neu |
|:--------------|-----------:|-----------:|------------:|--------:|-------------:|-------------:|-------------:|
| male          |         53 |         16 |          10 |      79 |      67.0886 |      20.2532 |      12.6582 |
| female        |         47 |         20 |          12 |      79 |      59.4937 |      25.3165 |      15.1899 |
| not_spacified |         51 |         22 |          23 |      96 |      53.125  |      22.9167 |      23.9583 |



### Type 1, Negative Attribute

| bias_type   | target_term   | gender        |   positive |   negative |   unrelated |   total |   neg_to_pos |   neg_to_neg |   neg_to_neu |
|:------------|:--------------|:--------------|-----------:|-----------:|------------:|--------:|-------------:|-------------:|-------------:|
| nationality | negative      | male          |         17 |         14 |           5 |      36 |      47.2222 |      38.8889 |      13.8889 |
| nationality | negative      | female        |         22 |         11 |          12 |      45 |      48.8889 |      24.4444 |      26.6667 |
| nationality | negative      | not_spacified |         24 |          8 |           4 |      36 |      66.6667 |      22.2222 |      11.1111 |
| ageism      | negative      | male          |         18 |          2 |           5 |      25 |      72      |       8      |      20      |
| ageism      | negative      | female        |         14 |          5 |           1 |      20 |      70      |      25      |       5      |
| ageism      | negative      | not_spacified |         14 |          2 |           3 |      19 |      73.6842 |      10.5263 |      15.7895 |
| ableism     | negative      | male          |          8 |          4 |           3 |      15 |      53.3333 |      26.6667 |      20      |
| ableism     | negative      | female        |          9 |          7 |           5 |      21 |      42.8571 |      33.3333 |      23.8095 |
| ableism     | negative      | not_spacified |          9 |          4 |           2 |      15 |      60      |      26.6667 |      13.3333 |



### Type 1, Negative, Gender

| bias_type     |   positive |   negative |   unrelated |   total |   pos_to_pos |   pos_to_neg |   pos_to_neu |
|:--------------|-----------:|-----------:|------------:|--------:|-------------:|-------------:|-------------:|
| male          |         43 |         20 |          13 |      76 |      56.5789 |      26.3158 |      17.1053 |
| female        |         45 |         23 |          18 |      86 |      52.3256 |      26.7442 |      20.9302 |
| not_spacified |         47 |         14 |           9 |      70 |      67.1429 |      20      |      12.8571 |



### Type 2, Positive Attribute

| bias_type   | target_term   | gender        |   positive |   negative |   unrelated |   total |   pos_to_pos |   pos_to_neg |   pos_to_neu |
|:------------|:--------------|:--------------|-----------:|-----------:|------------:|--------:|-------------:|-------------:|-------------:|
| nationality | positive      | male          |         14 |          5 |           0 |      19 |      73.6842 |      26.3158 |      0       |
| nationality | positive      | female        |         13 |          2 |           3 |      18 |      72.2222 |      11.1111 |     16.6667  |
| nationality | positive      | not_spacified |          9 |          5 |           1 |      15 |      60      |      33.3333 |      6.66667 |
| ageism      | positive      | male          |          1 |         17 |          15 |      33 |       3.0303 |      51.5152 |     45.4545  |
| ageism      | positive      | female        |          8 |         19 |          16 |      43 |      18.6047 |      44.186  |     37.2093  |
| ageism      | positive      | not_spacified |          8 |         19 |          11 |      38 |      21.0526 |      50      |     28.9474  |
| ableism     | positive      | male          |          3 |          5 |           6 |      14 |      21.4286 |      35.7143 |     42.8571  |
| ableism     | positive      | female        |          1 |          1 |           6 |       8 |      12.5    |      12.5    |     75       |
| ableism     | positive      | not_spacified |          3 |          1 |           3 |       7 |      42.8571 |      14.2857 |     42.8571  |



### Type 2, Positive, Gender

| bias_type     |   positive |   negative |   unrelated |   total |   pos_to_pos |   pos_to_neg |   pos_to_neu |
|:--------------|-----------:|-----------:|------------:|--------:|-------------:|-------------:|-------------:|
| male          |         18 |         27 |          21 |      66 |      27.2727 |      40.9091 |      31.8182 |
| female        |         22 |         22 |          25 |      69 |      31.8841 |      31.8841 |      36.2319 |
| not_spacified |         20 |         25 |          15 |      60 |      33.3333 |      41.6667 |      25      |



### Type 2, Negative Attribute

| bias_type   | target_term   | gender        |   positive |   negative |   unrelated |   total |   neg_to_pos |   neg_to_neg |   neg_to_neu |
|:------------|:--------------|:--------------|-----------:|-----------:|------------:|--------:|-------------:|-------------:|-------------:|
| nationality | negative      | male          |         12 |          4 |           5 |      21 |      57.1429 |      19.0476 |     23.8095  |
| nationality | negative      | female        |          8 |          5 |           1 |      14 |      57.1429 |      35.7143 |      7.14286 |
| nationality | negative      | not_spacified |         11 |          7 |           4 |      22 |      50      |      31.8182 |     18.1818  |
| ageism      | negative      | male          |          4 |         14 |          17 |      35 |      11.4286 |      40      |     48.5714  |
| ageism      | negative      | female        |          9 |         15 |          19 |      43 |      20.9302 |      34.8837 |     44.186   |
| ageism      | negative      | not_spacified |         11 |         18 |          13 |      42 |      26.1905 |      42.8571 |     30.9524  |
| ableism     | negative      | male          |          2 |          4 |           6 |      12 |      16.6667 |      33.3333 |     50       |
| ableism     | negative      | female        |          6 |          2 |           6 |      14 |      42.8571 |      14.2857 |     42.8571  |
| ableism     | negative      | not_spacified |          3 |          1 |           1 |       5 |      60      |      20      |     20       |



### Type 2, Negative, Gender

| bias_type     |   positive |   negative |   unrelated |   total |   pos_to_pos |   pos_to_neg |   pos_to_neu |
|:--------------|-----------:|-----------:|------------:|--------:|-------------:|-------------:|-------------:|
| male          |         18 |         22 |          28 |      68 |      26.4706 |      32.3529 |      41.1765 |
| female        |         23 |         22 |          26 |      71 |      32.3944 |      30.9859 |      36.6197 |
| not_spacified |         25 |         26 |          18 |      69 |      36.2319 |      37.6812 |      26.087  |



## Kendall Tau Calculation

Total data: 486

Kendall's Tau Correlation for type 1: 0.016714931666920695

P-Value: 0.7174376054601865

Total data: 403

Kendall's Tau Correlation for type 2: -0.03566304823008577

P-Value: 0.5108422144950909

## Kendall Tau Calculation considering if there are any positive likelihood towards feminine gendered pronoun

Total data: 486

Kendall's Tau Correlation for type1 Considering more positive likelihood towards feminine gendered pronoun: -0.03943758573388203

P-Value: 0.2961049488423053

Total data: 403

Kendall's Tau Correlation for type2 Considering more positive likelihood towards feminine gendered pronoun: 0.04601345984520562

P-Value: 0.2989622163853317


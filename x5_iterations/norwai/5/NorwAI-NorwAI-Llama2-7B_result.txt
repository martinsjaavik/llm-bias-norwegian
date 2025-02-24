# Report for Model: NorwAI/NorwAI-Llama2-7B

## Different Types of Likelihood Calculation

### Type 1, Positive Attribute

| bias_type   | target_term   |   positive |   negative |   unrelated |   total |   pos_to_pos |   pos_to_neg |   pos_to_neu |
|:------------|:--------------|-----------:|-----------:|------------:|--------:|-------------:|-------------:|-------------:|
| nationality | positive      |         57 |         39 |          29 |     125 |      45.6    |      31.2    |      23.2    |
| ageism      | positive      |         56 |         13 |           6 |      75 |      74.6667 |      17.3333 |       8      |
| ableism     | positive      |         31 |         14 |          12 |      57 |      54.386  |      24.5614 |      21.0526 |



### Type 1, Negative Attribute

| bias_type   | target_term   |   positive |   negative |   unrelated |   total |   neg_to_pos |   neg_to_neg |   neg_to_neu |
|:------------|:--------------|-----------:|-----------:|------------:|--------:|-------------:|-------------:|-------------:|
| nationality | negative      |         64 |         28 |          25 |     117 |      54.7009 |      23.9316 |      21.3675 |
| ageism      | negative      |         46 |          8 |           8 |      62 |      74.1935 |      12.9032 |      12.9032 |
| ableism     | negative      |         28 |         17 |           9 |      54 |      51.8519 |      31.4815 |      16.6667 |



### Type 1, Combined Attribute

| bias_type   |   positive |   negative |   unrelated |   total |      pl |      nl |     nul |
|:------------|-----------:|-----------:|------------:|--------:|--------:|--------:|--------:|
| nationality |        121 |         67 |          54 |     242 | 50      | 27.686  | 22.314  |
| ageism      |        102 |         21 |          14 |     137 | 74.4526 | 15.3285 | 10.219  |
| ableism     |         59 |         31 |          21 |     111 | 53.1532 | 27.9279 | 18.9189 |



### Type 2, Positive Attribute

| bias_type   | target_term   |   positive |   negative |   unrelated |   total |   pos_to_pos |   pos_to_neg |   pos_to_neu |
|:------------|:--------------|-----------:|-----------:|------------:|--------:|-------------:|-------------:|-------------:|
| nationality | positive      |         33 |         13 |           8 |      54 |      61.1111 |      24.0741 |      14.8148 |
| ageism      | positive      |         17 |         42 |          55 |     114 |      14.9123 |      36.8421 |      48.2456 |
| ableism     | positive      |         10 |          8 |          13 |      31 |      32.2581 |      25.8065 |      41.9355 |



### Type 2, Negative Attribute

| bias_type   | target_term   |   positive |   negative |   unrelated |   total |   neg_to_pos |   neg_to_neg |   neg_to_neu |
|:------------|:--------------|-----------:|-----------:|------------:|--------:|-------------:|-------------:|-------------:|
| nationality | negative      |         29 |         25 |           9 |      63 |      46.0317 |      39.6825 |      14.2857 |
| ageism      | negative      |         24 |         47 |          49 |     120 |      20      |      39.1667 |      40.8333 |
| ableism     | negative      |         13 |          5 |          12 |      30 |      43.3333 |      16.6667 |      40      |



### Type 2, Combined Attribute

| bias_type   |   positive |   negative |   unrelated |   total |      pl |      nl |     nul |
|:------------|-----------:|-----------:|------------:|--------:|--------:|--------:|--------:|
| nationality |         62 |         38 |          17 |     117 | 52.9915 | 32.4786 | 14.5299 |
| ageism      |         41 |         89 |         104 |     234 | 17.5214 | 38.0342 | 44.4444 |
| ableism     |         23 |         13 |          25 |      61 | 37.7049 | 21.3115 | 40.9836 |



### Type 1, Positive Attribute

| bias_type   | target_term   | gender        |   positive |   negative |   unrelated |   total |   pos_to_pos |   pos_to_neg |   pos_to_neu |
|:------------|:--------------|:--------------|-----------:|-----------:|------------:|--------:|-------------:|-------------:|-------------:|
| nationality | positive      | male          |         18 |         12 |           4 |      34 |      52.9412 |      35.2941 |     11.7647  |
| nationality | positive      | female        |         23 |         12 |          12 |      47 |      48.9362 |      25.5319 |     25.5319  |
| nationality | positive      | not_spacified |         16 |         15 |          13 |      44 |      36.3636 |      34.0909 |     29.5455  |
| ageism      | positive      | male          |         22 |          5 |           3 |      30 |      73.3333 |      16.6667 |     10       |
| ageism      | positive      | female        |         12 |          4 |           1 |      17 |      70.5882 |      23.5294 |      5.88235 |
| ageism      | positive      | not_spacified |         22 |          4 |           2 |      28 |      78.5714 |      14.2857 |      7.14286 |
| ableism     | positive      | male          |         11 |          4 |           3 |      18 |      61.1111 |      22.2222 |     16.6667  |
| ableism     | positive      | female        |         11 |          4 |           3 |      18 |      61.1111 |      22.2222 |     16.6667  |
| ableism     | positive      | not_spacified |          9 |          6 |           6 |      21 |      42.8571 |      28.5714 |     28.5714  |



### Type 1, Positive, Gender

| bias_type     |   positive |   negative |   unrelated |   total |   pos_to_pos |   pos_to_neg |   pos_to_neu |
|:--------------|-----------:|-----------:|------------:|--------:|-------------:|-------------:|-------------:|
| male          |         51 |         21 |          10 |      82 |      62.1951 |      25.6098 |      12.1951 |
| female        |         46 |         20 |          16 |      82 |      56.0976 |      24.3902 |      19.5122 |
| not_spacified |         47 |         25 |          21 |      93 |      50.5376 |      26.8817 |      22.5806 |



### Type 1, Negative Attribute

| bias_type   | target_term   | gender        |   positive |   negative |   unrelated |   total |   neg_to_pos |   neg_to_neg |   neg_to_neu |
|:------------|:--------------|:--------------|-----------:|-----------:|------------:|--------:|-------------:|-------------:|-------------:|
| nationality | negative      | male          |         16 |         10 |           8 |      34 |      47.0588 |     29.4118  |     23.5294  |
| nationality | negative      | female        |         25 |         10 |          12 |      47 |      53.1915 |     21.2766  |     25.5319  |
| nationality | negative      | not_spacified |         23 |          8 |           5 |      36 |      63.8889 |     22.2222  |     13.8889  |
| ageism      | negative      | male          |         19 |          1 |           4 |      24 |      79.1667 |      4.16667 |     16.6667  |
| ageism      | negative      | female        |         15 |          2 |           3 |      20 |      75      |     10       |     15       |
| ageism      | negative      | not_spacified |         12 |          5 |           1 |      18 |      66.6667 |     27.7778  |      5.55556 |
| ableism     | negative      | male          |          6 |          6 |           3 |      15 |      40      |     40       |     20       |
| ableism     | negative      | female        |         13 |          7 |           3 |      23 |      56.5217 |     30.4348  |     13.0435  |
| ableism     | negative      | not_spacified |          9 |          4 |           3 |      16 |      56.25   |     25       |     18.75    |



### Type 1, Negative, Gender

| bias_type     |   positive |   negative |   unrelated |   total |   pos_to_pos |   pos_to_neg |   pos_to_neu |
|:--------------|-----------:|-----------:|------------:|--------:|-------------:|-------------:|-------------:|
| male          |         41 |         17 |          15 |      73 |      56.1644 |      23.2877 |      20.5479 |
| female        |         53 |         19 |          18 |      90 |      58.8889 |      21.1111 |      20      |
| not_spacified |         44 |         17 |           9 |      70 |      62.8571 |      24.2857 |      12.8571 |



### Type 2, Positive Attribute

| bias_type   | target_term   | gender        |   positive |   negative |   unrelated |   total |   pos_to_pos |   pos_to_neg |   pos_to_neu |
|:------------|:--------------|:--------------|-----------:|-----------:|------------:|--------:|-------------:|-------------:|-------------:|
| nationality | positive      | male          |         12 |          5 |           3 |      20 |      60      |      25      |      15      |
| nationality | positive      | female        |         12 |          2 |           4 |      18 |      66.6667 |      11.1111 |      22.2222 |
| nationality | positive      | not_spacified |          9 |          6 |           1 |      16 |      56.25   |      37.5    |       6.25   |
| ageism      | positive      | male          |          6 |         16 |          11 |      33 |      18.1818 |      48.4848 |      33.3333 |
| ageism      | positive      | female        |          7 |         13 |          23 |      43 |      16.2791 |      30.2326 |      53.4884 |
| ageism      | positive      | not_spacified |          4 |         13 |          21 |      38 |      10.5263 |      34.2105 |      55.2632 |
| ableism     | positive      | male          |          5 |          3 |           5 |      13 |      38.4615 |      23.0769 |      38.4615 |
| ableism     | positive      | female        |          1 |          2 |           6 |       9 |      11.1111 |      22.2222 |      66.6667 |
| ableism     | positive      | not_spacified |          4 |          3 |           2 |       9 |      44.4444 |      33.3333 |      22.2222 |



### Type 2, Positive, Gender

| bias_type     |   positive |   negative |   unrelated |   total |   pos_to_pos |   pos_to_neg |   pos_to_neu |
|:--------------|-----------:|-----------:|------------:|--------:|-------------:|-------------:|-------------:|
| male          |         23 |         24 |          19 |      66 |      34.8485 |      36.3636 |      28.7879 |
| female        |         20 |         17 |          33 |      70 |      28.5714 |      24.2857 |      47.1429 |
| not_spacified |         17 |         22 |          24 |      63 |      26.9841 |      34.9206 |      38.0952 |



### Type 2, Negative Attribute

| bias_type   | target_term   | gender        |   positive |   negative |   unrelated |   total |   neg_to_pos |   neg_to_neg |   neg_to_neu |
|:------------|:--------------|:--------------|-----------:|-----------:|------------:|--------:|-------------:|-------------:|-------------:|
| nationality | negative      | male          |         11 |          7 |           3 |      21 |      52.381  |      33.3333 |      14.2857 |
| nationality | negative      | female        |         10 |          5 |           2 |      17 |      58.8235 |      29.4118 |      11.7647 |
| nationality | negative      | not_spacified |          8 |         13 |           4 |      25 |      32      |      52      |      16      |
| ageism      | negative      | male          |          6 |         18 |          11 |      35 |      17.1429 |      51.4286 |      31.4286 |
| ageism      | negative      | female        |          7 |         13 |          23 |      43 |      16.2791 |      30.2326 |      53.4884 |
| ageism      | negative      | not_spacified |         11 |         16 |          15 |      42 |      26.1905 |      38.0952 |      35.7143 |
| ableism     | negative      | male          |          6 |          2 |           3 |      11 |      54.5455 |      18.1818 |      27.2727 |
| ableism     | negative      | female        |          5 |          2 |           7 |      14 |      35.7143 |      14.2857 |      50      |
| ableism     | negative      | not_spacified |          2 |          1 |           2 |       5 |      40      |      20      |      40      |



### Type 2, Negative, Gender

| bias_type     |   positive |   negative |   unrelated |   total |   pos_to_pos |   pos_to_neg |   pos_to_neu |
|:--------------|-----------:|-----------:|------------:|--------:|-------------:|-------------:|-------------:|
| male          |         23 |         27 |          17 |      67 |      34.3284 |      40.2985 |      25.3731 |
| female        |         22 |         20 |          32 |      74 |      29.7297 |      27.027  |      43.2432 |
| not_spacified |         21 |         30 |          21 |      72 |      29.1667 |      41.6667 |      29.1667 |



## Kendall Tau Calculation

Total data: 490

Kendall's Tau Correlation for type 1: -0.036568096626405665

P-Value: 0.4299265334636494

Total data: 412

Kendall's Tau Correlation for type 2: 0.02563860872843812

P-Value: 0.6326142538630897

## Kendall Tau Calculation considering if there are any positive likelihood towards feminine gendered pronoun

Total data: 490

Kendall's Tau Correlation for type1 Considering more positive likelihood towards feminine gendered pronoun: -0.002748854643898376

P-Value: 0.9421210734288586

Total data: 412

Kendall's Tau Correlation for type2 Considering more positive likelihood towards feminine gendered pronoun: 0.03755655575454803

P-Value: 0.3912680811088497


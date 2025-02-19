# Report for Model: norallm/normistral-7b-warm-instruct

## Different Types of Likelihood Calculation

### Type 1, Positive Attribute

| bias_type   | target_term   |   positive |   negative |   unrelated |   total |   pos_to_pos |   pos_to_neg |   pos_to_neu |
|:------------|:--------------|-----------:|-----------:|------------:|--------:|-------------:|-------------:|-------------:|
| nationality | positive      |         73 |         28 |          23 |     124 |      58.871  |      22.5806 |     18.5484  |
| ageism      | positive      |         55 |         13 |           7 |      75 |      73.3333 |      17.3333 |      9.33333 |
| ableism     | positive      |         22 |         16 |          12 |      50 |      44      |      32      |     24       |



### Type 1, Negative Attribute

| bias_type   | target_term   |   positive |   negative |   unrelated |   total |   neg_to_pos |   neg_to_neg |   neg_to_neu |
|:------------|:--------------|-----------:|-----------:|------------:|--------:|-------------:|-------------:|-------------:|
| nationality | negative      |         57 |         37 |          17 |     111 |      51.3514 |      33.3333 |      15.3153 |
| ageism      | negative      |         31 |         25 |           7 |      63 |      49.2063 |      39.6825 |      11.1111 |
| ableism     | negative      |         23 |         17 |          15 |      55 |      41.8182 |      30.9091 |      27.2727 |



### Type 1, Combined Attribute

| bias_type   |   positive |   negative |   unrelated |   total |      pl |      nl |     nul |
|:------------|-----------:|-----------:|------------:|--------:|--------:|--------:|--------:|
| nationality |        130 |         65 |          40 |     235 | 55.3191 | 27.6596 | 17.0213 |
| ageism      |         86 |         38 |          14 |     138 | 62.3188 | 27.5362 | 10.1449 |
| ableism     |         45 |         33 |          27 |     105 | 42.8571 | 31.4286 | 25.7143 |



### Type 2, Positive Attribute

| bias_type   | target_term   |   positive |   negative |   unrelated |   total |   pos_to_pos |   pos_to_neg |   pos_to_neu |
|:------------|:--------------|-----------:|-----------:|------------:|--------:|-------------:|-------------:|-------------:|
| nationality | positive      |         22 |          6 |          27 |      55 |      40      |      10.9091 |      49.0909 |
| ageism      | positive      |         42 |         31 |          39 |     112 |      37.5    |      27.6786 |      34.8214 |
| ableism     | positive      |          5 |          9 |          12 |      26 |      19.2308 |      34.6154 |      46.1538 |



### Type 2, Negative Attribute

| bias_type   | target_term   |   positive |   negative |   unrelated |   total |   neg_to_pos |   neg_to_neg |   neg_to_neu |
|:------------|:--------------|-----------:|-----------:|------------:|--------:|-------------:|-------------:|-------------:|
| nationality | negative      |         27 |          9 |          27 |      63 |      42.8571 |      14.2857 |      42.8571 |
| ageism      | negative      |         53 |         33 |          30 |     116 |      45.6897 |      28.4483 |      25.8621 |
| ableism     | negative      |          6 |         15 |           6 |      27 |      22.2222 |      55.5556 |      22.2222 |



### Type 2, Combined Attribute

| bias_type   |   positive |   negative |   unrelated |   total |      pl |      nl |     nul |
|:------------|-----------:|-----------:|------------:|--------:|--------:|--------:|--------:|
| nationality |         49 |         15 |          54 |     118 | 41.5254 | 12.7119 | 45.7627 |
| ageism      |         95 |         64 |          69 |     228 | 41.6667 | 28.0702 | 30.2632 |
| ableism     |         11 |         24 |          18 |      53 | 20.7547 | 45.283  | 33.9623 |



### Type 1, Positive Attribute

| bias_type   | target_term   | gender        |   positive |   negative |   unrelated |   total |   pos_to_pos |   pos_to_neg |   pos_to_neu |
|:------------|:--------------|:--------------|-----------:|-----------:|------------:|--------:|-------------:|-------------:|-------------:|
| nationality | positive      | male          |         15 |         11 |           8 |      34 |      44.1176 |      32.3529 |     23.5294  |
| nationality | positive      | female        |         29 |          9 |           9 |      47 |      61.7021 |      19.1489 |     19.1489  |
| nationality | positive      | not_spacified |         29 |          8 |           6 |      43 |      67.4419 |      18.6047 |     13.9535  |
| ageism      | positive      | male          |         25 |          3 |           4 |      32 |      78.125  |       9.375  |     12.5     |
| ageism      | positive      | female        |          8 |          7 |           1 |      16 |      50      |      43.75   |      6.25    |
| ageism      | positive      | not_spacified |         22 |          3 |           2 |      27 |      81.4815 |      11.1111 |      7.40741 |
| ableism     | positive      | male          |          5 |          3 |           5 |      13 |      38.4615 |      23.0769 |     38.4615  |
| ableism     | positive      | female        |          9 |          5 |           3 |      17 |      52.9412 |      29.4118 |     17.6471  |
| ableism     | positive      | not_spacified |          8 |          8 |           4 |      20 |      40      |      40      |     20       |



### Type 1, Positive, Gender

| bias_type     |   positive |   negative |   unrelated |   total |   pos_to_pos |   pos_to_neg |   pos_to_neu |
|:--------------|-----------:|-----------:|------------:|--------:|-------------:|-------------:|-------------:|
| male          |         45 |         17 |          17 |      79 |      56.962  |      21.519  |      21.519  |
| female        |         46 |         21 |          13 |      80 |      57.5    |      26.25   |      16.25   |
| not_spacified |         59 |         19 |          12 |      90 |      65.5556 |      21.1111 |      13.3333 |



### Type 1, Negative Attribute

| bias_type   | target_term   | gender        |   positive |   negative |   unrelated |   total |   neg_to_pos |   neg_to_neg |   neg_to_neu |
|:------------|:--------------|:--------------|-----------:|-----------:|------------:|--------:|-------------:|-------------:|-------------:|
| nationality | negative      | male          |         15 |         14 |           7 |      36 |      41.6667 |      38.8889 |     19.4444  |
| nationality | negative      | female        |         20 |         16 |           5 |      41 |      48.7805 |      39.0244 |     12.1951  |
| nationality | negative      | not_spacified |         22 |          7 |           5 |      34 |      64.7059 |      20.5882 |     14.7059  |
| ageism      | negative      | male          |         10 |          7 |           4 |      21 |      47.619  |      33.3333 |     19.0476  |
| ageism      | negative      | female        |          9 |         11 |           2 |      22 |      40.9091 |      50      |      9.09091 |
| ageism      | negative      | not_spacified |         12 |          7 |           1 |      20 |      60      |      35      |      5       |
| ableism     | negative      | male          |          5 |          6 |           6 |      17 |      29.4118 |      35.2941 |     35.2941  |
| ableism     | negative      | female        |         12 |          7 |           4 |      23 |      52.1739 |      30.4348 |     17.3913  |
| ableism     | negative      | not_spacified |          6 |          4 |           5 |      15 |      40      |      26.6667 |     33.3333  |



### Type 1, Negative, Gender

| bias_type     |   positive |   negative |   unrelated |   total |   pos_to_pos |   pos_to_neg |   pos_to_neu |
|:--------------|-----------:|-----------:|------------:|--------:|-------------:|-------------:|-------------:|
| male          |         30 |         27 |          17 |      74 |      40.5405 |      36.4865 |      22.973  |
| female        |         41 |         34 |          11 |      86 |      47.6744 |      39.5349 |      12.7907 |
| not_spacified |         40 |         18 |          11 |      69 |      57.971  |      26.087  |      15.942  |



### Type 2, Positive Attribute

| bias_type   | target_term   | gender        |   positive |   negative |   unrelated |   total |   pos_to_pos |   pos_to_neg |   pos_to_neu |
|:------------|:--------------|:--------------|-----------:|-----------:|------------:|--------:|-------------:|-------------:|-------------:|
| nationality | positive      | male          |          8 |          1 |           9 |      18 |      44.4444 |      5.55556 |      50      |
| nationality | positive      | female        |          7 |          1 |          11 |      19 |      36.8421 |      5.26316 |      57.8947 |
| nationality | positive      | not_spacified |          7 |          4 |           7 |      18 |      38.8889 |     22.2222  |      38.8889 |
| ageism      | positive      | male          |         15 |          7 |          10 |      32 |      46.875  |     21.875   |      31.25   |
| ageism      | positive      | female        |         16 |          7 |          19 |      42 |      38.0952 |     16.6667  |      45.2381 |
| ageism      | positive      | not_spacified |         11 |         17 |          10 |      38 |      28.9474 |     44.7368  |      26.3158 |
| ableism     | positive      | male          |          2 |          6 |           4 |      12 |      16.6667 |     50       |      33.3333 |
| ableism     | positive      | female        |          0 |          1 |           5 |       6 |       0      |     16.6667  |      83.3333 |
| ableism     | positive      | not_spacified |          3 |          2 |           3 |       8 |      37.5    |     25       |      37.5    |



### Type 2, Positive, Gender

| bias_type     |   positive |   negative |   unrelated |   total |   pos_to_pos |   pos_to_neg |   pos_to_neu |
|:--------------|-----------:|-----------:|------------:|--------:|-------------:|-------------:|-------------:|
| male          |         25 |         14 |          23 |      62 |      40.3226 |      22.5806 |      37.0968 |
| female        |         23 |          9 |          35 |      67 |      34.3284 |      13.4328 |      52.2388 |
| not_spacified |         21 |         23 |          20 |      64 |      32.8125 |      35.9375 |      31.25   |



### Type 2, Negative Attribute

| bias_type   | target_term   | gender        |   positive |   negative |   unrelated |   total |   neg_to_pos |   neg_to_neg |   neg_to_neu |
|:------------|:--------------|:--------------|-----------:|-----------:|------------:|--------:|-------------:|-------------:|-------------:|
| nationality | negative      | male          |          9 |          3 |          10 |      22 |      40.9091 |      13.6364 |      45.4545 |
| nationality | negative      | female        |          5 |          3 |           9 |      17 |      29.4118 |      17.6471 |      52.9412 |
| nationality | negative      | not_spacified |         13 |          3 |           8 |      24 |      54.1667 |      12.5    |      33.3333 |
| ageism      | negative      | male          |         15 |         10 |           9 |      34 |      44.1176 |      29.4118 |      26.4706 |
| ageism      | negative      | female        |         17 |         13 |          10 |      40 |      42.5    |      32.5    |      25      |
| ageism      | negative      | not_spacified |         21 |         10 |          11 |      42 |      50      |      23.8095 |      26.1905 |
| ableism     | negative      | male          |          0 |          7 |           4 |      11 |       0      |      63.6364 |      36.3636 |
| ableism     | negative      | female        |          4 |          7 |           2 |      13 |      30.7692 |      53.8462 |      15.3846 |
| ableism     | negative      | not_spacified |          2 |          1 |           0 |       3 |      66.6667 |      33.3333 |       0      |



### Type 2, Negative, Gender

| bias_type     |   positive |   negative |   unrelated |   total |   pos_to_pos |   pos_to_neg |   pos_to_neu |
|:--------------|-----------:|-----------:|------------:|--------:|-------------:|-------------:|-------------:|
| male          |         24 |         20 |          23 |      67 |      35.8209 |      29.8507 |      34.3284 |
| female        |         26 |         23 |          21 |      70 |      37.1429 |      32.8571 |      30      |
| not_spacified |         36 |         14 |          19 |      69 |      52.1739 |      20.2899 |      27.5362 |



## Kendall Tau Calculation

Total data: 478

Kendall's Tau Correlation for type 1: 0.13665727140631292

P-Value: 0.004031113590755331

Total data: 399

Kendall's Tau Correlation for type 2: -0.021004893185344313

P-Value: 0.6987163533197291

## Kendall Tau Calculation considering if there are any positive likelihood towards feminine gendered pronoun

Total data: 478

Kendall's Tau Correlation for type1 Considering more positive likelihood towards feminine gendered pronoun: 0.0005908510005076942

P-Value: 0.9878588648711956

Total data: 399

Kendall's Tau Correlation for type2 Considering more positive likelihood towards feminine gendered pronoun: 0.0006030112876175401

P-Value: 0.9891469799972846


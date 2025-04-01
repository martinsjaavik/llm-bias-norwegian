# Report for Model: openai/gpt-4

## Different Types of Likelihood Calculation

### Type 1, Positive Attribute

| bias_type   | target_term   |   positive |   negative |   unrelated |   total |   pos_to_pos |   pos_to_neg |   pos_to_neu |
|:------------|:--------------|-----------:|-----------:|------------:|--------:|-------------:|-------------:|-------------:|
| nationality | positive      |        112 |          2 |          21 |     135 |      82.963  |      1.48148 |      15.5556 |
| ageism      | positive      |         58 |          0 |          11 |      69 |      84.058  |      0       |      15.942  |
| ableism     | positive      |         47 |          5 |          13 |      65 |      72.3077 |      7.69231 |      20      |



### Type 1, Negative Attribute

| bias_type   | target_term   |   positive |   negative |   unrelated |   total |   neg_to_pos |   neg_to_neg |   neg_to_neu |
|:------------|:--------------|-----------:|-----------:|------------:|--------:|-------------:|-------------:|-------------:|
| nationality | negative      |         92 |          9 |          22 |     123 |      74.7967 |      7.31707 |      17.8862 |
| ageism      | negative      |         41 |         13 |          18 |      72 |      56.9444 |     18.0556  |      25      |
| ableism     | negative      |         48 |          4 |          14 |      66 |      72.7273 |      6.06061 |      21.2121 |



### Type 1, Combined Attribute

| bias_type   |   positive |   negative |   unrelated |   total |      pl |      nl |     nul |
|:------------|-----------:|-----------:|------------:|--------:|--------:|--------:|--------:|
| nationality |        204 |         11 |          43 |     258 | 79.0698 | 4.26357 | 16.6667 |
| ageism      |         99 |         13 |          29 |     141 | 70.2128 | 9.21986 | 20.5674 |
| ableism     |         95 |          9 |          27 |     131 | 72.5191 | 6.87023 | 20.6107 |



### Type 2, Positive Attribute

| bias_type   | target_term   |   positive |   negative |   unrelated |   total |   pos_to_pos |   pos_to_neg |   pos_to_neu |
|:------------|:--------------|-----------:|-----------:|------------:|--------:|-------------:|-------------:|-------------:|
| nationality | positive      |         44 |          8 |          11 |      63 |      69.8413 |      12.6984 |      17.4603 |
| ageism      | positive      |         50 |         21 |          40 |     111 |      45.045  |      18.9189 |      36.036  |
| ableism     | positive      |          5 |          9 |          20 |      34 |      14.7059 |      26.4706 |      58.8235 |



### Type 2, Negative Attribute

| bias_type   | target_term   |   positive |   negative |   unrelated |   total |   neg_to_pos |   neg_to_neg |   neg_to_neu |
|:------------|:--------------|-----------:|-----------:|------------:|--------:|-------------:|-------------:|-------------:|
| nationality | negative      |         27 |         12 |           5 |      44 |      61.3636 |      27.2727 |      11.3636 |
| ageism      | negative      |         29 |         39 |          42 |     110 |      26.3636 |      35.4545 |      38.1818 |
| ableism     | negative      |          0 |         17 |          18 |      35 |       0      |      48.5714 |      51.4286 |



### Type 2, Combined Attribute

| bias_type   |   positive |   negative |   unrelated |   total |       pl |      nl |     nul |
|:------------|-----------:|-----------:|------------:|--------:|---------:|--------:|--------:|
| nationality |         71 |         20 |          16 |     107 | 66.3551  | 18.6916 | 14.9533 |
| ageism      |         79 |         60 |          82 |     221 | 35.7466  | 27.1493 | 37.1041 |
| ableism     |          5 |         26 |          38 |      69 |  7.24638 | 37.6812 | 55.0725 |



### Type 1, Positive Attribute

| bias_type   | target_term   | gender        |   positive |   negative |   unrelated |   total |   pos_to_pos |   pos_to_neg |   pos_to_neu |
|:------------|:--------------|:--------------|-----------:|-----------:|------------:|--------:|-------------:|-------------:|-------------:|
| nationality | positive      | male          |         28 |          2 |           6 |      36 |      77.7778 |      5.55556 |     16.6667  |
| nationality | positive      | female        |         44 |          0 |           5 |      49 |      89.7959 |      0       |     10.2041  |
| nationality | positive      | not_spacified |         40 |          0 |          10 |      50 |      80      |      0       |     20       |
| ageism      | positive      | male          |         22 |          0 |           6 |      28 |      78.5714 |      0       |     21.4286  |
| ageism      | positive      | female        |         12 |          0 |           1 |      13 |      92.3077 |      0       |      7.69231 |
| ageism      | positive      | not_spacified |         24 |          0 |           4 |      28 |      85.7143 |      0       |     14.2857  |
| ableism     | positive      | male          |         12 |          3 |           4 |      19 |      63.1579 |     15.7895  |     21.0526  |
| ableism     | positive      | female        |         17 |          0 |           4 |      21 |      80.9524 |      0       |     19.0476  |
| ableism     | positive      | not_spacified |         18 |          2 |           5 |      25 |      72      |      8       |     20       |



### Type 1, Positive, Gender

| bias_type     |   positive |   negative |   unrelated |   total |   pos_to_pos |   pos_to_neg |   pos_to_neu |
|:--------------|-----------:|-----------:|------------:|--------:|-------------:|-------------:|-------------:|
| male          |         62 |          5 |          16 |      83 |      74.6988 |      6.0241  |      19.2771 |
| female        |         73 |          0 |          10 |      83 |      87.9518 |      0       |      12.0482 |
| not_spacified |         82 |          2 |          19 |     103 |      79.6117 |      1.94175 |      18.4466 |



### Type 1, Negative Attribute

| bias_type   | target_term   | gender        |   positive |   negative |   unrelated |   total |   neg_to_pos |   neg_to_neg |   neg_to_neu |
|:------------|:--------------|:--------------|-----------:|-----------:|------------:|--------:|-------------:|-------------:|-------------:|
| nationality | negative      | male          |         26 |          3 |           7 |      36 |      72.2222 |      8.33333 |     19.4444  |
| nationality | negative      | female        |         36 |          3 |          10 |      49 |      73.4694 |      6.12245 |     20.4082  |
| nationality | negative      | not_spacified |         30 |          3 |           5 |      38 |      78.9474 |      7.89474 |     13.1579  |
| ageism      | negative      | male          |         19 |          3 |           5 |      27 |      70.3704 |     11.1111  |     18.5185  |
| ageism      | negative      | female        |         13 |          4 |           8 |      25 |      52      |     16       |     32       |
| ageism      | negative      | not_spacified |          9 |          6 |           5 |      20 |      45      |     30       |     25       |
| ableism     | negative      | male          |         11 |          2 |           6 |      19 |      57.8947 |     10.5263  |     31.5789  |
| ableism     | negative      | female        |         21 |          1 |           7 |      29 |      72.4138 |      3.44828 |     24.1379  |
| ableism     | negative      | not_spacified |         16 |          1 |           1 |      18 |      88.8889 |      5.55556 |      5.55556 |



### Type 1, Negative, Gender

| bias_type     |   positive |   negative |   unrelated |   total |   pos_to_pos |   pos_to_neg |   pos_to_neu |
|:--------------|-----------:|-----------:|------------:|--------:|-------------:|-------------:|-------------:|
| male          |         56 |          8 |          18 |      82 |      68.2927 |      9.7561  |      21.9512 |
| female        |         70 |          8 |          25 |     103 |      67.9612 |      7.76699 |      24.2718 |
| not_spacified |         55 |         10 |          11 |      76 |      72.3684 |     13.1579  |      14.4737 |



### Type 2, Positive Attribute

| bias_type   | target_term   | gender        |   positive |   negative |   unrelated |   total |   pos_to_pos |   pos_to_neg |   pos_to_neu |
|:------------|:--------------|:--------------|-----------:|-----------:|------------:|--------:|-------------:|-------------:|-------------:|
| nationality | positive      | male          |         15 |          1 |           6 |      22 |      68.1818 |      4.54545 |     27.2727  |
| nationality | positive      | female        |         17 |          2 |           2 |      21 |      80.9524 |      9.52381 |      9.52381 |
| nationality | positive      | not_spacified |         12 |          5 |           3 |      20 |      60      |     25       |     15       |
| ageism      | positive      | male          |         16 |          5 |          12 |      33 |      48.4848 |     15.1515  |     36.3636  |
| ageism      | positive      | female        |         18 |          6 |          18 |      42 |      42.8571 |     14.2857  |     42.8571  |
| ageism      | positive      | not_spacified |         16 |         10 |          10 |      36 |      44.4444 |     27.7778  |     27.7778  |
| ableism     | positive      | male          |          2 |          3 |           9 |      14 |      14.2857 |     21.4286  |     64.2857  |
| ableism     | positive      | female        |          1 |          4 |           4 |       9 |      11.1111 |     44.4444  |     44.4444  |
| ableism     | positive      | not_spacified |          2 |          2 |           7 |      11 |      18.1818 |     18.1818  |     63.6364  |



### Type 2, Positive, Gender

| bias_type     |   positive |   negative |   unrelated |   total |   pos_to_pos |   pos_to_neg |   pos_to_neu |
|:--------------|-----------:|-----------:|------------:|--------:|-------------:|-------------:|-------------:|
| male          |         33 |          9 |          27 |      69 |      47.8261 |      13.0435 |      39.1304 |
| female        |         36 |         12 |          24 |      72 |      50      |      16.6667 |      33.3333 |
| not_spacified |         30 |         17 |          20 |      67 |      44.7761 |      25.3731 |      29.8507 |



### Type 2, Negative Attribute

| bias_type   | target_term   | gender        |   positive |   negative |   unrelated |   total |   neg_to_pos |   neg_to_neg |   neg_to_neu |
|:------------|:--------------|:--------------|-----------:|-----------:|------------:|--------:|-------------:|-------------:|-------------:|
| nationality | negative      | male          |          6 |          5 |           2 |      13 |      46.1538 |      38.4615 |     15.3846  |
| nationality | negative      | female        |          4 |          2 |           1 |       7 |      57.1429 |      28.5714 |     14.2857  |
| nationality | negative      | not_spacified |         17 |          5 |           2 |      24 |      70.8333 |      20.8333 |      8.33333 |
| ageism      | negative      | male          |          8 |         10 |          15 |      33 |      24.2424 |      30.303  |     45.4545  |
| ageism      | negative      | female        |          8 |         16 |          14 |      38 |      21.0526 |      42.1053 |     36.8421  |
| ageism      | negative      | not_spacified |         13 |         13 |          13 |      39 |      33.3333 |      33.3333 |     33.3333  |
| ableism     | negative      | male          |          0 |          7 |           7 |      14 |       0      |      50      |     50       |
| ableism     | negative      | female        |          0 |          6 |           8 |      14 |       0      |      42.8571 |     57.1429  |
| ableism     | negative      | not_spacified |          0 |          4 |           3 |       7 |       0      |      57.1429 |     42.8571  |



### Type 2, Negative, Gender

| bias_type     |   positive |   negative |   unrelated |   total |   pos_to_pos |   pos_to_neg |   pos_to_neu |
|:--------------|-----------:|-----------:|------------:|--------:|-------------:|-------------:|-------------:|
| male          |         14 |         22 |          24 |      60 |      23.3333 |      36.6667 |      40      |
| female        |         12 |         24 |          23 |      59 |      20.339  |      40.678  |      38.9831 |
| not_spacified |         30 |         22 |          18 |      70 |      42.8571 |      31.4286 |      25.7143 |



## Kendall Tau Calculation

Total data: 530

Kendall's Tau Correlation for type 1: 0.12445710217159131

P-Value: 0.001021422542381834

Total data: 397

Kendall's Tau Correlation for type 2: 0.23909802105209726

P-Value: 1.1106223925998341e-05

## Kendall Tau Calculation considering if there are any positive likelihood towards feminine gendered pronoun

Total data: 530

Kendall's Tau Correlation for type1 Considering more positive likelihood towards feminine gendered pronoun: 0.03834104663581346

P-Value: 0.21509289247742625

Total data: 397

Kendall's Tau Correlation for type2 Considering more positive likelihood towards feminine gendered pronoun: -0.012810182159648242

P-Value: 0.7733088366067074


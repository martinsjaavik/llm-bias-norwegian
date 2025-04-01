# Report for Model: llama3

## Different Types of Likelihood Calculation

### Type 1, Positive Attribute

| bias_type   | target_term   |   positive |   negative |   unrelated |   total |   pos_to_pos |   pos_to_neg |   pos_to_neu |
|:------------|:--------------|-----------:|-----------:|------------:|--------:|-------------:|-------------:|-------------:|
| nationality | positive      |         51 |         57 |          23 |     131 |      38.9313 |      43.5115 |      17.5573 |
| ageism      | positive      |         35 |         25 |           8 |      68 |      51.4706 |      36.7647 |      11.7647 |
| ableism     | positive      |         18 |         36 |           8 |      62 |      29.0323 |      58.0645 |      12.9032 |



### Type 1, Negative Attribute

| bias_type   | target_term   |   positive |   negative |   unrelated |   total |   neg_to_pos |   neg_to_neg |   neg_to_neu |
|:------------|:--------------|-----------:|-----------:|------------:|--------:|-------------:|-------------:|-------------:|
| nationality | negative      |         29 |         66 |          23 |     118 |     24.5763  |      55.9322 |      19.4915 |
| ageism      | negative      |         19 |         43 |          10 |      72 |     26.3889  |      59.7222 |      13.8889 |
| ableism     | negative      |          5 |         43 |          18 |      66 |      7.57576 |      65.1515 |      27.2727 |



### Type 1, Combined Attribute

| bias_type   |   positive |   negative |   unrelated |   total |      pl |      nl |     nul |
|:------------|-----------:|-----------:|------------:|--------:|--------:|--------:|--------:|
| nationality |         80 |        123 |          46 |     249 | 32.1285 | 49.3976 | 18.4739 |
| ageism      |         54 |         68 |          18 |     140 | 38.5714 | 48.5714 | 12.8571 |
| ableism     |         23 |         79 |          26 |     128 | 17.9688 | 61.7188 | 20.3125 |



### Type 2, Positive Attribute

| bias_type   | target_term   |   positive |   negative |   unrelated |   total |   pos_to_pos |   pos_to_neg |   pos_to_neu |
|:------------|:--------------|-----------:|-----------:|------------:|--------:|-------------:|-------------:|-------------:|
| nationality | positive      |         46 |          8 |          10 |      64 |      71.875  |      12.5    |      15.625  |
| ageism      | positive      |         21 |         54 |          39 |     114 |      18.4211 |      47.3684 |      34.2105 |
| ableism     | positive      |          7 |         13 |           9 |      29 |      24.1379 |      44.8276 |      31.0345 |



### Type 2, Negative Attribute

| bias_type   | target_term   |   positive |   negative |   unrelated |   total |   neg_to_pos |   neg_to_neg |   neg_to_neu |
|:------------|:--------------|-----------:|-----------:|------------:|--------:|-------------:|-------------:|-------------:|
| nationality | negative      |         27 |         32 |          14 |      73 |      36.9863 |      43.8356 |     19.1781  |
| ageism      | negative      |         17 |         67 |          35 |     119 |      14.2857 |      56.3025 |     29.4118  |
| ableism     | negative      |         11 |         18 |           1 |      30 |      36.6667 |      60      |      3.33333 |



### Type 2, Combined Attribute

| bias_type   |   positive |   negative |   unrelated |   total |      pl |      nl |     nul |
|:------------|-----------:|-----------:|------------:|--------:|--------:|--------:|--------:|
| nationality |         73 |         40 |          24 |     137 | 53.2847 | 29.1971 | 17.5182 |
| ageism      |         38 |        121 |          74 |     233 | 16.309  | 51.9313 | 31.7597 |
| ableism     |         18 |         31 |          10 |      59 | 30.5085 | 52.5424 | 16.9492 |



### Type 1, Positive Attribute

| bias_type   | target_term   | gender        |   positive |   negative |   unrelated |   total |   pos_to_pos |   pos_to_neg |   pos_to_neu |
|:------------|:--------------|:--------------|-----------:|-----------:|------------:|--------:|-------------:|-------------:|-------------:|
| nationality | positive      | male          |         12 |         21 |           4 |      37 |      32.4324 |      56.7568 |      10.8108 |
| nationality | positive      | female        |         19 |         20 |           8 |      47 |      40.4255 |      42.5532 |      17.0213 |
| nationality | positive      | not_spacified |         20 |         16 |          11 |      47 |      42.5532 |      34.0426 |      23.4043 |
| ageism      | positive      | male          |         14 |         11 |           3 |      28 |      50      |      39.2857 |      10.7143 |
| ageism      | positive      | female        |          9 |          4 |           2 |      15 |      60      |      26.6667 |      13.3333 |
| ageism      | positive      | not_spacified |         12 |         10 |           3 |      25 |      48      |      40      |      12      |
| ableism     | positive      | male          |          6 |          8 |           3 |      17 |      35.2941 |      47.0588 |      17.6471 |
| ableism     | positive      | female        |          6 |         11 |           3 |      20 |      30      |      55      |      15      |
| ableism     | positive      | not_spacified |          6 |         17 |           2 |      25 |      24      |      68      |       8      |



### Type 1, Positive, Gender

| bias_type     |   positive |   negative |   unrelated |   total |   pos_to_pos |   pos_to_neg |   pos_to_neu |
|:--------------|-----------:|-----------:|------------:|--------:|-------------:|-------------:|-------------:|
| male          |         32 |         40 |          10 |      82 |      39.0244 |      48.7805 |      12.1951 |
| female        |         34 |         35 |          13 |      82 |      41.4634 |      42.6829 |      15.8537 |
| not_spacified |         38 |         43 |          16 |      97 |      39.1753 |      44.3299 |      16.4948 |



### Type 1, Negative Attribute

| bias_type   | target_term   | gender        |   positive |   negative |   unrelated |   total |   neg_to_pos |   neg_to_neg |   neg_to_neu |
|:------------|:--------------|:--------------|-----------:|-----------:|------------:|--------:|-------------:|-------------:|-------------:|
| nationality | negative      | male          |         11 |         21 |           5 |      37 |     29.7297  |      56.7568 |      13.5135 |
| nationality | negative      | female        |         10 |         26 |          10 |      46 |     21.7391  |      56.5217 |      21.7391 |
| nationality | negative      | not_spacified |          8 |         19 |           8 |      35 |     22.8571  |      54.2857 |      22.8571 |
| ageism      | negative      | male          |         10 |         14 |           3 |      27 |     37.037   |      51.8519 |      11.1111 |
| ageism      | negative      | female        |          3 |         17 |           4 |      24 |     12.5     |      70.8333 |      16.6667 |
| ageism      | negative      | not_spacified |          6 |         12 |           3 |      21 |     28.5714  |      57.1429 |      14.2857 |
| ableism     | negative      | male          |          3 |         12 |           4 |      19 |     15.7895  |      63.1579 |      21.0526 |
| ableism     | negative      | female        |          2 |         17 |           9 |      28 |      7.14286 |      60.7143 |      32.1429 |
| ableism     | negative      | not_spacified |          0 |         14 |           5 |      19 |      0       |      73.6842 |      26.3158 |



### Type 1, Negative, Gender

| bias_type     |   positive |   negative |   unrelated |   total |   pos_to_pos |   pos_to_neg |   pos_to_neu |
|:--------------|-----------:|-----------:|------------:|--------:|-------------:|-------------:|-------------:|
| male          |         24 |         47 |          12 |      83 |      28.9157 |      56.6265 |      14.4578 |
| female        |         15 |         60 |          23 |      98 |      15.3061 |      61.2245 |      23.4694 |
| not_spacified |         14 |         45 |          16 |      75 |      18.6667 |      60      |      21.3333 |



### Type 2, Positive Attribute

| bias_type   | target_term   | gender        |   positive |   negative |   unrelated |   total |   pos_to_pos |   pos_to_neg |   pos_to_neu |
|:------------|:--------------|:--------------|-----------:|-----------:|------------:|--------:|-------------:|-------------:|-------------:|
| nationality | positive      | male          |         14 |          4 |           5 |      23 |     60.8696  |      17.3913 |     21.7391  |
| nationality | positive      | female        |         18 |          1 |           2 |      21 |     85.7143  |       4.7619 |      9.52381 |
| nationality | positive      | not_spacified |         14 |          3 |           3 |      20 |     70       |      15      |     15       |
| ageism      | positive      | male          |          3 |         19 |          11 |      33 |      9.09091 |      57.5758 |     33.3333  |
| ageism      | positive      | female        |         10 |         20 |          13 |      43 |     23.2558  |      46.5116 |     30.2326  |
| ageism      | positive      | not_spacified |          8 |         15 |          15 |      38 |     21.0526  |      39.4737 |     39.4737  |
| ableism     | positive      | male          |          4 |          5 |           4 |      13 |     30.7692  |      38.4615 |     30.7692  |
| ableism     | positive      | female        |          1 |          5 |           1 |       7 |     14.2857  |      71.4286 |     14.2857  |
| ableism     | positive      | not_spacified |          2 |          3 |           4 |       9 |     22.2222  |      33.3333 |     44.4444  |



### Type 2, Positive, Gender

| bias_type     |   positive |   negative |   unrelated |   total |   pos_to_pos |   pos_to_neg |   pos_to_neu |
|:--------------|-----------:|-----------:|------------:|--------:|-------------:|-------------:|-------------:|
| male          |         21 |         28 |          20 |      69 |      30.4348 |      40.5797 |      28.9855 |
| female        |         29 |         26 |          16 |      71 |      40.8451 |      36.6197 |      22.5352 |
| not_spacified |         24 |         21 |          22 |      67 |      35.8209 |      31.3433 |      32.8358 |



### Type 2, Negative Attribute

| bias_type   | target_term   | gender        |   positive |   negative |   unrelated |   total |   neg_to_pos |   neg_to_neg |   neg_to_neu |
|:------------|:--------------|:--------------|-----------:|-----------:|------------:|--------:|-------------:|-------------:|-------------:|
| nationality | negative      | male          |         10 |         10 |           5 |      25 |     40       |      40      |     20       |
| nationality | negative      | female        |          6 |         11 |           4 |      21 |     28.5714  |      52.381  |     19.0476  |
| nationality | negative      | not_spacified |         11 |         11 |           5 |      27 |     40.7407  |      40.7407 |     18.5185  |
| ageism      | negative      | male          |          3 |         21 |          11 |      35 |      8.57143 |      60      |     31.4286  |
| ageism      | negative      | female        |          4 |         25 |          13 |      42 |      9.52381 |      59.5238 |     30.9524  |
| ageism      | negative      | not_spacified |         10 |         21 |          11 |      42 |     23.8095  |      50      |     26.1905  |
| ableism     | negative      | male          |          2 |          9 |           1 |      12 |     16.6667  |      75      |      8.33333 |
| ableism     | negative      | female        |          6 |          6 |           0 |      12 |     50       |      50      |      0       |
| ableism     | negative      | not_spacified |          3 |          3 |           0 |       6 |     50       |      50      |      0       |



### Type 2, Negative, Gender

| bias_type     |   positive |   negative |   unrelated |   total |   pos_to_pos |   pos_to_neg |   pos_to_neu |
|:--------------|-----------:|-----------:|------------:|--------:|-------------:|-------------:|-------------:|
| male          |         15 |         40 |          17 |      72 |      20.8333 |      55.5556 |      23.6111 |
| female        |         16 |         42 |          17 |      75 |      21.3333 |      56      |      22.6667 |
| not_spacified |         24 |         35 |          16 |      75 |      32      |      46.6667 |      21.3333 |



## Kendall Tau Calculation

Total data: 517

Kendall's Tau Correlation for type 1: 0.19007142082165746

P-Value: 3.811102246359517e-05

Total data: 429

Kendall's Tau Correlation for type 2: 0.17559130845844131

P-Value: 0.0007239871861834579

## Kendall Tau Calculation considering if there are any positive likelihood towards feminine gendered pronoun

Total data: 517

Kendall's Tau Correlation for type1 Considering more positive likelihood towards feminine gendered pronoun: -0.02200988443220634

P-Value: 0.5590754777465077

Total data: 429

Kendall's Tau Correlation for type2 Considering more positive likelihood towards feminine gendered pronoun: 0.026586467145907705

P-Value: 0.5310064848899324


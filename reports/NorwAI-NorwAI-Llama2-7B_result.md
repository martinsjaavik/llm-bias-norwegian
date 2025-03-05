# Report for Model: NorwAI/NorwAI-Llama2-7B

## Different Types of Likelihood Calculation

### Type 1, Positive Attribute

| bias_type   | target_term   |   positive |   negative |   unrelated |   total |   pos_to_pos |   pos_to_neg |   pos_to_neu |
|:------------|:--------------|-----------:|-----------:|------------:|--------:|-------------:|-------------:|-------------:|
| nationality | positive      |        388 |        231 |         157 |     776 |      50      |      29.768  |     20.232   |
| ageism      | positive      |        253 |         70 |          30 |     353 |      71.6714 |      19.83   |      8.49858 |
| ableism     | positive      |        134 |        136 |          83 |     353 |      37.9603 |      38.5269 |     23.5127  |



### Type 1, Negative Attribute

| bias_type   | target_term   |   positive |   negative |   unrelated |   total |   neg_to_pos |   neg_to_neg |   neg_to_neu |
|:------------|:--------------|-----------:|-----------:|------------:|--------:|-------------:|-------------:|-------------:|
| nationality | negative      |        374 |        226 |         161 |     761 |      49.1459 |      29.6978 |      21.1564 |
| ageism      | negative      |        235 |         62 |          59 |     356 |      66.0112 |      17.4157 |      16.573  |
| ableism     | negative      |        178 |        103 |          55 |     336 |      52.9762 |      30.6548 |      16.369  |



### Type 1, Combined Attribute

| bias_type   |   positive |   negative |   unrelated |   total |      pl |      nl |     nul |
|:------------|-----------:|-----------:|------------:|--------:|--------:|--------:|--------:|
| nationality |        762 |        457 |         318 |    1537 | 49.5771 | 29.7332 | 20.6897 |
| ageism      |        488 |        132 |          89 |     709 | 68.8293 | 18.6178 | 12.5529 |
| ableism     |        312 |        239 |         138 |     689 | 45.283  | 34.688  | 20.029  |



### Type 2, Positive Attribute

| bias_type   | target_term   |   positive |   negative |   unrelated |   total |   pos_to_pos |   pos_to_neg |   pos_to_neu |
|:------------|:--------------|-----------:|-----------:|------------:|--------:|-------------:|-------------:|-------------:|
| nationality | positive      |        106 |         56 |          27 |     189 |      56.0847 |      29.6296 |      14.2857 |
| ageism      | positive      |        187 |        222 |         239 |     648 |      28.858  |      34.2593 |      36.8827 |
| ableism     | positive      |         61 |         36 |          86 |     183 |      33.3333 |      19.6721 |      46.9945 |



### Type 2, Negative Attribute

| bias_type   | target_term   |   positive |   negative |   unrelated |   total |   neg_to_pos |   neg_to_neg |   neg_to_neu |
|:------------|:--------------|-----------:|-----------:|------------:|--------:|-------------:|-------------:|-------------:|
| nationality | negative      |         84 |         49 |          35 |     168 |      50      |      29.1667 |      20.8333 |
| ageism      | negative      |        157 |        236 |         255 |     648 |      24.2284 |      36.4198 |      39.3519 |
| ableism     | negative      |         57 |         70 |          78 |     205 |      27.8049 |      34.1463 |      38.0488 |



### Type 2, Combined Attribute

| bias_type   |   positive |   negative |   unrelated |   total |      pl |      nl |     nul |
|:------------|-----------:|-----------:|------------:|--------:|--------:|--------:|--------:|
| nationality |        190 |        105 |          62 |     357 | 53.2213 | 29.4118 | 17.3669 |
| ageism      |        344 |        458 |         494 |    1296 | 26.5432 | 35.3395 | 38.1173 |
| ableism     |        118 |        106 |         164 |     388 | 30.4124 | 27.3196 | 42.268  |



### Type 1, Positive Attribute

| bias_type   | target_term   | gender        |   positive |   negative |   unrelated |   total |   pos_to_pos |   pos_to_neg |   pos_to_neu |
|:------------|:--------------|:--------------|-----------:|-----------:|------------:|--------:|-------------:|-------------:|-------------:|
| nationality | positive      | male          |        121 |         83 |          55 |     259 |      46.7181 |      32.0463 |     21.2355  |
| nationality | positive      | female        |        139 |         67 |          50 |     256 |      54.2969 |      26.1719 |     19.5312  |
| nationality | positive      | not_spacified |        128 |         81 |          52 |     261 |      49.0421 |      31.0345 |     19.9234  |
| ageism      | positive      | male          |         76 |         30 |          10 |     116 |      65.5172 |      25.8621 |      8.62069 |
| ageism      | positive      | female        |         88 |         23 |           9 |     120 |      73.3333 |      19.1667 |      7.5     |
| ageism      | positive      | not_spacified |         89 |         17 |          11 |     117 |      76.0684 |      14.5299 |      9.40171 |
| ableism     | positive      | male          |         47 |         44 |          27 |     118 |      39.8305 |      37.2881 |     22.8814  |
| ableism     | positive      | female        |         44 |         46 |          28 |     118 |      37.2881 |      38.9831 |     23.7288  |
| ableism     | positive      | not_spacified |         43 |         46 |          28 |     117 |      36.7521 |      39.3162 |     23.9316  |



### Type 1, Positive, Gender

| bias_type     |   positive |   negative |   unrelated |   total |   pos_to_pos |   pos_to_neg |   pos_to_neu |
|:--------------|-----------:|-----------:|------------:|--------:|-------------:|-------------:|-------------:|
| male          |        244 |        157 |          92 |     493 |      49.4929 |      31.8458 |      18.6613 |
| female        |        271 |        136 |          87 |     494 |      54.8583 |      27.5304 |      17.6113 |
| not_spacified |        260 |        144 |          91 |     495 |      52.5253 |      29.0909 |      18.3838 |



### Type 1, Negative Attribute

| bias_type   | target_term   | gender        |   positive |   negative |   unrelated |   total |   neg_to_pos |   neg_to_neg |   neg_to_neu |
|:------------|:--------------|:--------------|-----------:|-----------:|------------:|--------:|-------------:|-------------:|-------------:|
| nationality | negative      | male          |        115 |         85 |          53 |     253 |      45.4545 |      33.5968 |      20.9486 |
| nationality | negative      | female        |        135 |         70 |          53 |     258 |      52.3256 |      27.1318 |      20.5426 |
| nationality | negative      | not_spacified |        124 |         71 |          55 |     250 |      49.6    |      28.4    |      22      |
| ageism      | negative      | male          |         77 |         22 |          23 |     122 |      63.1148 |      18.0328 |      18.8525 |
| ageism      | negative      | female        |         85 |         18 |          17 |     120 |      70.8333 |      15      |      14.1667 |
| ageism      | negative      | not_spacified |         73 |         22 |          19 |     114 |      64.0351 |      19.2982 |      16.6667 |
| ableism     | negative      | male          |         56 |         41 |          17 |     114 |      49.1228 |      35.9649 |      14.9123 |
| ableism     | negative      | female        |         63 |         29 |          18 |     110 |      57.2727 |      26.3636 |      16.3636 |
| ableism     | negative      | not_spacified |         59 |         33 |          20 |     112 |      52.6786 |      29.4643 |      17.8571 |



### Type 1, Negative, Gender

| bias_type     |   positive |   negative |   unrelated |   total |   pos_to_pos |   pos_to_neg |   pos_to_neu |
|:--------------|-----------:|-----------:|------------:|--------:|-------------:|-------------:|-------------:|
| male          |        248 |        148 |          93 |     489 |      50.7157 |      30.2658 |      19.0184 |
| female        |        283 |        117 |          88 |     488 |      57.9918 |      23.9754 |      18.0328 |
| not_spacified |        256 |        126 |          94 |     476 |      53.7815 |      26.4706 |      19.7479 |



### Type 2, Positive Attribute

| bias_type   | target_term   | gender        |   positive |   negative |   unrelated |   total |   pos_to_pos |   pos_to_neg |   pos_to_neu |
|:------------|:--------------|:--------------|-----------:|-----------:|------------:|--------:|-------------:|-------------:|-------------:|
| nationality | positive      | male          |         39 |         18 |           8 |      65 |      60      |      27.6923 |      12.3077 |
| nationality | positive      | female        |         31 |         15 |           9 |      55 |      56.3636 |      27.2727 |      16.3636 |
| nationality | positive      | not_spacified |         36 |         23 |          10 |      69 |      52.1739 |      33.3333 |      14.4928 |
| ageism      | positive      | male          |         68 |         65 |          83 |     216 |      31.4815 |      30.0926 |      38.4259 |
| ageism      | positive      | female        |         61 |         81 |          74 |     216 |      28.2407 |      37.5    |      34.2593 |
| ageism      | positive      | not_spacified |         58 |         76 |          82 |     216 |      26.8519 |      35.1852 |      37.963  |
| ableism     | positive      | male          |         23 |          9 |          28 |      60 |      38.3333 |      15      |      46.6667 |
| ableism     | positive      | female        |         19 |         14 |          29 |      62 |      30.6452 |      22.5806 |      46.7742 |
| ableism     | positive      | not_spacified |         19 |         13 |          29 |      61 |      31.1475 |      21.3115 |      47.541  |



### Type 2, Positive, Gender

| bias_type     |   positive |   negative |   unrelated |   total |   pos_to_pos |   pos_to_neg |   pos_to_neu |
|:--------------|-----------:|-----------:|------------:|--------:|-------------:|-------------:|-------------:|
| male          |        130 |         92 |         119 |     341 |      38.1232 |      26.9795 |      34.8974 |
| female        |        111 |        110 |         112 |     333 |      33.3333 |      33.033  |      33.6336 |
| not_spacified |        113 |        112 |         121 |     346 |      32.659  |      32.3699 |      34.9711 |



### Type 2, Negative Attribute

| bias_type   | target_term   | gender        |   positive |   negative |   unrelated |   total |   neg_to_pos |   neg_to_neg |   neg_to_neu |
|:------------|:--------------|:--------------|-----------:|-----------:|------------:|--------:|-------------:|-------------:|-------------:|
| nationality | negative      | male          |         25 |         21 |          13 |      59 |      42.3729 |      35.5932 |      22.0339 |
| nationality | negative      | female        |         30 |         15 |          10 |      55 |      54.5455 |      27.2727 |      18.1818 |
| nationality | negative      | not_spacified |         29 |         13 |          12 |      54 |      53.7037 |      24.0741 |      22.2222 |
| ageism      | negative      | male          |         41 |         94 |          81 |     216 |      18.9815 |      43.5185 |      37.5    |
| ageism      | negative      | female        |         57 |         70 |          89 |     216 |      26.3889 |      32.4074 |      41.2037 |
| ageism      | negative      | not_spacified |         59 |         72 |          85 |     216 |      27.3148 |      33.3333 |      39.3519 |
| ableism     | negative      | male          |         15 |         29 |          27 |      71 |      21.1268 |      40.8451 |      38.0282 |
| ableism     | negative      | female        |         21 |         22 |          24 |      67 |      31.3433 |      32.8358 |      35.8209 |
| ableism     | negative      | not_spacified |         21 |         19 |          27 |      67 |      31.3433 |      28.3582 |      40.2985 |



### Type 2, Negative, Gender

| bias_type     |   positive |   negative |   unrelated |   total |   pos_to_pos |   pos_to_neg |   pos_to_neu |
|:--------------|-----------:|-----------:|------------:|--------:|-------------:|-------------:|-------------:|
| male          |         81 |        144 |         121 |     346 |      23.4104 |      41.6185 |      34.9711 |
| female        |        108 |        107 |         123 |     338 |      31.9527 |      31.6568 |      36.3905 |
| not_spacified |        109 |        104 |         124 |     337 |      32.3442 |      30.8605 |      36.7953 |



## Kendall Tau Calculation

Total data: 2935

Kendall's Tau Correlation for type 1: -0.025476000452739508

P-Value: 0.18701339430809838

Total data: 2041

Kendall's Tau Correlation for type 2: 0.06422191233558211

P-Value: 0.007690957092143164

## Kendall Tau Calculation considering if there are any positive likelihood towards feminine gendered pronoun

Total data: 2935

Kendall's Tau Correlation for type1 Considering more positive likelihood towards feminine gendered pronoun: 0.046867594008747154

P-Value: 0.002951050604766507

Total data: 2041

Kendall's Tau Correlation for type2 Considering more positive likelihood towards feminine gendered pronoun: 0.01789119234046006

P-Value: 0.36313375268586634


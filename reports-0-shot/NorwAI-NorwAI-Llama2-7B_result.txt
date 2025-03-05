# Report for Model: NorwAI/NorwAI-Llama2-7B

## Different Types of Likelihood Calculation

### Type 1, Positive Attribute

| bias_type   | target_term   |   positive |   negative |   unrelated |   total |   pos_to_pos |   pos_to_neg |   pos_to_neu |
|:------------|:--------------|-----------:|-----------:|------------:|--------:|-------------:|-------------:|-------------:|
| nationality | positive      |        270 |        369 |         166 |     805 |      33.5404 |      45.8385 |      20.6211 |
| ageism      | positive      |        245 |         81 |          56 |     382 |      64.1361 |      21.2042 |      14.6597 |
| ableism     | positive      |        135 |        146 |          61 |     342 |      39.4737 |      42.6901 |      17.8363 |



### Type 1, Negative Attribute

| bias_type   | target_term   |   positive |   negative |   unrelated |   total |   neg_to_pos |   neg_to_neg |   neg_to_neu |
|:------------|:--------------|-----------:|-----------:|------------:|--------:|-------------:|-------------:|-------------:|
| nationality | negative      |        243 |        382 |         177 |     802 |      30.2993 |      47.6309 |      22.0698 |
| ageism      | negative      |        220 |         87 |          71 |     378 |      58.2011 |      23.0159 |      18.7831 |
| ableism     | negative      |        165 |        123 |          56 |     344 |      47.9651 |      35.7558 |      16.2791 |



### Type 1, Combined Attribute

| bias_type   |   positive |   negative |   unrelated |   total |      pl |      nl |     nul |
|:------------|-----------:|-----------:|------------:|--------:|--------:|--------:|--------:|
| nationality |        513 |        751 |         343 |    1607 | 31.9228 | 46.733  | 21.3441 |
| ageism      |        465 |        168 |         127 |     760 | 61.1842 | 22.1053 | 16.7105 |
| ableism     |        300 |        269 |         117 |     686 | 43.7318 | 39.2128 | 17.0554 |



### Type 2, Positive Attribute

| bias_type   | target_term   |   positive |   negative |   unrelated |   total |   pos_to_pos |   pos_to_neg |   pos_to_neu |
|:------------|:--------------|-----------:|-----------:|------------:|--------:|-------------:|-------------:|-------------:|
| nationality | positive      |        172 |         87 |          92 |     351 |      49.0028 |      24.7863 |      26.2108 |
| ageism      | positive      |        198 |        252 |         198 |     648 |      30.5556 |      38.8889 |      30.5556 |
| ableism     | positive      |         67 |         64 |          47 |     178 |      37.6404 |      35.9551 |      26.4045 |



### Type 2, Negative Attribute

| bias_type   | target_term   |   positive |   negative |   unrelated |   total |   neg_to_pos |   neg_to_neg |   neg_to_neu |
|:------------|:--------------|-----------:|-----------:|------------:|--------:|-------------:|-------------:|-------------:|
| nationality | negative      |        192 |        101 |          73 |     366 |      52.459  |      27.5956 |      19.9454 |
| ageism      | negative      |        145 |        277 |         226 |     648 |      22.3765 |      42.7469 |      34.8765 |
| ableism     | negative      |         51 |         97 |          58 |     206 |      24.7573 |      47.0874 |      28.1553 |



### Type 2, Combined Attribute

| bias_type   |   positive |   negative |   unrelated |   total |      pl |      nl |     nul |
|:------------|-----------:|-----------:|------------:|--------:|--------:|--------:|--------:|
| nationality |        364 |        188 |         165 |     717 | 50.7671 | 26.2204 | 23.0126 |
| ageism      |        343 |        529 |         424 |    1296 | 26.466  | 40.8179 | 32.716  |
| ableism     |        118 |        161 |         105 |     384 | 30.7292 | 41.9271 | 27.3438 |



### Type 1, Positive Attribute

| bias_type   | target_term   | gender        |   positive |   negative |   unrelated |   total |   pos_to_pos |   pos_to_neg |   pos_to_neu |
|:------------|:--------------|:--------------|-----------:|-----------:|------------:|--------:|-------------:|-------------:|-------------:|
| nationality | positive      | male          |         92 |        122 |          50 |     264 |      34.8485 |      46.2121 |      18.9394 |
| nationality | positive      | female        |         92 |        119 |          62 |     273 |      33.6996 |      43.5897 |      22.7106 |
| nationality | positive      | not_spacified |         86 |        128 |          54 |     268 |      32.0896 |      47.7612 |      20.1493 |
| ageism      | positive      | male          |         85 |         27 |          18 |     130 |      65.3846 |      20.7692 |      13.8462 |
| ageism      | positive      | female        |         80 |         25 |          21 |     126 |      63.4921 |      19.8413 |      16.6667 |
| ageism      | positive      | not_spacified |         80 |         29 |          17 |     126 |      63.4921 |      23.0159 |      13.4921 |
| ableism     | positive      | male          |         38 |         52 |          25 |     115 |      33.0435 |      45.2174 |      21.7391 |
| ableism     | positive      | female        |         48 |         48 |          18 |     114 |      42.1053 |      42.1053 |      15.7895 |
| ableism     | positive      | not_spacified |         49 |         46 |          18 |     113 |      43.3628 |      40.708  |      15.9292 |



### Type 1, Positive, Gender

| bias_type     |   positive |   negative |   unrelated |   total |   pos_to_pos |   pos_to_neg |   pos_to_neu |
|:--------------|-----------:|-----------:|------------:|--------:|-------------:|-------------:|-------------:|
| male          |        215 |        201 |          93 |     509 |      42.2397 |      39.4892 |      18.2711 |
| female        |        220 |        192 |         101 |     513 |      42.885  |      37.4269 |      19.6881 |
| not_spacified |        215 |        203 |          89 |     507 |      42.4063 |      40.0394 |      17.5542 |



### Type 1, Negative Attribute

| bias_type   | target_term   | gender        |   positive |   negative |   unrelated |   total |   neg_to_pos |   neg_to_neg |   neg_to_neu |
|:------------|:--------------|:--------------|-----------:|-----------:|------------:|--------:|-------------:|-------------:|-------------:|
| nationality | negative      | male          |         79 |        119 |          68 |     266 |      29.6992 |      44.7368 |      25.5639 |
| nationality | negative      | female        |         79 |        131 |          56 |     266 |      29.6992 |      49.2481 |      21.0526 |
| nationality | negative      | not_spacified |         85 |        132 |          53 |     270 |      31.4815 |      48.8889 |      19.6296 |
| ageism      | negative      | male          |         72 |         28 |          28 |     128 |      56.25   |      21.875  |      21.875  |
| ageism      | negative      | female        |         75 |         28 |          23 |     126 |      59.5238 |      22.2222 |      18.254  |
| ageism      | negative      | not_spacified |         73 |         31 |          20 |     124 |      58.871  |      25      |      16.129  |
| ableism     | negative      | male          |         45 |         49 |          20 |     114 |      39.4737 |      42.9825 |      17.5439 |
| ableism     | negative      | female        |         64 |         34 |          19 |     117 |      54.7009 |      29.0598 |      16.2393 |
| ableism     | negative      | not_spacified |         56 |         40 |          17 |     113 |      49.5575 |      35.3982 |      15.0442 |



### Type 1, Negative, Gender

| bias_type     |   positive |   negative |   unrelated |   total |   pos_to_pos |   pos_to_neg |   pos_to_neu |
|:--------------|-----------:|-----------:|------------:|--------:|-------------:|-------------:|-------------:|
| male          |        196 |        196 |         116 |     508 |      38.5827 |      38.5827 |      22.8346 |
| female        |        218 |        193 |          98 |     509 |      42.8291 |      37.9175 |      19.2534 |
| not_spacified |        214 |        203 |          90 |     507 |      42.2091 |      40.0394 |      17.7515 |



### Type 2, Positive Attribute

| bias_type   | target_term   | gender        |   positive |   negative |   unrelated |   total |   pos_to_pos |   pos_to_neg |   pos_to_neu |
|:------------|:--------------|:--------------|-----------:|-----------:|------------:|--------:|-------------:|-------------:|-------------:|
| nationality | positive      | male          |         58 |         29 |          29 |     116 |      50      |      25      |      25      |
| nationality | positive      | female        |         59 |         32 |          31 |     122 |      48.3607 |      26.2295 |      25.4098 |
| nationality | positive      | not_spacified |         55 |         26 |          32 |     113 |      48.6726 |      23.0088 |      28.3186 |
| ageism      | positive      | male          |         72 |         82 |          62 |     216 |      33.3333 |      37.963  |      28.7037 |
| ageism      | positive      | female        |         63 |         87 |          66 |     216 |      29.1667 |      40.2778 |      30.5556 |
| ageism      | positive      | not_spacified |         63 |         83 |          70 |     216 |      29.1667 |      38.4259 |      32.4074 |
| ableism     | positive      | male          |         23 |         23 |          15 |      61 |      37.7049 |      37.7049 |      24.5902 |
| ableism     | positive      | female        |         23 |         22 |          14 |      59 |      38.9831 |      37.2881 |      23.7288 |
| ableism     | positive      | not_spacified |         21 |         19 |          18 |      58 |      36.2069 |      32.7586 |      31.0345 |



### Type 2, Positive, Gender

| bias_type     |   positive |   negative |   unrelated |   total |   pos_to_pos |   pos_to_neg |   pos_to_neu |
|:--------------|-----------:|-----------:|------------:|--------:|-------------:|-------------:|-------------:|
| male          |        153 |        134 |         106 |     393 |      38.9313 |      34.0967 |      26.972  |
| female        |        145 |        141 |         111 |     397 |      36.5239 |      35.5164 |      27.9597 |
| not_spacified |        139 |        128 |         120 |     387 |      35.9173 |      33.0749 |      31.0078 |



### Type 2, Negative Attribute

| bias_type   | target_term   | gender        |   positive |   negative |   unrelated |   total |   neg_to_pos |   neg_to_neg |   neg_to_neu |
|:------------|:--------------|:--------------|-----------:|-----------:|------------:|--------:|-------------:|-------------:|-------------:|
| nationality | negative      | male          |         71 |         34 |          19 |     124 |      57.2581 |      27.4194 |      15.3226 |
| nationality | negative      | female        |         62 |         34 |          27 |     123 |      50.4065 |      27.6423 |      21.9512 |
| nationality | negative      | not_spacified |         59 |         33 |          27 |     119 |      49.5798 |      27.7311 |      22.6891 |
| ageism      | negative      | male          |         56 |         91 |          69 |     216 |      25.9259 |      42.1296 |      31.9444 |
| ageism      | negative      | female        |         45 |         93 |          78 |     216 |      20.8333 |      43.0556 |      36.1111 |
| ageism      | negative      | not_spacified |         44 |         93 |          79 |     216 |      20.3704 |      43.0556 |      36.5741 |
| ableism     | negative      | male          |         13 |         35 |          19 |      67 |      19.403  |      52.2388 |      28.3582 |
| ableism     | negative      | female        |         21 |         25 |          23 |      69 |      30.4348 |      36.2319 |      33.3333 |
| ableism     | negative      | not_spacified |         17 |         37 |          16 |      70 |      24.2857 |      52.8571 |      22.8571 |



### Type 2, Negative, Gender

| bias_type     |   positive |   negative |   unrelated |   total |   pos_to_pos |   pos_to_neg |   pos_to_neu |
|:--------------|-----------:|-----------:|------------:|--------:|-------------:|-------------:|-------------:|
| male          |        140 |        160 |         107 |     407 |      34.398  |      39.312  |      26.2899 |
| female        |        128 |        152 |         128 |     408 |      31.3725 |      37.2549 |      31.3725 |
| not_spacified |        120 |        163 |         122 |     405 |      29.6296 |      40.2469 |      30.1235 |



## Kendall Tau Calculation

Total data: 3053

Kendall's Tau Correlation for type 1: 0.007183925772966703

P-Value: 0.7110153473561291

Total data: 2397

Kendall's Tau Correlation for type 2: 0.06451396187941087

P-Value: 0.0036583902262912475

## Kendall Tau Calculation considering if there are any positive likelihood towards feminine gendered pronoun

Total data: 3053

Kendall's Tau Correlation for type1 Considering more positive likelihood towards feminine gendered pronoun: 0.015212091568446473

P-Value: 0.33663290949653535

Total data: 2397

Kendall's Tau Correlation for type2 Considering more positive likelihood towards feminine gendered pronoun: -0.009886680419777956

P-Value: 0.5854915443895763


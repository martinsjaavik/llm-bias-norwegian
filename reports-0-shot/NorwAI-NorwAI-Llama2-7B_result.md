# Report for Model: NorwAI/NorwAI-Llama2-7B

## Different Types of Likelihood Calculation

### Type 1, Positive Attribute

| bias_type   | target_term   |   positive |   negative |   unrelated |   total |   pos_to_pos |   pos_to_neg |   pos_to_neu |
|:------------|:--------------|-----------:|-----------:|------------:|--------:|-------------:|-------------:|-------------:|
| nationality | positive      |        506 |        131 |         178 |     815 |      62.0859 |     16.0736  |      21.8405 |
| ageism      | positive      |        309 |         32 |          49 |     390 |      79.2308 |      8.20513 |      12.5641 |
| ableism     | positive      |        196 |         97 |          61 |     354 |      55.3672 |     27.4011  |      17.2316 |



### Type 1, Negative Attribute

| bias_type   | target_term   |   positive |   negative |   unrelated |   total |   neg_to_pos |   neg_to_neg |   neg_to_neu |
|:------------|:--------------|-----------:|-----------:|------------:|--------:|-------------:|-------------:|-------------:|
| nationality | negative      |        260 |        366 |         183 |     809 |      32.1384 |      45.241  |      22.6205 |
| ageism      | negative      |        222 |         97 |          61 |     380 |      58.4211 |      25.5263 |      16.0526 |
| ableism     | negative      |        155 |        141 |          53 |     349 |      44.4126 |      40.4011 |      15.1862 |



### Type 1, Combined Attribute

| bias_type   |   positive |   negative |   unrelated |   total |      pl |      nl |     nul |
|:------------|-----------:|-----------:|------------:|--------:|--------:|--------:|--------:|
| nationality |        766 |        497 |         361 |    1624 | 47.1675 | 30.6034 | 22.2291 |
| ageism      |        531 |        129 |         110 |     770 | 68.961  | 16.7532 | 14.2857 |
| ableism     |        351 |        238 |         114 |     703 | 49.9289 | 33.8549 | 16.2162 |



### Type 2, Positive Attribute

| bias_type   | target_term   |   positive |   negative |   unrelated |   total |   pos_to_pos |   pos_to_neg |   pos_to_neu |
|:------------|:--------------|-----------:|-----------:|------------:|--------:|-------------:|-------------:|-------------:|
| nationality | positive      |        177 |         95 |          86 |     358 |      49.4413 |      26.5363 |      24.0223 |
| ageism      | positive      |        199 |        231 |         218 |     648 |      30.7099 |      35.6481 |      33.642  |
| ableism     | positive      |         63 |         64 |          54 |     181 |      34.8066 |      35.3591 |      29.8343 |



### Type 2, Negative Attribute

| bias_type   | target_term   |   positive |   negative |   unrelated |   total |   neg_to_pos |   neg_to_neg |   neg_to_neu |
|:------------|:--------------|-----------:|-----------:|------------:|--------:|-------------:|-------------:|-------------:|
| nationality | negative      |        198 |        102 |          62 |     362 |      54.6961 |      28.1768 |      17.1271 |
| ageism      | negative      |        161 |        294 |         193 |     648 |      24.8457 |      45.3704 |      29.784  |
| ableism     | negative      |         70 |         81 |          55 |     206 |      33.9806 |      39.3204 |      26.699  |



### Type 2, Combined Attribute

| bias_type   |   positive |   negative |   unrelated |   total |      pl |      nl |     nul |
|:------------|-----------:|-----------:|------------:|--------:|--------:|--------:|--------:|
| nationality |        375 |        197 |         148 |     720 | 52.0833 | 27.3611 | 20.5556 |
| ageism      |        360 |        525 |         411 |    1296 | 27.7778 | 40.5093 | 31.713  |
| ableism     |        133 |        145 |         109 |     387 | 34.3669 | 37.4677 | 28.1654 |



### Type 1, Positive Attribute

| bias_type   | target_term   | gender        |   positive |   negative |   unrelated |   total |   pos_to_pos |   pos_to_neg |   pos_to_neu |
|:------------|:--------------|:--------------|-----------:|-----------:|------------:|--------:|-------------:|-------------:|-------------:|
| nationality | positive      | male          |        165 |         40 |          65 |     270 |      61.1111 |     14.8148  |      24.0741 |
| nationality | positive      | female        |        171 |         42 |          59 |     272 |      62.8676 |     15.4412  |      21.6912 |
| nationality | positive      | not_spacified |        170 |         49 |          54 |     273 |      62.2711 |     17.9487  |      19.7802 |
| ageism      | positive      | male          |        107 |          8 |          16 |     131 |      81.6794 |      6.10687 |      12.2137 |
| ageism      | positive      | female        |        105 |         10 |          18 |     133 |      78.9474 |      7.5188  |      13.5338 |
| ageism      | positive      | not_spacified |         97 |         14 |          15 |     126 |      76.9841 |     11.1111  |      11.9048 |
| ableism     | positive      | male          |         62 |         34 |          22 |     118 |      52.5424 |     28.8136  |      18.6441 |
| ableism     | positive      | female        |         66 |         29 |          24 |     119 |      55.4622 |     24.3697  |      20.1681 |
| ableism     | positive      | not_spacified |         68 |         34 |          15 |     117 |      58.1197 |     29.0598  |      12.8205 |



### Type 1, Positive, Gender

| bias_type     |   positive |   negative |   unrelated |   total |   pos_to_pos |   pos_to_neg |   pos_to_neu |
|:--------------|-----------:|-----------:|------------:|--------:|-------------:|-------------:|-------------:|
| male          |        334 |         82 |         103 |     519 |      64.3545 |      15.7996 |      19.8459 |
| female        |        342 |         81 |         101 |     524 |      65.2672 |      15.458  |      19.2748 |
| not_spacified |        335 |         97 |          84 |     516 |      64.9225 |      18.7984 |      16.2791 |



### Type 1, Negative Attribute

| bias_type   | target_term   | gender        |   positive |   negative |   unrelated |   total |   neg_to_pos |   neg_to_neg |   neg_to_neu |
|:------------|:--------------|:--------------|-----------:|-----------:|------------:|--------:|-------------:|-------------:|-------------:|
| nationality | negative      | male          |         86 |        123 |          58 |     267 |      32.2097 |      46.0674 |      21.7228 |
| nationality | negative      | female        |         89 |        123 |          61 |     273 |      32.6007 |      45.0549 |      22.3443 |
| nationality | negative      | not_spacified |         85 |        120 |          64 |     269 |      31.5985 |      44.6097 |      23.7918 |
| ageism      | negative      | male          |         74 |         29 |          24 |     127 |      58.2677 |      22.8346 |      18.8976 |
| ageism      | negative      | female        |         76 |         35 |          17 |     128 |      59.375  |      27.3438 |      13.2812 |
| ageism      | negative      | not_spacified |         72 |         33 |          20 |     125 |      57.6    |      26.4    |      16      |
| ableism     | negative      | male          |         49 |         46 |          18 |     113 |      43.3628 |      40.708  |      15.9292 |
| ableism     | negative      | female        |         52 |         46 |          16 |     114 |      45.614  |      40.3509 |      14.0351 |
| ableism     | negative      | not_spacified |         54 |         49 |          19 |     122 |      44.2623 |      40.1639 |      15.5738 |



### Type 1, Negative, Gender

| bias_type     |   positive |   negative |   unrelated |   total |   pos_to_pos |   pos_to_neg |   pos_to_neu |
|:--------------|-----------:|-----------:|------------:|--------:|-------------:|-------------:|-------------:|
| male          |        209 |        198 |         100 |     507 |      41.2229 |      39.0533 |      19.7239 |
| female        |        217 |        204 |          94 |     515 |      42.1359 |      39.6117 |      18.2524 |
| not_spacified |        211 |        202 |         103 |     516 |      40.8915 |      39.1473 |      19.9612 |



### Type 2, Positive Attribute

| bias_type   | target_term   | gender        |   positive |   negative |   unrelated |   total |   pos_to_pos |   pos_to_neg |   pos_to_neu |
|:------------|:--------------|:--------------|-----------:|-----------:|------------:|--------:|-------------:|-------------:|-------------:|
| nationality | positive      | male          |         58 |         32 |          29 |     119 |      48.7395 |      26.8908 |      24.3697 |
| nationality | positive      | female        |         56 |         30 |          31 |     117 |      47.8632 |      25.641  |      26.4957 |
| nationality | positive      | not_spacified |         63 |         33 |          26 |     122 |      51.6393 |      27.0492 |      21.3115 |
| ageism      | positive      | male          |         55 |         86 |          75 |     216 |      25.463  |      39.8148 |      34.7222 |
| ageism      | positive      | female        |         72 |         69 |          75 |     216 |      33.3333 |      31.9444 |      34.7222 |
| ageism      | positive      | not_spacified |         72 |         76 |          68 |     216 |      33.3333 |      35.1852 |      31.4815 |
| ableism     | positive      | male          |         21 |         17 |          21 |      59 |      35.5932 |      28.8136 |      35.5932 |
| ableism     | positive      | female        |         22 |         23 |          17 |      62 |      35.4839 |      37.0968 |      27.4194 |
| ableism     | positive      | not_spacified |         20 |         24 |          16 |      60 |      33.3333 |      40      |      26.6667 |



### Type 2, Positive, Gender

| bias_type     |   positive |   negative |   unrelated |   total |   pos_to_pos |   pos_to_neg |   pos_to_neu |
|:--------------|-----------:|-----------:|------------:|--------:|-------------:|-------------:|-------------:|
| male          |        134 |        135 |         125 |     394 |      34.0102 |      34.264  |      31.7259 |
| female        |        150 |        122 |         123 |     395 |      37.9747 |      30.8861 |      31.1392 |
| not_spacified |        155 |        133 |         110 |     398 |      38.9447 |      33.4171 |      27.6382 |



### Type 2, Negative Attribute

| bias_type   | target_term   | gender        |   positive |   negative |   unrelated |   total |   neg_to_pos |   neg_to_neg |   neg_to_neu |
|:------------|:--------------|:--------------|-----------:|-----------:|------------:|--------:|-------------:|-------------:|-------------:|
| nationality | negative      | male          |         68 |         36 |          15 |     119 |      57.1429 |      30.2521 |      12.605  |
| nationality | negative      | female        |         70 |         24 |          27 |     121 |      57.8512 |      19.8347 |      22.314  |
| nationality | negative      | not_spacified |         60 |         42 |          20 |     122 |      49.1803 |      34.4262 |      16.3934 |
| ageism      | negative      | male          |         47 |        106 |          63 |     216 |      21.7593 |      49.0741 |      29.1667 |
| ageism      | negative      | female        |         64 |         85 |          67 |     216 |      29.6296 |      39.3519 |      31.0185 |
| ageism      | negative      | not_spacified |         50 |        103 |          63 |     216 |      23.1481 |      47.6852 |      29.1667 |
| ableism     | negative      | male          |         23 |         24 |          19 |      66 |      34.8485 |      36.3636 |      28.7879 |
| ableism     | negative      | female        |         28 |         26 |          16 |      70 |      40      |      37.1429 |      22.8571 |
| ableism     | negative      | not_spacified |         19 |         31 |          20 |      70 |      27.1429 |      44.2857 |      28.5714 |



### Type 2, Negative, Gender

| bias_type     |   positive |   negative |   unrelated |   total |   pos_to_pos |   pos_to_neg |   pos_to_neu |
|:--------------|-----------:|-----------:|------------:|--------:|-------------:|-------------:|-------------:|
| male          |        138 |        166 |          97 |     401 |      34.414  |      41.3965 |      24.1895 |
| female        |        162 |        135 |         110 |     407 |      39.8034 |      33.1695 |      27.027  |
| not_spacified |        129 |        176 |         103 |     408 |      31.6176 |      43.1373 |      25.2451 |



## Kendall Tau Calculation

Total data: 3097

Kendall's Tau Correlation for type 1: 0.27464869864271246

P-Value: 2.5089310430677146e-48

Total data: 2403

Kendall's Tau Correlation for type 2: 0.05158415346055328

P-Value: 0.01989714011203004

## Kendall Tau Calculation considering if there are any positive likelihood towards feminine gendered pronoun

Total data: 3097

Kendall's Tau Correlation for type1 Considering more positive likelihood towards feminine gendered pronoun: 0.00381247426733653

P-Value: 0.8038712863943286

Total data: 2403

Kendall's Tau Correlation for type2 Considering more positive likelihood towards feminine gendered pronoun: 0.044678858044173875

P-Value: 0.013524583637404539


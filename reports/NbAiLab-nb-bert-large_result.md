# Report for Model: NbAiLab/nb-bert-large

## Different Types of Likelihood Calculation

### Type 1, Positive Attribute

| bias_type   | target_term   |   positive |   negative |   unrelated |   total |   pos_to_pos |   pos_to_neg |   pos_to_neu |
|:------------|:--------------|-----------:|-----------:|------------:|--------:|-------------:|-------------:|-------------:|
| nationality | positive      |        394 |        258 |         203 |     855 |      46.0819 |      30.1754 |      23.7427 |
| ageism      | positive      |        193 |         94 |         142 |     429 |      44.9883 |      21.9114 |      33.1002 |
| ableism     | positive      |        166 |         79 |         151 |     396 |      41.9192 |      19.9495 |      38.1313 |



### Type 1, Negative Attribute

| bias_type   | target_term   |   positive |   negative |   unrelated |   total |   neg_to_pos |   neg_to_neg |   neg_to_neu |
|:------------|:--------------|-----------:|-----------:|------------:|--------:|-------------:|-------------:|-------------:|
| nationality | negative      |        435 |        236 |         184 |     855 |      50.8772 |      27.6023 |      21.5205 |
| ageism      | negative      |        190 |        110 |         128 |     428 |      44.3925 |      25.7009 |      29.9065 |
| ableism     | negative      |        144 |        113 |         139 |     396 |      36.3636 |      28.5354 |      35.101  |



### Type 1, Combined Attribute

| bias_type   |   positive |   negative |   unrelated |   total |      pl |      nl |     nul |
|:------------|-----------:|-----------:|------------:|--------:|--------:|--------:|--------:|
| nationality |        829 |        494 |         387 |    1710 | 48.4795 | 28.8889 | 22.6316 |
| ageism      |        383 |        204 |         270 |     857 | 44.6908 | 23.804  | 31.5053 |
| ableism     |        310 |        192 |         290 |     792 | 39.1414 | 24.2424 | 36.6162 |



### Type 2, Positive Attribute

| bias_type   | target_term   |   positive |   negative |   unrelated |   total |   pos_to_pos |   pos_to_neg |   pos_to_neu |
|:------------|:--------------|-----------:|-----------:|------------:|--------:|-------------:|-------------:|-------------:|
| nationality | positive      |        271 |         50 |          75 |     396 |      68.4343 |     12.6263  |      18.9394 |
| ageism      | positive      |        424 |         61 |         163 |     648 |      65.4321 |      9.41358 |      25.1543 |
| ableism     | positive      |         55 |         73 |          70 |     198 |      27.7778 |     36.8687  |      35.3535 |



### Type 2, Negative Attribute

| bias_type   | target_term   |   positive |   negative |   unrelated |   total |   neg_to_pos |   neg_to_neg |   neg_to_neu |
|:------------|:--------------|-----------:|-----------:|------------:|--------:|-------------:|-------------:|-------------:|
| nationality | negative      |        201 |        105 |          89 |     395 |      50.8861 |      26.5823 |      22.5316 |
| ageism      | negative      |        434 |         43 |         171 |     648 |      66.9753 |       6.6358 |      26.3889 |
| ableism     | negative      |         79 |         81 |          71 |     231 |      34.1991 |      35.0649 |      30.7359 |



### Type 2, Combined Attribute

| bias_type   |   positive |   negative |   unrelated |   total |      pl |       nl |     nul |
|:------------|-----------:|-----------:|------------:|--------:|--------:|---------:|--------:|
| nationality |        472 |        155 |         164 |     791 | 59.6713 | 19.5954  | 20.7332 |
| ageism      |        858 |        104 |         334 |    1296 | 66.2037 |  8.02469 | 25.7716 |
| ableism     |        134 |        154 |         141 |     429 | 31.2354 | 35.8974  | 32.8671 |



### Type 1, Positive Attribute

| bias_type   | target_term   | gender        |   positive |   negative |   unrelated |   total |   pos_to_pos |   pos_to_neg |   pos_to_neu |
|:------------|:--------------|:--------------|-----------:|-----------:|------------:|--------:|-------------:|-------------:|-------------:|
| nationality | positive      | male          |        126 |         89 |          70 |     285 |      44.2105 |      31.2281 |      24.5614 |
| nationality | positive      | female        |        128 |         87 |          70 |     285 |      44.9123 |      30.5263 |      24.5614 |
| nationality | positive      | not_spacified |        140 |         82 |          63 |     285 |      49.1228 |      28.7719 |      22.1053 |
| ageism      | positive      | male          |         69 |         23 |          51 |     143 |      48.2517 |      16.0839 |      35.6643 |
| ageism      | positive      | female        |         71 |         26 |          46 |     143 |      49.6503 |      18.1818 |      32.1678 |
| ageism      | positive      | not_spacified |         53 |         45 |          45 |     143 |      37.0629 |      31.4685 |      31.4685 |
| ableism     | positive      | male          |         56 |         25 |          51 |     132 |      42.4242 |      18.9394 |      38.6364 |
| ableism     | positive      | female        |         54 |         24 |          54 |     132 |      40.9091 |      18.1818 |      40.9091 |
| ableism     | positive      | not_spacified |         56 |         30 |          46 |     132 |      42.4242 |      22.7273 |      34.8485 |



### Type 1, Positive, Gender

| bias_type     |   positive |   negative |   unrelated |   total |   pos_to_pos |   pos_to_neg |   pos_to_neu |
|:--------------|-----------:|-----------:|------------:|--------:|-------------:|-------------:|-------------:|
| male          |        251 |        137 |         172 |     560 |      44.8214 |      24.4643 |      30.7143 |
| female        |        253 |        137 |         170 |     560 |      45.1786 |      24.4643 |      30.3571 |
| not_spacified |        249 |        157 |         154 |     560 |      44.4643 |      28.0357 |      27.5    |



### Type 1, Negative Attribute

| bias_type   | target_term   | gender        |   positive |   negative |   unrelated |   total |   neg_to_pos |   neg_to_neg |   neg_to_neu |
|:------------|:--------------|:--------------|-----------:|-----------:|------------:|--------:|-------------:|-------------:|-------------:|
| nationality | negative      | male          |        134 |         80 |          71 |     285 |      47.0175 |      28.0702 |      24.9123 |
| nationality | negative      | female        |        147 |         82 |          56 |     285 |      51.5789 |      28.7719 |      19.6491 |
| nationality | negative      | not_spacified |        154 |         74 |          57 |     285 |      54.0351 |      25.9649 |      20      |
| ageism      | negative      | male          |         65 |         36 |          42 |     143 |      45.4545 |      25.1748 |      29.3706 |
| ageism      | negative      | female        |         66 |         36 |          41 |     143 |      46.1538 |      25.1748 |      28.6713 |
| ageism      | negative      | not_spacified |         59 |         38 |          45 |     142 |      41.5493 |      26.7606 |      31.6901 |
| ableism     | negative      | male          |         49 |         36 |          47 |     132 |      37.1212 |      27.2727 |      35.6061 |
| ableism     | negative      | female        |         45 |         38 |          49 |     132 |      34.0909 |      28.7879 |      37.1212 |
| ableism     | negative      | not_spacified |         50 |         39 |          43 |     132 |      37.8788 |      29.5455 |      32.5758 |



### Type 1, Negative, Gender

| bias_type     |   positive |   negative |   unrelated |   total |   pos_to_pos |   pos_to_neg |   pos_to_neu |
|:--------------|-----------:|-----------:|------------:|--------:|-------------:|-------------:|-------------:|
| male          |        248 |        152 |         160 |     560 |      44.2857 |      27.1429 |      28.5714 |
| female        |        258 |        156 |         146 |     560 |      46.0714 |      27.8571 |      26.0714 |
| not_spacified |        263 |        151 |         145 |     559 |      47.0483 |      27.0125 |      25.9392 |



### Type 2, Positive Attribute

| bias_type   | target_term   | gender        |   positive |   negative |   unrelated |   total |   pos_to_pos |   pos_to_neg |   pos_to_neu |
|:------------|:--------------|:--------------|-----------:|-----------:|------------:|--------:|-------------:|-------------:|-------------:|
| nationality | positive      | male          |         87 |         16 |          29 |     132 |      65.9091 |     12.1212  |      21.9697 |
| nationality | positive      | female        |         91 |         17 |          24 |     132 |      68.9394 |     12.8788  |      18.1818 |
| nationality | positive      | not_spacified |         93 |         17 |          22 |     132 |      70.4545 |     12.8788  |      16.6667 |
| ageism      | positive      | male          |        149 |         14 |          53 |     216 |      68.9815 |      6.48148 |      24.537  |
| ageism      | positive      | female        |        137 |         12 |          67 |     216 |      63.4259 |      5.55556 |      31.0185 |
| ageism      | positive      | not_spacified |        138 |         35 |          43 |     216 |      63.8889 |     16.2037  |      19.9074 |
| ableism     | positive      | male          |         20 |         24 |          22 |      66 |      30.303  |     36.3636  |      33.3333 |
| ableism     | positive      | female        |         18 |         25 |          23 |      66 |      27.2727 |     37.8788  |      34.8485 |
| ableism     | positive      | not_spacified |         17 |         24 |          25 |      66 |      25.7576 |     36.3636  |      37.8788 |



### Type 2, Positive, Gender

| bias_type     |   positive |   negative |   unrelated |   total |   pos_to_pos |   pos_to_neg |   pos_to_neu |
|:--------------|-----------:|-----------:|------------:|--------:|-------------:|-------------:|-------------:|
| male          |        256 |         54 |         104 |     414 |      61.8357 |      13.0435 |      25.1208 |
| female        |        246 |         54 |         114 |     414 |      59.4203 |      13.0435 |      27.5362 |
| not_spacified |        248 |         76 |          90 |     414 |      59.9034 |      18.3575 |      21.7391 |



### Type 2, Negative Attribute

| bias_type   | target_term   | gender        |   positive |   negative |   unrelated |   total |   neg_to_pos |   neg_to_neg |   neg_to_neu |
|:------------|:--------------|:--------------|-----------:|-----------:|------------:|--------:|-------------:|-------------:|-------------:|
| nationality | negative      | male          |         69 |         33 |          30 |     132 |      52.2727 |     25       |      22.7273 |
| nationality | negative      | female        |         67 |         35 |          29 |     131 |      51.145  |     26.7176  |      22.1374 |
| nationality | negative      | not_spacified |         65 |         37 |          30 |     132 |      49.2424 |     28.0303  |      22.7273 |
| ageism      | negative      | male          |        153 |         14 |          49 |     216 |      70.8333 |      6.48148 |      22.6852 |
| ageism      | negative      | female        |        138 |          8 |          70 |     216 |      63.8889 |      3.7037  |      32.4074 |
| ageism      | negative      | not_spacified |        143 |         21 |          52 |     216 |      66.2037 |      9.72222 |      24.0741 |
| ableism     | negative      | male          |         26 |         28 |          23 |      77 |      33.7662 |     36.3636  |      29.8701 |
| ableism     | negative      | female        |         24 |         29 |          24 |      77 |      31.1688 |     37.6623  |      31.1688 |
| ableism     | negative      | not_spacified |         29 |         24 |          24 |      77 |      37.6623 |     31.1688  |      31.1688 |



### Type 2, Negative, Gender

| bias_type     |   positive |   negative |   unrelated |   total |   pos_to_pos |   pos_to_neg |   pos_to_neu |
|:--------------|-----------:|-----------:|------------:|--------:|-------------:|-------------:|-------------:|
| male          |        248 |         75 |         102 |     425 |      58.3529 |      17.6471 |      24      |
| female        |        229 |         72 |         123 |     424 |      54.0094 |      16.9811 |      29.0094 |
| not_spacified |        237 |         82 |         106 |     425 |      55.7647 |      19.2941 |      24.9412 |



## Kendall Tau Calculation

Total data: 3359

Kendall's Tau Correlation for type 1: 0.0020030345086507603

P-Value: 0.9139786713624085

Total data: 2516

Kendall's Tau Correlation for type 2: 0.04950194747258247

P-Value: 0.015053081971943192

## Kendall Tau Calculation considering if there are any positive likelihood towards feminine gendered pronoun

Total data: 3359

Kendall's Tau Correlation for type1 Considering more positive likelihood towards feminine gendered pronoun: 0.003933038024596732

P-Value: 0.7950391262328905

Total data: 2516

Kendall's Tau Correlation for type2 Considering more positive likelihood towards feminine gendered pronoun: -0.017804967129291454

P-Value: 0.2842352252597482


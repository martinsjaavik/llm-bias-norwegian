# Report for Model: ltg/norbert3-large

## Different Types of Likelihood Calculation

### Type 1, Positive Attribute

| bias_type   | target_term   |   positive |   negative |   unrelated |   total |   pos_to_pos |   pos_to_neg |   pos_to_neu |
|:------------|:--------------|-----------:|-----------:|------------:|--------:|-------------:|-------------:|-------------:|
| nationality | positive      |        378 |        113 |         364 |     855 |      44.2105 |      13.2164 |      42.5731 |
| ageism      | positive      |        247 |         51 |         131 |     429 |      57.5758 |      11.8881 |      30.5361 |
| ableism     | positive      |        104 |        147 |         145 |     396 |      26.2626 |      37.1212 |      36.6162 |



### Type 1, Negative Attribute

| bias_type   | target_term   |   positive |   negative |   unrelated |   total |   neg_to_pos |   neg_to_neg |   neg_to_neu |
|:------------|:--------------|-----------:|-----------:|------------:|--------:|-------------:|-------------:|-------------:|
| nationality | negative      |        342 |        139 |         374 |     855 |      40      |      16.2573 |      43.7427 |
| ageism      | negative      |        211 |         76 |         141 |     428 |      49.2991 |      17.757  |      32.9439 |
| ableism     | negative      |        120 |        138 |         138 |     396 |      30.303  |      34.8485 |      34.8485 |



### Type 1, Combined Attribute

| bias_type   |   positive |   negative |   unrelated |   total |      pl |      nl |     nul |
|:------------|-----------:|-----------:|------------:|--------:|--------:|--------:|--------:|
| nationality |        720 |        252 |         738 |    1710 | 42.1053 | 14.7368 | 43.1579 |
| ageism      |        458 |        127 |         272 |     857 | 53.4422 | 14.8191 | 31.7386 |
| ableism     |        224 |        285 |         283 |     792 | 28.2828 | 35.9848 | 35.7323 |



### Type 2, Positive Attribute

| bias_type   | target_term   |   positive |   negative |   unrelated |   total |   pos_to_pos |   pos_to_neg |   pos_to_neu |
|:------------|:--------------|-----------:|-----------:|------------:|--------:|-------------:|-------------:|-------------:|
| nationality | positive      |        130 |        121 |         145 |     396 |      32.8283 |      30.5556 |      36.6162 |
| ageism      | positive      |        177 |        283 |         188 |     648 |      27.3148 |      43.6728 |      29.0123 |
| ableism     | positive      |         97 |         62 |          39 |     198 |      48.9899 |      31.3131 |      19.697  |



### Type 2, Negative Attribute

| bias_type   | target_term   |   positive |   negative |   unrelated |   total |   neg_to_pos |   neg_to_neg |   neg_to_neu |
|:------------|:--------------|-----------:|-----------:|------------:|--------:|-------------:|-------------:|-------------:|
| nationality | negative      |        116 |        141 |         138 |     395 |      29.3671 |      35.6962 |      34.9367 |
| ageism      | negative      |        215 |        233 |         200 |     648 |      33.179  |      35.9568 |      30.8642 |
| ableism     | negative      |        104 |         78 |          49 |     231 |      45.0216 |      33.7662 |      21.2121 |



### Type 2, Combined Attribute

| bias_type   |   positive |   negative |   unrelated |   total |      pl |      nl |     nul |
|:------------|-----------:|-----------:|------------:|--------:|--------:|--------:|--------:|
| nationality |        246 |        262 |         283 |     791 | 31.0999 | 33.1226 | 35.7775 |
| ageism      |        392 |        516 |         388 |    1296 | 30.2469 | 39.8148 | 29.9383 |
| ableism     |        201 |        140 |          88 |     429 | 46.8531 | 32.634  | 20.5128 |



### Type 1, Positive Attribute

| bias_type   | target_term   | gender        |   positive |   negative |   unrelated |   total |   pos_to_pos |   pos_to_neg |   pos_to_neu |
|:------------|:--------------|:--------------|-----------:|-----------:|------------:|--------:|-------------:|-------------:|-------------:|
| nationality | positive      | male          |        120 |         43 |         122 |     285 |      42.1053 |     15.0877  |      42.807  |
| nationality | positive      | female        |        124 |         30 |         131 |     285 |      43.5088 |     10.5263  |      45.9649 |
| nationality | positive      | not_spacified |        134 |         40 |         111 |     285 |      47.0175 |     14.0351  |      38.9474 |
| ageism      | positive      | male          |         85 |         14 |          44 |     143 |      59.4406 |      9.79021 |      30.7692 |
| ageism      | positive      | female        |         87 |         16 |          40 |     143 |      60.8392 |     11.1888  |      27.972  |
| ageism      | positive      | not_spacified |         75 |         21 |          47 |     143 |      52.4476 |     14.6853  |      32.8671 |
| ableism     | positive      | male          |         35 |         47 |          50 |     132 |      26.5152 |     35.6061  |      37.8788 |
| ableism     | positive      | female        |         35 |         47 |          50 |     132 |      26.5152 |     35.6061  |      37.8788 |
| ableism     | positive      | not_spacified |         34 |         53 |          45 |     132 |      25.7576 |     40.1515  |      34.0909 |



### Type 1, Positive, Gender

| bias_type     |   positive |   negative |   unrelated |   total |   pos_to_pos |   pos_to_neg |   pos_to_neu |
|:--------------|-----------:|-----------:|------------:|--------:|-------------:|-------------:|-------------:|
| male          |        240 |        104 |         216 |     560 |      42.8571 |      18.5714 |      38.5714 |
| female        |        246 |         93 |         221 |     560 |      43.9286 |      16.6071 |      39.4643 |
| not_spacified |        243 |        114 |         203 |     560 |      43.3929 |      20.3571 |      36.25   |



### Type 1, Negative Attribute

| bias_type   | target_term   | gender        |   positive |   negative |   unrelated |   total |   neg_to_pos |   neg_to_neg |   neg_to_neu |
|:------------|:--------------|:--------------|-----------:|-----------:|------------:|--------:|-------------:|-------------:|-------------:|
| nationality | negative      | male          |        113 |         48 |         124 |     285 |      39.6491 |      16.8421 |      43.5088 |
| nationality | negative      | female        |        106 |         46 |         133 |     285 |      37.193  |      16.1404 |      46.6667 |
| nationality | negative      | not_spacified |        123 |         45 |         117 |     285 |      43.1579 |      15.7895 |      41.0526 |
| ageism      | negative      | male          |         71 |         25 |          47 |     143 |      49.6503 |      17.4825 |      32.8671 |
| ageism      | negative      | female        |         71 |         27 |          45 |     143 |      49.6503 |      18.8811 |      31.4685 |
| ageism      | negative      | not_spacified |         69 |         24 |          49 |     142 |      48.5915 |      16.9014 |      34.507  |
| ableism     | negative      | male          |         38 |         45 |          49 |     132 |      28.7879 |      34.0909 |      37.1212 |
| ableism     | negative      | female        |         41 |         44 |          47 |     132 |      31.0606 |      33.3333 |      35.6061 |
| ableism     | negative      | not_spacified |         41 |         49 |          42 |     132 |      31.0606 |      37.1212 |      31.8182 |



### Type 1, Negative, Gender

| bias_type     |   positive |   negative |   unrelated |   total |   pos_to_pos |   pos_to_neg |   pos_to_neu |
|:--------------|-----------:|-----------:|------------:|--------:|-------------:|-------------:|-------------:|
| male          |        222 |        118 |         220 |     560 |      39.6429 |      21.0714 |      39.2857 |
| female        |        218 |        117 |         225 |     560 |      38.9286 |      20.8929 |      40.1786 |
| not_spacified |        233 |        118 |         208 |     559 |      41.6816 |      21.1091 |      37.2093 |



### Type 2, Positive Attribute

| bias_type   | target_term   | gender        |   positive |   negative |   unrelated |   total |   pos_to_pos |   pos_to_neg |   pos_to_neu |
|:------------|:--------------|:--------------|-----------:|-----------:|------------:|--------:|-------------:|-------------:|-------------:|
| nationality | positive      | male          |         42 |         41 |          49 |     132 |      31.8182 |      31.0606 |      37.1212 |
| nationality | positive      | female        |         44 |         39 |          49 |     132 |      33.3333 |      29.5455 |      37.1212 |
| nationality | positive      | not_spacified |         44 |         41 |          47 |     132 |      33.3333 |      31.0606 |      35.6061 |
| ageism      | positive      | male          |         56 |         89 |          71 |     216 |      25.9259 |      41.2037 |      32.8704 |
| ageism      | positive      | female        |         62 |         92 |          62 |     216 |      28.7037 |      42.5926 |      28.7037 |
| ageism      | positive      | not_spacified |         59 |        102 |          55 |     216 |      27.3148 |      47.2222 |      25.463  |
| ableism     | positive      | male          |         33 |         20 |          13 |      66 |      50      |      30.303  |      19.697  |
| ableism     | positive      | female        |         30 |         23 |          13 |      66 |      45.4545 |      34.8485 |      19.697  |
| ableism     | positive      | not_spacified |         34 |         19 |          13 |      66 |      51.5152 |      28.7879 |      19.697  |



### Type 2, Positive, Gender

| bias_type     |   positive |   negative |   unrelated |   total |   pos_to_pos |   pos_to_neg |   pos_to_neu |
|:--------------|-----------:|-----------:|------------:|--------:|-------------:|-------------:|-------------:|
| male          |        131 |        150 |         133 |     414 |      31.6425 |      36.2319 |      32.1256 |
| female        |        136 |        154 |         124 |     414 |      32.8502 |      37.1981 |      29.9517 |
| not_spacified |        137 |        162 |         115 |     414 |      33.0918 |      39.1304 |      27.7778 |



### Type 2, Negative Attribute

| bias_type   | target_term   | gender        |   positive |   negative |   unrelated |   total |   neg_to_pos |   neg_to_neg |   neg_to_neu |
|:------------|:--------------|:--------------|-----------:|-----------:|------------:|--------:|-------------:|-------------:|-------------:|
| nationality | negative      | male          |         39 |         46 |          47 |     132 |      29.5455 |      34.8485 |      35.6061 |
| nationality | negative      | female        |         41 |         45 |          45 |     131 |      31.2977 |      34.3511 |      34.3511 |
| nationality | negative      | not_spacified |         36 |         50 |          46 |     132 |      27.2727 |      37.8788 |      34.8485 |
| ageism      | negative      | male          |         74 |         73 |          69 |     216 |      34.2593 |      33.7963 |      31.9444 |
| ageism      | negative      | female        |         74 |         68 |          74 |     216 |      34.2593 |      31.4815 |      34.2593 |
| ageism      | negative      | not_spacified |         67 |         92 |          57 |     216 |      31.0185 |      42.5926 |      26.3889 |
| ableism     | negative      | male          |         35 |         27 |          15 |      77 |      45.4545 |      35.0649 |      19.4805 |
| ableism     | negative      | female        |         35 |         27 |          15 |      77 |      45.4545 |      35.0649 |      19.4805 |
| ableism     | negative      | not_spacified |         34 |         24 |          19 |      77 |      44.1558 |      31.1688 |      24.6753 |



### Type 2, Negative, Gender

| bias_type     |   positive |   negative |   unrelated |   total |   pos_to_pos |   pos_to_neg |   pos_to_neu |
|:--------------|-----------:|-----------:|------------:|--------:|-------------:|-------------:|-------------:|
| male          |        148 |        146 |         131 |     425 |      34.8235 |      34.3529 |      30.8235 |
| female        |        150 |        140 |         134 |     424 |      35.3774 |      33.0189 |      31.6038 |
| not_spacified |        137 |        166 |         122 |     425 |      32.2353 |      39.0588 |      28.7059 |



## Kendall Tau Calculation

Total data: 3359

Kendall's Tau Correlation for type 1: 0.041190897963029126

P-Value: 0.026027395134562623

Total data: 2516

Kendall's Tau Correlation for type 2: -0.02386759713983131

P-Value: 0.27098419534031415

## Kendall Tau Calculation considering if there are any positive likelihood towards feminine gendered pronoun

Total data: 3359

Kendall's Tau Correlation for type1 Considering more positive likelihood towards feminine gendered pronoun: 0.005100293090036135

P-Value: 0.735710364685701

Total data: 2516

Kendall's Tau Correlation for type2 Considering more positive likelihood towards feminine gendered pronoun: 0.0045292007147894175

P-Value: 0.7980924673810887


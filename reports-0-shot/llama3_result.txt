# Report for Model: llama3

## Different Types of Likelihood Calculation

### Type 1, Positive Attribute

| bias_type   | target_term   |   positive |   negative |   unrelated |   total |   pos_to_pos |   pos_to_neg |   pos_to_neu |
|:------------|:--------------|-----------:|-----------:|------------:|--------:|-------------:|-------------:|-------------:|
| nationality | positive      |        357 |        292 |         163 |     812 |      43.9655 |      35.9606 |      20.0739 |
| ageism      | positive      |        195 |         86 |         105 |     386 |      50.5181 |      22.2798 |      27.2021 |
| ableism     | positive      |        115 |        161 |          89 |     365 |      31.5068 |      44.1096 |      24.3836 |



### Type 1, Negative Attribute

| bias_type   | target_term   |   positive |   negative |   unrelated |   total |   neg_to_pos |   neg_to_neg |   neg_to_neu |
|:------------|:--------------|-----------:|-----------:|------------:|--------:|-------------:|-------------:|-------------:|
| nationality | negative      |        199 |        481 |         146 |     826 |      24.092  |      58.2324 |      17.6755 |
| ageism      | negative      |        136 |        160 |          97 |     393 |      34.6056 |      40.7125 |      24.6819 |
| ableism     | negative      |         95 |        180 |          93 |     368 |      25.8152 |      48.913  |      25.2717 |



### Type 1, Combined Attribute

| bias_type   |   positive |   negative |   unrelated |   total |      pl |      nl |     nul |
|:------------|-----------:|-----------:|------------:|--------:|--------:|--------:|--------:|
| nationality |        556 |        773 |         309 |    1638 | 33.9438 | 47.1917 | 18.8645 |
| ageism      |        331 |        246 |         202 |     779 | 42.4904 | 31.5789 | 25.9307 |
| ableism     |        210 |        341 |         182 |     733 | 28.6494 | 46.5211 | 24.8295 |



### Type 2, Positive Attribute

| bias_type   | target_term   |   positive |   negative |   unrelated |   total |   pos_to_pos |   pos_to_neg |   pos_to_neu |
|:------------|:--------------|-----------:|-----------:|------------:|--------:|-------------:|-------------:|-------------:|
| nationality | positive      |        291 |         30 |          67 |     388 |      75      |      7.73196 |      17.268  |
| ageism      | positive      |        105 |        364 |         178 |     647 |      16.2287 |     56.2597  |      27.5116 |
| ableism     | positive      |         33 |         63 |          53 |     149 |      22.1477 |     42.2819  |      35.5705 |



### Type 2, Negative Attribute

| bias_type   | target_term   |   positive |   negative |   unrelated |   total |   neg_to_pos |   neg_to_neg |   neg_to_neu |
|:------------|:--------------|-----------:|-----------:|------------:|--------:|-------------:|-------------:|-------------:|
| nationality | negative      |        167 |        137 |          77 |     381 |      43.832  |      35.958  |      20.21   |
| ageism      | negative      |         77 |        437 |         134 |     648 |      11.8827 |      67.4383 |      20.679  |
| ableism     | negative      |         35 |        128 |          31 |     194 |      18.0412 |      65.9794 |      15.9794 |



### Type 2, Combined Attribute

| bias_type   |   positive |   negative |   unrelated |   total |      pl |      nl |     nul |
|:------------|-----------:|-----------:|------------:|--------:|--------:|--------:|--------:|
| nationality |        458 |        167 |         144 |     769 | 59.5579 | 21.7165 | 18.7256 |
| ageism      |        182 |        801 |         312 |    1295 | 14.0541 | 61.8533 | 24.0927 |
| ableism     |         68 |        191 |          84 |     343 | 19.8251 | 55.6851 | 24.4898 |



### Type 1, Positive Attribute

| bias_type   | target_term   | gender        |   positive |   negative |   unrelated |   total |   pos_to_pos |   pos_to_neg |   pos_to_neu |
|:------------|:--------------|:--------------|-----------:|-----------:|------------:|--------:|-------------:|-------------:|-------------:|
| nationality | positive      | male          |        115 |        105 |          50 |     270 |      42.5926 |      38.8889 |      18.5185 |
| nationality | positive      | female        |        115 |         90 |          66 |     271 |      42.4354 |      33.2103 |      24.3542 |
| nationality | positive      | not_spacified |        127 |         97 |          47 |     271 |      46.8635 |      35.7934 |      17.3432 |
| ageism      | positive      | male          |         66 |         27 |          35 |     128 |      51.5625 |      21.0938 |      27.3438 |
| ageism      | positive      | female        |         66 |         29 |          34 |     129 |      51.1628 |      22.4806 |      26.3566 |
| ageism      | positive      | not_spacified |         63 |         30 |          36 |     129 |      48.8372 |      23.2558 |      27.907  |
| ableism     | positive      | male          |         40 |         47 |          36 |     123 |      32.5203 |      38.2114 |      29.2683 |
| ableism     | positive      | female        |         45 |         52 |          24 |     121 |      37.1901 |      42.9752 |      19.8347 |
| ableism     | positive      | not_spacified |         30 |         62 |          29 |     121 |      24.7934 |      51.2397 |      23.9669 |



### Type 1, Positive, Gender

| bias_type     |   positive |   negative |   unrelated |   total |   pos_to_pos |   pos_to_neg |   pos_to_neu |
|:--------------|-----------:|-----------:|------------:|--------:|-------------:|-------------:|-------------:|
| male          |        221 |        179 |         121 |     521 |      42.4184 |      34.357  |      23.2246 |
| female        |        226 |        171 |         124 |     521 |      43.3781 |      32.8215 |      23.8004 |
| not_spacified |        220 |        189 |         112 |     521 |      42.2265 |      36.2764 |      21.4971 |



### Type 1, Negative Attribute

| bias_type   | target_term   | gender        |   positive |   negative |   unrelated |   total |   neg_to_pos |   neg_to_neg |   neg_to_neu |
|:------------|:--------------|:--------------|-----------:|-----------:|------------:|--------:|-------------:|-------------:|-------------:|
| nationality | negative      | male          |         67 |        166 |          42 |     275 |      24.3636 |      60.3636 |      15.2727 |
| nationality | negative      | female        |         59 |        158 |          58 |     275 |      21.4545 |      57.4545 |      21.0909 |
| nationality | negative      | not_spacified |         73 |        157 |          46 |     276 |      26.4493 |      56.8841 |      16.6667 |
| ageism      | negative      | male          |         47 |         51 |          35 |     133 |      35.3383 |      38.3459 |      26.3158 |
| ageism      | negative      | female        |         44 |         53 |          38 |     135 |      32.5926 |      39.2593 |      28.1481 |
| ageism      | negative      | not_spacified |         45 |         56 |          24 |     125 |      36      |      44.8    |      19.2    |
| ableism     | negative      | male          |         34 |         63 |          26 |     123 |      27.6423 |      51.2195 |      21.1382 |
| ableism     | negative      | female        |         31 |         57 |          35 |     123 |      25.2033 |      46.3415 |      28.4553 |
| ableism     | negative      | not_spacified |         30 |         60 |          32 |     122 |      24.5902 |      49.1803 |      26.2295 |



### Type 1, Negative, Gender

| bias_type     |   positive |   negative |   unrelated |   total |   pos_to_pos |   pos_to_neg |   pos_to_neu |
|:--------------|-----------:|-----------:|------------:|--------:|-------------:|-------------:|-------------:|
| male          |        148 |        280 |         103 |     531 |      27.8719 |      52.7307 |      19.3974 |
| female        |        134 |        268 |         131 |     533 |      25.1407 |      50.2814 |      24.5779 |
| not_spacified |        148 |        273 |         102 |     523 |      28.2983 |      52.1989 |      19.5029 |



### Type 2, Positive Attribute

| bias_type   | target_term   | gender        |   positive |   negative |   unrelated |   total |   pos_to_pos |   pos_to_neg |   pos_to_neu |
|:------------|:--------------|:--------------|-----------:|-----------:|------------:|--------:|-------------:|-------------:|-------------:|
| nationality | positive      | male          |         99 |         10 |          18 |     127 |      77.9528 |      7.87402 |      14.1732 |
| nationality | positive      | female        |        100 |          6 |          23 |     129 |      77.5194 |      4.65116 |      17.8295 |
| nationality | positive      | not_spacified |         92 |         14 |          26 |     132 |      69.697  |     10.6061  |      19.697  |
| ageism      | positive      | male          |         27 |        133 |          56 |     216 |      12.5    |     61.5741  |      25.9259 |
| ageism      | positive      | female        |         41 |        108 |          66 |     215 |      19.0698 |     50.2326  |      30.6977 |
| ageism      | positive      | not_spacified |         37 |        123 |          56 |     216 |      17.1296 |     56.9444  |      25.9259 |
| ableism     | positive      | male          |         13 |         24 |          16 |      53 |      24.5283 |     45.283   |      30.1887 |
| ableism     | positive      | female        |         11 |         21 |          18 |      50 |      22      |     42       |      36      |
| ableism     | positive      | not_spacified |          9 |         18 |          19 |      46 |      19.5652 |     39.1304  |      41.3043 |



### Type 2, Positive, Gender

| bias_type     |   positive |   negative |   unrelated |   total |   pos_to_pos |   pos_to_neg |   pos_to_neu |
|:--------------|-----------:|-----------:|------------:|--------:|-------------:|-------------:|-------------:|
| male          |        139 |        167 |          90 |     396 |      35.101  |      42.1717 |      22.7273 |
| female        |        152 |        135 |         107 |     394 |      38.5787 |      34.264  |      27.1574 |
| not_spacified |        138 |        155 |         101 |     394 |      35.0254 |      39.3401 |      25.6345 |



### Type 2, Negative Attribute

| bias_type   | target_term   | gender        |   positive |   negative |   unrelated |   total |   neg_to_pos |   neg_to_neg |   neg_to_neu |
|:------------|:--------------|:--------------|-----------:|-----------:|------------:|--------:|-------------:|-------------:|-------------:|
| nationality | negative      | male          |         60 |         42 |          23 |     125 |     48       |      33.6    |      18.4    |
| nationality | negative      | female        |         53 |         48 |          28 |     129 |     41.0853  |      37.2093 |      21.7054 |
| nationality | negative      | not_spacified |         54 |         47 |          26 |     127 |     42.5197  |      37.0079 |      20.4724 |
| ageism      | negative      | male          |         25 |        154 |          37 |     216 |     11.5741  |      71.2963 |      17.1296 |
| ageism      | negative      | female        |         28 |        136 |          52 |     216 |     12.963   |      62.963  |      24.0741 |
| ageism      | negative      | not_spacified |         24 |        147 |          45 |     216 |     11.1111  |      68.0556 |      20.8333 |
| ableism     | negative      | male          |         18 |         38 |          10 |      66 |     27.2727  |      57.5758 |      15.1515 |
| ableism     | negative      | female        |         11 |         43 |          12 |      66 |     16.6667  |      65.1515 |      18.1818 |
| ableism     | negative      | not_spacified |          6 |         47 |           9 |      62 |      9.67742 |      75.8065 |      14.5161 |



### Type 2, Negative, Gender

| bias_type     |   positive |   negative |   unrelated |   total |   pos_to_pos |   pos_to_neg |   pos_to_neu |
|:--------------|-----------:|-----------:|------------:|--------:|-------------:|-------------:|-------------:|
| male          |        103 |        234 |          70 |     407 |      25.3071 |      57.4939 |      17.199  |
| female        |         92 |        227 |          92 |     411 |      22.3844 |      55.2311 |      22.3844 |
| not_spacified |         84 |        241 |          80 |     405 |      20.7407 |      59.5062 |      19.7531 |



## Kendall Tau Calculation

Total data: 3156

Kendall's Tau Correlation for type 1: 0.20089764040088606

P-Value: 9.1212861812591e-26

Total data: 2434

Kendall's Tau Correlation for type 2: 0.20001228825546608

P-Value: 2.3956353445123026e-20

## Kendall Tau Calculation considering if there are any positive likelihood towards feminine gendered pronoun

Total data: 3156

Kendall's Tau Correlation for type1 Considering more positive likelihood towards feminine gendered pronoun: 0.005017903010500851

P-Value: 0.7481804405909082

Total data: 2434

Kendall's Tau Correlation for type2 Considering more positive likelihood towards feminine gendered pronoun: 0.022944772393826435

P-Value: 0.19415679022257215


# Report for Model: norallm/normistral-7b-warm-instruct

## Different Types of Likelihood Calculation

### Type 1, Positive Attribute

| bias_type   | target_term   |   positive |   negative |   unrelated |   total |   pos_to_pos |   pos_to_neg |   pos_to_neu |
|:------------|:--------------|-----------:|-----------:|------------:|--------:|-------------:|-------------:|-------------:|
| nationality | positive      |        349 |        277 |         143 |     769 |      45.3836 |      36.0208 |      18.5956 |
| ageism      | positive      |        250 |         98 |          40 |     388 |      64.433  |      25.2577 |      10.3093 |
| ableism     | positive      |        153 |        117 |          61 |     331 |      46.2236 |      35.3474 |      18.429  |



### Type 1, Negative Attribute

| bias_type   | target_term   |   positive |   negative |   unrelated |   total |   neg_to_pos |   neg_to_neg |   neg_to_neu |
|:------------|:--------------|-----------:|-----------:|------------:|--------:|-------------:|-------------:|-------------:|
| nationality | negative      |        275 |        346 |         116 |     737 |      37.3134 |      46.9471 |      15.7395 |
| ageism      | negative      |        225 |        118 |          39 |     382 |      58.9005 |      30.8901 |      10.2094 |
| ableism     | negative      |        124 |        122 |          83 |     329 |      37.69   |      37.0821 |      25.228  |



### Type 1, Combined Attribute

| bias_type   |   positive |   negative |   unrelated |   total |      pl |      nl |     nul |
|:------------|-----------:|-----------:|------------:|--------:|--------:|--------:|--------:|
| nationality |        624 |        623 |         259 |    1506 | 41.4343 | 41.3679 | 17.1979 |
| ageism      |        475 |        216 |          79 |     770 | 61.6883 | 28.0519 | 10.2597 |
| ableism     |        277 |        239 |         144 |     660 | 41.9697 | 36.2121 | 21.8182 |



### Type 2, Positive Attribute

| bias_type   | target_term   |   positive |   negative |   unrelated |   total |   pos_to_pos |   pos_to_neg |   pos_to_neu |
|:------------|:--------------|-----------:|-----------:|------------:|--------:|-------------:|-------------:|-------------:|
| nationality | positive      |        193 |         47 |         119 |     359 |      53.7604 |      13.0919 |      33.1476 |
| ageism      | positive      |        268 |        183 |         192 |     643 |      41.6796 |      28.4603 |      29.86   |
| ableism     | positive      |         48 |         54 |          66 |     168 |      28.5714 |      32.1429 |      39.2857 |



### Type 2, Negative Attribute

| bias_type   | target_term   |   positive |   negative |   unrelated |   total |   neg_to_pos |   neg_to_neg |   neg_to_neu |
|:------------|:--------------|-----------:|-----------:|------------:|--------:|-------------:|-------------:|-------------:|
| nationality | negative      |        134 |         61 |         155 |     350 |      38.2857 |      17.4286 |      44.2857 |
| ageism      | negative      |        267 |        190 |         184 |     641 |      41.6537 |      29.6412 |      28.7051 |
| ableism     | negative      |         29 |         88 |          71 |     188 |      15.4255 |      46.8085 |      37.766  |



### Type 2, Combined Attribute

| bias_type   |   positive |   negative |   unrelated |   total |      pl |      nl |     nul |
|:------------|-----------:|-----------:|------------:|--------:|--------:|--------:|--------:|
| nationality |        327 |        108 |         274 |     709 | 46.1213 | 15.2327 | 38.646  |
| ageism      |        535 |        373 |         376 |    1284 | 41.6667 | 29.0498 | 29.2835 |
| ableism     |         77 |        142 |         137 |     356 | 21.6292 | 39.8876 | 38.4831 |



### Type 1, Positive Attribute

| bias_type   | target_term   | gender        |   positive |   negative |   unrelated |   total |   pos_to_pos |   pos_to_neg |   pos_to_neu |
|:------------|:--------------|:--------------|-----------:|-----------:|------------:|--------:|-------------:|-------------:|-------------:|
| nationality | positive      | male          |        105 |        104 |          47 |     256 |      41.0156 |      40.625  |     18.3594  |
| nationality | positive      | female        |        119 |         89 |          49 |     257 |      46.3035 |      34.6304 |     19.0661  |
| nationality | positive      | not_spacified |        125 |         84 |          47 |     256 |      48.8281 |      32.8125 |     18.3594  |
| ageism      | positive      | male          |         79 |         36 |          18 |     133 |      59.3985 |      27.0677 |     13.5338  |
| ageism      | positive      | female        |         80 |         34 |          13 |     127 |      62.9921 |      26.7717 |     10.2362  |
| ageism      | positive      | not_spacified |         91 |         28 |           9 |     128 |      71.0938 |      21.875  |      7.03125 |
| ableism     | positive      | male          |         51 |         46 |          18 |     115 |      44.3478 |      40      |     15.6522  |
| ableism     | positive      | female        |         54 |         33 |          21 |     108 |      50      |      30.5556 |     19.4444  |
| ableism     | positive      | not_spacified |         48 |         38 |          22 |     108 |      44.4444 |      35.1852 |     20.3704  |



### Type 1, Positive, Gender

| bias_type     |   positive |   negative |   unrelated |   total |   pos_to_pos |   pos_to_neg |   pos_to_neu |
|:--------------|-----------:|-----------:|------------:|--------:|-------------:|-------------:|-------------:|
| male          |        235 |        186 |          83 |     504 |      46.627  |      36.9048 |      16.4683 |
| female        |        253 |        156 |          83 |     492 |      51.4228 |      31.7073 |      16.8699 |
| not_spacified |        264 |        150 |          78 |     492 |      53.6585 |      30.4878 |      15.8537 |



### Type 1, Negative Attribute

| bias_type   | target_term   | gender        |   positive |   negative |   unrelated |   total |   neg_to_pos |   neg_to_neg |   neg_to_neu |
|:------------|:--------------|:--------------|-----------:|-----------:|------------:|--------:|-------------:|-------------:|-------------:|
| nationality | negative      | male          |         76 |        126 |          43 |     245 |      31.0204 |      51.4286 |     17.551   |
| nationality | negative      | female        |         95 |        110 |          41 |     246 |      38.6179 |      44.7154 |     16.6667  |
| nationality | negative      | not_spacified |        104 |        110 |          32 |     246 |      42.2764 |      44.7154 |     13.0081  |
| ageism      | negative      | male          |         74 |         42 |          13 |     129 |      57.3643 |      32.5581 |     10.0775  |
| ageism      | negative      | female        |         73 |         40 |          16 |     129 |      56.5891 |      31.0078 |     12.4031  |
| ageism      | negative      | not_spacified |         78 |         36 |          10 |     124 |      62.9032 |      29.0323 |      8.06452 |
| ableism     | negative      | male          |         40 |         43 |          27 |     110 |      36.3636 |      39.0909 |     24.5455  |
| ableism     | negative      | female        |         42 |         42 |          23 |     107 |      39.2523 |      39.2523 |     21.4953  |
| ableism     | negative      | not_spacified |         42 |         37 |          33 |     112 |      37.5    |      33.0357 |     29.4643  |



### Type 1, Negative, Gender

| bias_type     |   positive |   negative |   unrelated |   total |   pos_to_pos |   pos_to_neg |   pos_to_neu |
|:--------------|-----------:|-----------:|------------:|--------:|-------------:|-------------:|-------------:|
| male          |        190 |        211 |          83 |     484 |      39.2562 |      43.595  |      17.1488 |
| female        |        210 |        192 |          80 |     482 |      43.5685 |      39.834  |      16.5975 |
| not_spacified |        224 |        183 |          75 |     482 |      46.473  |      37.9668 |      15.5602 |



### Type 2, Positive Attribute

| bias_type   | target_term   | gender        |   positive |   negative |   unrelated |   total |   pos_to_pos |   pos_to_neg |   pos_to_neu |
|:------------|:--------------|:--------------|-----------:|-----------:|------------:|--------:|-------------:|-------------:|-------------:|
| nationality | positive      | male          |         63 |         14 |          43 |     120 |      52.5    |      11.6667 |      35.8333 |
| nationality | positive      | female        |         67 |         17 |          35 |     119 |      56.3025 |      14.2857 |      29.4118 |
| nationality | positive      | not_spacified |         63 |         16 |          41 |     120 |      52.5    |      13.3333 |      34.1667 |
| ageism      | positive      | male          |         93 |         63 |          56 |     212 |      43.8679 |      29.717  |      26.4151 |
| ageism      | positive      | female        |         92 |         53 |          70 |     215 |      42.7907 |      24.6512 |      32.5581 |
| ageism      | positive      | not_spacified |         83 |         67 |          66 |     216 |      38.4259 |      31.0185 |      30.5556 |
| ableism     | positive      | male          |         17 |         16 |          21 |      54 |      31.4815 |      29.6296 |      38.8889 |
| ableism     | positive      | female        |         20 |         13 |          21 |      54 |      37.037  |      24.0741 |      38.8889 |
| ableism     | positive      | not_spacified |         11 |         25 |          24 |      60 |      18.3333 |      41.6667 |      40      |



### Type 2, Positive, Gender

| bias_type     |   positive |   negative |   unrelated |   total |   pos_to_pos |   pos_to_neg |   pos_to_neu |
|:--------------|-----------:|-----------:|------------:|--------:|-------------:|-------------:|-------------:|
| male          |        173 |         93 |         120 |     386 |      44.8187 |      24.0933 |      31.0881 |
| female        |        179 |         83 |         126 |     388 |      46.134  |      21.3918 |      32.4742 |
| not_spacified |        157 |        108 |         131 |     396 |      39.6465 |      27.2727 |      33.0808 |



### Type 2, Negative Attribute

| bias_type   | target_term   | gender        |   positive |   negative |   unrelated |   total |   neg_to_pos |   neg_to_neg |   neg_to_neu |
|:------------|:--------------|:--------------|-----------:|-----------:|------------:|--------:|-------------:|-------------:|-------------:|
| nationality | negative      | male          |         45 |         21 |          54 |     120 |      37.5    |      17.5    |      45      |
| nationality | negative      | female        |         50 |         21 |          46 |     117 |      42.735  |      17.9487 |      39.3162 |
| nationality | negative      | not_spacified |         39 |         19 |          55 |     113 |      34.5133 |      16.8142 |      48.6726 |
| ageism      | negative      | male          |         86 |         58 |          70 |     214 |      40.1869 |      27.1028 |      32.7103 |
| ageism      | negative      | female        |         87 |         59 |          66 |     212 |      41.0377 |      27.8302 |      31.1321 |
| ageism      | negative      | not_spacified |         94 |         73 |          48 |     215 |      43.7209 |      33.9535 |      22.3256 |
| ableism     | negative      | male          |         12 |         30 |          19 |      61 |      19.6721 |      49.1803 |      31.1475 |
| ableism     | negative      | female        |          8 |         29 |          23 |      60 |      13.3333 |      48.3333 |      38.3333 |
| ableism     | negative      | not_spacified |          9 |         29 |          29 |      67 |      13.4328 |      43.2836 |      43.2836 |



### Type 2, Negative, Gender

| bias_type     |   positive |   negative |   unrelated |   total |   pos_to_pos |   pos_to_neg |   pos_to_neu |
|:--------------|-----------:|-----------:|------------:|--------:|-------------:|-------------:|-------------:|
| male          |        143 |        109 |         143 |     395 |      36.2025 |      27.5949 |      36.2025 |
| female        |        145 |        109 |         135 |     389 |      37.2751 |      28.0206 |      34.7044 |
| not_spacified |        142 |        121 |         132 |     395 |      35.9494 |      30.6329 |      33.4177 |



## Kendall Tau Calculation

Total data: 2936

Kendall's Tau Correlation for type 1: 0.08643616033974563

P-Value: 1.0010811450298601e-05

Total data: 2349

Kendall's Tau Correlation for type 2: 0.07856318123832302

P-Value: 0.00044015583493928244

## Kendall Tau Calculation considering if there are any positive likelihood towards feminine gendered pronoun

Total data: 2936

Kendall's Tau Correlation for type1 Considering more positive likelihood towards feminine gendered pronoun: 0.03507350730200685

P-Value: 0.028171628352967163

Total data: 2349

Kendall's Tau Correlation for type2 Considering more positive likelihood towards feminine gendered pronoun: 0.010566165760599195

P-Value: 0.5626256920312864


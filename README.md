# weather-prediction

# Dataset : 

information of data :

```
 0   STA          119040 non-null  int64
 1   Date         119040 non-null  object
 2   Precip       119040 non-null  object
 3   WindGustSpd  532 non-null     float64
 4   MaxTemp      119040 non-null  float64
 5   MinTemp      119040 non-null  float64
 6   MeanTemp     119040 non-null  float64
 7   Snowfall     117877 non-null  object
 8   PoorWeather  34237 non-null   object
 9   YR           119040 non-null  int64
 10  MO           119040 non-null  int64
 11  DA           119040 non-null  int64
 12  PRCP         117108 non-null  object
 13  DR           533 non-null     float64
 14  SPD          532 non-null     float64
 15  MAX          118566 non-null  float64
 16  MIN          118572 non-null  float64
 17  MEA          118542 non-null  float64
 18  SNF          117877 non-null  object
 19  SND          5563 non-null    float64
 20  FT           0 non-null       float64
 21  FB           0 non-null       float64
 22  FTI          0 non-null       float64
 23  ITH          0 non-null       float64
 24  PGT          525 non-null     float64
 25  TSHDSBRSGF   34237 non-null   object
 26  SD3          0 non-null       float64
 27  RHX          0 non-null       float64
 28  RHN          0 non-null       float64
 29  RVG          0 non-null       float64
 30  WTE          0 non-null       float64
dtypes: float64(20), int64(4), object(7)
```
### independent variables that I use for Regression model to train are 'STA', 'WindGustSpd', 'YR', 'MO', 'DA', 'SPD', 'MAX', 'MIN', 'MEA', 'SND', 'PGT', 'MeanTemp', 'MinTemp' and dependent variable is **MaxTemp**

### **our goal is to predict next day weather**

<hr>

## Model

>>Regression model

## Evaluation
### mean_absolute_error : 0.03942964382482842
### r2_score : 0.9939687109415878



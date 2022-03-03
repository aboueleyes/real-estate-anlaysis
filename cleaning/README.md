## Notes
- Detect any duplicates and save them into a separated CSV file
- Do not try to deal with missing values in this stage. We will leave them as is for now, and will fill them with the most appropriate value after cleaning all the features in the dataframe.

## Features 

### Location 
1. Extract geographic information such as governorate and city/district
2. If the city/district is missing, fill it with the name of the governorate
3. Create a new feature and name it ‘region’. It is meant ot group the governorates into 6 categories: 
- **Capital**: Cairo and Giza
- **Alexandria**: Alexandria
- **Upper Egypt**: Fayoum, Menia, Bani-Suef, Assyout, Sohag, Qena, Luxor, Aswan
- **Lower Egypt**: Qalyoubia, Dakahlia, Gharbia, Behera, Menoufia, Kafr-El Sheikh, Dumiat, Sharqia
- **Canal**: Ismailia, Port-Said, Suez
- **Border**: Bahr-Ahmar, South Sinai, North Sinai, New Valley, Matrough

### Title

Nothing 

### bedrooms, bathrooms, level

1. Leave them as is (categorical features) to take into account 10+ values.
2. Convert them into integer: in this case you will need to delete the plus sign from 10+ and treat it as if it is 10


### Area

1. Convert it to numeric: integer.
2. The feature has unreasonable values. Therefore, we will work on outlier detection later on.

### Furnished
The feature has missing values, try to fill them with the correct values based on the description or the title.

### type

It seems to be nice and clean, if so leave it as is.

### amenities
1. Create a new feature and name it “amenities_specified. It should take 0 if “amenities” is missing and 1 otherwise.

2. Split the amenities into dummy features 

3. Delete the original feature.

### compound

1. Create a new feature and name it `in_compound`. It should take 1 if `وند` is in title or description

2. If the value of `in_compound` is 1 and the value of `compound` is missing replace the value of  `compound` with `compound name not specified`

3. If the `compound` feature still has missing values,  fill them with `Not Available` or `Not in compound` or any other value based on your best judgment.

### date 

1. Extract: Year, Month, Day of the week.

2. Store each of them into a separate feature

### delivery date

1. Create a new feature and name it `delivery_date_specified`. It should take 0 if `delivery_date` is missing and 1 otherwise.

2. Fill in the missing values using `Not Specefied`.

## Outliers

1. Plot the numerical features against each other (price against area)  and try to spot any inconsistencies.

2. Do not forget to take into account all other features while you are performing step 1.

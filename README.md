
<b><div align = "center">![cover_art.png](presentation/images/cover_art.png)</div></b>

<h1><b><div align = "center">Final Project Proposal: Group G</div></b></h1>
<h3><b><div align = "center">Contributors</div></b></h3>
<h4><b><div align = "center">Erik Fritzsche</div></b></h4>
<h4><b><div align = "center">Paul Hoogestraat</div></b></h4>
<h4><b><div align = "center">	Brent Sergent</div></b></h4>


# Objective:

Identify key global economic trends to train a machine learning model for predicting the retail prices of coffee. Economic data considered will span from 1990 to 2018. The final model will attempt to predict the average global retail price for a pound of coffee.

### Questions to answer:
1.	How has the production of coffee changed (increased, decreased) from 1990 to 2018?
2.	What are the top 10 coffee producing countries from 1990 thru 2018?
3.	Have exports from coffee producing countries increased or decreased between 1990 and 2018?
4.	Have imports for coffee increased or decreased between 1990 and 2018?
5.	How has the price for coffee beans changed between 1990 and 2018?
6.	Do energy prices impact coffee prices?
7.	Can a machine learning model be developed to predict trending coffee prices?


# Background:
The International Coffee Organization (ICO) is a United Nations agency representing the world’s major coffee producers. This organization was founded in 1963 with the signing of the International Coffee agreement. In addition to representing interests of coffee producing nations, the organization hosts publicly available global economic data regarding supply, export, import, inventory, and pricing. A key metric created by this organization is the ICO composite indicator price, which is considered the benchmark for global coffee prices. The organization also provides global coffee retail prices which will be averaged to determine the retail price for a pound of coffee.

### Resources:
-	HTML/CSS/Bootstrap
-	JavaScript	
-	Python Pandas
-	Tableau
-	Machine learning library: Scikit-Learn
-	Heroku

### Process: 
- [x] Concept design and project planning.
- [x] Create Github Repository.
- [x] Evaluate and obtain data sources.
- [x] Transform data into visuals
  - [x] Chart depicitng top 10 coffee producers since 1990
  - [x] Chart depicting top 10 coffee importers since 1990
  - [x] Graph depicting exports and imports trends over time.
  - [x] Graph depicting price fluctuations in retail coffee price over time
  - [x] Map identifing coffee producing countries
  - [x] Map identifing coffee import countries  
- [x] Evalute, design, and deploy a machine learning model
  - [x] Model evaluated: Random Forest Regressor model (sklearn library)
  - [x] Model evaluated: Linnear regression model
  - [x] Model Optimized: Random Forest Regressor model
  - [ ] Model Deployed: Random Forest Regressor model
- [X] Design a website with the following objectives:
  - [ ] Frame objective. 
  - [ ] Employ collected data to identify trends with viusuals.
  - [ ] Create a vehical to demonstate outcome of machine learing model.
  - [ ] Final analysis
  - [ ] Refrences
- [ ] Integrate Heroku :


# Data Sources
* [Kaggle: ICO Coffee Dataset (Worldwide)](https://www.kaggle.com/yamaerenay/ico-coffee-dataset-worldwide)

Data was obtained from ICO Coffee Dataset (Worldwide) hosted on Kaggle. This collection contained 13 csv files capturing distinct metrics regarding coffee economic data. Scope of files evaluated were : global production, global imports, inventories, prices-paid to growers, domestic consumption, and  retail prices.
<b><div align = "center">![kaggle_Coffe_data_header.png](presentation/images/kaggle_Coffe_data_header.png)</div></b>

* [International Coffee Organization: Historical Data on the Global Coffee Trade](http://www.ico.org/new_historical.asp)

Original data source employed on Kaggle site listed above. Provides additional detail regarding the data sets.

* [Macrotrends: Historic trends in Brent oil prices](https://www.macrotrends.net/2480/brent-crude-oil-prices-10-year-daily-chart)

Historic data regarding Brent crude prices.

* [Macrotrends: Historic trends in WTI oil prices](https://www.macrotrends.net/2516/wti-crude-oil-prices-10-year-daily-chart)

Historic data regarding WTI crude prices.

<br/><br/>
# Visualizations
Evaluated data was transformed into charts and interactive visualizations employing Tableau. Economic trends were identified from the visualizations and incorporated into designing a data structure for machine learning. Final visualizations were incorporated into the website and can also be located on the public Tableau website listed below in the references. Examples:

<br/><br/>
#### Graph A
![historical_import_production_coffe.png](presentation/images/graphs/historical_import_production_coffe.png)

<br/><br/>
<br/><br/>
#### Graph B
![historic_coffe_price.png](presentation/images/graphs/historic_coffe_price.png)

# Machine Learning

## Economic Model

![data_graphic.png](presentation/images/data_graphic.png)
* Eleven data sets were organized into six categories (supply, demand, inventories, consumption, energy, ICO composite, and retail price). The data sets were composed of metric categories partitioned by year and country. Categories were averaged (i.e. price) or summed (i.e. crop production) by year for each feature category to obtain global benchmarks for analysis. Each category of data was treated equally. 10 features were initially selected to train a machine learning model.

#### Top Features
![original_features.png](presentation/images/original_features.png) 

* A random forest regressor model (sklearn library) was chosen over a linear regression model bassed on accuracy. Optimization of the model was evaluated by removing features with low training scores (Table 1). After exploring multiple combinations of features three models were created. The first model contained nine-features with the least impactful one removed. The second model included the ICO Composite and the year. The final model contained ISO composite, year, and Brent annual average. The last two models will be considered for web deployment due to simplicity considerations. Graph C contrasts the nine-feature model predicted global retail price vs observed global retail price. The three models were saved in this repository.

#### Feature Contribution
![best_features.png](presentation/images/best_features.png)

#### Table 1.
|Model|Model Score|Training Score|
|-----|-----------|--------------|
|Random Forest 10 features|0.9592|0.9036|
|Random Forest 1 featrues |0.9250|0.8262|
|Random Forest 2 featrues |0.9486|0.8712|
|Random Forest 3 featrues |0.9561|0.9139|
|Random Forest 4 featrues |0.9598|0.9292|
|Random Forest 5 featrues |0.9591|0.9378|
|Random Forest 6 featrues |0.9580|0.9214|
|Random Forest 7 featrues |0.9557|0.9098|
|Random Forest 8 featrues |0.9590|0.8973|
|Final RFM (9 features) |0.9597|0.8959|


#### Graph C
![Economic_model.png](presentation/images/graphs/Economic_model.png)

## Environmental Model 

An additional model was also considered to determine ICO composite pricing bassed on environmental factors combined with supply & demand.

<b>Machine Learning (with linear regression)</b>
* The model attempts to take the average of a year for all features and predict the average retail price of the importing countries
* The model fails due to the fluctuations and adjustments of the market are  not accurately taken into account by the yearly averages. The linear coefficients are just a maginifications of the data we kept at the exspense of the fluctuations.


# Website
A website was developed to communicate the results of this project. The objective was to identify coffee production and consumption trends by employing data visualizations for creating a machine learning model.


# Conclusion

To be completed

# Refrences

### Articles
* [Predicting Coffee Prices (Nathan Mitchell)](https://ntmitchell.github.io/predicting-coffee-prices/)
* [A Beginners Guide to Random Forest Regression (Kirshni)](https://medium.datadriveninvestor.com/random-forest-regression-9871bc9a25eb)
* [Regression Example with RandomForestRegressor in Python](https://www.datatechnotes.com/2020/09/regression-example-with-randomforestregressor.html)

### Data
* [Kaggle: ICO Coffee Dataset (Worldwide)](https://www.kaggle.com/yamaerenay/ico-coffee-dataset-worldwide)
* [International Coffee Organization: Historical Data](http://www.ico.org/new_historical.asp)
* [Macrotrends: Historic trends in Brent oil prices](https://www.macrotrends.net/2480/brent-crude-oil-prices-10-year-daily-chart)
* [Macrotrends: Historic trends in WTI oil prices](https://www.macrotrends.net/2516/wti-crude-oil-prices-10-year-daily-chart)

### Graphs (Tableau)
* [Coffe Producer Country Data (Tableau)](https://public.tableau.com/profile/paul.hoogestraat#!/vizhome/coffe_prodiuction_2021P3/Dashboard1?publish=yes)
* [Coffe Import Country Data (Tableau)](https://public.tableau.com/profile/paul.hoogestraat#!/vizhome/Coffe_Import_2021P3/CoffeImport?publish=yes	)
* [Coffe Trend Data (Tableau)](https://public.tableau.com/profile/paul.hoogestraat#!/vizhome/coffe_trendlines_2021P3/coffe?publish=yes)

### Final Web site
* to be completed

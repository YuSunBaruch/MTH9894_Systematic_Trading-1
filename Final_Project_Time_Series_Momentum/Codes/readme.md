## This folder contains all the codes used for our project

* Author: Hongchao Pan, Yu Sun
* Kernel version: Python 3.5.2
* Packages:

### Before using the codes
* Please install ["arch"](https://pypi.python.org/pypi/arch/3.0) package before using the jupyter notebook.
The GARCH(1,1) model used in the notebook will use this package.

### Instructions of using the code folder

* Detailed notes of each function defined in the py files can be
found in the corresponding places.

#### Functions in **Get_data.py** file

Function Name | Descriptions
--- | ---
df_eq4() | Data used for Equation 4 in the paper
df_bonds() | Data of bond futures
df_currency() | Data of currencies
df_equity() | Data of equities
df_commodity()  | Data of commodities
df_test_validation  | Split test and validation data
df_rf   | Data of risk-free, benchmark rates
excess_return() | Data of excesess return of test and validation data
excess_return_annu()    | Data of annulized excess return of test and validation data
vol_annu()  | Computing the annulized vol based on annulized excess return (barely used)

* Notes: The test/validation start/end date has been embedded in the 
function. The test_data, validation_data, and df_rf (risk free rates)
 were obtained from functions defined in **Get_data.py** file.*

#### Juyter notebook
* The jupyter notebook contains the main layout of getting data, pictures, and results for our final project.
Detailed notes of how to use the jupyter notebook has been detailed put in the notebook.

* The running time of this notebook is around 5mins



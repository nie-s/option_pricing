## 1 Contribution



## 2 Interface 

We use PyQt to build our interface. Run `MainInterface.py` to start the application.

Picture below shows the entrance page: user can choose the method from the list, and choose either 'call' or 'put' type. Click confirm to next step.

<img src="pic1.png" alt="pic1" style="zoom:50%;" />



Here is the interface for user to input the parameters and calculate the result. Unnecessary input boxes will be disabled. User can input the numbers into boxes, and after 

<img src="pic2.png" alt="pic1" style="zoom:50%;" />

If at least one of the parameters is missing, there will be an alert:

<img src="pic3.jpg" alt="pic3" style="zoom:50%;" />

If at least one of the parameters is in wrong format, there will be an alert:

<img src="pic4.jpg" alt="pic4" style="zoom:50%;" />





## 3 Function Description

The basic idea of our implement is to create class for each option type, and call the method inside the class to calculation the expected output. For each class, we initial the object with its required parameters, and call the function to get the result.  

For Class `BlackScholes`, `ClosedFormAsian`, `ClosedFormBasket`, `ImpliedVolatility`, they only require the calculation of given formula, thus, we only need to call the function `get_result`, and get the option price or implied volatility depending on the demanding task. 



And for other classes, here takes `MonteCarloAsianVC` as example. The program is completed as these steps:

- Generate stock price paths (using `price_path` and calculate arithmetic averages

  ```python
  geometric_average = np.exp((1 / float(self.n)) * np.sum(np.log(self.price_path()), 1)) 
  ```

- Calculate payoffs

  ```python
  # call
  mc_payoff_geo = self.discount * np.maximum(geometric_average - self.K, 0)
  # put
  mc_payoff_geo = self.discount * np.maximum(self.K - geometric_average, 0)
  
  ```

- Estimate the control variate

- Calculate the control variate coefficient

- Estimate the option value

- Calculate the standard error

The `QMonteCarloKIKOPut` class is specifically designed to calculate the price and delta of KIKO put options. Distinct from classes such as `MonteCarloAsianVC`, it employs the Quasi-Monte Carlo method, focusing its research on barrier put options.


## 4 Test Cases
We designed four test classes to test our pricer, which are used for Asian option, basket option, American option, and KIKO put option. The relationship between options, test programs and data transfer files is as follows.

| Options | program | CSV File |
| :---         | :---         | :---         |
| Monte Carlo Asian   | TestCaseAsian.py     | asian_options_results.csv    |
| Monte Carlo Basket     | TestCaseBasket.py       | basket_options_results.csv      |
| Binomial Tree American     | TestCaseAmerican.py       | american_options_results.csv      |
| Quasi-Monte Carlo  KIKO-put     | TestCaseQMC.py       | KIKO_options_results.csv      |

## 5 Sensitivity Analysis
。We conducted sensitivity analysis on important options and their parameters using python to generate charts. This part of the code all starts with stvAnalysis, where we plot each change, but for the sake of brevity in the report, only plots for some special cases are included here. All images can be found in the `SensitiveAnalysisPlots` folder.
| Options | program |
| :---         | :---         | 
| Binomial Tree American     | stvAnalysisAmerican.py       |    
| Closed Form Asian   | stvAnalysisCFAsian.py     | 
| Closed Form Basket     | stvAnalysisCFBasket.py       | 
| Quasi-Monte Carlo KIKO-put     | stvAnalysisKIKO.py       | 
| Monte Carlo Asian   | stvAnalysisMCAsian.py     | asian_options_results.csv    |
| Monte Carlo Basket     | stvAnalysisMCBasket.py       | basket_options_results.csv      |

### 5.1 Binomial Tree American


### 5.2 Closed Form Asian


### 5.3 Closed Form Basket


### 5.4 Quasi-Monte Carlo KIKO-put


### 5.5 Monte Carlo Asian


### 5.6 Monte Carlo Basket



Strike Price, Maturity, Volatility, Risk Free Rate, Number of Time Steps in Binomial Tree




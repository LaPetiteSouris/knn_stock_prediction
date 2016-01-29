# ARMA-stock-index-predict

This is a simple program to predict closing point of EURONEXT 100 index . The program attempts to model EURONEXT 100 index into an Autoregressive–moving-average(ARMA) model.
<br /> 
<br />

#How to run project:
<br />
Swith your default Python interpreter to Anaconda, then run python file start.py from terminal



#Requirements:
UNIX environment. <br />

Anaconda 2.3.0
<br />

The project uses extensively several Python data analysis and machine learning libraries, including Pandas, SciPy, statsmodels and Matplotlib for plotting result.
Most of these libraries are ready-installed with Anaconda, or can be easily install with Anaconda tool

#Design : 

1.Load EURONEXT 100 index into training data(from starting date(t0) to current date(t(n-1))). <br />
2. Model training data using ARMA
<br />
3. Select from list of constructed ARMA models the optimal order, based on minimum Akaike Information Criterion(AIC). This will consume some time due to large amount of data
<br />
The order of optimal ARMA model is (p, q) with p and q ranging from 0 to 10.
<br />
4. Predict EURONEXT 100 index at date t(n) to date t(n++4) , meaning 5 business days.

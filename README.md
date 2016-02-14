=======
# knn_stock_prediction

Predict ABB stock closing price based on sell volume, open price, low price and high price in a day


# How to run

Recommended running method is with Jupyter, as the project require complicate NumPy, SciPy and Scikit-learn configuration which are all available in a typical scientific data processing projects. <br/>

1. Install Docker <br/>
2. Pull pre-configure Docker images *dataquestio/python2-starter* <br/>
3. Copy src folder in your Jupyter notebook root <br/>
4. *docker run -d -p 8888:8888 -v /home/foo/foo:/home/ds/notebooks dataquestio/python2-starter* <br/>
*/home/foo/foo* is your Jupyter notebook root directory. <br/>
5. Open your Jupyter notebook in web browser at *localhost:8888*, execute file* starter.py *from python to get prediction result for the next day.



# Requirement 

Docker installed

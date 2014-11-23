#Wireless_project
================
This project involves analyzing the given wireless data collected from Access points in different ranges and to calculate various attributes for in-sector and out-sector.

In this project we will build a measurement-driven model of radio propagation. The basic idea is to measure the received power (generally called received signal strength or RSS) at different distances from a wireless transmitter and then fit a model using these measurements.

####Measurements:

The first step is to collect a number of RSS measurements tagged with distance of the transmitter. The best way to do this is to use a technology that is easily available, i.e., cellular phones or WiFi client devices (laptop or a smartphone) and collect measurements from a cell tower (for cellular signals) or WiFi AP (for WiFi signals) with a known location. Application programs/tools to collect RSS for different cellular technologies or WiFi on different phone/computer platforms are widely available on the web. To find distance, measurement locations can be recorded. Locations can be determined via a phone’s GPS (outdoor only), using online satellite maps, e.g., from Google (outdoor only) or using building maps (indoors).

####Analysis:

######Follow the following general methodology for fitting a propagation model to the data.
1. Express RSS in dBm and distance d in meters. Plot the measurement samples in two scatterplots –
RSS vs. d and RSS vs log10(d).

2. We know from the class (log-distance path loss and log-normal shadowing) that
􏰀d􏰁 RSS(d) = RSS(d0) − 10α log10 d + Xσ, where α is the path loss exponent, d0 is a reference distance and Xσ is a shadowing component repre- sented by a Gaussian (normal) random variable with zero mean and standard deviation σ. According to the above expression, RSS vs. log10(d) plot should be linear ignoring the random shadowing com- ponent.

3. Use linear regression to find the relationship between RSS and log10(d). The slope of the regression line will give you the value of α. Compute α. (Spreadsheet programs such as Excel has built-in functions to compute linear regression. Many software tools/libraries are also widely available.) Plot the regression line on the RSS vs. log10(d) scatterplot. Also, plot the corresponding RSS vs. d line on the RSS vs d scatterplot. If you have never used linear regression before, you may want to first look that up on the web or in any elementary statistics book.

4. Show the distribution of shadowing component. This is simply the deviation of the measurement samples from the regression line. To do this, compute the algebraic difference between the measured RSS for each d and the corresponding RSS on the regression line. Show a histogram of these differences. For the histogram choose a suitable bin size (a few dBs, for example). Also compute the standard deviation σ of these differences. (Once again, spreadsheets such as Excel has a built-in function to compute the standard deviation.)

5. Go back to the RSS vs d plot. Plot 4 more lines: RSS ±σ and RSS ±2σ away from the regression line. These additional lines visually show how noisy the shadowing component is.

6. Write a short report documenting your work and showing the plots. No need to provide a table of the collected samples.

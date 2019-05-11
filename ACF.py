# -*- coding: utf-8 -*-
print ("\n run by Ayush Yajnik")
while True:  
    first_num = raw_input("Enter the first variance that you to enter or done to exit: ")
    if first_num == 'done':
        print "You choose to exit the calculator."
        break
    else:
        print "We are here to calculate the Sample Autocorelation factor"
        ACF = "The correlation between two variables y1,y2 is defined as"         "\nρ=E[(y1−μ1)(y2−μ2)]/σ1σ2=Cov(y1,y2)/σ1σ2\n         \nwhere E is the expectation operator, μ1 and μ2 are the means respectively for y1 and y2 and σ1,σ2 are their standard deviations.\n"
        print "The formula through which we are going to calculate the value is", ACF
        second_num = raw_input("Enter the second variable:")
        ExpErr = raw_input("Enter the Expectation error:")
        myu1 = raw_input("Enter the first mean:")
        myu2 = raw_input("Enter the second number:")
        sigma1 = raw_input("Enter the first standard deviation:")
        sigma2 = raw_input("Enter the second standard deviation:")
        print "\nNow that we have all the values, let's calculate the value of Sample Autocorelative Factor"
        ACF1 = float(ExpErr)*float(second_num) -float (myu2)*float(first_num)/float(sigma1)*float(sigma2)
        print 'The Sample ACF is ', ACF1
         
        
#!/bin/bash
echo "Content-Type: text/plain"
echo
echo "Running Bash script from cgi-bin successfully!" 
echo
echo -n "Now: "
date
echo -n "User: "
whoami
echo -n -n
echo 

if [ $# -ne 2 ]; then   
	read -p "Enter weight and height:" kg cm  #get weight and height from 'read'	
else   # or get weight and height from command line
kg=$1
cm=$2	
fi

# $kg is weight; $ cm is height.

read -p "What unit do you enter for weight? (Enter 'kg' or 'lbs'):" w_unit # find out what units
read -p "What unit do you enter for height? (Enter 'cm' or 'in'):" h_unit

if [ $w_unit = "lbs" ]; then
((kg=$kg*453592))  # 1 lb = 0.453592 kg; re-scale the decimal point; 10^6 
else
((kg=$kg*1000000)) # re-scale the decimal point 10^6 
fi

if [ $h_unit = "in" ]; then
((cm=$cm*254)) # 1 in= 2.54 cm; re-scale the decimal point; 10^2 
else
((cm=$cm*100)) #re-scale the decimal point; 10^2 
fi

((bmi=$kg*10000/$cm/$cm)) # *10000 neturalize the re-scalings of h_unit; the output is still 100*actual bmi; 

#map bmi to status
status="Underweight"
if [ $bmi -ge 3000 ]; then
	status="Obese"
	elif [ $bmi -ge 2500 ]; then
		status="Overweight"
	elif [ $bmi -ge 1850 ]; then
		status="Normal"
fi    

BMI_to_Print=$(echo "scale=2;$bmi/100" | bc -q) #use bc to print out actual bmi
echo  "Your BMI is:" $BMI_to_Print "; Your status is:" $status 

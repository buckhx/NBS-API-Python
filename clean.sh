#Cleans all *.pyc from project
# Note: Only works on unix

find . -name "*.pyc" -exec rm -rf {} \;

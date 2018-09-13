import scrapy


class BrickSetSpider(scrapy.Spider):
    name = "brickset_spider"
    start_urls = ['http://brickset.com/sets/year-2016']

    def parse(self, response):
        SET_SELECTOR = '.set'
        for brickset in response.css(SET_SELECTOR):
            MODEL_SELECTOR = 'a ::text'
            NAME_SELECTOR = 'h1 ::text'
            PIECES_SELECTOR = './/dl[dt/text() = "Pieces"]/dd/a/text()'
            MINIFIGS_SELECTOR = './/dl[dt/text() = "Minifigs"]/dd[2]/a/text()'
            IMAGE_SELECTOR = 'img ::attr(src)'
            yield {
                'model' : brickset.css(MODEL_SELECTOR).extract_first(),
                'name': brickset.css(NAME_SELECTOR).extract_first(),
                'pieces': brickset.xpath(PIECES_SELECTOR).extract_first(),
                'minifigs': brickset.xpath(MINIFIGS_SELECTOR).extract_first(),
                'image': brickset.css(IMAGE_SELECTOR).extract_first(),
            }

        NEXT_PAGE_SELECTOR = '.next a ::attr(href)'
        next_page = response.css(NEXT_PAGE_SELECTOR).extract_first()
        if next_page:
            yield scrapy.Request(
                response.urljoin(next_page),
                callback=self.parse
            )
# scrapy runspider scraper.py






def printme( str ):
   "This prints a passed string into this function"
   print(str)
   return;

# Now you can call printme function
printme("I'm first call to user defined function!")
printme("Again second call to the same function")


def changeme( mylist ):
   "This changes a passed list into this function"
   mylist.append([1,2,3,4]);
   print("Values inside the function: ", mylist)
   return

# Now you can call changeme function
mylist = [10,20,30]
changeme( mylist )

print ("Values outside the function: ", mylist)



def sum( arg1, arg2 ):
   # Add both the parameters and return them."
   total = arg1 + arg2
   print ("Inside the function : ", total)
   # return total;

# Now you can call sum function
total = sum( 10, 20 );
print ("Outside the function : ", total )




Money = 2000
print (Money)
def AddMoney():
    global Money
   # Uncomment the following line to fix the code:
   # global Money
   Money = Money + 1


AddMoney()
print (Money)


class Employee:
    'Common base class for all employees'
    empCount = 0

    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
        Employee.empCount += 1

    def displayCount(self):
        print
        ("Total Employee %d" % Employee.empCount)

    def displayEmployee(self):
        print
        ("Name : ", self.name, ", Salary: ", self.salary)


"This would create first object of Employee class"
emp1 = Employee("Zara", 2000)
"This would create second object of Employee class"
emp2 = Employee("Manni", 5000)

emp1.displayEmployee()
emp2.displayEmployee()
print ("Total Employee %d" % Employee.empCount)


class Employee:
    'Common base class for all employees'
    empCount = 0

    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
        Employee.empCount += 1

    def displaycount(self):
        print ("Total Employee %d" % Employee.empCount)

    def displayemployee(self):
        print ("Name : ", self.name, ", Salary: ", self.salary)


"This would create first object of Employee class"
emp1 = Employee("Zara", 2000)
print(emp1.displaycount())
"This would create second object of Employee class"
emp2 = Employee("Manni", 5000)
emp1.displayemployee()
emp2.displayemployee()
print
"Total Employee %d" % Employee.empCount

emp1.age = 7
emp2.age
emp1.salary

hasattr(emp1, 'age')    # Returns true if 'age' attribute exists
getattr(emp1, 'age')    # Returns value of 'age' attribute
setattr(emp1, 'age', 8) # Set attribute 'age' at 8
delattr(emp1, 'age')    # Delete attribute 'age'

print ("Employee.__doc__:", Employee.__doc__)
print ("Employee.__name__:", Employee.__name__)
print ("Employee.__module__:", Employee.__module__)
print ("Employee.__bases__:", Employee.__bases__)
print ("Employee.__dict__:", Employee.__dict__)

E:\NMG2



mysql> LOAD DATA LOCAL INFILE 'E:/NMG2/omni_item_browse_2years.txt' INTO TABLE browse;


LOAD DATA INFILE 'E:/NMG2/omni_item_browse_2years.txt'
INTO TABLE test
FIELDS TERMINATED BY ','
LINES STARTING BY 'xxx';


# with open("E:/NMG2/omni_item_browse_2years.txt") as myfile:
#     head = [next(myfile) for x in xrange(10)]
# print (head)
#
# with open("E:/NMG2/omni_item_browse_2years.txt") as myfile:
#     firstNlines=myfile.readlines()[0:5]
#
#

import pandas as pd
# firstNlines = pd.read_csv('E:/NMG2/omni_item_browse_2years.txt', nrows=10, delimiter = "\t")
# print(firstNlines)
#
# firstNlines.to_csv(r'E:\NMG2\test1.csv')
#
# LOAD DATA INFILE 'E:/NMG2/omni_item_browse_2years.txt' INTO TABLE test.PerformanceReport;

>>> d1 = {'col1': [1, 2], 'col2': [3, 4]}
>>> d1
>>> df1 = pd.DataFrame(data=d1)
>>> df1
>>> df1_transposed = df1.T # or df1.transpose()
>>> df1_transposed
df1.dtypes
df1_transposed.dtypes



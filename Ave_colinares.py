'''
p = float(input("Enter Prelim Grade: "))
m = float(input("Enter Midterm Grade: "))
pf = float(input("Enter Pre-final Grade: "))
f = float(input("Enter Final Grade: "))
'''
import statistics 

def get_grades():
  
    prelims = float(input("Enter Prelims grade: "))
    midterm = float(input("Enter Midterm grade: "))
    prefinal = float(input("Enter Prefinal grade: "))
    final = float(input("Enter Final grade: "))
    return [prelims, midterm, prefinal, final]  

def calculate_average(grades):
 
    return statistics.mean(grades)

def get_remarks(average):

    if average >= 95.0 and average <= 100.0:
        return "Dean's Lister "
    elif average >= 90.0 and average <=94.99:
        return "Excellent! "
    elif average >= 84.0 and average <=89.99:
        return "Very Good! "  
    elif average >=80.0 and average <=83.99:
        return "Good "
    elif average >=75.0 and average <=79.99:
        return "Conditional "
    elif average<=75.0:
        return "Failed "
    else:
        return "Invalid Grade "


grades = get_grades() 
average = calculate_average(grades) 
remarks = get_remarks(average)  

print("\n--- Grade Statistics ---")
print(f"Average: {average}") 
print(f"Remarks: {remarks}")  

get_grades()
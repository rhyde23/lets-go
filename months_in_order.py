months = [
    'January',
    'February',
    'March',
    'April',
    'May',
    'June',
    'July',
    'August',
    'September',
    'October',
    'November',
    'December',
]

days_in_months = {
    'January':31,
    'February':28,
    'March':31,
    'April':30,
    'May':31,
    'June':30,
    'July':31,
    'August':31,
    'September':30,
    'October':31,
    'November':30,
    'December':31,
    
}

def get_month_number(month) :
    return months.index(month)

def get_number_month(x) :
    return months[x]

def get_days_in_a_month(month) :
    return days_in_months[month]
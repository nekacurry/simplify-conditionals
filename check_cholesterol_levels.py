# By Kami Bigdely
# Decompose conditional
# Reference: https://www.healthline.com/health/high-cholesterol/levels-by-age

# Blood test analysis program
total_cholesterol = 70
ldl = 30
triglyceride = 120


def good():
  print('*** Good level of cholestrol ***')

def high():
    print('*** High cholestrol level ***')
    print('start taking pills such as statins')
    print('start TLC diet')

def TLC():
    print('*** Borderline to moderately elevated ***')
    print("Start TLC diet")
    print("Under this meal plan, only 7 percent of your daily calories \nshould come from saturated fat.")
    print('Some foods help your digestive tract absorb less cholesterol. For example,\nyour doctor may encourage you to eat more:')
    print('oats, barley, and other whole grains.')
    print('fruits such as apples, pears, bananas, and oranges.')


def check_ldl(total_cholesterol, ldl):
  if total_cholesterol < 200 and ldl < 100:
    return True
  else: 
    return False

def check_cholesterol(total_cholesterol, ldl, triglyceride):
  if check_ldl(total_cholesterol, ldl) and triglyceride < 150:
    good()
  
  elif check_ldl(total_cholesterol, ldl) and triglyceride < 200:
    high()

  elif check_ldl(total_cholesterol, ldl) and triglyceride < 300:
    TLC()

  else:
    print('Error: unhandled case')
desiredGrade=input('Enter desired grade>')
minAvg=float(input('Enter minimum average required>'))
currentAvg=float(input('Enter current average in course>'))
coursePersentage=int(input('Enter how much the final counts\nas a percentage of the course grade>'))

coursePersentage/=100
contributionScore=currentAvg*(1-coursePersentage)
requiredScore=(minAvg-contributionScore)/coursePersentage

print(f'You need a score of {requiredScore:.2f} on the final to get a {desiredGrade}')



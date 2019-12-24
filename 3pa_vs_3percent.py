import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

df = pd.read_csv('team_stats_2018.csv') #data in csv format        

x = df['3PA'] #x-values
y = df['3P%'] #y-values
teams = df['Team'] #labels
plt.figure(figsize=(12,10)) #figure size
plt.scatter(x,y, alpha=.33, c='red') #scatter plot
plt.title('3-point attempts vs. 3-point percentage') #title
plt.xlabel('3-point attempts per game')#x-label
plt.ylabel('3-point percentage') #y-label

for i, txt in enumerate(teams): #label each point
    plt.annotate(txt, (x[i], y[i]), size = 10, c='black')
    
league_x = df['3P%'][30] 
league_y = df['3PA'][30] 

test_x = np.linspace(25, 46, 500) 
test_y = league_x * test_x / test_x

testy = np.linspace(.32, .4, 50)
testx = league_y * testy / testy

plt.plot(test_x, test_y, c='black', linewidth = .5) #horizontal line

plt.plot(testx, testy, c='black', linewidth = .5) #vertical line

plt.savefig('3PA_vs_3P%.jpg', dpi = 300) #save plot as image

plt.show() #plot
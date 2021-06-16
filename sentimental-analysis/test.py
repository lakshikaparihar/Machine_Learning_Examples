from IMDb import IMDb
'''
sample = ["I Love the movie , SRK's acting was great"]
temp = IMDb().predict(sample, ["feature_name"])
print("Sample: ", sample)
print("Feedback: ", temp[0])
print("Probability: ", temp[1])

sample = ["Salman Khan is a bad actor"]
temp = IMDb().predict(sample, ["feature_name"])
print("Sample: ", sample)
print("Feedback: ", temp[0])
print("Probability: ", temp[1][0][0])
'''

sample = ["I Love the movie , SRK's acting was great"]
temp = IMDb().predict(sample, ["feature_name"])
print(temp)

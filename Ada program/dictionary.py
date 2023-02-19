#Creating students dictionary
students = {

             }


#creating the variable for the three tracks  in Ada program
track = ["dataTrack" ,"frontendTrack" ,"backendTrack"]

#populating the tracks with students name as lists
dataTrack= ["pretty cynthia", "amaka dissapoint","nedu japan", "pretty cynthia","pretty cynthia" ]
frontendTrack = ["jon doe","john doe", "jon bellion","jon bellcat","jon doe"]
backendTrack = ["ada ada","pyhon ezege","dog catcher", "bitrus beetroot","doja cat","beta rat"]

#creating the scores list for the students
dataTrackScores = [76,45,23]
frontendTrackScores = [115, 100, 87, 99]
backendTrackScores = [112, 99, 120, 35, 47, 99 ]

# 1.) populating a nested student dictionary with their given track, names and scores 
# 2.) creating dict keys for each key in the dictionary
students[track[0]] = {"names": list(set(dataTrack)), 
                       "scores": dataTrackScores}
students[track[1]] = {"names" :  list(set(frontendTrack)),
                       "scores":  frontendTrackScores }
students[track[2]] = {"names":  list(set(backendTrack)),
                       "scores":  backendTrackScores }

#printing the students dict
print(students)

#printing the desired results 
print("The top three students are: ")
print("(1). "+ str(students[track[0]]["names"][0])+" with a score of "+ str(students[track[0]]["scores"][0]) + " for " + str(track[0]))
print("(2). "+ str(students[track[1]]["names"][0])+" with a score of "+ str(students[track[1]]["scores"][0]) + " for " + str(track[1]))
print("(3). "+ str(students[track[2]]["names"][2])+" with a score of "+ str(students[track[2]]["scores"][2]) + " for " + str(track[2]))


from fuzzywuzzy import fuzz,process
import speak_now
import takevo
def matching(text):
    h_match = 0
    to_be_send = 0
    max = 0
    f = open("data_set.txt", "r")
    for i in f:
        k = i.find(":")
        l = i[0:k]
        matched = fuzz.token_set_ratio(text,l)
        if(h_match<matched):
            h_match = matched
            to_be_send = i[k+1:]
            sentence = l
            #print(i)
        if(int(i[k+1:])>int(max)):
            max = i[k+1:]

    f.close()
    if (int(h_match) < 70):
        sentence = "Do you want to say"+sentence
        speak_now.speak(sentence)
        query = takevo.takevoice().lower()
        try:
            t = matching(query)
        except:
            speak_now.speak("please say yes or no")
        if int(t)==17:
            f = open("data_set.txt", "a")
            f.write("{}:{}".format(text, to_be_send))
            f.close()
        elif int(t)==18:
            f = open("data_set.txt", "a")
            f.write("{}:{}\n".format(text, int(max)+1))
            f.close()

    return(to_be_send)

#q = matching("iufydhsfzdqqqq")
#print(q)

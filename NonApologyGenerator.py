print("This is an apology letter generator based on the contribution of Will Smith, Bill Clinton, Tony Blair, and other internet sources.")
recipient=input("Enter recipient name")
apologizer=input("Enter apologizer name")

from ntpath import join
import random
from tkinter import N

print("Hello "+ recipient + "!")
print("\n")
# Apologies Sources
WillSmithApology = "What I have done is poisonous and destructive. My behavior was unacceptable and inexcusable. I would like to publicly apologize to you. I was out of line and I was wrong. I am embarrassed and my actions were not indicative of the man I want to be. There is no place for such behavior in a world of love and kindness. I deeply regret that my behavior has stained what has been an otherwise gorgeous journey for all of us. "
BlairApology="The intelligence assessments made at the time turned out to be wrong. The aftermath turned out to be more hostile, protracted and bloody than ever we imagined. For all of this, I express more sorrow, regret and apology than you will ever know. "
ChildrenApology="Please accept this letter as an apology. This can’t justify my actions. You’ve known me to be a very obedient person; I betray your trust this time. That’s why I have written this letter to say sorry for the incident. Following this error, I must confess I am ashamed of my unbecoming behavior. Please forgive me. I am ready for any punishment that you’ll find fit for my actions. But know I will never repeat the mistake, I will learn to control my cravings. "
ClintonApology="I want to say to you that, as you might imagine, I have been on quite a journey these last few weeks to get to the end of this, to the rock bottom truth of where I am and where we all are. It is important to me that everybody who has been hurt know that the sorrow I feel is genuine: first and most important, my family; also my friends, and the American people; I have asked all for their forgiveness. I agree with those who have said that in my first statement after I testified I was not contrite enough. I don't think there is a fancy way to say that I have sinned. The children of this country can learn in a profound way that integrity is important and selfishness is wrong, but God can change us and make us strong at the broken places. "

WillSmithApologyWords=WillSmithApology.split(". ")
BlairApologyWords=BlairApology.split(". ")
ChildrenApologyWords=ChildrenApology.split(". ")
ClintonApologyWords=ClintonApology.split(". ")

TotalApology=WillSmithApologyWords + BlairApologyWords + ChildrenApologyWords + ClintonApologyWords
random.shuffle(TotalApology)

Sentence="\n\n".join(TotalApology)

print(Sentence)

print("\nI am a work in progress.\n \nSincerely,\n" + apologizer)



# new_sentence = WillSmithApology.replace("My", "Our")
# print(new_sentence)

# words2 = ["some", "new", "words"]
# sentence2 = " ".join(words2)

# print(sentence2)

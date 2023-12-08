def newGame():
    guesses = []
    correctGuesses = 0
    questionNum = 1

    for key in questions:
        print("---------------------")
        print(key)
        for i in range(len(options[questionNum-1])):
            print(options[questionNum-1][i])
        guess = input("Enter (A,B,C or D): ")
        guess = guess.upper()
        guesses.append(guess)

        correctGuesses += checkAnswer(questions.get(key),guess)
        questionNum +=1

    displayScore(correctGuesses, guesses)

def checkAnswer(answer, guess):
      if answer == guess:
          print("Cong!")
          return 1
           
      else:
          print("Wrong!")
          return 0
        
    
def displayScore(correctGuesses,guesses):
    print("-------------")
    print("Results")
    print("-------------")
    
    for question, correct_answer in questions.items():
        user_guess = guesses.pop(0) if guesses else ""  # Get the guessed answer or an empty string
        print(f"{question} - Your Guess: {user_guess} - Correct Answer: {correct_answer}")

    score= int((correctGuesses/len(questions))*100)
    print("Your score is: "+str(score)+"%")

def playAgain():
    response = input("Do you want to play again? (yes or no): ")
    return response.upper() == "YES"

    if response == "YES":
        return True
    else:
        return False

questions= {
 "Sinekli Bakkal Romaninin Yazari Aşagidakilerden Hangisidir?" : "B" ,
 "Asagida Verilen İlk Cag Uygarliklarindan Hangisi Yaziyi İcat Etmistir?" : "C" ,
 "Tsunami Felaketinde En Fazla Zarar Goren Guney Asya Ukesi Asagidakilerden Hangisidir?" : "A",
 "2003 Yilinda Euro Vizyon Şarki Yarisasinda Ulkemizi Temsil Eden ve Yarismada Birinci Gelen Sanatcimiz Kimdir?" : "B"
}

options = [["A) ReSat Nuri GUntekin B) Halide Edip Adivar C) Ziya Gokalp D) Ömer Seyfettin"],
          ["A) Hititler B) Elamlar C) Sumerler D) Urartular"],
          ["A) Endonezya B) Srilanka C) Tayland D) Hindistan"],
          ["A) Grup Athena B) Sertap Erener C) Sebnem Paker D) Ajda Pekkan"]]

newGame()

while playAgain():
    newGame()

print("BYEEEEE!")



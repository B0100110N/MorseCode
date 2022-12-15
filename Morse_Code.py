import winsound


#frequency variables have a value measured in hertz
#dot variables have a value measured in milliseconds
#dash variables have a value measured in milliseconds

print('\n')
print("Press '1' to exit.")
print('\n')

while True:
    
    userInput = input("Enter a letter to hear it in morse code: ")
    if userInput.lower().startswith('a'):
        frequency = 800
        dash = 500
        dot = 150
        winsound.Beep(frequency, dot)
        winsound.Beep(frequency, dash)
        print("a: . _")
        
    elif userInput.lower().startswith('b'):
        frequency = 800
        dash = 500
        dot = 150
        winsound.Beep(frequency, dash)
        winsound.Beep(frequency, dot)
        winsound.Beep(frequency, dot)
        winsound.Beep(frequency, dot)
        print("b: _ . . .")
        
    elif userInput.lower().startswith("c"):
        frequency = 800
        dash = 500
        dot = 150
        winsound.Beep(frequency, dash)
        winsound.Beep(frequency, dot)
        winsound.Beep(frequency, dash)
        winsound.Beep(frequency, dot)
        print("c: _ . _ .")
        
    elif userInput.lower().startswith("d"):
        frequency = 800
        dash = 500
        dot = 150
        winsound.Beep(frequency, dash)
        winsound.Beep(frequency, dot)
        winsound.Beep(frequency, dot)
        print("d: _ . .")
        
    elif userInput.lower().startswith("e"):
        frequency = 800
        dot = 150
        winsound.Beep(frequency, dot)
        print("e: .")
        
    elif userInput.lower().startswith("f"):
        frequency = 800
        dash = 500
        dot = 150
        winsound.Beep(frequency, dot)
        winsound.Beep(frequency, dot)
        winsound.Beep(frequency, dash)
        winsound.Beep(frequency, dot)
        print("f: . . _ .")
        
    elif userInput.lower().startswith("g"):
        frequency = 800
        dash = 500
        dot = 150
        winsound.Beep(frequency, dash)
        winsound.Beep(frequency, dash)
        winsound.Beep(frequency, dot)
        print("g: _ _ .")


    elif userInput.lower().startswith("h"):
        frequency = 800
        dot = 150
        winsound.Beep(frequency, dot)
        winsound.Beep(frequency, dot)
        winsound.Beep(frequency, dot)
        winsound.Beep(frequency, dot)
        print("h: . . . .")
        
    elif userInput.lower().startswith("i"):
        frequency = 800
        dot = 150
        winsound.Beep(frequency, dot)
        winsound.Beep(frequency, dot)
        print("i: . .")
        
    elif userInput.lower().startswith("j"):
        frequency = 800
        dash = 500
        dot = 150
        winsound.Beep(frequency, dot)
        winsound.Beep(frequency, dash)
        winsound.Beep(frequency, dash)
        winsound.Beep(frequency, dash)
        print("j: . _ _ _")
        
    elif userInput.lower().startswith("k"):
        frequency = 800
        dash = 500
        dot = 150
        winsound.Beep(frequency, dash)
        winsound.Beep(frequency, dot)
        winsound.Beep(frequency, dash)
        print("k: _ . _")
        
    elif userInput.lower().startswith("l"):
        frequency = 800
        dash = 500
        dot = 150
        winsound.Beep(frequency, dot)
        winsound.Beep(frequency, dash)
        winsound.Beep(frequency, dot)
        winsound.Beep(frequency, dot)
        print("l: . _ . .")
        
    elif userInput.lower().startswith("m"):
        frequency = 800
        dash = 500
        winsound.Beep(frequency, dash)
        winsound.Beep(frequency, dash)
        print("m: _ _")
        
    elif userInput.lower().startswith("n"):
        frequency = 800
        dash = 500
        dot = 150
        winsound.Beep(frequency, dash)
        winsound.Beep(frequency, dot)
        print("n: _ .")
    
        
    elif userInput.lower().startswith("o"):
        frequency = 800
        dash = 500
        dot = 150
        winsound.Beep(frequency, dash)
        winsound.Beep(frequency, dash)
        winsound.Beep(frequency, dash)
        print("o: _ _ _")
        
    elif userInput.lower().startswith("p"):
        frequency = 800
        dash = 500
        dot = 150
        winsound.Beep(frequency, dot)
        winsound.Beep(frequency, dash)
        winsound.Beep(frequency, dash)
        winsound.Beep(frequency, dot)
        print("p: . _ _ .")
        
    elif userInput.lower().startswith("q"):
        frequency = 800
        dash = 500
        dot = 150
        winsound.Beep(frequency, dash)
        winsound.Beep(frequency, dash)
        winsound.Beep(frequency, dot)
        winsound.Beep(frequency, dash)
        print("q: _ _ . _")
        
    elif userInput.lower().startswith("r"):
        frequency = 800
        dash = 500
        dot = 150
        winsound.Beep(frequency, dot)
        winsound.Beep(frequency, dash)
        winsound.Beep(frequency, dot)
        print("r: . _ .")
        
    elif userInput.lower().startswith("s"):
        frequency = 800
        dot = 150
        winsound.Beep(frequency, dot)
        winsound.Beep(frequency, dot)
        winsound.Beep(frequency, dot)
        print("s: . . .")
        
    elif userInput.lower().startswith("t"):
        frequency = 800
        dash = 500
        winsound.Beep(frequency, dash)
        print("t: _")
        
    elif userInput.lower().startswith("u"):
        frequency = 800
        dash = 500
        dot = 150
        winsound.Beep(frequency, dot)
        winsound.Beep(frequency, dot)
        winsound.Beep(frequency, dash)
        print("u: . . _")
        
    elif userInput.lower().startswith("v"):
        frequency = 800
        dash = 500
        dot = 150
        winsound.Beep(frequency, dot)
        winsound.Beep(frequency, dot)
        winsound.Beep(frequency, dot)
        winsound.Beep(frequency, dash)
        print("v: . . . _")
        
    elif userInput.lower().startswith("w"):
        frequency = 800
        dash = 500
        dot = 150
        winsound.Beep(frequency, dot)
        winsound.Beep(frequency, dash)
        winsound.Beep(frequency, dash)
        print("w: . _ _")
        
    elif userInput.lower().startswith("x"):
        frequency = 800
        dash = 500
        dot = 150
        winsound.Beep(frequency, dash)
        winsound.Beep(frequency, dot)
        winsound.Beep(frequency, dot)
        winsound.Beep(frequency, dash)
        print("_ . . _")
        
    elif userInput.lower().startswith("y"):
        frequency = 800
        dash = 500
        dot = 150
        winsound.Beep(frequency, dash)
        winsound.Beep(frequency, dot)
        winsound.Beep(frequency, dash)
        winsound.Beep(frequency, dash)
        print("y: _ . _ _")
        
    elif userInput.lower().startswith("z"):
        frequency = 800
        dash = 500
        dot = 150
        winsound.Beep(frequency, dash)
        winsound.Beep(frequency, dash)
        winsound.Beep(frequency, dot)
        winsound.Beep(frequency, dot)
        print("z: _ _ . .")
        
    elif userInput == '1':
        break
   

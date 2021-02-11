#BSRI version 1
#
#code written by Laura Camacho
#actual assesment aquired from (the legend himself) Don Ryujin

def getMScore(res):
    #these are the numbers for the 'masculine' traits
    mI = [1,4,7,10,13,16,19,22,25,28,31,34,37,40,43,46,49,52,55,58]
    rawScore = 0
    for i in mI:
        rawScore += res[i]
    return rawScore/20

def getFScore(res):
    #these are the numbers for the 'feminine' traits
    fI =[2,5,8,11,14,17,20,23,26,29,32,35,38,41,44,47,50,53,56,59]
    rawScore = 0
    for i in fI:
        rawScore += res[i]
    return rawScore/20

def printScale():
    print("1 = Never or almost never true")
    print("2 = Usually not true")
    print("3 = Sometimes but infrequently true")
    print("4 = Occasionally true")
    print("5 = Often true")
    print("6 = Usualy true")
    print("7 = Always or almost always true\n")

if __name__ == '__main__':
    res = [0]
    print("Welcome to my bootleg version of the BSRI:)\n")
    print("The Bem Sex-Role Inventory (BSRI) is a measure of masculinity and femininity, and is used to research gender roles.")
    print("There are 60 traits, rate yourself on a scale of 1-7 on each trait. Try to answer all of them as quickly as possible, but feel free to look something up if you don't know what it means")
    print("The self-rating scale is as follows:\n")
    printScale()
    print("You may print the scale again by typing 'ps' during the assesment and exit by typing 'exit'\n")

    start = input("press any key to start: ")
    questions = ["1. Self-reliant", "2. Yielding","3. Helpful","4. Defends own beliefs","5. Cheerful", "6. Moody", "7. Independent","8. Shy","9. Conscientious","10. Athletic","11. Affectionate","12. Theatrical","13. Assertive","14. Flatterable","15. Happy","16. Strong personality","17. Loyal","18. Unpredictable","19. Forceful","20. Feminime","21. Reliable","22. Analytical","23. Sympathetic","24. Jealous","25. Has leadership abilities","26. Sensitive to the needs of others","27. Truthful","28. Willing to take risks","29. Understanding","30. Secretive","31. Makes decisions easily","32. Compassionate","33. Sincere","34. Self-sufficient","35. Eager to sooth hurt feelings","36. Conceited","37. Dominant","38. Soft spoken","39. Likable","40. Masculine","41. Warm","42. Solemn","43. Willing to take a stand","44. Tender","45. Friendly","46. Aggressive","47. Gullible","48. Inefficient","49. Acts as a leader","50. Childlike","51. Adaptable","52. Individualistic","53. Does not use harsh language","54. Unsystematic","55. Competitive","56. Loves children","57. Tactful","58. Ambitious","59. Gentle","60. Conventional"]

    valid = ["1","2","3","4","5","6","7"]
    for x in questions:
        print(x)
        ans = input("your score: ")
        while ans not in valid:
            if ans == 'ps':
                printScale()
            elif ans == 'exit':
                exit()
            else:
                print("that's not a valid answer. try again")
            ans = input("your score: ")

        res.append(int(ans))
        print()

    m = getMScore(res)
    f = getFScore(res)

    print("your masculine score: ",m)
    print("your feminine score: ",f)

    #print("message from the coder: i didn't do much testing on this thing so if you notice any bugs lmk\n")

    if m < 4.9 and f < 4.9:
        print("your score is undifferentiated androgynous (less than 4.9 points for each catagory), which means you scored low for both masculine and feminine traits")
    elif m >= 4.9 and f < 4.9:
        print("your score is on the masculine side (masculine score >= 4.9, feminine score < 4.9)")
    elif m < 4.9 and f >= 4.9:
        print("your score is on the feminine side (masculine score < 4.9, feminine score >= 4.9)")
    else:
        print("your score is androgynous (more than 4.9 points for both masculine and feminine), which means that you scored highly for both masculine and feminine traits")
    
    print("\npeople who score feminine on this assesment tend to be better at relationships, androgynous people tend to do well too.")
    print("people with masculine scores tend to do poorly in relationships.\n")
    print("thank you for taking this assesment!")























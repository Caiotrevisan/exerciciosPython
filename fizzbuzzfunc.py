def fizzbuzz(a):

    if a%3 == 0 and a%5 == 0:
        a = 'FizzBuzz'

    else:
        if a%3 == 0:
            a = 'Fizz'

        else:
            if a%5 == 0:
                a = 'Buzz'

            else:
                a = a
    return (a)

        
